import struct

import transcriber.settings as settings
from transcriber.messages import Activity, IpalMessage
from transcribers.transcriber import Transcriber


class MAVLinkTranscriber(Transcriber):
    # Packet definition:https://mavlink.io/en/guide/serialization.html
    _name = "MAVLink"

    @classmethod
    def matches_protocol(self, pkt):
        port_matches = (
            int(pkt["UDP"].srcport) in settings.MAVLINK_PORT
            or int(pkt["UDP"].dstport) in settings.MAVLINK_PORT
        )
        has_magic = pkt["UDP"].payload[:2] == "fd"  # Version 2
        return has_magic and port_matches

    def parse_packet(self, pkt):
        # Assumption: MAVLink2 with fixed header length 10
        HEADER_LENGTH = 10

        # load from hex formated udp payload, strip ":" so it's proper hex
        # turn into bytes as we can access bytes by indices
        raw = bytes.fromhex(pkt.udp.payload.replace(":", ""))

        ipal_message = IpalMessage(
            id=self._id_counter.get_next_id(),
            timestamp=float(pkt.sniff_time.timestamp()),
            src=f"{pkt['IP'].src}:{pkt['UDP'].srcport}:{raw[5]}",
            dest=f"{pkt['IP'].dst}:{pkt['UDP'].dstport}",
            protocol="MAVLink",
            length=HEADER_LENGTH + raw[1],  # ignores optional checksum
            type=struct.unpack("<I", raw[7:10] + b"\0")[0],
            activity="inform",
            responds_to=[],
        )

        # udp payload includes first 10 bytes of MAVLink header
        # the payload length is indicated in byte 1
        # so proper payload is [header_len:header_len+payload_len]
        ipal_message.data = {"_raw": raw[HEADER_LENGTH : HEADER_LENGTH + raw[1]].hex()}

        return [ipal_message]
