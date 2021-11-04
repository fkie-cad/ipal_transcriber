import transcriber.settings as settings


def position_sign(vars):
    if vars[1] in ["N", "E"]:
        return +vars[0]
    elif vars[1] in ["S", "W"]:
        return -vars[0]
    else:
        settings.logger.warning("Encountered unknown character '{}'".format(vars[1]))


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
            "method": position_sign,
            "name": "latitude",
            "remove": True,
        },
        {  # Position East-West
            "type": "RMC",
            "var": ["RMC4", "RMC5"],
            "method": position_sign,
            "name": "longitude",
            "remove": True,
        },
        {  # Position North-South
            "type": "GGA",
            "var": ["GGA1", "GGA2"],
            "method": position_sign,
            "name": "latitude",
            "remove": True,
        },
        {  # Position East-West
            "type": "GGA",
            "var": ["GGA3", "GGA4"],
            "method": position_sign,
            "name": "longitude",
            "remove": True,
        },
    ],
    "rename": {
        ".*:GG": "GNSS",
    },
}
