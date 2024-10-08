from enum import Enum, auto

import transcriber.settings as settings
from transcriber.messages import Activity, IpalMessage
from transcribers.ais import decode_ais
from transcribers.transcriber import Transcriber


class VariableType(Enum):
    NUMBER = auto()
    STRING = auto()


class NMEA0183(Transcriber):
    # Abstract NMEA 0183 class responsible for parsing raw NMEA 0183 sentences
    # independently of the overlying protocol (UDP or IEC-450).

    _sentence_structures = {
        "DBT": [
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.STRING,
        ],
        "DPT": [VariableType.NUMBER, VariableType.NUMBER, VariableType.NUMBER],
        "GGA": [
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.STRING,
            VariableType.STRING,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.NUMBER,
        ],
        "GLL": [
            VariableType.STRING,
            VariableType.STRING,
            VariableType.STRING,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.STRING,
        ],
        "GNS": [
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.STRING,
            VariableType.STRING,
            VariableType.STRING,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
        ],
        "GSA": [
            VariableType.STRING,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
        ],
        "GSV": [
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
        ],
        "HDM": [VariableType.NUMBER, VariableType.STRING],
        "HDT": [VariableType.NUMBER, VariableType.STRING],
        "RMC": [
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.STRING,
            VariableType.STRING,
            VariableType.STRING,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.STRING,
        ],
        "ROT": [VariableType.NUMBER, VariableType.STRING],
        "RPM": [
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.STRING,
        ],
        "TLL": [
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.STRING,
            VariableType.STRING,
            VariableType.STRING,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.STRING,
        ],
        "TTM": [
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.STRING,
            VariableType.STRING,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.STRING,
        ],
        "VBW": [
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.STRING,
        ],
        "VHW": [
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.STRING,
        ],
        "VLW": [
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.STRING,
        ],
        "VTG": [
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.STRING,
        ],
        "ZDA": [
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
        ],
        "RMB": [
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.STRING,
            VariableType.STRING,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.STRING,
        ],
        "APB": [
            VariableType.STRING,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.STRING,
            VariableType.STRING,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.STRING,
        ],
        "RSA": [
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.STRING,
        ],
        "DTM": [
            VariableType.STRING,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.STRING,
            VariableType.NUMBER,
            VariableType.STRING,
        ],
    }

    def checksum(self, msg):
        checksum = 0x00
        for c in msg:
            checksum ^= ord(c)
        return checksum

    @classmethod
    def state_identifier(cls, msg, key):
        # In NMEA 0183 usually only the key is relevant and neither src nor dest are.
        return key

    def parse_sentence(self, msg, res):
        if msg[0] == "!" and not msg.startswith("!AIVDM"):
            settings.logger.warning(f"Unsupported NMEA type '{msg[0]}'")
            return None

        msg = msg[1:-2]  # remove header ($ or !) and \r\n

        if msg[-3] == "*":  # has checksum?
            # Test and remove checksum from message
            res.crc = self.checksum(msg[:-3]) == int(msg[-2:], 16)
            msg = msg[:-3]

        hdr = msg.split(",")[0]
        tokens = msg.split(",")[1:]

        if hdr[0] == "P":  # Proprietary sentence
            settings.logger.warning(f"Unsupported proprietary NMEA sentence '{hdr}'")
            return None

        elif hdr[4] == "Q":  # Query sentence
            talker = hdr[:2]
            listener = hdr[2:4]
            request = tokens[0]

            res.src += f":{talker}"
            res.dest += f":{listener}"
            res.activity = Activity.INTERROGATE
            res.type = request
            res.data = {}

            res._add_to_request_queue = True
            res._flow = (res.dest.split(":")[0], request)

        elif hdr == "AIVDM":
            talkerID = hdr[:2]
            sentenceID = hdr[2:]

            res.src += f":{talkerID}"
            res.type = sentenceID

            # AIS can be fragmented
            fragments = int(tokens[0])

            if fragments == 1:
                res.data = decode_ais([tokens[3:]])

            else:
                message_id = int(tokens[2])
                res._flow = (res.src.split(":")[0], sentenceID, message_id)

                res._add_to_request_queue = True
                res._match_to_requests = True
                res._ais = tokens

        else:  # Regular sentence
            talkerID = hdr[:2]
            sentenceID = hdr[2:]

            res.src += f":{talkerID}"
            res.type = sentenceID

            res._match_to_requests = True
            res._flow = (res.src.split(":")[0], sentenceID)

            if sentenceID not in self._sentence_structures:
                settings.logger.warning(f"Not implemented NMEA sentence '{sentenceID}'")
                return None
            structure = self._sentence_structures[sentenceID]

            # The number of tokens might not match the number of expected fields,
            # e.g. GLL sentences only have a 7th element from NMEA version 2.3 onwards
            # Warn on lack of tokens, error on excessive tokens
            if len(tokens) > len(structure):
                settings.logger.error(
                    f"{sentenceID} sentence contains {len(tokens)} fields, expected {len(structure)}: discarding sentence"
                )
                return None
            if len(tokens) < len(structure):
                settings.logger.warning(
                    f"{sentenceID} sentence contains {len(tokens)} fields, expected {len(structure)}"
                )

            for i in range(len(tokens)):
                token = tokens[i]
                varname = sentenceID + str(i)

                if token == "":  # Ignore tokens not present
                    continue

                if structure[i] == VariableType.NUMBER:
                    if "." in token:
                        res.data[varname] = float(token)
                    else:
                        res.data[varname] = int(token)

                elif structure[i] == VariableType.STRING:
                    res.data[varname] = token

                else:
                    settings.logger.warning("Not implemented variable type")

        return res

    def match_response(self, requests, response):
        if response.type == "VDM":  # match fragmented AIS sentences
            assert (
                len(set([msg._ais[0] for msg in requests])) == 1
            )  # only one fragment size
            assert (
                len(set([msg._ais[2] for msg in requests])) == 1
            )  # the same message id

            fragments = int(requests[0]._ais[0])
            if len(requests) < fragments:
                return []  # not all fragments collected yet

            # Assemble fragments
            ais = [None] * fragments
            for msg in requests:
                ais[int(msg._ais[1]) - 1] = msg._ais[3:]

            # Adapt response
            response.data = decode_ais(ais)
            response.responds_to = [r.id for r in requests if r.id != response.id]

            return requests  # Delete messages  from queue

        else:  # match NMEA-0183 requests
            response.responds_to = [r.id for r in requests]
            return requests


