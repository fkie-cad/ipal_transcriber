from time import time
from transcriber.messages import IpalMessage, Activity
from transcribers.transcriber import Transcriber
import transcriber.settings as settings


class MQTTProtocol:

    CONNECT = 1
    CONNACK = 2
    PUBLISH = 3
    PUBACK = 4
    PUBREC = 5
    PUBREL = 6
    PUBCOMP = 7
    SUBSCRIBE = 8
    SUBACK = 9
    UNSUBSCRIBE = 10
    UNSUBACK = 11
    PINGREQ = 12
    PINGRESP = 13
    DISCONNECT = 14

    def __init__(self):
        self._msgid_topics = dict()

    def save_state(self, request):
        type = self.msgtype(request)
        if type == self.SUBSCRIBE and request.get_field("msgid") and request.get_field("topic"):
            self._msgid_topics[request.get_field("msgid")] = request.get_field("topic")

    def resolve_state(self, request):
        type = self.msgtype(request)
        state = {}
        if type == self.SUBACK:
            topic = self._msgid_topics[request.get_field("msgid")]
            state[topic] = None
        return state

    def data(self, request):
        type = self.msgtype(request)
        if type in [self.PUBLISH, self.SUBSCRIBE]:
            try:
                value = "".join([chr(int(c, 16))
                                for c in str(request.get_field("msg")).split(":")])
            except:
                value = None
            return {
                request.get_field("topic"): value
            }
        elif type == self.SUBACK:
            _data = self.resolve_state(request)
            return _data
        else:
            return {}

    @classmethod
    def activity(cls, message_type):
        return {
            cls.CONNECT: Activity.COMMAND,
            cls.CONNACK: Activity.ACTION,
            cls.PUBLISH: Activity.INFORM,
            cls.PUBACK: Activity.ACTION,
            cls.PUBREC: Activity.ACTION,
            cls.PUBREL: Activity.ACTION,
            cls.PUBCOMP: Activity.COMMAND,
            cls.SUBSCRIBE: Activity.INTERROGATE,
            cls.SUBACK: Activity.INFORM,
            cls.UNSUBSCRIBE: Activity.COMMAND,
            cls.UNSUBACK: Activity.ACTION,
            cls.PINGREQ: Activity.INTERROGATE,
            cls.PINGRESP: Activity.INFORM,
            cls.DISCONNECT: Activity.COMMAND
        }.get(message_type, Activity.UNKNOWN)

    @classmethod
    def msgtype(cls, request):
        return int(request.get_field("msgtype"))


class MQTTTranscriber(Transcriber):
    _name = "mqtt"  # currently only 3.1
    mqtt_state = MQTTProtocol()

    @classmethod
    def state_identifier(cls, msg, key):
        if msg.activity in [str(Activity.INTERROGATE), str(Activity.COMMAND)]:
            return "{}:{}".format(msg.dest, key)
        elif msg.activity in [str(Activity.INFORM), str(Activity.ACTION)]:
            return "{}:{}".format(msg.src, key)
        else:
            settings.logger.critical("Unknown activity {}".format(msg.activity))
            return "{}:{}".format(msg.src, key)

    def matches_protocol(self, pkt):
        return "MQTT" in pkt

    def parse_packet(self, pkt):
        mqtt_layer = pkt.get_multiple_layers("MQTT")
        requests = []

        for request in mqtt_layer:
            requests.append(self._mqtt_to_ipal(request, pkt))

        return requests

    def _mqtt_to_ipal(self, request, pkt):
        self.mqtt_state.save_state(request)
        src = "{}:{}".format(pkt["IP"].src, pkt["TCP"].srcport)
        dest = "{}:{}".format(pkt["IP"].dst, pkt["TCP"].dstport)
        type = MQTTProtocol.msgtype(request)
        length = request.len
        activity = MQTTProtocol.activity(type)
        try:
            responds = [int(pkt["TCP"].get_field("analysis_acks_frame"))]
        except:
            responds = []

        # Usually this is static, but state may need transition (like SUBACK->topic)
        data = self.mqtt_state.data(request)

        return IpalMessage(
            id=self._id_counter.get_next_id(),
            timestamp=float(pkt.sniff_time.timestamp()),
            protocol=self._name,
            malicious=None,
            src=src,
            dest=dest,
            length=length,
            crc=None,
            type=type,
            activity=str(activity),
            responds_to=responds,
            data=data
        )
