#!/usr/bin/env python3
import argparse
import gzip
import importlib.util
import json
import logging
import os
import pyshark
import sys

from scapy.main import init_session as scapy_init
from scapy.utils import rdpcap, PcapNgReader
try:
    from scapy.contrib.ethercat import EtherCatNOP
except ImportError:
    print("You need to install scapy from https://github.com/plustik/scapy")
    print("Running 'pip install git+https://github.com/plustik/scapy.git' should work.")
    exit(1)

import transcriber.settings as settings
import transcriber.packet_processor as packet_processor
import transcriber.state_extractor as state_extractor

from transcribers.utils import get_all_transcribers


# Wrapper for hiding .gz files
def open_file(filename, mode):
    if filename.endswith(".gz"):
        return gzip.open(filename, mode=mode, compresslevel=settings.compresslevel)
    else:
        return open(filename, mode=mode, buffering=1)


# Load modification rules from rules file
def load_rule_file(path):
    settings.rulesin = path

    try:
        spec = importlib.util.spec_from_file_location("module.name", path)
        settings.rules = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(settings.rules)
    except Exception as e:
        settings.logging.error("Could not load rule file!")
        settings.logging.error(e)
        exit(1)


# Initialize logger
def initialize_logger(args):

    # Logging
    if args.log:
        settings.log = getattr(logging, args.log.upper(), None)

        if not isinstance(settings.log, int):
            logging.getLogger("ipal-transcriber").error(
                "Option '--log' parameter not found"
            )
            exit(1)

    if args.logfile:
        settings.logfile = args.logfile
        logging.basicConfig(
            filename=settings.logfile,
            level=settings.log,
            format=settings.logformat,
        )
    else:
        logging.basicConfig(level=settings.log, format=settings.logformat)

    settings.logger = logging.getLogger("ipal-transcriber")


# Parse attack.json file
def parse_malicious_file(path):
    settings.malicious = {"pkts": {}, "time": []}
    settings.maliciousin = path

    # Load josn file
    with open_file(settings.maliciousin, "r") as fin:
        attacks = json.load(fin)

    # Pre-parse attacks for faster lookups
    for attack in attacks:

        # Test attack structure
        assert "id" in attack and "attack_point" in attack and "description" in attack

        # Packet label
        if "ipalid" in attack:
            assert "start" not in attack and "end" not in attack
            settings.malicious["pkts"][attack["ipalid"]] = attack["id"]
        elif "start" in attack and "end" in attack:
            assert "ipalid" not in attack
            settings.malicious["time"].append(
                (attack["start"], attack["end"], attack["id"])
            )
        else:
            settings.logger.error("Invalid attack structure")
            settings.logger.error(attack)
            exit(1)


# Build parser arguments
def prepare_arg_parser(parser):

    # Interface or PCAP option
    parser.add_argument(
        "--interface",
        metavar="INTERFACE",
        help="traffic input interface (Use either this or --pcap)",
        required=False,
    )
    parser.add_argument(
        "--pcap",
        metavar="FILE",
        help="path to pcap file (Use either this or --interface)",
        required=False,
    )

    # Input config
    parser.add_argument(
        "--protocols",
        metavar="STR",
        help="specify a subset of the available transcribers {}. (Default: all)".format(
            list(get_all_transcribers().keys())
        ),
        nargs="+",
        required=False,
    )
    parser.add_argument(
        "--rules",
        metavar="FILE",
        help="file containing rules to transform transcribed messages.",
        required=False,
    )
    parser.add_argument(
        "--timeout",
        metavar="INT",
        help="number of milliseconds a packet can be responded to. Used for response matching (Default: 250ms)",
        required=False,
    )
    parser.add_argument(
        "--malicious",
        dest="malicious",
        metavar="FILE",
        help="Attack json file for labeling the packets according to the attacks in a dataset.",
        required=False,
    )
    parser.add_argument(
        "--malicious.default",
        dest="maliciousdefault",
        metavar="BOOL",
        help="set this option to 'true' or 'false' to define default malicious annotation. (Default: None). Can be used in combination with --malicious",
        required=False,
    )
    parser.add_argument(
        "--crc",
        metavar="STR",
        help="options for CRC calculations are at 'transport', 'application', combined with 'or', or 'and'. (Default: and)",
        required=False,
    )

    # IPAL output file
    parser.add_argument(
        "--ipal.output",
        dest="ipalout",
        metavar="FILE",
        help="output location for ipal messages ('-' stdout, '*.gz' compress).",
        required=False,
    )

    # Logging
    parser.add_argument(
        "--log",
        dest="log",
        metavar="STR",
        help="define logging level as one of DEBUG, INFO, WARNING, ERROR, or CRITICAL. (Default: WARNING)",
        required=False,
    )
    parser.add_argument(
        "--logfile",
        dest="logfile",
        metavar="FILE",
        default=False,
        help="define file to log to. (Default: stderr)",
        required=False,
    )

    # Gzip compress level
    parser.add_argument(
        "--compresslevel",
        dest="compresslevel",
        metavar="INT",
        default=9,
        help="set the gzip compress level. 0 no compress, 1 fast/large, ..., 9 slow/tiny. (Default: 9)",
        required=False,
    )


