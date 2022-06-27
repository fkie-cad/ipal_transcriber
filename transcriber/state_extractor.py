#!/usr/bin/env python3
import argparse
import gzip
import json
import logging
import sys
import os

import transcriber.settings as settings
from transcriber.messages import IpalMessage
from state_extractors.utils import get_all_state_extractors


# Wrapper for hiding .gz files
def open_file(filename, mode):
    if filename.endswith(".gz"):
        return gzip.open(filename, mode=mode, compresslevel=settings.compresslevel)
    else:
        return open(filename, mode=mode, buffering=1)


# Build parser arguments
def add_arguments_to_parser(parser):
    parser.add_argument(
        "--state.output",
        dest="stateout",
        metavar="FILE",
        help="output location for state information. ('-' stdout, '*.gz' copress)",
        required=False,
    )

    parser.add_argument(
        "--filter",
        dest="filter",
        metavar="LIST",
        help="semicolon separated list of state names to filter for. (Default: no filter)",
        required=False,
    )

    parser.add_argument(
        "--complete-only",
        dest="complete",
        metavar="BOOL",
        help="output complete states after filterinig only. (Default: True)",
        required=False,
    )

    parser.add_argument(
        "--state-in-message",
        dest="stateinmessage",
        metavar="BOOL",
        help="embed state inside the messages. (Default: False)",
        required=False,
    )

    # Add subparsers for available state-extractor methods
    subparsers = parser.add_subparsers(
        title="State Extractors",
        help="These are available state extractor methods. Use -h for further options on each method.",
        dest="state_extractor",
    )

    for name, state_extractor in get_all_state_extractors().items():
        subparser = subparsers.add_parser(name, help=state_extractor._description)
        subparser.set_defaults(state_extractor=state_extractor)
        state_extractor.add_arguments_to_parser(subparser)


# Returns state_extractor according to the arguments
def parse_arguments(args):

    if args.stateout:
        settings.stateout = args.stateout
    if settings.stateout:
        if settings.stateout != "stdout" and settings.stateout != "-":
            # clear the file we are about to write to
            open_file(settings.stateout, "wt").close()
            settings.stateoutfd = open_file(settings.stateout, "wt")
        else:
            settings.stateoutfd = sys.stdout

    if args.filter:
        settings.filter = args.filter.split(";")

    if args.complete:
        if args.complete.lower() == "true":
            settings.completeonly = True
        elif args.complete.lower() == "false":
            settings.completeonly = False
        else:
            settings.logger.error("--complete-only can be either 'true' or 'false'")

    if settings.completeonly and settings.filter is None:
        settings.logger.error("'--complete-only' requires filter")
        exit(1)

    if args.stateinmessage:
        if args.stateinmessage.lower() == "true":
            settings.stateinmessage = True
        elif args.stateinmessage.lower() == "false":
            settings.stateinmessage = False
        else:
            settings.logger.error("--state-in-message can be either 'true' or 'false'")

    # Lookup and initilize selected state-extractor
    if args.state_extractor:
        settings.state_extractor = args.state_extractor
        return args.state_extractor(args)
    else:
        return None


def parse_main_arguments():
    # Default in-/output for standalone program is stdin-/out
    if settings.ipalin is None:
        settings.ipalin = "-"
    if settings.stateout is None:
        settings.stateout = "-"

    # Build argument parser
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--ipal.input",
        dest="ipalin",
        metavar="FILE",
        help="input location for message information. ('-' stdin, '*gz' compressed)",
        required=False,
    )

    add_arguments_to_parser(parser)

    # Gzip compress level
    parser.add_argument(
        "--compresslevel",
        dest="compresslevel",
        metavar="INT",
        default=9,
        help="set the gzip compress level. 0 no compress, 1 fast/large, ..., 9 slow/tiny. (Default: 9)",
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

    # Parse arguments
    args = parser.parse_args()

    # Logging
    if args.log:
        settings.log = getattr(logging, args.log.upper(), None)

        if not isinstance(settings.log, int):
            settings.logger.error("Option '--log' parameter not found")
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
    settings.logger = logging.getLogger("ipal-state-extractor")

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

    # ipalin only relevant for standalone program.
    if args.ipalin:
        settings.ipalin = args.ipalin
    if settings.ipalin:
        if settings.ipalin != "stdin" and settings.ipalin != "-":
            settings.ipalinfd = open_file(settings.ipalin, "r")
        else:
            settings.ipalinfd = sys.stdin
    else:
        settings.logger.error("Option '--ipal.input' required.")
        exit(1)

    return args


def main():
    # Prepare pargparse for main
    args = parse_main_arguments()

    # Initialize state extractor
    state_extractor = parse_arguments(args)
    if state_extractor is None:
        settings.logger.error("Define a state_extractor!")
        exit(1)

    # Convert json into message!
    try:
        for line in settings.ipalinfd.readlines():
            msg = IpalMessage.from_json(json.loads(line))
            state_extractor.update_state(msg)

        state_extractor.finalize()  # Finalize

    except BrokenPipeError:
        # Python flushes standard streams on exit; redirect remaining output
        # to devnull to avoid another BrokenPipeError at shutdown
        devnull = os.open(os.devnull, os.O_WRONLY)
        os.dup2(devnull, sys.stdout.fileno())
        # sys.exit(1)  # Python exits with error code 1 on EPIPE

    if settings.stateoutfd and settings.stateoutfd != sys.stdout:
        settings.stateoutfd.close()
    if settings.ipalinfd and settings.ipalinfd != sys.stdin:
        settings.ipalinfd.close()


if __name__ == "__main__":
    main()
