import struct


def to_float(vars):
    if vars[0] is None:
        return None

    return struct.unpack("<f", bytes.fromhex(vars[0]))[0]


def to_int(vars):
    if vars[0] is None:
        return None

    return struct.unpack("<h", bytes.fromhex(vars[0]))[0]


JS = {
    "protocols": ["cip"],
    "rename": {
        "192.168.1.10:44818": "PLC1",
        "192.168.1.20:44818": "PLC2",
        "192.168.1.30:44818": "PLC3",
    },
    "rules": [
        {
            "type": "76",
            "var": ["LIT101"],
            "method": to_float,
            "name": "LIT101",
            "remove": False,
        },
        {
            "type": "76",
            "var": ["FIT201"],
            "method": to_float,
            "name": "FIT201",
            "remove": False,
        },
        {
            "type": "76",
            "var": ["LIT301"],
            "method": to_float,
            "name": "LIT301",
            "remove": False,
        },
        {
            "type": "76",
            "var": ["MV101"],
            "method": to_int,
            "name": "MV101",
            "remove": False,
        },
        {
            "type": "76",
            "var": ["P101"],
            "method": to_int,
            "name": "P101",
            "remove": False,
        },
    ],
}
