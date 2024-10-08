from enum import Enum
from typing import Any, Dict, List

import transcriber.settings as settings


class NavigationStatus(Enum):
    UNDERWAY_ENGINE = 0
    AT_ANCHOR = 1
    NOT_UNDER_COMMAND = 2
    RESTRICTED_MANOEUVRABILITY = 3
    CONSTRAINED_BY_DRAUGHT = 4
    MOORED = 5
    AGROUND = 6
    ENGAGED_IN_FISHING = 7
    UNDERWAY_SAILING = 8
    RESERVED_FOR_FUTURE_1 = 9
    RESERVED_FOR_FUTURE_2 = 10
    RESERVED_FOR_FUTURE_3 = 11
    RESERVED_FOR_FUTURE_4 = 12
    RESERVED_FOR_FUTURE_5 = 13
    AIS_SART_ACTIVE = 14
    NOT_DEFINED = 15


def decode_ais(fragments: List[str]) -> Dict[str, Any]:
    """
    given an armored AIS data string, dearmor and decode it,
    returning fields and their values as a {field:value} dictionary
    """
    radio_channel = fragments[0][0]
    bits = []

    for tokens in fragments:
        assert radio_channel == tokens[0]  # Same radio channel across fragments
        payload = tokens[1]
        fill_bits = int(tokens[2])
        bits += _dearmor_ascii(payload, fill_bits)

    fields = _decode_bit_string(bits)
    fields["radio"] = radio_channel

    return fields


def _dearmor_ascii(payload: str, fill_bits: int) -> List[int]:
    """
    remove the ASCII armoring from the raw data string
    returns the dearmored bit string as a List of bits
    """

    output = [0] * (len(payload) * 6)
    index = 0

    for char in payload:
        byte = ord(char) - 48
        byte = byte if byte < 40 else byte - 8

        for i in range(6):
            output[index + 5 - i] = byte % 2
            byte >>= 1
        index += 6

    if fill_bits > 0:
        output = output[:-fill_bits]
    return output


def _decode_bit_string(bits: List[int]) -> Dict[str, Any]:
    """
    decode the dearmored bit string, returns the fields and their
    value as a {field:value} dictionary
    """

    # check the message type field
    message_type = _bits_to_unsigned_int(bits, 0, 5)
    if message_type == 1 or message_type == 2 or message_type == 3:
        return _decode_class_A_report(bits)  # class A report

    elif message_type == 5:
        return _decode_static_and_voyage_related_data(bits)

    elif message_type == 18:
        return _decode_standard_class_B_report(bits)
    # 19 Extended Class B equipment position report

    elif message_type == 24:
        return _decode_static_data_report(bits)

    # 21 Aids-to-navigation report
    # 25 Static data report

    settings.logger.warning(f"Unsupported AIS message type ({message_type})")
    return {"message_type": message_type}


def _bits_to_unsigned_int(bits: List[int], start: int, end: int) -> int:
    """
    interpret the given range of a bit string as an unsigned integer
    as specified in the NMEA AIS sentence standard
    """

    assert start <= end
    val = 0
    index = start

    while index <= end:
        val <<= 1
        val += bits[index]
        index += 1

    return val


def _bits_to_signed_int(bits: List[int], start: int, end: int) -> int:
    """
    interpret the given range of a bit string as a signed integer
    as specified in the NMEA AIS sentence standard
    """
    assert start < end
    val = 0
    index = start + 1
    complement = 0

    if bits[start] == 1:
        # negative number, take the complement of each bit
        complement = 1

    while index <= end:
        val <<= 1
        val += (bits[index] + complement) % 2
        index += 1

    if complement == 1:
        val += 1
        val *= -1

    return val


def _bits_to_signed_float(
    bits: List[int], start: int, end: int, resolution: float
) -> float:
    """
    interpret the given range of a bit string as a signed float
    as specified in the NMEA AIS sentence standard

    the resolution should be the step size by which the range of the
    actual integer value is scaled.
    """

    int_val = _bits_to_signed_int(bits, start, end)
    return resolution * int_val


