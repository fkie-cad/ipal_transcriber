import json
import time
from scapy.packet import Packet as ScapyPacket

import transcriber.settings as settings
from transcriber.request_queue import RequestQueue
from transcriber.rule_processor import RuleProcessor
from transcribers.utils import IpalIdCounter, get_all_transcribers


class PacketProcessor:

    _first = True

    def __init__(self):
        # counter that ensures uniqueness for all ids assigned to a transcriber message
        counter = IpalIdCounter()

        # instantiate transcriberes for selected protocols
        self.transcribers = {}
        for protocol, transcriber in get_all_transcribers().items():
            if protocol in settings.protocols:
                self.transcribers[protocol] = transcriber(counter)

        # prepare the queue to store messages as long as future message may match with them
        self.queue = RequestQueue(self.transcribers)

        # prepare the rule processor
        if settings.rules:
            self.rule_processor = RuleProcessor(settings.rules)

    def process_packet(self, pkt):

        # 0th pipeline step: store timing information for eval output

        if settings.evalout:
            t0 = float(pkt.sniff_time.timestamp())
            t1 = time.time()

        # 1st pipeline step: Transform packets request/response packets into an abstract form

        # check if the current packet can be handled by any of the selected transcribers and ignore it otherwise
        if isinstance(pkt, ScapyPacket) and "ethercat" in settings.protocols and self.transcribers["ethercat"].matches_protocol(pkt):
            protocol = "ethercat"
        elif isinstance(pkt, ScapyPacket) and "ethercat" in settings.protocols:
            settings.logger.debug("Fount non-EtherCat scapy packet. Scapy packets are only supported by EtherCat transcriber.")
            return
        elif isinstance(pkt, ScapyPacket):
            settings.logger.debug("Fount scapy packet, but EtherCat transcriber is disabled. Scapy packets are only supported by EtherCat transcriber.")
            return

        elif isinstance(pkt, pyshark.packet.packet.Packet):
            for protocol in settings.protocols:
                if protocol == "ethercat":
                    continue
                if self.transcribers[protocol].matches_protocol(pkt):
                    break
            else:
                settings.logger.debug("No parser for package: {}".format(pkt))
                return

        else:
            settings.logger.debug("Found unsupported packet type.")
            return

        # now we can parse the packet
        ipal_messages = self.transcribers[protocol].parse_packet(pkt)
        if len(ipal_messages) == 0:
            settings.logger.debug(
                "Transcriber of protocol {} did not return any IPAL messages for packet {}".format(
                    protocol, pkt
                )
            )
            return

        # Attach transport checksum if required
        if settings.crc in ["transport", "and", "or"]:
            self.handle_checksum(ipal_messages, pkt)

        # store timing information for eval output
        if settings.evalout:
            t2 = time.time()

        # 2nd pipeline step: match requests and responses

        self.queue.update_queue(ipal_messages)

        # store timing information for eval output
        if settings.evalout:
            t3 = time.time()

        # 3rd pipeline step: apply rules

        if settings.rules:
            for msg in ipal_messages:
                self.rule_processor.apply(msg)

        # 4th pipeline step: annotate malicious & output

        # Add malicious annotation
        for msg in ipal_messages:
            self.annotate_malicious(msg)
            self.output_ipal_message(msg)

        # Apply state extractor
        if settings.state_extractor:
            for msg in ipal_messages:
                settings.state_extractor.update_state(msg)

        # 5th pipeline step: store timing information for eval output

        # output eval results in the form of time spent in the different steps of the pipeline, but for now only if exactly one message was parsed from a given packet.
        if settings.evalout and len(ipal_messages) == 1:
            t4 = time.time()
            output = str(msg.activity) + " {:.15f} {:.15f} {:.15f} {:.15f}\n".format(
                t1 - t0, t2 - t1, t3 - t2, t4 - t3
            )
            settings.evaloutfd.write(output)
            settings.evaloutfd.flush()

    def handle_checksum(self, ipal_messages, pkt):

        # Get transport checksum status
        if "TCP" in pkt:
            crc = int(pkt["TCP"].checksum_status)
        elif "UDP" in pkt:
            crc = int(pkt["UDP"].checksum_status)
        else:
            crc = None
            settings.logger.debug(
                "Packet has neither TCP nor UDP layer for checksum calculation!"
            )
        crc = crc == 1 if crc in [0, 1] else None

        # Apply crc according to settings
        for msg in ipal_messages:
            if msg.crc is None or settings.crc == "transport":
                msg.crc = crc
            elif settings.crc == "and":
                msg.crc = msg.crc and crc
            elif settings.crc == "or":
                msg.crc = msg.crc or crc
            else:
                settings.logger.critical("Unknown crc condition encountered.")

    def annotate_malicious(self, msg):
        # Default value
        msg.malicious = settings.maliciousdefault

        if settings.malicious is None:
            return

        # Malicious by packet number
        if msg.id in settings.malicious["pkts"]:
            msg.malicious = settings.malicious["pkts"][msg.id]

        # Malicious by time range
        for start, end, mal in settings.malicious["time"]:
            if start <= msg.timestamp and msg.timestamp <= end:
                msg.malicious = mal

    def output_ipal_message(self, msg):
        if not settings.ipalout:
            return

        output = msg.export_json()

        if self._first:
            output["_transcriber-config"] = settings.transcriber_settings_to_dict()
            self._first = False

        settings.ipaloutfd.write(json.dumps(output) + "\n")
        settings.ipaloutfd.flush()

    def finalize(self):
        if settings.ipalout:
            settings.ipaloutfd.flush()
        if settings.state_extractor:
            settings.state_extractor.finalize()
        if settings.evalout:
            settings.evaloutfd.flush()
