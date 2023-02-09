from transcriber.messages import IpalMessage, Activity
from transcribers.nmea0183 import NMEA0183


class IEC450Transcriber(NMEA0183):
    _name = "iec450"

    def matches_protocol(self, pkt):
        if "UDP" not in pkt or not pkt["UDP"].get("payload", default=None):
            return False

        raw = bytes.fromhex(pkt["UDP"].payload.replace(":", ""))
        if raw is None or raw[:6] != b"UdPbC\x00" or raw[-2:] != b"\r\n":
            return False

        return True

    def parse_packet(self, pkt):
        ip = pkt["IP"]
        udp = pkt["UDP"]
        raw = bytes.fromhex(pkt["UDP"].payload.replace(":", ""))
        msg = raw.decode("ascii")

        src = "{}:{}".format(ip.src, udp.srcport)
        dest = "{}:{}".format(ip.dst, udp.dstport)
        timestamp = float(pkt.sniff_time.timestamp())
        length = len(msg)

        res = IpalMessage(
            id=self._id_counter.get_next_id(),
            src=src,
            dest=dest,
            timestamp=timestamp,
            protocol=self._name,
            activity=Activity.INFORM,
            length=length,
        )

        # extract data/NMEA0183, assume that msg corresponds to exactly one (1) sentence
        msg = msg.split("\\")[2]
        ipal_message = self.parse_sentence(msg, res)
        return [ipal_message] if ipal_message is not None else []