def _bits_to_unsigned_float(
    bits: List[int], start: int, end: int, resolution: float
) -> float:
    """
    interpret the given range of a bit string as an unsigned float
    as specified in the NMEA AIS sentence standard

    the resolution should be the step size by which the range of the
    actual integer value is scaled.
    """
    int_val = _bits_to_unsigned_int(bits, start, end)
    return resolution * int_val


def _bits_to_bool(bits: List[int], start: int, end: int) -> bool:
    """
    interpret the given range of a bit string as a bool
    as specified in the NMEA AIS sentence standard
    """
    assert start == end
    return bits[start] == 1


def _bits_to_string(bits: List[int], start: int, end: int) -> str:
    """
    interpret the given range of a bit string as a string
    as specified in the NMEA AIS sentence standard
    """
    ASCII = "@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_ !\"#$%&'()*+,-./0123456789:;<=>?"
    assert (end - start + 1) % 6 == 0
    out = ""

    for i in range((end - start + 1) // 6):
        b = _bits_to_unsigned_int(bits, start + 6 * i, start + 6 * (i + 1) - 1)
        if b == 0:
            break
        out += ASCII[b]

    return out


def _decode_class_A_report(bits: List[int]) -> Dict[str, Any]:
    """
    parser for AIS class A position reports (1, 2, 3)
    https://www.navcen.uscg.gov/?pageName=AISMessagesA
    """
    assert len(bits) >= 149

    rot = _bits_to_signed_int(bits, 42, 49)
    if rot == -128:
        rot = None
    else:
        rot = _bits_to_signed_float(bits, 42, 49, 0.21128248)
        # square while preserving sign
        rot = rot * rot if rot > 0.0 else -1 * rot * rot

    true_heading = _bits_to_unsigned_int(bits, 128, 136)
    if true_heading == 511:  # not available
        true_heading = None

    output = {
        "message_type": _bits_to_unsigned_int(bits, 0, 5),
        "repeat_indicator": _bits_to_unsigned_int(bits, 6, 7),
        "mmsi": _bits_to_unsigned_int(bits, 8, 37),
        "navigation_status": NavigationStatus(_bits_to_unsigned_int(bits, 38, 41)).name,
        "rate_of_turn": rot,
        "speed_over_ground": _bits_to_unsigned_float(
            bits, 50, 59, 0.1
        ),  # speed in knots
        "position_accuracy": _bits_to_bool(bits, 60, 60),
        "longitude": _bits_to_signed_float(bits, 61, 88, 0.00000166666666666),
        "latitude": _bits_to_signed_float(bits, 89, 115, 0.00000166666666666),
        "course_over_ground": _bits_to_unsigned_float(bits, 116, 127, 0.1),
        "true_heading": true_heading,
        "timestamp": _bits_to_unsigned_int(bits, 137, 142),
        "maneuver_indicator": _bits_to_unsigned_int(bits, 143, 144),
        # "spare": (bits, ),
        "raim": _bits_to_bool(bits, 148, 148),
    }

    return output


def _decode_static_and_voyage_related_data(bits: List[int]) -> Dict[str, Any]:
    """
    parser for AIS CLASS A SHIP STATIC AND VOYAGE RELATED DATA (5)
    https://www.navcen.uscg.gov/?pageName=AISMessagesAStatic
    """
    assert len(bits) >= 424

    output = {
        "message_type": _bits_to_unsigned_int(bits, 0, 5),
        "repeat_indicator": _bits_to_unsigned_int(bits, 6, 7),
        "mmsi": _bits_to_unsigned_int(bits, 8, 37),
        "ais_version": _bits_to_unsigned_int(bits, 38, 39),
        "imo_number": _bits_to_unsigned_int(bits, 40, 69),
        "call_sign": _bits_to_string(bits, 70, 111),
        "name": _bits_to_string(bits, 112, 231),
        "vessel_type": _bits_to_unsigned_int(bits, 232, 239),
        # "overall_dimension": (bits, 240, 269), # TODO
        # "gnss_device_type": (bits, 270, 273), # TODO
        # "eta": (bits, 274, 293), # TODO
        # "maximum_draught": (bits, 294, 301), # TODO
        "destination": _bits_to_string(bits, 302, 421),
        "dte": _bits_to_bool(bits, 422, 422),
        # "spare": (bits, 423, 423),
    }

    return output


def _decode_standard_class_B_report(bits: List[int]) -> Dict[str, Any]:
    """
    parser for AIS STANDARD CLASS B EQUIPMENT POSITION REPORT (18)
    https://www.navcen.uscg.gov/?pageName=AISMessagesB
    """
    assert len(bits) >= 168

    true_heading = _bits_to_unsigned_int(bits, 124, 132)
    if true_heading == 511:  # not available
        true_heading = None

    output = {
        "message_type": _bits_to_unsigned_int(bits, 0, 5),
        "repeat_indicator": _bits_to_unsigned_int(bits, 6, 7),
        "mmsi": _bits_to_unsigned_int(bits, 8, 37),
        # "spare": (bits, 38, 45),
        "speed_over_ground": _bits_to_unsigned_float(
            bits, 46, 55, 0.1
        ),  # speed in knots
        "position_accuracy": _bits_to_bool(bits, 56, 56),
        "longitude": _bits_to_signed_float(bits, 57, 84, 0.00000166666666666),
        "latitude": _bits_to_signed_float(bits, 85, 111, 0.00000166666666666),
        "course_over_ground": _bits_to_unsigned_float(bits, 112, 123, 0.1),
        "true_heading": true_heading,
        "timestamp": _bits_to_unsigned_int(bits, 133, 138),
        # "spare": (bits, 139, 140),
        "unit_flag": _bits_to_bool(bits, 141, 141),
        "display_flag": _bits_to_bool(bits, 142, 142),
        "dsc_flag": _bits_to_bool(bits, 143, 143),
        "band_flag": _bits_to_bool(bits, 144, 144),
        "message_22_flag": _bits_to_bool(bits, 145, 145),
        "mode_flag": _bits_to_bool(bits, 146, 146),
        "raim": _bits_to_bool(bits, 147, 147),
        "communication_sector_flag": _bits_to_bool(bits, 148, 148),
        # "communication_state": _bits_to_bool(bits, 149, 167), # TODO
    }

    return output


def _decode_static_data_report(bits: List[int]) -> Dict[str, Any]:
    """
    parser for STATIC DATA REPORT (24)
    https://www.navcen.uscg.gov/?pageName=AISMessagesB
    """
    assert len(bits) >= 160

    part = _bits_to_unsigned_int(bits, 38, 39)

    if part == 0:  # Part A
        output = {
            "message_type": _bits_to_unsigned_int(bits, 0, 5),
            "repeat_indicator": _bits_to_unsigned_int(bits, 6, 7),
            "mmsi": _bits_to_unsigned_int(bits, 8, 37),
            "part": _bits_to_unsigned_int(bits, 38, 39),
            "name": _bits_to_string(bits, 40, 159),
        }

    else:  # Part B
        output = {
            "message_type": _bits_to_unsigned_int(bits, 0, 5),
            "repeat_indicator": _bits_to_unsigned_int(bits, 6, 7),
            "mmsi": _bits_to_unsigned_int(bits, 8, 37),
            "part": _bits_to_unsigned_int(bits, 38, 39),
            "vessel_type": _bits_to_unsigned_int(bits, 40, 47),
            "vendor_id": _bits_to_unsigned_int(bits, 48, 89),
            "call_sign": _bits_to_string(bits, 90, 131),
            # "overall_dimension": _bits_to_unsigned_int(bits, 132, 161), # TODO
            "gnss_device_type": _bits_to_unsigned_int(bits, 162, 165),
            # "spare": (bits, 166, 167),
        }

    return output
