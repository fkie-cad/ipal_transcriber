import json
import sys
from enum import Enum, auto


class Activity(Enum):
    INTERROGATE = 0  # Request for data
    INFORM = 1  # Requested/unsolicited data
    COMMAND = 2  # Change values or system/call method
    ACTION = 3  # Response to commands or (unsolicited) performed actions
    CONFIRMATION = 4  # for a msg specifically only acknowledging a prior msg.
    UNKNOWN = 99

    def __str__(self):
        if self == Activity.INTERROGATE:
            return "interrogate"
        elif self == Activity.COMMAND:
            return "command"
        elif self == Activity.INFORM:
            return "inform"
        elif self == Activity.ACTION:
            return "action"
        elif self == Activity.CONFIRMATION:
            return "confirmation"
        elif self == Activity.UNKNOWN:
            return "unknown"
        else:
            raise TypeError(self)

    @classmethod
    def from_str(cls, label):
        if label == "interrogate":
            return Activity.INTERROGATE
        elif label == "command":
            return Activity.COMMAND
        elif label == "inform":
            return Activity.INFORM
        elif label == "action":
            return Activity.ACTION
        elif label == "confirmation":
            return Activity.CONFIRMATION
        elif label == "unknown":
            return Activity.UNKNOWN
        else:
            raise TypeError(label)


class IpalMessage:
    _add_to_request_queue = False
    _match_to_requests = False

    def __init__(
        self,
        id=-1,
        timestamp=-1,
        protocol="",
        malicious=None,
        src="",
        dest="",
        length=None,
        crc=None,
        type=None,
        activity=Activity.UNKNOWN,
        responds_to=None,
        data=None,
        flow=None,
    ):
        # Meta data
        self.id = id
        self.timestamp = timestamp
        self.protocol = protocol
        self.malicious = malicious

        # Basic packet features
        self.src = src
        self.dest = dest
        self.length = length
        self.crc = crc

        # Message type
        self.type = type
        self.activity = activity
        self.responds_to = responds_to
        if responds_to is None:
            # https://docs.quantifiedcode.com/python-anti-patterns/correctness/mutable_default_value_as_argument.html
            self.responds_to = []

        # Process data
        self.data = data if data is not None else {}

        # Internal transcriber data
        self._flow = flow

    def __str__(self):
        return json.dumps(self.export_json(), indent=4)

    @classmethod
    def from_json(cls, js):
        return IpalMessage(
            id=js["id"],
            timestamp=js["timestamp"],
            protocol=js["protocol"],
            malicious=js["malicious"],
            src=js["src"],
            dest=js["dest"],
            length=js["length"],
            crc=js["crc"],
            type=js["type"],
            activity=Activity.from_str(js["activity"]),
            responds_to=js["responds to"],
            data=js["data"],
        )

    def export_json(self):
        return {
            "id": self.id,
            "timestamp": float(self.timestamp),
            "protocol": self.protocol,
            "malicious": self.malicious,
            "src": self.src,
            "dest": self.dest,
            "length": self.length,
            "crc": self.crc,
            "type": self.type,
            "activity": str(self.activity),
            "responds to": self.responds_to,
            "data": self.data,
        }
