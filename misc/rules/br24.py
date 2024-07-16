from math import sqrt
from typing import List, Union

from transcribers.br24 import _ImagePacketType, _RegisterPacketType, _ReportPacketType


def scale(vars: List[int]) -> float:
    return vars[0] * 100 / 255


def parse_filter(vars: List[int]) -> Union[int, float]:
    if vars[0] == 0:
        # manual mode, float value
        return scale(vars[1:])
    # auto mode, enum value
    return vars[1]


def parse_ascii(vars: List[List[int]]) -> str:
    res = ""
    for char in vars[0]:
        if char == 0:
            continue
        res += chr(char)
    return res


JS = {
    "protocols": ["Navico-BR24"],
    "rules": [
        {
            "type": str(_ReportPacketType.REP_SETTINGS),
            "var": ["range"],
            "method": lambda x: x[0] / 10,
            "name": "range",
            "remove": False,
        },
        {
            "type": str(_ReportPacketType.REP_SETTINGS),
            "var": ["gain"],
            "method": scale,
            "name": "gain",
            "remove": False,
        },
        {
            "type": str(_ReportPacketType.REP_SETTINGS),
            "var": ["sea_clutter"],
            "method": scale,
            "name": "sea_clutter",
            "remove": False,
        },
        {
            "type": str(_ReportPacketType.REP_SETTINGS),
            "var": ["rain_clutter"],
            "method": scale,
            "name": "rain_clutter",
            "remove": False,
        },
        {
            "type": str(_ReportPacketType.REP_FIRMWARE),
            "var": ["firmware_date"],
            "method": parse_ascii,
            "name": "firmware_date",
            "remove": False,
        },
        {
            "type": str(_ReportPacketType.REP_FIRMWARE),
            "var": ["firmware_time"],
            "method": parse_ascii,
            "name": "firmware_time",
            "remove": False,
        },
        {
            "type": str(_ReportPacketType.REP_BEARING),
            "var": ["bearing_alignment"],
            "method": lambda x: x[0] / 10,
            "name": "bearing_alignment",
            "remove": False,
        },
        {
            "type": str(_ReportPacketType.REP_SCAN),
            "var": ["sls"],
            "method": scale,
            "name": "sls",
            "remove": False,
        },
        {
            "type": str(_RegisterPacketType.REG_FILTERS),
            "var": ["auto_flag", "filter_value"],
            "method": parse_filter,
            "name": "filter_value",
            "remove": False,
        },
    ],
}


for i in range(32):
    JS["rules"].append(
        {
            "type": str(_ImagePacketType.IMG_DEFAULT),
            "var": [f"scanline_{i}:angle"],
            "method": lambda x: x[0] // 2,
            "name": f"scanline_{i}:angle",
            "remove": False,
        }
    )
    JS["rules"].append(
        {
            "type": str(_ImagePacketType.IMG_DEFAULT),
            "var": [f"scanline_{i}:range"],
            "method": lambda x: (x[0] * 10) / sqrt(2),
            "name": f"scanline_{i}:range",
            "remove": False,
        }
    )
