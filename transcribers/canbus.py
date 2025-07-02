import transcriber.settings as settings
from transcriber.messages import Activity, IpalMessage
from transcribers.transcriber import Transcriber


class CANTranscriber(Transcriber):
    _name = "canbus"

    """
    The CAN transcriber heavily depends on the usage of rule files (cf. README.md) to decode the actual CAN data.
    Have a look at the exemplary rule file at `misc/rules/canbus_rules.py`.
    """

    def matches_protocol(self, pkt):
        return "CAN" in pkt

    def parse_packet(self, pkt):

        res = []

        for can in pkt.get_multiple_layers("CAN"):

            length = int(can.len)
            code = int(can.id)
            can_data = str(pkt.data.data)

            res.append(
                IpalMessage(
                    id=self._id_counter.get_next_id(),
                    src=None,
                    dest=None,
                    timestamp=float(pkt.sniff_time.timestamp()),
                    protocol=self._name,
                    length=length,
                    type=code,
                    data={"raw_data": can_data, "arbitration_id": code},
                    activity=Activity.INFORM,
                )
            )

        return res

    def match_response(self, requests, response):
        remove_from_queue = []
        return remove_from_queue
