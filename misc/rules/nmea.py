from typing import List

import transcriber.settings as settings


def ddm_str_to_dd(vars: List[str]) -> float:
    mod = 1
    hours = 0
    minutes = 0.0

    if vars[1] in ["N", "S"]:
        hours = int(vars[0][:2])
        minutes = float(vars[0][2:])
    elif vars[1] in ["W", "E"]:
        hours = int(vars[0][:3])
        minutes = float(vars[0][3:])
    else:
        settings.logger.warning(f"Encountered unknown character '{vars[1]}'")

    if vars[1] in ["S", "W"]:
        mod = -1

    return mod * (hours + (minutes / 60.0))


JS = {
    "protocols": ["nmea0183udp", "iec450"],
    "rules": [
        {  # Rename RMC0 -> UTC
            "type": "RMC",
            "var": ["RMC0"],
            "method": lambda x: x[0],
            "name": "UTC",
            "remove": True,
        },
        {  # Position North-South
            "type": "RMC",
            "var": ["RMC2", "RMC3"],
            "method": ddm_str_to_dd,
            "name": "latitude",
            "remove": True,
        },
        {  # Position East-West
            "type": "RMC",
            "var": ["RMC4", "RMC5"],
            "method": ddm_str_to_dd,
            "name": "longitude",
            "remove": True,
        },
        {  # Position North-South
            "type": "GGA",
            "var": ["GGA1", "GGA2"],
            "method": ddm_str_to_dd,
            "name": "latitude",
            "remove": True,
        },
        {  # Position East-West
            "type": "GGA",
            "var": ["GGA3", "GGA4"],
            "method": ddm_str_to_dd,
            "name": "longitude",
            "remove": True,
        },
    ],
    "rename": {
        ".*:GG": "GNSS",
    },
}