class NMEA0183UDPTranscriber(NMEA0183):
    _name = "nmea0183udp"

    def matches_protocol(self, pkt):
        if "UDP" not in pkt:
            return False

        raw = bytes.fromhex(pkt["UDP"].payload.replace(":", ""))

        if (
            raw is None
            or (raw[0] != ord("$") and raw[0] != ord("!"))
            or (raw[-2:] != b"\r\n")
        ):
            return False

        return True

    def parse_packet(self, pkt):
        ip = pkt["IP"]
        udp = pkt["UDP"]
        msg = bytes.fromhex(udp.payload.replace(":", "")).decode("ascii")

        src = f"{ip.src}:{udp.srcport}"
        dest = f"{ip.dst}:{udp.dstport}"
        timestamp = float(pkt.sniff_time.timestamp())

        # handle the case where more than one sentence is in the UDP payload
        sentences = [f"{sentence}\r\n" for sentence in msg.split("\r\n")[:-1]]

        ipal_messages = []

        for sentence in sentences:
            length = len(sentence)

            res = IpalMessage(
                id=self._id_counter.get_next_id(),
                src=src,
                dest=dest,
                timestamp=timestamp,
                protocol=self._name,
                activity=Activity.INFORM,
                length=length,
            )

            ipal_message = self.parse_sentence(sentence, res)
            if ipal_message is not None:
                ipal_messages.append(ipal_message)

        return ipal_messages
