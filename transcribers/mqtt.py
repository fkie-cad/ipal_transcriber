# This MQTT Transcriber was implemented by
# Leonardo Pompe, RWTH Aachen University, 2022
# Stefan Lenz, RWTH Aachen University, 2022
# Tim Nebel, RWTH Aachen University, 2022

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

    PUBLISH_COMMANDS = {PUBLISH, PUBACK, PUBREC, PUBREL, PUBCOMP}
    TOPIC_COMMANDS = {SUBSCRIBE, SUBACK, UNSUBSCRIBE, UNSUBACK}
    REQUEST_COMMANDS = {CONNECT, PUBLISH, PUBREL, SUBSCRIBE, UNSUBSCRIBE, PINGREQ}
    RESPONSE_COMMANDS = {CONNACK, PUBACK, PUBREC, PUBCOMP, SUBACK, UNSUBACK, PINGRESP}
    SIMPLE_REQUESTS = {CONNECT, UNSUBSCRIBE, PINGREQ}

    @classmethod
    def data(cls, request):
        type = cls.msgtype(request)
        if type in [cls.PUBLISH, cls.SUBSCRIBE]:
            try:
                value = "".join(
                    [chr(int(c, 16)) for c in str(request.get_field("msg")).split(":")]
                )
            except:  # noqa: E722
                value = None
            return {request.get_field("topic"): value}
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
            cls.DISCONNECT: Activity.COMMAND,
        }.get(message_type, Activity.UNKNOWN)

    @classmethod
    def msgtype(cls, request):
        return int(request.get_field("msgtype"))

    @classmethod
    def command_response(cls, request):
        # empty set means initiate
        return {
            cls.CONNECT: set(),
            cls.CONNACK: {cls.CONNECT},
            cls.PUBLISH: set(),
            cls.PUBACK: {cls.PUBLISH},
            cls.PUBREC: {cls.PUBLISH},
            cls.PUBREL: {cls.PUBLISH},
            cls.PUBCOMP: {cls.PUBLISH},
            cls.SUBSCRIBE: set(),
            cls.SUBACK: {cls.SUBSCRIBE},
            cls.UNSUBSCRIBE: set(),
            cls.UNSUBACK: {cls.UNSUBSCRIBE},
            cls.PINGREQ: set(),
            cls.PINGRESP: {cls.PINGREQ},
            cls.DISCONNECT: set(),
        }.get(request.type, set())


class MQTTTranscriber(Transcriber):
    _name = "mqtt"  # currently only 3.1

    @classmethod
    def state_identifier(cls, msg, key):

        if msg.activity in [Activity.INTERROGATE, Activity.COMMAND]:
            return "{}:{}".format(msg.dest, key)
        elif msg.activity in [Activity.INFORM, Activity.ACTION]:
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
        src = "{}:{}".format(pkt["IP"].src, pkt["TCP"].srcport)
        dest = "{}:{}".format(pkt["IP"].dst, pkt["TCP"].dstport)
        type = MQTTProtocol.msgtype(request)
        length = 2 + int(request.len)  # 2 Byte MQTT Headers
        activity = MQTTProtocol.activity(type)

        data = MQTTProtocol.data(request)

        ipal_message = IpalMessage(
            id=self._id_counter.get_next_id(),
            timestamp=float(pkt.sniff_time.timestamp()),
            protocol=self._name,
            malicious=None,
            src=src,
            dest=dest,
            length=length,
            crc=None,
            type=type,
            activity=activity,
            responds_to=None,  # added in match_response
            data=data,
        )

        # depending on the message type, add the message to the request queue or match it to a request in the queue
        ipal_message._add_to_request_queue = type in MQTTProtocol.REQUEST_COMMANDS
        ipal_message._match_to_requests = type in MQTTProtocol.RESPONSE_COMMANDS

        return ipal_message

    def match_response(self, requests, response):
        remove_from_queue = []
        match_types = MQTTProtocol.command_response(response)

        if len(match_types) == 0:
            return []

        for request in requests:
            if (
                request.type in match_types
                and request.src == response.dest
                and request.dest == response.src
            ):
                if (
                    request.type == MQTTProtocol.PUBLISH
                    and response.type == MQTTProtocol.PUBACK
                ):
                    response.responds_to.append(request.id)
                    remove_from_queue.append(request)
                    break

                elif (
                    request.type == MQTTProtocol.PUBLISH
                    and response.type == MQTTProtocol.PUBREC
                ):  # PubREC
                    response.responds_to.append(request.id)
                    # do not remove request from queue because PUBCOMP is part of the 4-way exchange MQTT with in QoS 2

                elif response.type == MQTTProtocol.PUBCOMP:  # PubCOMP
                    # completes the 4 way exchange of QoS 2 MQTT
                    # includes two requests: PUBLISH and PUBREL
                    if request.type == MQTTProtocol.PUBLISH:
                        response.responds_to.append(request.id)
                        remove_from_queue.append(request)
                    elif request.type == MQTTProtocol.PUBREL:
                        response.responds_to.append(request.id)
                        remove_from_queue.append(request)

                elif response.type == MQTTProtocol.SUBACK:
                    # check for matching topics
                    request_topics = set(request.data.keys())
                    response_topics = set(response.data.keys())
                    if response_topics.issubset(request_topics):
                        response.responds_to.append(request.id)
                        remove_from_queue.append(request)

                # all other message types are matched by source and destination and by the following message types:
                # Connect 1 -> ConnACK 2
                # Unsubscribe 10 -> UnsubACK 11
                # PingREQ 12 -> PingRESP 13
                elif (
                    request.type in MQTTProtocol.SIMPLE_REQUESTS
                    and request.type + 1 == response.type
                ):
                    response.responds_to.append(request.id)
                    remove_from_queue.append(request)

        return remove_from_queue
