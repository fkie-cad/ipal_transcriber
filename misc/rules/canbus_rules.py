import cantools

DBC_PATH = "misc/rules/subaru.dbc"  # default name in repo
try:
    DB = cantools.database.load_file(DBC_PATH)
except Exception:
    DB = None


def decode_can(vars_):

    arb_id, payload = vars_
    if DB is None:
        return {"unknown_message": payload}

    try:
        decoded_raw = DB.decode_message(
            arb_id,
            bytes.fromhex(payload),
            decode_choices=False,  # enums instead of names
        )
        decoded = {}
        for k, v in decoded_raw.items():
            if isinstance(v, (int, float, str)):
                decoded[k] = v
            else:
                decoded[k] = v.name

        return {**decoded}
    except KeyError:  # ID not in DBC
        return {"unknown_message": payload}
    except Exception:  # malformed frame, etc.
        return {"decode_error": payload}


JS = {
    "protocols": ["canbus"],
    "rules": [
        {
            "var": ["arbitration_id", "raw_data"],
            "method": decode_can,
            "flatten": True,
            "remove": False,
        },
        {
            "var": ["raw_data"],
            "remove": True,
        },
    ],
    "rename": {},
}
