import transcriber.settings as settings
from transcriber.messages import Activity, IpalMessage
from transcribers.transcriber import Transcriber


class MAVLinkTranscriber(Transcriber):
    _name = "MAVLink"

    @classmethod
    def matches_protocol(self, pkt):
        return "MAVLINK_PROTO" in pkt

    def parse_packet(self, pkt):
        HEADER_LENGTH = 10
        ipal_message = IpalMessage(
            id=self._id_counter.get_next_id(),
            timestamp=pkt.sniff_time.timestamp(),  # included so its nicer
            src=f"{pkt['IP'].src}:{pkt['UDP'].srcport}:{pkt['MAVLINK_PROTO'].sysid}",
            dest=f"{pkt['IP'].dst}:{pkt['UDP'].dstport}",
            protocol="MAVLink",
            length=len(bytes.fromhex(pkt.udp.payload.replace(':', ''))),  # length of full packet, just payload would be: pkt['MAVLINK_PROTO'].length
            type=int(pkt['MAVLINK_PROTO'].msgid),
            activity="inform",
            responds_to=[],
            # load from hex formated udp payload, strip ":" so it's proper hex
            # turn into bytes as we can access bytes by indices
            # udp payload includes first 10 bytes of MAVLink header: Assumption: MAVLink2 with fixed header length 10
            # so proper payload is [header_len:payload_len+header_len]
            data={'_raw': ((bytes.fromhex(pkt.udp.payload.replace(':', '')))[HEADER_LENGTH:int(pkt['MAVLINK_PROTO'].length) + HEADER_LENGTH]).hex()}
        )
        return [ipal_message]