# check compatibility of arguements and store them for global access
def load_settings(args):  # noqa: C901

    # Gzip compress level
    if args.compresslevel:
        try:
            settings.compresslevel = int(args.compresslevel)
        except ValueError:
            settings.logger.error(
                "Option '--compresslevel' must be an integer from 0-9"
            )
            exit(1)

        if settings.compresslevel < 0 or 9 < settings.compresslevel:
            settings.logger.error(
                "Option '--compresslevel' must be an integer from 0-9"
            )
            exit(1)

    # Forbidden combinations
    if (not args.pcap and not args.interface) or (args.pcap and args.interface):
        settings.logger.error(
            "Use either --pcap or --interface to indicate source of transcribed traffic"
        )
        exit(1)

    # Selected protocols
    if args.protocols:
        for protocol in args.protocols:
            if protocol not in list(get_all_transcribers().keys()):
                settings.logger.error("Unknown protocol: {}".format(protocol))
                exit(1)
        settings.protocols = args.protocols
    else:
        settings.protocols = list(get_all_transcribers().keys())

    # Load rule file
    if args.rules:
        load_rule_file(args.rules)

    # Malicious annotations
    if args.malicious:
        try:
            parse_malicious_file(args.malicious)
        except Exception as e:
            settings.logger.error("Error loading --malicious json:")
            settings.logger.error(e)
            exit(1)

    if args.maliciousdefault:
        if args.maliciousdefault.lower() == "true":
            settings.maliciousdefault = True
        elif args.maliciousdefault.lower() == "false":
            settings.maliciousdefault = False
        else:
            settings.logger.error("--malicious.default can be either 'true' or 'false'")
            exit(1)

    # Parse transcriber configurations
    if args.timeout:
        try:
            settings.timeout = 1.0 * int(args.timeout) / 1000
        except Exception as e:
            settings.logger.error(
                "--timeout can not be parsed. Has to be an integer in [ms]"
            )
            settings.logger.error(e)
            exit(1)

    if args.crc:
        if args.crc not in ["transport", "application", "and", "or"]:
            settings.logger.error(
                "Option '--crc' has to be one of 'transport', 'application', 'or', or 'and'"
            )
            exit(1)
        settings.crc = args.crc

    # Open IPAL file
    if args.ipalout:
        settings.ipalout = args.ipalout
    if settings.ipalout:
        if settings.ipalout != "stdout" and settings.ipalout != "-":
            # clear the file we are about to write to
            open_file(settings.ipalout, "wt").close()
            settings.ipaloutfd = open_file(settings.ipalout, "wt")
        else:
            settings.ipaloutfd = sys.stdout

    # Open eval file
    if settings.evalout:
        if settings.evalout != "stdout" and settings.evalout != "-":
            # clear the file we are about to write to
            open_file(settings.evalout, "wt").close()
            settings.evaloutfd = open_file(settings.evalout, "wt")
        else:
            settings.evaloutfd = sys.stdout


def main():
    # Argument parser and settings
    parser = argparse.ArgumentParser()
    prepare_arg_parser(parser)
    state_extractor.add_arguments_to_parser(parser)

    args = parser.parse_args()
    initialize_logger(args)
    load_settings(args)
    settings.state_extractor = state_extractor.parse_arguments(args)

    # Create PacketProcessor and start reading from pcap or interface
    pkt_processor = packet_processor.PacketProcessor()

    try:
        if args.pcap:
            settings.source = args.pcap
            scapy_init(None)
            reader = PcapNgReader(args.pcap)
            while True:
                try:
                    pkt = reader.read_packet()  # type: Packet
                except EOFError:
                    break
                pkt_processor.process_packet(pkt)

        elif args.interface:
            settings.source = args.interface
            capture = pyshark.LiveCapture(
                interface=args.interface,
                custom_parameters=settings.pyshark_options,
                decode_as=settings.pyshark_decode_as,
            )
            capture.apply_on_packets(pkt_processor.process_packet)

        pkt_processor.finalize()  # Flushes data

    except BrokenPipeError:
        # Python flushes standard streams on exit; redirect remaining output
        # to devnull to avoid another BrokenPipeError at shutdown
        devnull = os.open(os.devnull, os.O_WRONLY)
        os.dup2(devnull, sys.stdout.fileno())
        # sys.exit(1)  # Python exits with error code 1 on EPIPE

    # Close files
    if settings.ipalout and settings.ipaloutfd != sys.stdout:
        settings.ipaloutfd.close()
    if settings.stateout and settings.stateoutfd != sys.stdout:
        settings.stateoutfd.close()
    if settings.evalout and settings.evaloutfd != sys.stdout:
        settings.evaloutfd.close()


if __name__ == "__main__":
    main()
