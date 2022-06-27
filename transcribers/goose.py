import struct
from dataclasses import dataclass
from typing import List, Union, Optional

from pyshark.packet.fields import LayerField
from pyshark.packet.packet import Packet

from transcriber.messages import IpalMessage, Activity
from transcribers.transcriber import Transcriber


class UnknownValueTypeException(Exception):
    pass


@dataclass
class TimeQuality:
    leap_second_known: bool
    clock_failure: bool
    clock_not_synchronized: bool
    time_accuracy_of_fractions_of_second: Optional[int]


@dataclass
class Quality:
    validity: str
    overflow: bool
    out_of_range: bool
    bad_reference: bool
    oscillatory: bool
    failure: bool
    old_data: bool
    inconsistent: bool
    inaccurate: bool
    source: str
    test: bool
    operator_blocked: bool
    raw_bitstring: str


class GooseTranscriber(Transcriber):
    _name = "goose"

    """
    IEC 61850-7-1, 6.4.3.4
    The GOOSE model has several attributes that control the publishing process, for example:
    – GoEna to remotely enable/disable the publishing,
    – GoID send in the message to be used as a handle for the receiving application,
    – DatSet references the data set whose values are to be published,
    – ConfRev contains the configuration revision to indicate deletion of a member of the data set or the
      reordering of the members, or changing the DatSet reference,
    – NdsCom indicates in the message that some commissioning is required.

    IEC 61850-8-1
    goCBRef
    This VisibleString shall have a maximum size of 129 octets. The value shall be the reference to the
    associated GoCB that is controlling the GOOSE message.
    (GoCB is a GOOSE Control Block)
    """

    def matches_protocol(self, pkt: Packet) -> bool:
        return "GOOSE" in pkt

    def parse_packet(self, pkt: Packet) -> List[IpalMessage]:
        ipal_message = IpalMessage(
            id=self._id_counter.get_next_id(),
            protocol=self._name,
            src=pkt["eth"].src.replace(":", ""),
            dest=pkt["eth"].dst.replace(":", ""),
            timestamp=float(pkt.sniff_time.timestamp()),
            length=int(pkt["goose"].length),
            activity=Activity.INFORM,
        )
        dat_set = pkt["goose"].datset
        ipal_message.data = {
            f"{dat_set}-{i:03d}": self.to_value(data)
            for i, data in enumerate(pkt["goose"].data.fields)
        }
        ipal_message.data["stNum"] = int(pkt["goose"].stNum.showname_value)
        ipal_message.data["sqNum"] = int(pkt["goose"].sqNum.showname_value)

        return [ipal_message]

    def to_value(self, data: LayerField) -> Union[int, float, str]:
        if data.showname_value == "structure (2)":
            return "[structure]"
        if data.showname_value == "bit-string (4)":
            return self.parse_bitstring(data.binary_value)
        if data.showname_value == "integer (5)":
            return int.from_bytes(data.binary_value, "big")
        if data.showname_value == "floating-point (7)":
            return self.parse_float(data.binary_value)
        if data.showname_value == "boolean (3)":
            return self.parse_bool(data.binary_value)
        if data.showname_value == "visible-string (10)":
            return data.binary_value.decode()
        if data.showname_value == "utc-time (17)":
            return self.parse_utc_time(data.binary_value)
        raise UnknownValueTypeException(data.showname_value)

    @staticmethod
    def parse_bitstring(data: bytes) -> str:
        if len(data) == 3:
            return GooseTranscriber.parse_quality(data).raw_bitstring
        length_of_padding_at_end = data[0]
        full_bit_string = GooseTranscriber.format_bytes_as_bitstring(data[1:])
        return full_bit_string[:-length_of_padding_at_end]

    @staticmethod
    def format_bytes_as_bitstring(data) -> str:
        bytes_as_bits = [GooseTranscriber.byte_to_eight_bits(x) for x in data]
        return "".join(bytes_as_bits)

    @staticmethod
    def byte_to_eight_bits(single_byte: int) -> str:
        return bin(single_byte)[2:].zfill(8)

    @staticmethod
    def parse_quality(data: bytes) -> Quality:
        validity = GooseTranscriber.get_validity((data[1] & 0b11000000) >> 6)
        overflow = bool(data[1] & 0b00100000)
        out_of_range = bool(data[1] & 0b00010000)
        bad_reference = bool(data[1] & 0b00001000)
        oscillatory = bool(data[1] & 0b00000100)
        failure = bool(data[1] & 0b00000010)
        old_data = bool(data[1] & 0b00000001)
        inconsistent = bool(data[2] & 0b10000000)
        inaccurate = bool(data[2] & 0b01000000)
        source = "Substituted" if bool(data[2] & 0b00100000) else "Process"
        test = bool(data[2] & 0b00010000)
        operator_blocked = bool(data[2] & 0b00001000)
        raw_bitstring = f"{data[1]:0>8b}{data[2]:0>8b}"[:13]

        return Quality(
            validity=validity,
            overflow=overflow,
            out_of_range=out_of_range,
            bad_reference=bad_reference,
            oscillatory=oscillatory,
            failure=failure,
            old_data=old_data,
            inconsistent=inconsistent,
            inaccurate=inaccurate,
            source=source,
            test=test,
            operator_blocked=operator_blocked,
            raw_bitstring=raw_bitstring,
        )

    @staticmethod
    def get_validity(value: int) -> str:
        cases = ["Good", "Invalid", "Reserved", "Questionable"]
        return cases[value]

    @staticmethod
    def parse_bool(data: bytes) -> str:
        return data.hex()

    @staticmethod
    def parse_float(data: bytes) -> float:
        if data[0] == 8:
            return struct.unpack("!f", data[1:])[0]
        raise NotImplementedError()

    @staticmethod
    def parse_utc_time(data: bytes) -> float:
        seconds = struct.unpack("!i", data[:4])[0]
        nanoseconds = struct.unpack("!i", b"\x00" + data[4:7])[0]
        return seconds + (nanoseconds / (2**24))

    @staticmethod
    def parse_utc_time_quality(data: bytes) -> TimeQuality:
        quality = data[7]

        leap_second_known = bool(quality & 0b10000000)
        clock_failure = bool(quality & 0b01000000)
        clock_not_synchronized = bool(quality & 0b00100000)
        time_accuracy_of_fractions_of_second = quality & 0b00011111
        if time_accuracy_of_fractions_of_second == 31:
            time_accuracy_of_fractions_of_second = None

        return TimeQuality(
            leap_second_known=leap_second_known,
            clock_failure=clock_failure,
            clock_not_synchronized=clock_not_synchronized,
            time_accuracy_of_fractions_of_second=time_accuracy_of_fractions_of_second,
        )
