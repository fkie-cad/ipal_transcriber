# These rules have been automatically generated with the mavlinik_xml_parser.py tool!
import struct

JS = {
    "protocols": ["MAVLink"],
    "rules": [
        {
            "type": "1",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "onboard_control_sensors_present(MAV_SYS_STATUS_SENSOR)",
            "remove": False,
        },
        {
            "type": "1",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "onboard_control_sensors_enabled(MAV_SYS_STATUS_SENSOR)",
            "remove": False,
        },
        {
            "type": "1",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "onboard_control_sensors_health(MAV_SYS_STATUS_SENSOR)",
            "remove": False,
        },
        {
            "type": "1",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "onboard_control_sensors_present_extended(MAV_SYS_STATUS_SENSOR_EXTENDED)",
            "remove": False,
        },
        {
            "type": "1",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "onboard_control_sensors_enabled_extended(MAV_SYS_STATUS_SENSOR_EXTENDED)",
            "remove": False,
        },
        {
            "type": "1",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "onboard_control_sensors_health_extended(MAV_SYS_STATUS_SENSOR_EXTENDED)",
            "remove": False,
        },
        {
            "type": "1",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][48:52]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "load",
            "remove": False,
        },
        {
            "type": "1",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][52:56]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "voltage_battery",
            "remove": False,
        },
        {
            "type": "1",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][56:60]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "current_battery",
            "remove": False,
        },
        {
            "type": "1",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][60:64]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "drop_rate_comm",
            "remove": False,
        },
        {
            "type": "1",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][64:68]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "errors_comm",
            "remove": False,
        },
        {
            "type": "1",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][68:72]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "errors_count1",
            "remove": False,
        },
        {
            "type": "1",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][72:76]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "errors_count2",
            "remove": False,
        },
        {
            "type": "1",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][76:80]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "errors_count3",
            "remove": False,
        },
        {
            "type": "1",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][80:84]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "errors_count4",
            "remove": False,
        },
        {
            "type": "1",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<b", bytes.fromhex(x[0][84:86]).ljust(struct.calcsize("<b"), b"\x00")
            )[0],
            "name": "battery_remaining",
            "remove": False,
        },
        {
            "type": "2",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_unix_usec",
            "remove": False,
        },
        {
            "type": "2",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "4",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "4",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "seq",
            "remove": False,
        },
        {
            "type": "4",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][24:26]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "4",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][26:28]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "5",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][0:2]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "5",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][2:4]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "control_request",
            "remove": False,
        },
        {
            "type": "5",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][4:6]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "version",
            "remove": False,
        },
        {
            "type": "5",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 6 : i + 8]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 50, 2)
                ]
            ).rstrip("\x00"),
            "name": "passkey",
            "remove": False,
        },
        {
            "type": "6",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][0:2]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "gcs_system_id",
            "remove": False,
        },
        {
            "type": "6",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][2:4]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "control_request",
            "remove": False,
        },
        {
            "type": "6",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][4:6]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "ack",
            "remove": False,
        },
        {
            "type": "7",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 0 : i + 2]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 64, 2)
                ]
            ).rstrip("\x00"),
            "name": "key",
            "remove": False,
        },
        {
            "type": "8",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "timestamp",
            "remove": False,
        },
        {
            "type": "8",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "tx_rate",
            "remove": False,
        },
        {
            "type": "8",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "rx_rate",
            "remove": False,
        },
        {
            "type": "8",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "messages_sent",
            "remove": False,
        },
        {
            "type": "8",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "messages_received",
            "remove": False,
        },
        {
            "type": "8",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "messages_lost",
            "remove": False,
        },
        {
            "type": "8",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][56:60]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "rx_parse_err",
            "remove": False,
        },
        {
            "type": "8",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][60:64]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "tx_overflows",
            "remove": False,
        },
        {
            "type": "8",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][64:68]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "rx_overflows",
            "remove": False,
        },
        {
            "type": "8",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][68:70]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "tx_buf",
            "remove": False,
        },
        {
            "type": "8",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][70:72]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "rx_buf",
            "remove": False,
        },
        {
            "type": "11",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "custom_mode",
            "remove": False,
        },
        {
            "type": "11",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][8:10]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "11",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][10:12]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "base_mode(MAV_MODE)",
            "remove": False,
        },
        {
            "type": "20",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][0:4]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "param_index",
            "remove": False,
        },
        {
            "type": "20",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][4:6]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "20",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][6:8]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "20",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 8 : i + 10]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 32, 2)
                ]
            ).rstrip("\x00"),
            "name": "param_id",
            "remove": False,
        },
        {
            "type": "21",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][0:2]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "21",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][2:4]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "22",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "param_value",
            "remove": False,
        },
        {
            "type": "22",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][8:12]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "param_count",
            "remove": False,
        },
        {
            "type": "22",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][12:16]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "param_index",
            "remove": False,
        },
        {
            "type": "22",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 16 : i + 18]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 32, 2)
                ]
            ).rstrip("\x00"),
            "name": "param_id",
            "remove": False,
        },
        {
            "type": "22",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][48:50]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "param_type(MAV_PARAM_TYPE)",
            "remove": False,
        },
        {
            "type": "23",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "param_value",
            "remove": False,
        },
        {
            "type": "23",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][8:10]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "23",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][10:12]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "23",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 12 : i + 14]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 32, 2)
                ]
            ).rstrip("\x00"),
            "name": "param_id",
            "remove": False,
        },
        {
            "type": "23",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][44:46]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "param_type(MAV_PARAM_TYPE)",
            "remove": False,
        },
        {
            "type": "24",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "24",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lat",
            "remove": False,
        },
        {
            "type": "24",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lon",
            "remove": False,
        },
        {
            "type": "24",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "alt",
            "remove": False,
        },
        {
            "type": "24",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "alt_ellipsoid",
            "remove": False,
        },
        {
            "type": "24",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "h_acc",
            "remove": False,
        },
        {
            "type": "24",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "v_acc",
            "remove": False,
        },
        {
            "type": "24",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][64:72]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "vel_acc",
            "remove": False,
        },
        {
            "type": "24",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][72:80]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "hdg_acc",
            "remove": False,
        },
        {
            "type": "24",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][80:84]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "eph",
            "remove": False,
        },
        {
            "type": "24",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][84:88]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "epv",
            "remove": False,
        },
        {
            "type": "24",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][88:92]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "vel",
            "remove": False,
        },
        {
            "type": "24",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][92:96]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "cog",
            "remove": False,
        },
        {
            "type": "24",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][96:100]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "yaw",
            "remove": False,
        },
        {
            "type": "24",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][100:102]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "fix_type(GPS_FIX_TYPE)",
            "remove": False,
        },
        {
            "type": "24",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][102:104]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "satellites_visible",
            "remove": False,
        },
        {
            "type": "25",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][0:2]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "satellites_visible",
            "remove": False,
        },
        {
            "type": "25",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 2 : i + 4]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 40, 2)
            ],
            "name": "satellite_prn",
            "remove": False,
        },
        {
            "type": "25",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 42 : i + 44]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 40, 2)
            ],
            "name": "satellite_used",
            "remove": False,
        },
        {
            "type": "25",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 82 : i + 84]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 40, 2)
            ],
            "name": "satellite_elevation",
            "remove": False,
        },
        {
            "type": "25",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 122 : i + 124]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 40, 2)
            ],
            "name": "satellite_azimuth",
            "remove": False,
        },
        {
            "type": "25",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 162 : i + 164]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 40, 2)
            ],
            "name": "satellite_snr",
            "remove": False,
        },
        {
            "type": "26",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "26",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][8:12]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "xacc",
            "remove": False,
        },
        {
            "type": "26",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][12:16]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "yacc",
            "remove": False,
        },
        {
            "type": "26",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][16:20]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "zacc",
            "remove": False,
        },
        {
            "type": "26",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][20:24]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "xgyro",
            "remove": False,
        },
        {
            "type": "26",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][24:28]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "ygyro",
            "remove": False,
        },
        {
            "type": "26",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][28:32]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "zgyro",
            "remove": False,
        },
        {
            "type": "26",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][32:36]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "xmag",
            "remove": False,
        },
        {
            "type": "26",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][36:40]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "ymag",
            "remove": False,
        },
        {
            "type": "26",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][40:44]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "zmag",
            "remove": False,
        },
        {
            "type": "26",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][44:48]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "temperature",
            "remove": False,
        },
        {
            "type": "27",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "27",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][16:20]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "xacc",
            "remove": False,
        },
        {
            "type": "27",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][20:24]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "yacc",
            "remove": False,
        },
        {
            "type": "27",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][24:28]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "zacc",
            "remove": False,
        },
        {
            "type": "27",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][28:32]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "xgyro",
            "remove": False,
        },
        {
            "type": "27",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][32:36]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "ygyro",
            "remove": False,
        },
        {
            "type": "27",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][36:40]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "zgyro",
            "remove": False,
        },
        {
            "type": "27",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][40:44]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "xmag",
            "remove": False,
        },
        {
            "type": "27",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][44:48]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "ymag",
            "remove": False,
        },
        {
            "type": "27",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][48:52]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "zmag",
            "remove": False,
        },
        {
            "type": "27",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][52:56]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "temperature",
            "remove": False,
        },
        {
            "type": "27",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][56:58]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "id",
            "remove": False,
        },
        {
            "type": "28",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "28",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][16:20]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "press_abs",
            "remove": False,
        },
        {
            "type": "28",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][20:24]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "press_diff1",
            "remove": False,
        },
        {
            "type": "28",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][24:28]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "press_diff2",
            "remove": False,
        },
        {
            "type": "28",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][28:32]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "temperature",
            "remove": False,
        },
        {
            "type": "29",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "29",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "press_abs",
            "remove": False,
        },
        {
            "type": "29",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "press_diff",
            "remove": False,
        },
        {
            "type": "29",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][24:28]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "temperature",
            "remove": False,
        },
        {
            "type": "29",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][28:32]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "temperature_press_diff",
            "remove": False,
        },
        {
            "type": "30",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "30",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "roll",
            "remove": False,
        },
        {
            "type": "30",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "pitch",
            "remove": False,
        },
        {
            "type": "30",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yaw",
            "remove": False,
        },
        {
            "type": "30",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "rollspeed",
            "remove": False,
        },
        {
            "type": "30",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "pitchspeed",
            "remove": False,
        },
        {
            "type": "30",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yawspeed",
            "remove": False,
        },
        {
            "type": "31",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "31",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "q1",
            "remove": False,
        },
        {
            "type": "31",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "q2",
            "remove": False,
        },
        {
            "type": "31",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "q3",
            "remove": False,
        },
        {
            "type": "31",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "q4",
            "remove": False,
        },
        {
            "type": "31",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "rollspeed",
            "remove": False,
        },
        {
            "type": "31",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "pitchspeed",
            "remove": False,
        },
        {
            "type": "31",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yawspeed",
            "remove": False,
        },
        {
            "type": "31",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 64 : i + 72]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 32, 8)
            ],
            "name": "repr_offset_q",
            "remove": False,
        },
        {
            "type": "32",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "32",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "x",
            "remove": False,
        },
        {
            "type": "32",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "y",
            "remove": False,
        },
        {
            "type": "32",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "z",
            "remove": False,
        },
        {
            "type": "32",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vx",
            "remove": False,
        },
        {
            "type": "32",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vy",
            "remove": False,
        },
        {
            "type": "32",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vz",
            "remove": False,
        },
        {
            "type": "33",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "33",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lat",
            "remove": False,
        },
        {
            "type": "33",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lon",
            "remove": False,
        },
        {
            "type": "33",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "alt",
            "remove": False,
        },
        {
            "type": "33",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "relative_alt",
            "remove": False,
        },
        {
            "type": "33",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][40:44]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "vx",
            "remove": False,
        },
        {
            "type": "33",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][44:48]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "vy",
            "remove": False,
        },
        {
            "type": "33",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][48:52]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "vz",
            "remove": False,
        },
        {
            "type": "33",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][52:56]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "hdg",
            "remove": False,
        },
        {
            "type": "34",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "34",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][8:12]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "chan1_scaled",
            "remove": False,
        },
        {
            "type": "34",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][12:16]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "chan2_scaled",
            "remove": False,
        },
        {
            "type": "34",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][16:20]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "chan3_scaled",
            "remove": False,
        },
        {
            "type": "34",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][20:24]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "chan4_scaled",
            "remove": False,
        },
        {
            "type": "34",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][24:28]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "chan5_scaled",
            "remove": False,
        },
        {
            "type": "34",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][28:32]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "chan6_scaled",
            "remove": False,
        },
        {
            "type": "34",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][32:36]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "chan7_scaled",
            "remove": False,
        },
        {
            "type": "34",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][36:40]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "chan8_scaled",
            "remove": False,
        },
        {
            "type": "34",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][40:42]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "port",
            "remove": False,
        },
        {
            "type": "34",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][42:44]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "rssi",
            "remove": False,
        },
        {
            "type": "35",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "35",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][8:12]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan1_raw",
            "remove": False,
        },
        {
            "type": "35",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][12:16]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan2_raw",
            "remove": False,
        },
        {
            "type": "35",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][16:20]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan3_raw",
            "remove": False,
        },
        {
            "type": "35",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][20:24]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan4_raw",
            "remove": False,
        },
        {
            "type": "35",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][24:28]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan5_raw",
            "remove": False,
        },
        {
            "type": "35",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][28:32]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan6_raw",
            "remove": False,
        },
        {
            "type": "35",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][32:36]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan7_raw",
            "remove": False,
        },
        {
            "type": "35",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][36:40]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan8_raw",
            "remove": False,
        },
        {
            "type": "35",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][40:42]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "port",
            "remove": False,
        },
        {
            "type": "35",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][42:44]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "rssi",
            "remove": False,
        },
        {
            "type": "36",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "36",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][8:12]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "servo1_raw",
            "remove": False,
        },
        {
            "type": "36",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][12:16]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "servo2_raw",
            "remove": False,
        },
        {
            "type": "36",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][16:20]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "servo3_raw",
            "remove": False,
        },
        {
            "type": "36",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][20:24]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "servo4_raw",
            "remove": False,
        },
        {
            "type": "36",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][24:28]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "servo5_raw",
            "remove": False,
        },
        {
            "type": "36",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][28:32]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "servo6_raw",
            "remove": False,
        },
        {
            "type": "36",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][32:36]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "servo7_raw",
            "remove": False,
        },
        {
            "type": "36",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][36:40]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "servo8_raw",
            "remove": False,
        },
        {
            "type": "36",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][40:44]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "servo9_raw",
            "remove": False,
        },
        {
            "type": "36",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][44:48]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "servo10_raw",
            "remove": False,
        },
        {
            "type": "36",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][48:52]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "servo11_raw",
            "remove": False,
        },
        {
            "type": "36",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][52:56]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "servo12_raw",
            "remove": False,
        },
        {
            "type": "36",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][56:60]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "servo13_raw",
            "remove": False,
        },
        {
            "type": "36",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][60:64]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "servo14_raw",
            "remove": False,
        },
        {
            "type": "36",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][64:68]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "servo15_raw",
            "remove": False,
        },
        {
            "type": "36",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][68:72]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "servo16_raw",
            "remove": False,
        },
        {
            "type": "36",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][72:74]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "port",
            "remove": False,
        },
        {
            "type": "37",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][0:4]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "start_index",
            "remove": False,
        },
        {
            "type": "37",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][4:8]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "end_index",
            "remove": False,
        },
        {
            "type": "37",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][8:10]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "37",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][10:12]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "37",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][12:14]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "mission_type(MAV_MISSION_TYPE)",
            "remove": False,
        },
        {
            "type": "38",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][0:4]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "start_index",
            "remove": False,
        },
        {
            "type": "38",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][4:8]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "end_index",
            "remove": False,
        },
        {
            "type": "38",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][8:10]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "38",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][10:12]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "38",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][12:14]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "mission_type(MAV_MISSION_TYPE)",
            "remove": False,
        },
        {
            "type": "39",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "param1",
            "remove": False,
        },
        {
            "type": "39",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "param2",
            "remove": False,
        },
        {
            "type": "39",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "param3",
            "remove": False,
        },
        {
            "type": "39",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "param4",
            "remove": False,
        },
        {
            "type": "39",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "x",
            "remove": False,
        },
        {
            "type": "39",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "y",
            "remove": False,
        },
        {
            "type": "39",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "z",
            "remove": False,
        },
        {
            "type": "39",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][56:60]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "seq",
            "remove": False,
        },
        {
            "type": "39",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][60:64]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "command(MAV_CMD)",
            "remove": False,
        },
        {
            "type": "39",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][64:66]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "39",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][66:68]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "39",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][68:70]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "frame(MAV_FRAME)",
            "remove": False,
        },
        {
            "type": "39",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][70:72]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "current",
            "remove": False,
        },
        {
            "type": "39",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][72:74]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "autocontinue",
            "remove": False,
        },
        {
            "type": "39",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][74:76]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "mission_type(MAV_MISSION_TYPE)",
            "remove": False,
        },
        {
            "type": "40",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][0:4]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "seq",
            "remove": False,
        },
        {
            "type": "40",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][4:6]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "40",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][6:8]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "40",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][8:10]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "mission_type(MAV_MISSION_TYPE)",
            "remove": False,
        },
        {
            "type": "41",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][0:4]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "seq",
            "remove": False,
        },
        {
            "type": "41",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][4:6]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "41",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][6:8]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "42",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][0:4]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "seq",
            "remove": False,
        },
        {
            "type": "42",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][4:8]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "total",
            "remove": False,
        },
        {
            "type": "42",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][8:10]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "mission_state(MISSION_STATE)",
            "remove": False,
        },
        {
            "type": "42",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][10:12]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "mission_mode",
            "remove": False,
        },
        {
            "type": "43",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][0:2]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "43",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][2:4]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "43",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][4:6]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "mission_type(MAV_MISSION_TYPE)",
            "remove": False,
        },
        {
            "type": "44",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][0:4]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "count",
            "remove": False,
        },
        {
            "type": "44",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][4:6]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "44",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][6:8]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "44",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][8:10]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "mission_type(MAV_MISSION_TYPE)",
            "remove": False,
        },
        {
            "type": "45",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][0:2]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "45",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][2:4]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "45",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][4:6]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "mission_type(MAV_MISSION_TYPE)",
            "remove": False,
        },
        {
            "type": "46",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][0:4]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "seq",
            "remove": False,
        },
        {
            "type": "47",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][0:2]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "47",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][2:4]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "47",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][4:6]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "type(MAV_MISSION_RESULT)",
            "remove": False,
        },
        {
            "type": "47",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][6:8]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "mission_type(MAV_MISSION_TYPE)",
            "remove": False,
        },
        {
            "type": "48",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "48",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "latitude",
            "remove": False,
        },
        {
            "type": "48",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "longitude",
            "remove": False,
        },
        {
            "type": "48",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "altitude",
            "remove": False,
        },
        {
            "type": "48",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][40:42]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "49",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "49",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "latitude",
            "remove": False,
        },
        {
            "type": "49",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "longitude",
            "remove": False,
        },
        {
            "type": "49",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "altitude",
            "remove": False,
        },
        {
            "type": "50",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "param_value0",
            "remove": False,
        },
        {
            "type": "50",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "scale",
            "remove": False,
        },
        {
            "type": "50",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "param_value_min",
            "remove": False,
        },
        {
            "type": "50",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "param_value_max",
            "remove": False,
        },
        {
            "type": "50",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][32:36]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "param_index",
            "remove": False,
        },
        {
            "type": "50",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][36:38]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "50",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][38:40]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "50",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 40 : i + 42]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 32, 2)
                ]
            ).rstrip("\x00"),
            "name": "param_id",
            "remove": False,
        },
        {
            "type": "50",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][72:74]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "parameter_rc_channel_index",
            "remove": False,
        },
        {
            "type": "51",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][0:4]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "seq",
            "remove": False,
        },
        {
            "type": "51",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][4:6]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "51",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][6:8]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "51",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][8:10]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "mission_type(MAV_MISSION_TYPE)",
            "remove": False,
        },
        {
            "type": "54",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "p1x",
            "remove": False,
        },
        {
            "type": "54",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "p1y",
            "remove": False,
        },
        {
            "type": "54",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "p1z",
            "remove": False,
        },
        {
            "type": "54",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "p2x",
            "remove": False,
        },
        {
            "type": "54",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "p2y",
            "remove": False,
        },
        {
            "type": "54",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "p2z",
            "remove": False,
        },
        {
            "type": "54",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][48:50]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "54",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][50:52]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "54",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][52:54]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "frame(MAV_FRAME)",
            "remove": False,
        },
        {
            "type": "55",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "p1x",
            "remove": False,
        },
        {
            "type": "55",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "p1y",
            "remove": False,
        },
        {
            "type": "55",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "p1z",
            "remove": False,
        },
        {
            "type": "55",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "p2x",
            "remove": False,
        },
        {
            "type": "55",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "p2y",
            "remove": False,
        },
        {
            "type": "55",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "p2z",
            "remove": False,
        },
        {
            "type": "55",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][48:50]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "frame(MAV_FRAME)",
            "remove": False,
        },
        {
            "type": "61",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "61",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 16 : i + 24]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 32, 8)
            ],
            "name": "q",
            "remove": False,
        },
        {
            "type": "61",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "rollspeed",
            "remove": False,
        },
        {
            "type": "61",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "pitchspeed",
            "remove": False,
        },
        {
            "type": "61",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][64:72]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yawspeed",
            "remove": False,
        },
        {
            "type": "61",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 72 : i + 80]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 72, 8)
            ],
            "name": "covariance",
            "remove": False,
        },
        {
            "type": "62",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "nav_roll",
            "remove": False,
        },
        {
            "type": "62",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "nav_pitch",
            "remove": False,
        },
        {
            "type": "62",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "alt_error",
            "remove": False,
        },
        {
            "type": "62",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "aspd_error",
            "remove": False,
        },
        {
            "type": "62",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "xtrack_error",
            "remove": False,
        },
        {
            "type": "62",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][40:44]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "nav_bearing",
            "remove": False,
        },
        {
            "type": "62",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][44:48]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "target_bearing",
            "remove": False,
        },
        {
            "type": "62",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][48:52]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "wp_dist",
            "remove": False,
        },
        {
            "type": "63",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "63",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lat",
            "remove": False,
        },
        {
            "type": "63",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lon",
            "remove": False,
        },
        {
            "type": "63",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "alt",
            "remove": False,
        },
        {
            "type": "63",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "relative_alt",
            "remove": False,
        },
        {
            "type": "63",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vx",
            "remove": False,
        },
        {
            "type": "63",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vy",
            "remove": False,
        },
        {
            "type": "63",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][64:72]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vz",
            "remove": False,
        },
        {
            "type": "63",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 72 : i + 80]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 288, 8)
            ],
            "name": "covariance",
            "remove": False,
        },
        {
            "type": "63",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][360:362]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "estimator_type(MAV_ESTIMATOR_TYPE)",
            "remove": False,
        },
        {
            "type": "64",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "64",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "x",
            "remove": False,
        },
        {
            "type": "64",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "y",
            "remove": False,
        },
        {
            "type": "64",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "z",
            "remove": False,
        },
        {
            "type": "64",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vx",
            "remove": False,
        },
        {
            "type": "64",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vy",
            "remove": False,
        },
        {
            "type": "64",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vz",
            "remove": False,
        },
        {
            "type": "64",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][64:72]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "ax",
            "remove": False,
        },
        {
            "type": "64",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][72:80]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "ay",
            "remove": False,
        },
        {
            "type": "64",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][80:88]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "az",
            "remove": False,
        },
        {
            "type": "64",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 88 : i + 96]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 360, 8)
            ],
            "name": "covariance",
            "remove": False,
        },
        {
            "type": "64",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][448:450]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "estimator_type(MAV_ESTIMATOR_TYPE)",
            "remove": False,
        },
        {
            "type": "65",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "65",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][8:12]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan1_raw",
            "remove": False,
        },
        {
            "type": "65",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][12:16]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan2_raw",
            "remove": False,
        },
        {
            "type": "65",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][16:20]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan3_raw",
            "remove": False,
        },
        {
            "type": "65",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][20:24]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan4_raw",
            "remove": False,
        },
        {
            "type": "65",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][24:28]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan5_raw",
            "remove": False,
        },
        {
            "type": "65",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][28:32]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan6_raw",
            "remove": False,
        },
        {
            "type": "65",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][32:36]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan7_raw",
            "remove": False,
        },
        {
            "type": "65",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][36:40]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan8_raw",
            "remove": False,
        },
        {
            "type": "65",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][40:44]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan9_raw",
            "remove": False,
        },
        {
            "type": "65",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][44:48]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan10_raw",
            "remove": False,
        },
        {
            "type": "65",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][48:52]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan11_raw",
            "remove": False,
        },
        {
            "type": "65",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][52:56]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan12_raw",
            "remove": False,
        },
        {
            "type": "65",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][56:60]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan13_raw",
            "remove": False,
        },
        {
            "type": "65",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][60:64]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan14_raw",
            "remove": False,
        },
        {
            "type": "65",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][64:68]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan15_raw",
            "remove": False,
        },
        {
            "type": "65",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][68:72]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan16_raw",
            "remove": False,
        },
        {
            "type": "65",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][72:76]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan17_raw",
            "remove": False,
        },
        {
            "type": "65",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][76:80]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan18_raw",
            "remove": False,
        },
        {
            "type": "65",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][80:82]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "chancount",
            "remove": False,
        },
        {
            "type": "65",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][82:84]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "rssi",
            "remove": False,
        },
        {
            "type": "66",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][0:4]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "req_message_rate",
            "remove": False,
        },
        {
            "type": "66",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][4:6]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "66",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][6:8]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "66",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][8:10]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "req_stream_id",
            "remove": False,
        },
        {
            "type": "66",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][10:12]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "start_stop",
            "remove": False,
        },
        {
            "type": "67",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][0:4]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "message_rate",
            "remove": False,
        },
        {
            "type": "67",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][4:6]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "stream_id",
            "remove": False,
        },
        {
            "type": "67",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][6:8]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "on_off",
            "remove": False,
        },
        {
            "type": "69",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][0:4]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "x",
            "remove": False,
        },
        {
            "type": "69",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][4:8]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "y",
            "remove": False,
        },
        {
            "type": "69",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][8:12]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "z",
            "remove": False,
        },
        {
            "type": "69",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][12:16]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "r",
            "remove": False,
        },
        {
            "type": "69",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][16:20]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "buttons",
            "remove": False,
        },
        {
            "type": "69",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][20:24]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "buttons2",
            "remove": False,
        },
        {
            "type": "69",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][24:28]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "s",
            "remove": False,
        },
        {
            "type": "69",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][28:32]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "t",
            "remove": False,
        },
        {
            "type": "69",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][32:34]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target",
            "remove": False,
        },
        {
            "type": "69",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][34:36]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "enabled_extensions",
            "remove": False,
        },
        {
            "type": "70",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][0:4]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan1_raw",
            "remove": False,
        },
        {
            "type": "70",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][4:8]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan2_raw",
            "remove": False,
        },
        {
            "type": "70",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][8:12]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan3_raw",
            "remove": False,
        },
        {
            "type": "70",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][12:16]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan4_raw",
            "remove": False,
        },
        {
            "type": "70",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][16:20]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan5_raw",
            "remove": False,
        },
        {
            "type": "70",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][20:24]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan6_raw",
            "remove": False,
        },
        {
            "type": "70",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][24:28]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan7_raw",
            "remove": False,
        },
        {
            "type": "70",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][28:32]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan8_raw",
            "remove": False,
        },
        {
            "type": "70",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][32:36]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan9_raw",
            "remove": False,
        },
        {
            "type": "70",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][36:40]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan10_raw",
            "remove": False,
        },
        {
            "type": "70",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][40:44]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan11_raw",
            "remove": False,
        },
        {
            "type": "70",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][44:48]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan12_raw",
            "remove": False,
        },
        {
            "type": "70",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][48:52]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan13_raw",
            "remove": False,
        },
        {
            "type": "70",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][52:56]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan14_raw",
            "remove": False,
        },
        {
            "type": "70",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][56:60]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan15_raw",
            "remove": False,
        },
        {
            "type": "70",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][60:64]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan16_raw",
            "remove": False,
        },
        {
            "type": "70",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][64:68]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan17_raw",
            "remove": False,
        },
        {
            "type": "70",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][68:72]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan18_raw",
            "remove": False,
        },
        {
            "type": "70",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][72:74]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "70",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][74:76]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "73",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "param1",
            "remove": False,
        },
        {
            "type": "73",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "param2",
            "remove": False,
        },
        {
            "type": "73",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "param3",
            "remove": False,
        },
        {
            "type": "73",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "param4",
            "remove": False,
        },
        {
            "type": "73",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "x",
            "remove": False,
        },
        {
            "type": "73",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "y",
            "remove": False,
        },
        {
            "type": "73",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "z",
            "remove": False,
        },
        {
            "type": "73",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][56:60]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "seq",
            "remove": False,
        },
        {
            "type": "73",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][60:64]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "command(MAV_CMD)",
            "remove": False,
        },
        {
            "type": "73",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][64:66]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "73",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][66:68]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "73",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][68:70]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "frame(MAV_FRAME)",
            "remove": False,
        },
        {
            "type": "73",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][70:72]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "current",
            "remove": False,
        },
        {
            "type": "73",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][72:74]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "autocontinue",
            "remove": False,
        },
        {
            "type": "73",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][74:76]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "mission_type(MAV_MISSION_TYPE)",
            "remove": False,
        },
        {
            "type": "74",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "airspeed",
            "remove": False,
        },
        {
            "type": "74",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "groundspeed",
            "remove": False,
        },
        {
            "type": "74",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "alt",
            "remove": False,
        },
        {
            "type": "74",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "climb",
            "remove": False,
        },
        {
            "type": "74",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][32:36]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "heading",
            "remove": False,
        },
        {
            "type": "74",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][36:40]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "throttle",
            "remove": False,
        },
        {
            "type": "75",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "param1",
            "remove": False,
        },
        {
            "type": "75",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "param2",
            "remove": False,
        },
        {
            "type": "75",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "param3",
            "remove": False,
        },
        {
            "type": "75",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "param4",
            "remove": False,
        },
        {
            "type": "75",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "x",
            "remove": False,
        },
        {
            "type": "75",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "y",
            "remove": False,
        },
        {
            "type": "75",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "z",
            "remove": False,
        },
        {
            "type": "75",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][56:60]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "command(MAV_CMD)",
            "remove": False,
        },
        {
            "type": "75",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][60:62]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "75",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][62:64]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "75",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][64:66]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "frame(MAV_FRAME)",
            "remove": False,
        },
        {
            "type": "75",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][66:68]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "current",
            "remove": False,
        },
        {
            "type": "75",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][68:70]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "autocontinue",
            "remove": False,
        },
        {
            "type": "76",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "param1",
            "remove": False,
        },
        {
            "type": "76",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "param2",
            "remove": False,
        },
        {
            "type": "76",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "param3",
            "remove": False,
        },
        {
            "type": "76",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "param4",
            "remove": False,
        },
        {
            "type": "76",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "param5",
            "remove": False,
        },
        {
            "type": "76",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "param6",
            "remove": False,
        },
        {
            "type": "76",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "param7",
            "remove": False,
        },
        {
            "type": "76",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][56:60]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "command(MAV_CMD)",
            "remove": False,
        },
        {
            "type": "76",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][60:62]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "76",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][62:64]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "76",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][64:66]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "confirmation",
            "remove": False,
        },
        {
            "type": "77",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "result_param2",
            "remove": False,
        },
        {
            "type": "77",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][8:12]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "command(MAV_CMD)",
            "remove": False,
        },
        {
            "type": "77",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][12:14]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "result(MAV_RESULT)",
            "remove": False,
        },
        {
            "type": "77",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][14:16]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "progress",
            "remove": False,
        },
        {
            "type": "77",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][16:18]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "77",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][18:20]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "80",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][0:4]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "command(MAV_CMD)",
            "remove": False,
        },
        {
            "type": "80",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][4:6]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "80",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][6:8]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "81",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "81",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "roll",
            "remove": False,
        },
        {
            "type": "81",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "pitch",
            "remove": False,
        },
        {
            "type": "81",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yaw",
            "remove": False,
        },
        {
            "type": "81",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "thrust",
            "remove": False,
        },
        {
            "type": "81",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][40:42]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "mode_switch",
            "remove": False,
        },
        {
            "type": "81",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][42:44]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "manual_override_switch",
            "remove": False,
        },
        {
            "type": "82",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "82",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 8 : i + 16]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 32, 8)
            ],
            "name": "q",
            "remove": False,
        },
        {
            "type": "82",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "body_roll_rate",
            "remove": False,
        },
        {
            "type": "82",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "body_pitch_rate",
            "remove": False,
        },
        {
            "type": "82",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "body_yaw_rate",
            "remove": False,
        },
        {
            "type": "82",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][64:72]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "thrust",
            "remove": False,
        },
        {
            "type": "82",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 72 : i + 80]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 24, 8)
            ],
            "name": "thrust_body",
            "remove": False,
        },
        {
            "type": "82",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][96:98]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "82",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][98:100]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "82",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][100:102]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "type_mask(ATTITUDE_TARGET_TYPEMASK)",
            "remove": False,
        },
        {
            "type": "83",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "83",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 8 : i + 16]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 32, 8)
            ],
            "name": "q",
            "remove": False,
        },
        {
            "type": "83",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "body_roll_rate",
            "remove": False,
        },
        {
            "type": "83",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "body_pitch_rate",
            "remove": False,
        },
        {
            "type": "83",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "body_yaw_rate",
            "remove": False,
        },
        {
            "type": "83",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][64:72]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "thrust",
            "remove": False,
        },
        {
            "type": "83",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][72:74]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "type_mask(ATTITUDE_TARGET_TYPEMASK)",
            "remove": False,
        },
        {
            "type": "84",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "84",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "x",
            "remove": False,
        },
        {
            "type": "84",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "y",
            "remove": False,
        },
        {
            "type": "84",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "z",
            "remove": False,
        },
        {
            "type": "84",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vx",
            "remove": False,
        },
        {
            "type": "84",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vy",
            "remove": False,
        },
        {
            "type": "84",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vz",
            "remove": False,
        },
        {
            "type": "84",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "afx",
            "remove": False,
        },
        {
            "type": "84",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][64:72]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "afy",
            "remove": False,
        },
        {
            "type": "84",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][72:80]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "afz",
            "remove": False,
        },
        {
            "type": "84",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][80:88]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yaw",
            "remove": False,
        },
        {
            "type": "84",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][88:96]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yaw_rate",
            "remove": False,
        },
        {
            "type": "84",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][96:100]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "type_mask(POSITION_TARGET_TYPEMASK)",
            "remove": False,
        },
        {
            "type": "84",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][100:102]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "84",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][102:104]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "84",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][104:106]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "coordinate_frame(MAV_FRAME)",
            "remove": False,
        },
        {
            "type": "85",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "85",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "x",
            "remove": False,
        },
        {
            "type": "85",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "y",
            "remove": False,
        },
        {
            "type": "85",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "z",
            "remove": False,
        },
        {
            "type": "85",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vx",
            "remove": False,
        },
        {
            "type": "85",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vy",
            "remove": False,
        },
        {
            "type": "85",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vz",
            "remove": False,
        },
        {
            "type": "85",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "afx",
            "remove": False,
        },
        {
            "type": "85",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][64:72]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "afy",
            "remove": False,
        },
        {
            "type": "85",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][72:80]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "afz",
            "remove": False,
        },
        {
            "type": "85",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][80:88]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yaw",
            "remove": False,
        },
        {
            "type": "85",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][88:96]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yaw_rate",
            "remove": False,
        },
        {
            "type": "85",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][96:100]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "type_mask(POSITION_TARGET_TYPEMASK)",
            "remove": False,
        },
        {
            "type": "85",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][100:102]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "coordinate_frame(MAV_FRAME)",
            "remove": False,
        },
        {
            "type": "86",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "86",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lat_int",
            "remove": False,
        },
        {
            "type": "86",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lon_int",
            "remove": False,
        },
        {
            "type": "86",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "alt",
            "remove": False,
        },
        {
            "type": "86",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vx",
            "remove": False,
        },
        {
            "type": "86",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vy",
            "remove": False,
        },
        {
            "type": "86",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vz",
            "remove": False,
        },
        {
            "type": "86",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "afx",
            "remove": False,
        },
        {
            "type": "86",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][64:72]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "afy",
            "remove": False,
        },
        {
            "type": "86",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][72:80]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "afz",
            "remove": False,
        },
        {
            "type": "86",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][80:88]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yaw",
            "remove": False,
        },
        {
            "type": "86",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][88:96]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yaw_rate",
            "remove": False,
        },
        {
            "type": "86",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][96:100]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "type_mask(POSITION_TARGET_TYPEMASK)",
            "remove": False,
        },
        {
            "type": "86",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][100:102]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "86",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][102:104]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "86",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][104:106]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "coordinate_frame(MAV_FRAME)",
            "remove": False,
        },
        {
            "type": "87",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "87",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lat_int",
            "remove": False,
        },
        {
            "type": "87",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lon_int",
            "remove": False,
        },
        {
            "type": "87",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "alt",
            "remove": False,
        },
        {
            "type": "87",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vx",
            "remove": False,
        },
        {
            "type": "87",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vy",
            "remove": False,
        },
        {
            "type": "87",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vz",
            "remove": False,
        },
        {
            "type": "87",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "afx",
            "remove": False,
        },
        {
            "type": "87",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][64:72]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "afy",
            "remove": False,
        },
        {
            "type": "87",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][72:80]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "afz",
            "remove": False,
        },
        {
            "type": "87",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][80:88]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yaw",
            "remove": False,
        },
        {
            "type": "87",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][88:96]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yaw_rate",
            "remove": False,
        },
        {
            "type": "87",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][96:100]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "type_mask(POSITION_TARGET_TYPEMASK)",
            "remove": False,
        },
        {
            "type": "87",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][100:102]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "coordinate_frame(MAV_FRAME)",
            "remove": False,
        },
        {
            "type": "89",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "89",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "x",
            "remove": False,
        },
        {
            "type": "89",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "y",
            "remove": False,
        },
        {
            "type": "89",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "z",
            "remove": False,
        },
        {
            "type": "89",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "roll",
            "remove": False,
        },
        {
            "type": "89",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "pitch",
            "remove": False,
        },
        {
            "type": "89",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yaw",
            "remove": False,
        },
        {
            "type": "90",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "90",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "roll",
            "remove": False,
        },
        {
            "type": "90",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "pitch",
            "remove": False,
        },
        {
            "type": "90",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yaw",
            "remove": False,
        },
        {
            "type": "90",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "rollspeed",
            "remove": False,
        },
        {
            "type": "90",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "pitchspeed",
            "remove": False,
        },
        {
            "type": "90",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yawspeed",
            "remove": False,
        },
        {
            "type": "90",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][64:72]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lat",
            "remove": False,
        },
        {
            "type": "90",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][72:80]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lon",
            "remove": False,
        },
        {
            "type": "90",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][80:88]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "alt",
            "remove": False,
        },
        {
            "type": "90",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][88:92]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "vx",
            "remove": False,
        },
        {
            "type": "90",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][92:96]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "vy",
            "remove": False,
        },
        {
            "type": "90",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][96:100]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "vz",
            "remove": False,
        },
        {
            "type": "90",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][100:104]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "xacc",
            "remove": False,
        },
        {
            "type": "90",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][104:108]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "yacc",
            "remove": False,
        },
        {
            "type": "90",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][108:112]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "zacc",
            "remove": False,
        },
        {
            "type": "91",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "91",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "roll_ailerons",
            "remove": False,
        },
        {
            "type": "91",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "pitch_elevator",
            "remove": False,
        },
        {
            "type": "91",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yaw_rudder",
            "remove": False,
        },
        {
            "type": "91",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "throttle",
            "remove": False,
        },
        {
            "type": "91",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "aux1",
            "remove": False,
        },
        {
            "type": "91",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "aux2",
            "remove": False,
        },
        {
            "type": "91",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][64:72]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "aux3",
            "remove": False,
        },
        {
            "type": "91",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][72:80]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "aux4",
            "remove": False,
        },
        {
            "type": "91",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][80:82]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "mode(MAV_MODE)",
            "remove": False,
        },
        {
            "type": "91",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][82:84]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "nav_mode",
            "remove": False,
        },
        {
            "type": "92",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "92",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][16:20]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan1_raw",
            "remove": False,
        },
        {
            "type": "92",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][20:24]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan2_raw",
            "remove": False,
        },
        {
            "type": "92",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][24:28]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan3_raw",
            "remove": False,
        },
        {
            "type": "92",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][28:32]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan4_raw",
            "remove": False,
        },
        {
            "type": "92",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][32:36]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan5_raw",
            "remove": False,
        },
        {
            "type": "92",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][36:40]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan6_raw",
            "remove": False,
        },
        {
            "type": "92",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][40:44]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan7_raw",
            "remove": False,
        },
        {
            "type": "92",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][44:48]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan8_raw",
            "remove": False,
        },
        {
            "type": "92",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][48:52]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan9_raw",
            "remove": False,
        },
        {
            "type": "92",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][52:56]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan10_raw",
            "remove": False,
        },
        {
            "type": "92",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][56:60]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan11_raw",
            "remove": False,
        },
        {
            "type": "92",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][60:64]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "chan12_raw",
            "remove": False,
        },
        {
            "type": "92",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][64:66]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "rssi",
            "remove": False,
        },
        {
            "type": "93",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "93",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][16:32]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "flags",
            "remove": False,
        },
        {
            "type": "93",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 32 : i + 40]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 128, 8)
            ],
            "name": "controls",
            "remove": False,
        },
        {
            "type": "93",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][160:162]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "mode(MAV_MODE_FLAG)",
            "remove": False,
        },
        {
            "type": "100",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "100",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "flow_comp_m_x",
            "remove": False,
        },
        {
            "type": "100",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "flow_comp_m_y",
            "remove": False,
        },
        {
            "type": "100",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "ground_distance",
            "remove": False,
        },
        {
            "type": "100",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "flow_rate_x",
            "remove": False,
        },
        {
            "type": "100",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "flow_rate_y",
            "remove": False,
        },
        {
            "type": "100",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][56:60]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "flow_x",
            "remove": False,
        },
        {
            "type": "100",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][60:64]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "flow_y",
            "remove": False,
        },
        {
            "type": "100",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][64:66]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "sensor_id",
            "remove": False,
        },
        {
            "type": "100",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][66:68]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "quality",
            "remove": False,
        },
        {
            "type": "101",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "usec",
            "remove": False,
        },
        {
            "type": "101",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "x",
            "remove": False,
        },
        {
            "type": "101",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "y",
            "remove": False,
        },
        {
            "type": "101",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "z",
            "remove": False,
        },
        {
            "type": "101",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "roll",
            "remove": False,
        },
        {
            "type": "101",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "pitch",
            "remove": False,
        },
        {
            "type": "101",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yaw",
            "remove": False,
        },
        {
            "type": "101",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 64 : i + 72]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 168, 8)
            ],
            "name": "covariance",
            "remove": False,
        },
        {
            "type": "101",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][232:234]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "reset_counter",
            "remove": False,
        },
        {
            "type": "102",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "usec",
            "remove": False,
        },
        {
            "type": "102",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "x",
            "remove": False,
        },
        {
            "type": "102",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "y",
            "remove": False,
        },
        {
            "type": "102",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "z",
            "remove": False,
        },
        {
            "type": "102",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "roll",
            "remove": False,
        },
        {
            "type": "102",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "pitch",
            "remove": False,
        },
        {
            "type": "102",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yaw",
            "remove": False,
        },
        {
            "type": "102",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 64 : i + 72]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 168, 8)
            ],
            "name": "covariance",
            "remove": False,
        },
        {
            "type": "102",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][232:234]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "reset_counter",
            "remove": False,
        },
        {
            "type": "103",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "usec",
            "remove": False,
        },
        {
            "type": "103",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "x",
            "remove": False,
        },
        {
            "type": "103",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "y",
            "remove": False,
        },
        {
            "type": "103",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "z",
            "remove": False,
        },
        {
            "type": "103",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 40 : i + 48]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 72, 8)
            ],
            "name": "covariance",
            "remove": False,
        },
        {
            "type": "103",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][112:114]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "reset_counter",
            "remove": False,
        },
        {
            "type": "104",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "usec",
            "remove": False,
        },
        {
            "type": "104",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "x",
            "remove": False,
        },
        {
            "type": "104",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "y",
            "remove": False,
        },
        {
            "type": "104",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "z",
            "remove": False,
        },
        {
            "type": "104",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "roll",
            "remove": False,
        },
        {
            "type": "104",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "pitch",
            "remove": False,
        },
        {
            "type": "104",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yaw",
            "remove": False,
        },
        {
            "type": "104",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 64 : i + 72]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 168, 8)
            ],
            "name": "covariance",
            "remove": False,
        },
        {
            "type": "105",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "105",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "xacc",
            "remove": False,
        },
        {
            "type": "105",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yacc",
            "remove": False,
        },
        {
            "type": "105",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "zacc",
            "remove": False,
        },
        {
            "type": "105",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "xgyro",
            "remove": False,
        },
        {
            "type": "105",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "ygyro",
            "remove": False,
        },
        {
            "type": "105",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "zgyro",
            "remove": False,
        },
        {
            "type": "105",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][64:72]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "xmag",
            "remove": False,
        },
        {
            "type": "105",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][72:80]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "ymag",
            "remove": False,
        },
        {
            "type": "105",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][80:88]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "zmag",
            "remove": False,
        },
        {
            "type": "105",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][88:96]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "abs_pressure",
            "remove": False,
        },
        {
            "type": "105",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][96:104]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "diff_pressure",
            "remove": False,
        },
        {
            "type": "105",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][104:112]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "pressure_alt",
            "remove": False,
        },
        {
            "type": "105",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][112:120]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "temperature",
            "remove": False,
        },
        {
            "type": "105",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][120:124]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "fields_updated(HIGHRES_IMU_UPDATED_FLAGS)",
            "remove": False,
        },
        {
            "type": "105",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][124:126]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "id",
            "remove": False,
        },
        {
            "type": "106",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "106",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "integration_time_us",
            "remove": False,
        },
        {
            "type": "106",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "integrated_x",
            "remove": False,
        },
        {
            "type": "106",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "integrated_y",
            "remove": False,
        },
        {
            "type": "106",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "integrated_xgyro",
            "remove": False,
        },
        {
            "type": "106",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "integrated_ygyro",
            "remove": False,
        },
        {
            "type": "106",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "integrated_zgyro",
            "remove": False,
        },
        {
            "type": "106",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][64:72]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_delta_distance_us",
            "remove": False,
        },
        {
            "type": "106",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][72:80]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "distance",
            "remove": False,
        },
        {
            "type": "106",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][80:84]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "temperature",
            "remove": False,
        },
        {
            "type": "106",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][84:86]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "sensor_id",
            "remove": False,
        },
        {
            "type": "106",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][86:88]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "quality",
            "remove": False,
        },
        {
            "type": "107",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "107",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "xacc",
            "remove": False,
        },
        {
            "type": "107",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yacc",
            "remove": False,
        },
        {
            "type": "107",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "zacc",
            "remove": False,
        },
        {
            "type": "107",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "xgyro",
            "remove": False,
        },
        {
            "type": "107",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "ygyro",
            "remove": False,
        },
        {
            "type": "107",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "zgyro",
            "remove": False,
        },
        {
            "type": "107",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][64:72]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "xmag",
            "remove": False,
        },
        {
            "type": "107",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][72:80]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "ymag",
            "remove": False,
        },
        {
            "type": "107",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][80:88]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "zmag",
            "remove": False,
        },
        {
            "type": "107",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][88:96]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "abs_pressure",
            "remove": False,
        },
        {
            "type": "107",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][96:104]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "diff_pressure",
            "remove": False,
        },
        {
            "type": "107",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][104:112]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "pressure_alt",
            "remove": False,
        },
        {
            "type": "107",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][112:120]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "temperature",
            "remove": False,
        },
        {
            "type": "107",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][120:128]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "fields_updated(HIL_SENSOR_UPDATED_FLAGS)",
            "remove": False,
        },
        {
            "type": "107",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][128:130]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "id",
            "remove": False,
        },
        {
            "type": "108",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "q1",
            "remove": False,
        },
        {
            "type": "108",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "q2",
            "remove": False,
        },
        {
            "type": "108",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "q3",
            "remove": False,
        },
        {
            "type": "108",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "q4",
            "remove": False,
        },
        {
            "type": "108",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "roll",
            "remove": False,
        },
        {
            "type": "108",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "pitch",
            "remove": False,
        },
        {
            "type": "108",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yaw",
            "remove": False,
        },
        {
            "type": "108",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "xacc",
            "remove": False,
        },
        {
            "type": "108",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][64:72]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yacc",
            "remove": False,
        },
        {
            "type": "108",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][72:80]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "zacc",
            "remove": False,
        },
        {
            "type": "108",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][80:88]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "xgyro",
            "remove": False,
        },
        {
            "type": "108",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][88:96]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "ygyro",
            "remove": False,
        },
        {
            "type": "108",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][96:104]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "zgyro",
            "remove": False,
        },
        {
            "type": "108",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][104:112]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "lat",
            "remove": False,
        },
        {
            "type": "108",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][112:120]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "lon",
            "remove": False,
        },
        {
            "type": "108",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][120:128]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "alt",
            "remove": False,
        },
        {
            "type": "108",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][128:136]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "std_dev_horz",
            "remove": False,
        },
        {
            "type": "108",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][136:144]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "std_dev_vert",
            "remove": False,
        },
        {
            "type": "108",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][144:152]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vn",
            "remove": False,
        },
        {
            "type": "108",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][152:160]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "ve",
            "remove": False,
        },
        {
            "type": "108",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][160:168]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vd",
            "remove": False,
        },
        {
            "type": "108",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][168:176]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lat_int",
            "remove": False,
        },
        {
            "type": "108",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][176:184]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lon_int",
            "remove": False,
        },
        {
            "type": "109",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][0:4]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "rxerrors",
            "remove": False,
        },
        {
            "type": "109",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][4:8]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "fixed",
            "remove": False,
        },
        {
            "type": "109",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][8:10]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "rssi",
            "remove": False,
        },
        {
            "type": "109",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][10:12]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "remrssi",
            "remove": False,
        },
        {
            "type": "109",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][12:14]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "txbuf",
            "remove": False,
        },
        {
            "type": "109",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][14:16]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "noise",
            "remove": False,
        },
        {
            "type": "109",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][16:18]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "remnoise",
            "remove": False,
        },
        {
            "type": "110",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][0:2]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_network",
            "remove": False,
        },
        {
            "type": "110",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][2:4]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "110",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][4:6]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "110",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 6 : i + 8]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 502, 2)
            ],
            "name": "payload",
            "remove": False,
        },
        {
            "type": "111",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<q"), b"\x00")
            )[0],
            "name": "tc1",
            "remove": False,
        },
        {
            "type": "111",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<q", bytes.fromhex(x[0][16:32]).ljust(struct.calcsize("<q"), b"\x00")
            )[0],
            "name": "ts1",
            "remove": False,
        },
        {
            "type": "111",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][32:34]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "111",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][34:36]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "112",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "112",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "seq",
            "remove": False,
        },
        {
            "type": "113",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "113",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lat",
            "remove": False,
        },
        {
            "type": "113",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lon",
            "remove": False,
        },
        {
            "type": "113",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "alt",
            "remove": False,
        },
        {
            "type": "113",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][40:44]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "eph",
            "remove": False,
        },
        {
            "type": "113",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][44:48]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "epv",
            "remove": False,
        },
        {
            "type": "113",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][48:52]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "vel",
            "remove": False,
        },
        {
            "type": "113",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][52:56]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "vn",
            "remove": False,
        },
        {
            "type": "113",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][56:60]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "ve",
            "remove": False,
        },
        {
            "type": "113",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][60:64]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "vd",
            "remove": False,
        },
        {
            "type": "113",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][64:68]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "cog",
            "remove": False,
        },
        {
            "type": "113",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][68:72]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "yaw",
            "remove": False,
        },
        {
            "type": "113",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][72:74]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "fix_type",
            "remove": False,
        },
        {
            "type": "113",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][74:76]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "satellites_visible",
            "remove": False,
        },
        {
            "type": "113",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][76:78]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "id",
            "remove": False,
        },
        {
            "type": "114",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "114",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "integration_time_us",
            "remove": False,
        },
        {
            "type": "114",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "integrated_x",
            "remove": False,
        },
        {
            "type": "114",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "integrated_y",
            "remove": False,
        },
        {
            "type": "114",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "integrated_xgyro",
            "remove": False,
        },
        {
            "type": "114",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "integrated_ygyro",
            "remove": False,
        },
        {
            "type": "114",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "integrated_zgyro",
            "remove": False,
        },
        {
            "type": "114",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][64:72]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_delta_distance_us",
            "remove": False,
        },
        {
            "type": "114",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][72:80]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "distance",
            "remove": False,
        },
        {
            "type": "114",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][80:84]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "temperature",
            "remove": False,
        },
        {
            "type": "114",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][84:86]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "sensor_id",
            "remove": False,
        },
        {
            "type": "114",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][86:88]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "quality",
            "remove": False,
        },
        {
            "type": "115",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "115",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 16 : i + 24]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 32, 8)
            ],
            "name": "attitude_quaternion",
            "remove": False,
        },
        {
            "type": "115",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "rollspeed",
            "remove": False,
        },
        {
            "type": "115",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "pitchspeed",
            "remove": False,
        },
        {
            "type": "115",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][64:72]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yawspeed",
            "remove": False,
        },
        {
            "type": "115",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][72:80]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lat",
            "remove": False,
        },
        {
            "type": "115",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][80:88]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lon",
            "remove": False,
        },
        {
            "type": "115",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][88:96]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "alt",
            "remove": False,
        },
        {
            "type": "115",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][96:100]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "vx",
            "remove": False,
        },
        {
            "type": "115",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][100:104]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "vy",
            "remove": False,
        },
        {
            "type": "115",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][104:108]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "vz",
            "remove": False,
        },
        {
            "type": "115",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][108:112]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "ind_airspeed",
            "remove": False,
        },
        {
            "type": "115",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][112:116]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "true_airspeed",
            "remove": False,
        },
        {
            "type": "115",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][116:120]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "xacc",
            "remove": False,
        },
        {
            "type": "115",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][120:124]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "yacc",
            "remove": False,
        },
        {
            "type": "115",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][124:128]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "zacc",
            "remove": False,
        },
        {
            "type": "116",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "116",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][8:12]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "xacc",
            "remove": False,
        },
        {
            "type": "116",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][12:16]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "yacc",
            "remove": False,
        },
        {
            "type": "116",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][16:20]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "zacc",
            "remove": False,
        },
        {
            "type": "116",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][20:24]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "xgyro",
            "remove": False,
        },
        {
            "type": "116",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][24:28]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "ygyro",
            "remove": False,
        },
        {
            "type": "116",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][28:32]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "zgyro",
            "remove": False,
        },
        {
            "type": "116",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][32:36]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "xmag",
            "remove": False,
        },
        {
            "type": "116",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][36:40]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "ymag",
            "remove": False,
        },
        {
            "type": "116",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][40:44]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "zmag",
            "remove": False,
        },
        {
            "type": "116",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][44:48]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "temperature",
            "remove": False,
        },
        {
            "type": "117",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][0:4]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "start",
            "remove": False,
        },
        {
            "type": "117",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][4:8]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "end",
            "remove": False,
        },
        {
            "type": "117",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][8:10]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "117",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][10:12]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "118",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_utc",
            "remove": False,
        },
        {
            "type": "118",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "size",
            "remove": False,
        },
        {
            "type": "118",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][16:20]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "id",
            "remove": False,
        },
        {
            "type": "118",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][20:24]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "num_logs",
            "remove": False,
        },
        {
            "type": "118",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][24:28]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "last_log_num",
            "remove": False,
        },
        {
            "type": "119",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "ofs",
            "remove": False,
        },
        {
            "type": "119",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "count",
            "remove": False,
        },
        {
            "type": "119",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][16:20]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "id",
            "remove": False,
        },
        {
            "type": "119",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][20:22]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "119",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][22:24]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "120",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "ofs",
            "remove": False,
        },
        {
            "type": "120",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][8:12]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "id",
            "remove": False,
        },
        {
            "type": "120",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][12:14]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "count",
            "remove": False,
        },
        {
            "type": "120",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 14 : i + 16]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 180, 2)
            ],
            "name": "data",
            "remove": False,
        },
        {
            "type": "121",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][0:2]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "121",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][2:4]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "122",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][0:2]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "122",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][2:4]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "123",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][0:2]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "123",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][2:4]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "123",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][4:6]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "len",
            "remove": False,
        },
        {
            "type": "123",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 6 : i + 8]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 220, 2)
            ],
            "name": "data",
            "remove": False,
        },
        {
            "type": "124",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "124",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lat",
            "remove": False,
        },
        {
            "type": "124",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lon",
            "remove": False,
        },
        {
            "type": "124",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "alt",
            "remove": False,
        },
        {
            "type": "124",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "dgps_age",
            "remove": False,
        },
        {
            "type": "124",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "alt_ellipsoid",
            "remove": False,
        },
        {
            "type": "124",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "h_acc",
            "remove": False,
        },
        {
            "type": "124",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][64:72]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "v_acc",
            "remove": False,
        },
        {
            "type": "124",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][72:80]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "vel_acc",
            "remove": False,
        },
        {
            "type": "124",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][80:88]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "hdg_acc",
            "remove": False,
        },
        {
            "type": "124",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][88:92]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "eph",
            "remove": False,
        },
        {
            "type": "124",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][92:96]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "epv",
            "remove": False,
        },
        {
            "type": "124",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][96:100]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "vel",
            "remove": False,
        },
        {
            "type": "124",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][100:104]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "cog",
            "remove": False,
        },
        {
            "type": "124",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][104:108]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "yaw",
            "remove": False,
        },
        {
            "type": "124",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][108:110]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "fix_type(GPS_FIX_TYPE)",
            "remove": False,
        },
        {
            "type": "124",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][110:112]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "satellites_visible",
            "remove": False,
        },
        {
            "type": "124",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][112:114]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "dgps_numch",
            "remove": False,
        },
        {
            "type": "125",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][0:4]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "Vcc",
            "remove": False,
        },
        {
            "type": "125",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][4:8]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "Vservo",
            "remove": False,
        },
        {
            "type": "125",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][8:12]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "flags(MAV_POWER_STATUS)",
            "remove": False,
        },
        {
            "type": "126",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "baudrate",
            "remove": False,
        },
        {
            "type": "126",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][8:12]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "timeout",
            "remove": False,
        },
        {
            "type": "126",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][12:14]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "device(SERIAL_CONTROL_DEV)",
            "remove": False,
        },
        {
            "type": "126",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][14:16]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "flags(SERIAL_CONTROL_FLAG)",
            "remove": False,
        },
        {
            "type": "126",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][16:18]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "count",
            "remove": False,
        },
        {
            "type": "126",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 18 : i + 20]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 140, 2)
            ],
            "name": "data",
            "remove": False,
        },
        {
            "type": "126",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][158:160]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "126",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][160:162]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "127",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_last_baseline_ms",
            "remove": False,
        },
        {
            "type": "127",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "tow",
            "remove": False,
        },
        {
            "type": "127",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "baseline_a_mm",
            "remove": False,
        },
        {
            "type": "127",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "baseline_b_mm",
            "remove": False,
        },
        {
            "type": "127",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "baseline_c_mm",
            "remove": False,
        },
        {
            "type": "127",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "accuracy",
            "remove": False,
        },
        {
            "type": "127",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "iar_num_hypotheses",
            "remove": False,
        },
        {
            "type": "127",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][56:60]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "wn",
            "remove": False,
        },
        {
            "type": "127",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][60:62]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "rtk_receiver_id",
            "remove": False,
        },
        {
            "type": "127",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][62:64]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "rtk_health",
            "remove": False,
        },
        {
            "type": "127",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][64:66]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "rtk_rate",
            "remove": False,
        },
        {
            "type": "127",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][66:68]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "nsats",
            "remove": False,
        },
        {
            "type": "127",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][68:70]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "baseline_coords_type(RTK_BASELINE_COORDINATE_SYSTEM)",
            "remove": False,
        },
        {
            "type": "128",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_last_baseline_ms",
            "remove": False,
        },
        {
            "type": "128",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "tow",
            "remove": False,
        },
        {
            "type": "128",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "baseline_a_mm",
            "remove": False,
        },
        {
            "type": "128",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "baseline_b_mm",
            "remove": False,
        },
        {
            "type": "128",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "baseline_c_mm",
            "remove": False,
        },
        {
            "type": "128",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "accuracy",
            "remove": False,
        },
        {
            "type": "128",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "iar_num_hypotheses",
            "remove": False,
        },
        {
            "type": "128",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][56:60]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "wn",
            "remove": False,
        },
        {
            "type": "128",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][60:62]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "rtk_receiver_id",
            "remove": False,
        },
        {
            "type": "128",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][62:64]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "rtk_health",
            "remove": False,
        },
        {
            "type": "128",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][64:66]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "rtk_rate",
            "remove": False,
        },
        {
            "type": "128",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][66:68]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "nsats",
            "remove": False,
        },
        {
            "type": "128",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][68:70]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "baseline_coords_type(RTK_BASELINE_COORDINATE_SYSTEM)",
            "remove": False,
        },
        {
            "type": "129",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "129",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][8:12]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "xacc",
            "remove": False,
        },
        {
            "type": "129",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][12:16]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "yacc",
            "remove": False,
        },
        {
            "type": "129",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][16:20]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "zacc",
            "remove": False,
        },
        {
            "type": "129",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][20:24]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "xgyro",
            "remove": False,
        },
        {
            "type": "129",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][24:28]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "ygyro",
            "remove": False,
        },
        {
            "type": "129",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][28:32]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "zgyro",
            "remove": False,
        },
        {
            "type": "129",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][32:36]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "xmag",
            "remove": False,
        },
        {
            "type": "129",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][36:40]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "ymag",
            "remove": False,
        },
        {
            "type": "129",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][40:44]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "zmag",
            "remove": False,
        },
        {
            "type": "129",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][44:48]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "temperature",
            "remove": False,
        },
        {
            "type": "130",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "size",
            "remove": False,
        },
        {
            "type": "130",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][8:12]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "width",
            "remove": False,
        },
        {
            "type": "130",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][12:16]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "height",
            "remove": False,
        },
        {
            "type": "130",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][16:20]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "packets",
            "remove": False,
        },
        {
            "type": "130",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][20:22]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "type(MAVLINK_DATA_STREAM_TYPE)",
            "remove": False,
        },
        {
            "type": "130",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][22:24]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "payload",
            "remove": False,
        },
        {
            "type": "130",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][24:26]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "jpg_quality",
            "remove": False,
        },
        {
            "type": "131",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][0:4]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "seqnr",
            "remove": False,
        },
        {
            "type": "131",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 4 : i + 6]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 506, 2)
            ],
            "name": "data",
            "remove": False,
        },
        {
            "type": "132",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "132",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "horizontal_fov",
            "remove": False,
        },
        {
            "type": "132",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vertical_fov",
            "remove": False,
        },
        {
            "type": "132",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 24 : i + 32]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 32, 8)
            ],
            "name": "quaternion",
            "remove": False,
        },
        {
            "type": "132",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][56:60]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "min_distance",
            "remove": False,
        },
        {
            "type": "132",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][60:64]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "max_distance",
            "remove": False,
        },
        {
            "type": "132",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][64:68]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "current_distance",
            "remove": False,
        },
        {
            "type": "132",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][68:70]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "type(MAV_DISTANCE_SENSOR)",
            "remove": False,
        },
        {
            "type": "132",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][70:72]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "id",
            "remove": False,
        },
        {
            "type": "132",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][72:74]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "orientation(MAV_SENSOR_ORIENTATION)",
            "remove": False,
        },
        {
            "type": "132",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][74:76]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "covariance",
            "remove": False,
        },
        {
            "type": "132",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][76:78]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "signal_quality",
            "remove": False,
        },
        {
            "type": "133",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "mask",
            "remove": False,
        },
        {
            "type": "133",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lat",
            "remove": False,
        },
        {
            "type": "133",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lon",
            "remove": False,
        },
        {
            "type": "133",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][32:36]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "grid_spacing",
            "remove": False,
        },
        {
            "type": "134",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lat",
            "remove": False,
        },
        {
            "type": "134",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lon",
            "remove": False,
        },
        {
            "type": "134",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][16:20]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "grid_spacing",
            "remove": False,
        },
        {
            "type": "134",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<h",
                    bytes.fromhex(x[0][i + 20 : i + 24]).ljust(
                        struct.calcsize("<h"), b"\x00"
                    ),
                )[0]
                for i in range(0, 64, 4)
            ],
            "name": "data",
            "remove": False,
        },
        {
            "type": "134",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][84:86]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "gridbit",
            "remove": False,
        },
        {
            "type": "135",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lat",
            "remove": False,
        },
        {
            "type": "135",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lon",
            "remove": False,
        },
        {
            "type": "136",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lat",
            "remove": False,
        },
        {
            "type": "136",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lon",
            "remove": False,
        },
        {
            "type": "136",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "terrain_height",
            "remove": False,
        },
        {
            "type": "136",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "current_height",
            "remove": False,
        },
        {
            "type": "136",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][32:36]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "spacing",
            "remove": False,
        },
        {
            "type": "136",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][36:40]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "pending",
            "remove": False,
        },
        {
            "type": "136",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][40:44]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "loaded",
            "remove": False,
        },
        {
            "type": "137",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "137",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "press_abs",
            "remove": False,
        },
        {
            "type": "137",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "press_diff",
            "remove": False,
        },
        {
            "type": "137",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][24:28]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "temperature",
            "remove": False,
        },
        {
            "type": "137",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][28:32]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "temperature_press_diff",
            "remove": False,
        },
        {
            "type": "138",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "138",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 16 : i + 24]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 32, 8)
            ],
            "name": "q",
            "remove": False,
        },
        {
            "type": "138",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "x",
            "remove": False,
        },
        {
            "type": "138",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "y",
            "remove": False,
        },
        {
            "type": "138",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][64:72]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "z",
            "remove": False,
        },
        {
            "type": "138",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 72 : i + 80]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 168, 8)
            ],
            "name": "covariance",
            "remove": False,
        },
        {
            "type": "139",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "139",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 16 : i + 24]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 64, 8)
            ],
            "name": "controls",
            "remove": False,
        },
        {
            "type": "139",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][80:82]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "group_mlx",
            "remove": False,
        },
        {
            "type": "139",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][82:84]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "139",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][84:86]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "140",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "140",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 16 : i + 24]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 64, 8)
            ],
            "name": "controls",
            "remove": False,
        },
        {
            "type": "140",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][80:82]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "group_mlx",
            "remove": False,
        },
        {
            "type": "141",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "141",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "altitude_monotonic",
            "remove": False,
        },
        {
            "type": "141",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "altitude_amsl",
            "remove": False,
        },
        {
            "type": "141",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "altitude_local",
            "remove": False,
        },
        {
            "type": "141",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "altitude_relative",
            "remove": False,
        },
        {
            "type": "141",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "altitude_terrain",
            "remove": False,
        },
        {
            "type": "141",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "bottom_clearance",
            "remove": False,
        },
        {
            "type": "142",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][0:2]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "request_id",
            "remove": False,
        },
        {
            "type": "142",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][2:4]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "uri_type",
            "remove": False,
        },
        {
            "type": "142",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 4 : i + 6]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 240, 2)
            ],
            "name": "uri",
            "remove": False,
        },
        {
            "type": "142",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][244:246]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "transfer_type",
            "remove": False,
        },
        {
            "type": "142",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 246 : i + 248]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 240, 2)
            ],
            "name": "storage",
            "remove": False,
        },
        {
            "type": "143",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "143",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "press_abs",
            "remove": False,
        },
        {
            "type": "143",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "press_diff",
            "remove": False,
        },
        {
            "type": "143",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][24:28]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "temperature",
            "remove": False,
        },
        {
            "type": "143",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][28:32]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "temperature_press_diff",
            "remove": False,
        },
        {
            "type": "144",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "timestamp",
            "remove": False,
        },
        {
            "type": "144",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][16:32]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "custom_state",
            "remove": False,
        },
        {
            "type": "144",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lat",
            "remove": False,
        },
        {
            "type": "144",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lon",
            "remove": False,
        },
        {
            "type": "144",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "alt",
            "remove": False,
        },
        {
            "type": "144",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 56 : i + 64]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 24, 8)
            ],
            "name": "vel",
            "remove": False,
        },
        {
            "type": "144",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 80 : i + 88]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 24, 8)
            ],
            "name": "acc",
            "remove": False,
        },
        {
            "type": "144",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 104 : i + 112]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 32, 8)
            ],
            "name": "attitude_q",
            "remove": False,
        },
        {
            "type": "144",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 136 : i + 144]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 24, 8)
            ],
            "name": "rates",
            "remove": False,
        },
        {
            "type": "144",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 160 : i + 168]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 24, 8)
            ],
            "name": "position_cov",
            "remove": False,
        },
        {
            "type": "144",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][184:186]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "est_capabilities",
            "remove": False,
        },
        {
            "type": "146",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "146",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "x_acc",
            "remove": False,
        },
        {
            "type": "146",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "y_acc",
            "remove": False,
        },
        {
            "type": "146",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "z_acc",
            "remove": False,
        },
        {
            "type": "146",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "x_vel",
            "remove": False,
        },
        {
            "type": "146",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "y_vel",
            "remove": False,
        },
        {
            "type": "146",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "z_vel",
            "remove": False,
        },
        {
            "type": "146",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][64:72]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "x_pos",
            "remove": False,
        },
        {
            "type": "146",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][72:80]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "y_pos",
            "remove": False,
        },
        {
            "type": "146",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][80:88]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "z_pos",
            "remove": False,
        },
        {
            "type": "146",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][88:96]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "airspeed",
            "remove": False,
        },
        {
            "type": "146",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 96 : i + 104]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 24, 8)
            ],
            "name": "vel_variance",
            "remove": False,
        },
        {
            "type": "146",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 120 : i + 128]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 24, 8)
            ],
            "name": "pos_variance",
            "remove": False,
        },
        {
            "type": "146",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 144 : i + 152]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 32, 8)
            ],
            "name": "q",
            "remove": False,
        },
        {
            "type": "146",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][176:184]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "roll_rate",
            "remove": False,
        },
        {
            "type": "146",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][184:192]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "pitch_rate",
            "remove": False,
        },
        {
            "type": "146",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][192:200]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yaw_rate",
            "remove": False,
        },
        {
            "type": "147",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "current_consumed",
            "remove": False,
        },
        {
            "type": "147",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "energy_consumed",
            "remove": False,
        },
        {
            "type": "147",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "time_remaining",
            "remove": False,
        },
        {
            "type": "147",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "fault_bitmask(MAV_BATTERY_FAULT)",
            "remove": False,
        },
        {
            "type": "147",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][32:36]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "temperature",
            "remove": False,
        },
        {
            "type": "147",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<H",
                    bytes.fromhex(x[0][i + 36 : i + 40]).ljust(
                        struct.calcsize("<H"), b"\x00"
                    ),
                )[0]
                for i in range(0, 40, 4)
            ],
            "name": "voltages",
            "remove": False,
        },
        {
            "type": "147",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][76:80]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "current_battery",
            "remove": False,
        },
        {
            "type": "147",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<H",
                    bytes.fromhex(x[0][i + 80 : i + 84]).ljust(
                        struct.calcsize("<H"), b"\x00"
                    ),
                )[0]
                for i in range(0, 16, 4)
            ],
            "name": "voltages_ext",
            "remove": False,
        },
        {
            "type": "147",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][96:98]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "id",
            "remove": False,
        },
        {
            "type": "147",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][98:100]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "battery_function(MAV_BATTERY_FUNCTION)",
            "remove": False,
        },
        {
            "type": "147",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][100:102]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "type(MAV_BATTERY_TYPE)",
            "remove": False,
        },
        {
            "type": "147",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<b", bytes.fromhex(x[0][102:104]).ljust(struct.calcsize("<b"), b"\x00")
            )[0],
            "name": "battery_remaining",
            "remove": False,
        },
        {
            "type": "147",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][104:106]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "charge_state(MAV_BATTERY_CHARGE_STATE)",
            "remove": False,
        },
        {
            "type": "147",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][106:108]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "mode(MAV_BATTERY_MODE)",
            "remove": False,
        },
        {
            "type": "148",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "capabilities(MAV_PROTOCOL_CAPABILITY)",
            "remove": False,
        },
        {
            "type": "148",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][16:32]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "uid",
            "remove": False,
        },
        {
            "type": "148",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "flight_sw_version",
            "remove": False,
        },
        {
            "type": "148",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "middleware_sw_version",
            "remove": False,
        },
        {
            "type": "148",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "os_sw_version",
            "remove": False,
        },
        {
            "type": "148",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "board_version",
            "remove": False,
        },
        {
            "type": "148",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][64:68]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "vendor_id",
            "remove": False,
        },
        {
            "type": "148",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][68:72]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "product_id",
            "remove": False,
        },
        {
            "type": "148",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 72 : i + 74]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 16, 2)
            ],
            "name": "flight_custom_version",
            "remove": False,
        },
        {
            "type": "148",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 88 : i + 90]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 16, 2)
            ],
            "name": "middleware_custom_version",
            "remove": False,
        },
        {
            "type": "148",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 104 : i + 106]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 16, 2)
            ],
            "name": "os_custom_version",
            "remove": False,
        },
        {
            "type": "148",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 120 : i + 122]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 36, 2)
            ],
            "name": "uid2",
            "remove": False,
        },
        {
            "type": "149",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "149",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "angle_x",
            "remove": False,
        },
        {
            "type": "149",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "angle_y",
            "remove": False,
        },
        {
            "type": "149",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "distance",
            "remove": False,
        },
        {
            "type": "149",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "size_x",
            "remove": False,
        },
        {
            "type": "149",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "size_y",
            "remove": False,
        },
        {
            "type": "149",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "x",
            "remove": False,
        },
        {
            "type": "149",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][64:72]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "y",
            "remove": False,
        },
        {
            "type": "149",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][72:80]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "z",
            "remove": False,
        },
        {
            "type": "149",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 80 : i + 88]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 32, 8)
            ],
            "name": "q",
            "remove": False,
        },
        {
            "type": "149",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][112:114]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_num",
            "remove": False,
        },
        {
            "type": "149",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][114:116]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "frame(MAV_FRAME)",
            "remove": False,
        },
        {
            "type": "149",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][116:118]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "type(LANDING_TARGET_TYPE)",
            "remove": False,
        },
        {
            "type": "149",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][118:120]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "position_valid",
            "remove": False,
        },
        {
            "type": "162",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "breach_time",
            "remove": False,
        },
        {
            "type": "162",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][8:12]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "breach_count",
            "remove": False,
        },
        {
            "type": "162",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][12:14]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "breach_status",
            "remove": False,
        },
        {
            "type": "162",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][14:16]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "breach_type(FENCE_BREACH)",
            "remove": False,
        },
        {
            "type": "162",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][16:18]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "breach_mitigation(FENCE_MITIGATE)",
            "remove": False,
        },
        {
            "type": "192",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "fitness",
            "remove": False,
        },
        {
            "type": "192",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "ofs_x",
            "remove": False,
        },
        {
            "type": "192",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "ofs_y",
            "remove": False,
        },
        {
            "type": "192",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "ofs_z",
            "remove": False,
        },
        {
            "type": "192",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "diag_x",
            "remove": False,
        },
        {
            "type": "192",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "diag_y",
            "remove": False,
        },
        {
            "type": "192",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "diag_z",
            "remove": False,
        },
        {
            "type": "192",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "offdiag_x",
            "remove": False,
        },
        {
            "type": "192",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][64:72]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "offdiag_y",
            "remove": False,
        },
        {
            "type": "192",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][72:80]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "offdiag_z",
            "remove": False,
        },
        {
            "type": "192",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][80:88]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "orientation_confidence",
            "remove": False,
        },
        {
            "type": "192",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][88:96]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "scale_factor",
            "remove": False,
        },
        {
            "type": "192",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][96:98]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "compass_id",
            "remove": False,
        },
        {
            "type": "192",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][98:100]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "cal_mask",
            "remove": False,
        },
        {
            "type": "192",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][100:102]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "cal_status(MAG_CAL_STATUS)",
            "remove": False,
        },
        {
            "type": "192",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][102:104]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "autosaved",
            "remove": False,
        },
        {
            "type": "192",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][104:106]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "old_orientation(MAV_SENSOR_ORIENTATION)",
            "remove": False,
        },
        {
            "type": "192",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][106:108]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "new_orientation(MAV_SENSOR_ORIENTATION)",
            "remove": False,
        },
        {
            "type": "225",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "ecu_index",
            "remove": False,
        },
        {
            "type": "225",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "rpm",
            "remove": False,
        },
        {
            "type": "225",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "fuel_consumed",
            "remove": False,
        },
        {
            "type": "225",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "fuel_flow",
            "remove": False,
        },
        {
            "type": "225",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "engine_load",
            "remove": False,
        },
        {
            "type": "225",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "throttle_position",
            "remove": False,
        },
        {
            "type": "225",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "spark_dwell_time",
            "remove": False,
        },
        {
            "type": "225",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "barometric_pressure",
            "remove": False,
        },
        {
            "type": "225",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][64:72]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "intake_manifold_pressure",
            "remove": False,
        },
        {
            "type": "225",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][72:80]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "intake_manifold_temperature",
            "remove": False,
        },
        {
            "type": "225",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][80:88]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "cylinder_head_temperature",
            "remove": False,
        },
        {
            "type": "225",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][88:96]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "ignition_timing",
            "remove": False,
        },
        {
            "type": "225",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][96:104]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "injection_time",
            "remove": False,
        },
        {
            "type": "225",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][104:112]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "exhaust_gas_temperature",
            "remove": False,
        },
        {
            "type": "225",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][112:120]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "throttle_out",
            "remove": False,
        },
        {
            "type": "225",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][120:128]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "pt_compensation",
            "remove": False,
        },
        {
            "type": "225",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][128:136]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "ignition_voltage",
            "remove": False,
        },
        {
            "type": "225",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][136:144]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "fuel_pressure",
            "remove": False,
        },
        {
            "type": "225",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][144:146]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "health",
            "remove": False,
        },
        {
            "type": "230",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "230",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vel_ratio",
            "remove": False,
        },
        {
            "type": "230",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "pos_horiz_ratio",
            "remove": False,
        },
        {
            "type": "230",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "pos_vert_ratio",
            "remove": False,
        },
        {
            "type": "230",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "mag_ratio",
            "remove": False,
        },
        {
            "type": "230",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "hagl_ratio",
            "remove": False,
        },
        {
            "type": "230",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "tas_ratio",
            "remove": False,
        },
        {
            "type": "230",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][64:72]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "pos_horiz_accuracy",
            "remove": False,
        },
        {
            "type": "230",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][72:80]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "pos_vert_accuracy",
            "remove": False,
        },
        {
            "type": "230",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][80:84]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "flags(ESTIMATOR_STATUS_FLAGS)",
            "remove": False,
        },
        {
            "type": "231",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "231",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "wind_x",
            "remove": False,
        },
        {
            "type": "231",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "wind_y",
            "remove": False,
        },
        {
            "type": "231",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "wind_z",
            "remove": False,
        },
        {
            "type": "231",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "var_horiz",
            "remove": False,
        },
        {
            "type": "231",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "var_vert",
            "remove": False,
        },
        {
            "type": "231",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "wind_alt",
            "remove": False,
        },
        {
            "type": "231",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][64:72]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "horiz_accuracy",
            "remove": False,
        },
        {
            "type": "231",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][72:80]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vert_accuracy",
            "remove": False,
        },
        {
            "type": "232",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "232",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_week_ms",
            "remove": False,
        },
        {
            "type": "232",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lat",
            "remove": False,
        },
        {
            "type": "232",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lon",
            "remove": False,
        },
        {
            "type": "232",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "alt",
            "remove": False,
        },
        {
            "type": "232",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "hdop",
            "remove": False,
        },
        {
            "type": "232",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vdop",
            "remove": False,
        },
        {
            "type": "232",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][64:72]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vn",
            "remove": False,
        },
        {
            "type": "232",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][72:80]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "ve",
            "remove": False,
        },
        {
            "type": "232",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][80:88]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vd",
            "remove": False,
        },
        {
            "type": "232",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][88:96]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "speed_accuracy",
            "remove": False,
        },
        {
            "type": "232",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][96:104]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "horiz_accuracy",
            "remove": False,
        },
        {
            "type": "232",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][104:112]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vert_accuracy",
            "remove": False,
        },
        {
            "type": "232",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][112:116]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "ignore_flags(GPS_INPUT_IGNORE_FLAGS)",
            "remove": False,
        },
        {
            "type": "232",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][116:120]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "time_week",
            "remove": False,
        },
        {
            "type": "232",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][120:124]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "yaw",
            "remove": False,
        },
        {
            "type": "232",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][124:126]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "gps_id",
            "remove": False,
        },
        {
            "type": "232",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][126:128]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "fix_type",
            "remove": False,
        },
        {
            "type": "232",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][128:130]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "satellites_visible",
            "remove": False,
        },
        {
            "type": "233",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][0:2]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "flags",
            "remove": False,
        },
        {
            "type": "233",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][2:4]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "len",
            "remove": False,
        },
        {
            "type": "233",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 4 : i + 6]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 360, 2)
            ],
            "name": "data",
            "remove": False,
        },
        {
            "type": "234",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "custom_mode",
            "remove": False,
        },
        {
            "type": "234",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "latitude",
            "remove": False,
        },
        {
            "type": "234",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "longitude",
            "remove": False,
        },
        {
            "type": "234",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][24:28]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "roll",
            "remove": False,
        },
        {
            "type": "234",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][28:32]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "pitch",
            "remove": False,
        },
        {
            "type": "234",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][32:36]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "heading",
            "remove": False,
        },
        {
            "type": "234",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][36:40]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "heading_sp",
            "remove": False,
        },
        {
            "type": "234",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][40:44]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "altitude_amsl",
            "remove": False,
        },
        {
            "type": "234",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][44:48]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "altitude_sp",
            "remove": False,
        },
        {
            "type": "234",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][48:52]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "wp_distance",
            "remove": False,
        },
        {
            "type": "234",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][52:54]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "base_mode(MAV_MODE_FLAG)",
            "remove": False,
        },
        {
            "type": "234",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][54:56]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "landed_state(MAV_LANDED_STATE)",
            "remove": False,
        },
        {
            "type": "234",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<b", bytes.fromhex(x[0][56:58]).ljust(struct.calcsize("<b"), b"\x00")
            )[0],
            "name": "throttle",
            "remove": False,
        },
        {
            "type": "234",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][58:60]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "airspeed",
            "remove": False,
        },
        {
            "type": "234",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][60:62]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "airspeed_sp",
            "remove": False,
        },
        {
            "type": "234",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][62:64]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "groundspeed",
            "remove": False,
        },
        {
            "type": "234",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<b", bytes.fromhex(x[0][64:66]).ljust(struct.calcsize("<b"), b"\x00")
            )[0],
            "name": "climb_rate",
            "remove": False,
        },
        {
            "type": "234",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][66:68]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "gps_nsat",
            "remove": False,
        },
        {
            "type": "234",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][68:70]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "gps_fix_type(GPS_FIX_TYPE)",
            "remove": False,
        },
        {
            "type": "234",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][70:72]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "battery_remaining",
            "remove": False,
        },
        {
            "type": "234",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<b", bytes.fromhex(x[0][72:74]).ljust(struct.calcsize("<b"), b"\x00")
            )[0],
            "name": "temperature",
            "remove": False,
        },
        {
            "type": "234",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<b", bytes.fromhex(x[0][74:76]).ljust(struct.calcsize("<b"), b"\x00")
            )[0],
            "name": "temperature_air",
            "remove": False,
        },
        {
            "type": "234",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][76:78]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "failsafe",
            "remove": False,
        },
        {
            "type": "234",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][78:80]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "wp_num",
            "remove": False,
        },
        {
            "type": "235",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "timestamp",
            "remove": False,
        },
        {
            "type": "235",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "latitude",
            "remove": False,
        },
        {
            "type": "235",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "longitude",
            "remove": False,
        },
        {
            "type": "235",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][24:28]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "custom_mode",
            "remove": False,
        },
        {
            "type": "235",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][28:32]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "altitude",
            "remove": False,
        },
        {
            "type": "235",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][32:36]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "target_altitude",
            "remove": False,
        },
        {
            "type": "235",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][36:40]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "target_distance",
            "remove": False,
        },
        {
            "type": "235",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][40:44]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "wp_num",
            "remove": False,
        },
        {
            "type": "235",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][44:48]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "failure_flags(HL_FAILURE_FLAG)",
            "remove": False,
        },
        {
            "type": "235",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][48:50]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "type(MAV_TYPE)",
            "remove": False,
        },
        {
            "type": "235",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][50:52]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "autopilot(MAV_AUTOPILOT)",
            "remove": False,
        },
        {
            "type": "235",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][52:54]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "heading",
            "remove": False,
        },
        {
            "type": "235",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][54:56]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_heading",
            "remove": False,
        },
        {
            "type": "235",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][56:58]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "throttle",
            "remove": False,
        },
        {
            "type": "235",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][58:60]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "airspeed",
            "remove": False,
        },
        {
            "type": "235",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][60:62]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "airspeed_sp",
            "remove": False,
        },
        {
            "type": "235",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][62:64]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "groundspeed",
            "remove": False,
        },
        {
            "type": "235",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][64:66]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "windspeed",
            "remove": False,
        },
        {
            "type": "235",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][66:68]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "wind_heading",
            "remove": False,
        },
        {
            "type": "235",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][68:70]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "eph",
            "remove": False,
        },
        {
            "type": "235",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][70:72]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "epv",
            "remove": False,
        },
        {
            "type": "235",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<b", bytes.fromhex(x[0][72:74]).ljust(struct.calcsize("<b"), b"\x00")
            )[0],
            "name": "temperature_air",
            "remove": False,
        },
        {
            "type": "235",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<b", bytes.fromhex(x[0][74:76]).ljust(struct.calcsize("<b"), b"\x00")
            )[0],
            "name": "climb_rate",
            "remove": False,
        },
        {
            "type": "235",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<b", bytes.fromhex(x[0][76:78]).ljust(struct.calcsize("<b"), b"\x00")
            )[0],
            "name": "battery",
            "remove": False,
        },
        {
            "type": "235",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<b", bytes.fromhex(x[0][78:80]).ljust(struct.calcsize("<b"), b"\x00")
            )[0],
            "name": "custom0",
            "remove": False,
        },
        {
            "type": "235",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<b", bytes.fromhex(x[0][80:82]).ljust(struct.calcsize("<b"), b"\x00")
            )[0],
            "name": "custom1",
            "remove": False,
        },
        {
            "type": "235",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<b", bytes.fromhex(x[0][82:84]).ljust(struct.calcsize("<b"), b"\x00")
            )[0],
            "name": "custom2",
            "remove": False,
        },
        {
            "type": "241",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "241",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vibration_x",
            "remove": False,
        },
        {
            "type": "241",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vibration_y",
            "remove": False,
        },
        {
            "type": "241",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vibration_z",
            "remove": False,
        },
        {
            "type": "241",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "clipping_0",
            "remove": False,
        },
        {
            "type": "241",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "clipping_1",
            "remove": False,
        },
        {
            "type": "241",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "clipping_2",
            "remove": False,
        },
        {
            "type": "242",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "242",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "latitude",
            "remove": False,
        },
        {
            "type": "242",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "longitude",
            "remove": False,
        },
        {
            "type": "242",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "altitude",
            "remove": False,
        },
        {
            "type": "242",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "x",
            "remove": False,
        },
        {
            "type": "242",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "y",
            "remove": False,
        },
        {
            "type": "242",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "z",
            "remove": False,
        },
        {
            "type": "242",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 64 : i + 72]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 32, 8)
            ],
            "name": "q",
            "remove": False,
        },
        {
            "type": "242",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][96:104]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "approach_x",
            "remove": False,
        },
        {
            "type": "242",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][104:112]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "approach_y",
            "remove": False,
        },
        {
            "type": "242",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][112:120]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "approach_z",
            "remove": False,
        },
        {
            "type": "243",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "243",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "latitude",
            "remove": False,
        },
        {
            "type": "243",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "longitude",
            "remove": False,
        },
        {
            "type": "243",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "altitude",
            "remove": False,
        },
        {
            "type": "243",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "x",
            "remove": False,
        },
        {
            "type": "243",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "y",
            "remove": False,
        },
        {
            "type": "243",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "z",
            "remove": False,
        },
        {
            "type": "243",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 64 : i + 72]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 32, 8)
            ],
            "name": "q",
            "remove": False,
        },
        {
            "type": "243",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][96:104]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "approach_x",
            "remove": False,
        },
        {
            "type": "243",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][104:112]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "approach_y",
            "remove": False,
        },
        {
            "type": "243",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][112:120]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "approach_z",
            "remove": False,
        },
        {
            "type": "243",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][120:122]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "244",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "interval_us",
            "remove": False,
        },
        {
            "type": "244",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][8:12]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "message_id",
            "remove": False,
        },
        {
            "type": "245",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][0:2]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "vtol_state(MAV_VTOL_STATE)",
            "remove": False,
        },
        {
            "type": "245",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][2:4]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "landed_state(MAV_LANDED_STATE)",
            "remove": False,
        },
        {
            "type": "246",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "ICAO_address",
            "remove": False,
        },
        {
            "type": "246",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lat",
            "remove": False,
        },
        {
            "type": "246",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lon",
            "remove": False,
        },
        {
            "type": "246",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "altitude",
            "remove": False,
        },
        {
            "type": "246",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][32:36]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "heading",
            "remove": False,
        },
        {
            "type": "246",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][36:40]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "hor_velocity",
            "remove": False,
        },
        {
            "type": "246",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][40:44]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "ver_velocity",
            "remove": False,
        },
        {
            "type": "246",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][44:48]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "flags(ADSB_FLAGS)",
            "remove": False,
        },
        {
            "type": "246",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][48:52]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "squawk",
            "remove": False,
        },
        {
            "type": "246",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][52:54]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "altitude_type(ADSB_ALTITUDE_TYPE)",
            "remove": False,
        },
        {
            "type": "246",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 54 : i + 56]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 18, 2)
                ]
            ).rstrip("\x00"),
            "name": "callsign",
            "remove": False,
        },
        {
            "type": "246",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][72:74]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "emitter_type(ADSB_EMITTER_TYPE)",
            "remove": False,
        },
        {
            "type": "246",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][74:76]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "tslc",
            "remove": False,
        },
        {
            "type": "247",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "id",
            "remove": False,
        },
        {
            "type": "247",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "time_to_minimum_delta",
            "remove": False,
        },
        {
            "type": "247",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "altitude_minimum_delta",
            "remove": False,
        },
        {
            "type": "247",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "horizontal_minimum_delta",
            "remove": False,
        },
        {
            "type": "247",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][32:34]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "src(MAV_COLLISION_SRC)",
            "remove": False,
        },
        {
            "type": "247",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][34:36]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "action(MAV_COLLISION_ACTION)",
            "remove": False,
        },
        {
            "type": "247",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][36:38]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "threat_level(MAV_COLLISION_THREAT_LEVEL)",
            "remove": False,
        },
        {
            "type": "248",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][0:4]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "message_type",
            "remove": False,
        },
        {
            "type": "248",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][4:6]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_network",
            "remove": False,
        },
        {
            "type": "248",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][6:8]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "248",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][8:10]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "248",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 10 : i + 12]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 498, 2)
            ],
            "name": "payload",
            "remove": False,
        },
        {
            "type": "249",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][0:4]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "address",
            "remove": False,
        },
        {
            "type": "249",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][4:6]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "ver",
            "remove": False,
        },
        {
            "type": "249",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][6:8]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "type",
            "remove": False,
        },
        {
            "type": "249",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<b",
                    bytes.fromhex(x[0][i + 8 : i + 10]).ljust(
                        struct.calcsize("<b"), b"\x00"
                    ),
                )[0]
                for i in range(0, 64, 2)
            ],
            "name": "value",
            "remove": False,
        },
        {
            "type": "250",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "250",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "x",
            "remove": False,
        },
        {
            "type": "250",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "y",
            "remove": False,
        },
        {
            "type": "250",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "z",
            "remove": False,
        },
        {
            "type": "250",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 40 : i + 42]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 20, 2)
                ]
            ).rstrip("\x00"),
            "name": "name",
            "remove": False,
        },
        {
            "type": "251",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "251",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "value",
            "remove": False,
        },
        {
            "type": "251",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 16 : i + 18]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 20, 2)
                ]
            ).rstrip("\x00"),
            "name": "name",
            "remove": False,
        },
        {
            "type": "252",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "252",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "value",
            "remove": False,
        },
        {
            "type": "252",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 16 : i + 18]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 20, 2)
                ]
            ).rstrip("\x00"),
            "name": "name",
            "remove": False,
        },
        {
            "type": "253",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][0:4]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "id",
            "remove": False,
        },
        {
            "type": "253",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][4:6]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "severity(MAV_SEVERITY)",
            "remove": False,
        },
        {
            "type": "253",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 6 : i + 8]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 100, 2)
                ]
            ).rstrip("\x00"),
            "name": "text",
            "remove": False,
        },
        {
            "type": "253",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][106:108]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "chunk_seq",
            "remove": False,
        },
        {
            "type": "254",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "254",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "value",
            "remove": False,
        },
        {
            "type": "254",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][16:18]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "ind",
            "remove": False,
        },
        {
            "type": "256",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "initial_timestamp",
            "remove": False,
        },
        {
            "type": "256",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][16:18]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "256",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][18:20]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "256",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 20 : i + 22]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 64, 2)
            ],
            "name": "secret_key",
            "remove": False,
        },
        {
            "type": "257",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "257",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "last_change_ms",
            "remove": False,
        },
        {
            "type": "257",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][16:18]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "state",
            "remove": False,
        },
        {
            "type": "258",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][0:2]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "258",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][2:4]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "258",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 4 : i + 6]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 60, 2)
                ]
            ).rstrip("\x00"),
            "name": "tune",
            "remove": False,
        },
        {
            "type": "258",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 64 : i + 66]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 400, 2)
                ]
            ).rstrip("\x00"),
            "name": "tune2",
            "remove": False,
        },
        {
            "type": "259",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "259",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "firmware_version",
            "remove": False,
        },
        {
            "type": "259",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "focal_length",
            "remove": False,
        },
        {
            "type": "259",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "sensor_size_h",
            "remove": False,
        },
        {
            "type": "259",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "sensor_size_v",
            "remove": False,
        },
        {
            "type": "259",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "flags(CAMERA_CAP_FLAGS)",
            "remove": False,
        },
        {
            "type": "259",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][48:52]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "resolution_h",
            "remove": False,
        },
        {
            "type": "259",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][52:56]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "resolution_v",
            "remove": False,
        },
        {
            "type": "259",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][56:60]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "cam_definition_version",
            "remove": False,
        },
        {
            "type": "259",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 60 : i + 62]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 64, 2)
            ],
            "name": "vendor_name",
            "remove": False,
        },
        {
            "type": "259",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 124 : i + 126]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 64, 2)
            ],
            "name": "model_name",
            "remove": False,
        },
        {
            "type": "259",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][188:190]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "lens_id",
            "remove": False,
        },
        {
            "type": "259",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 190 : i + 192]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 280, 2)
                ]
            ).rstrip("\x00"),
            "name": "cam_definition_uri",
            "remove": False,
        },
        {
            "type": "260",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "260",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "zoomLevel",
            "remove": False,
        },
        {
            "type": "260",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "focusLevel",
            "remove": False,
        },
        {
            "type": "260",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][24:26]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "mode_id(CAMERA_MODE)",
            "remove": False,
        },
        {
            "type": "261",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "261",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "total_capacity",
            "remove": False,
        },
        {
            "type": "261",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "used_capacity",
            "remove": False,
        },
        {
            "type": "261",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "available_capacity",
            "remove": False,
        },
        {
            "type": "261",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "read_speed",
            "remove": False,
        },
        {
            "type": "261",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "write_speed",
            "remove": False,
        },
        {
            "type": "261",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][48:50]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "storage_id",
            "remove": False,
        },
        {
            "type": "261",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][50:52]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "storage_count",
            "remove": False,
        },
        {
            "type": "261",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][52:54]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "status(STORAGE_STATUS)",
            "remove": False,
        },
        {
            "type": "261",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][54:56]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "type(STORAGE_TYPE)",
            "remove": False,
        },
        {
            "type": "261",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 56 : i + 58]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 64, 2)
                ]
            ).rstrip("\x00"),
            "name": "name",
            "remove": False,
        },
        {
            "type": "261",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][120:122]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "storage_usage(STORAGE_USAGE_FLAG)",
            "remove": False,
        },
        {
            "type": "262",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "262",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "image_interval",
            "remove": False,
        },
        {
            "type": "262",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "recording_time_ms",
            "remove": False,
        },
        {
            "type": "262",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "available_capacity",
            "remove": False,
        },
        {
            "type": "262",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "image_count",
            "remove": False,
        },
        {
            "type": "262",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][40:42]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "image_status",
            "remove": False,
        },
        {
            "type": "262",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][42:44]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "video_status",
            "remove": False,
        },
        {
            "type": "263",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_utc",
            "remove": False,
        },
        {
            "type": "263",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "263",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lat",
            "remove": False,
        },
        {
            "type": "263",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lon",
            "remove": False,
        },
        {
            "type": "263",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "alt",
            "remove": False,
        },
        {
            "type": "263",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "relative_alt",
            "remove": False,
        },
        {
            "type": "263",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 56 : i + 64]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 32, 8)
            ],
            "name": "q",
            "remove": False,
        },
        {
            "type": "263",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][88:96]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "image_index",
            "remove": False,
        },
        {
            "type": "263",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][96:98]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "camera_id",
            "remove": False,
        },
        {
            "type": "263",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<b", bytes.fromhex(x[0][98:100]).ljust(struct.calcsize("<b"), b"\x00")
            )[0],
            "name": "capture_result",
            "remove": False,
        },
        {
            "type": "263",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 100 : i + 102]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 410, 2)
                ]
            ).rstrip("\x00"),
            "name": "file_url",
            "remove": False,
        },
        {
            "type": "264",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "arming_time_utc",
            "remove": False,
        },
        {
            "type": "264",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][16:32]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "takeoff_time_utc",
            "remove": False,
        },
        {
            "type": "264",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][32:48]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "flight_uuid",
            "remove": False,
        },
        {
            "type": "264",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "265",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "265",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "roll",
            "remove": False,
        },
        {
            "type": "265",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "pitch",
            "remove": False,
        },
        {
            "type": "265",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yaw",
            "remove": False,
        },
        {
            "type": "265",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yaw_absolute",
            "remove": False,
        },
        {
            "type": "266",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][0:4]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "sequence",
            "remove": False,
        },
        {
            "type": "266",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][4:6]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "266",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][6:8]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "266",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][8:10]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "length",
            "remove": False,
        },
        {
            "type": "266",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][10:12]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "first_message_offset",
            "remove": False,
        },
        {
            "type": "266",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 12 : i + 14]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 498, 2)
            ],
            "name": "data",
            "remove": False,
        },
        {
            "type": "267",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][0:4]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "sequence",
            "remove": False,
        },
        {
            "type": "267",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][4:6]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "267",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][6:8]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "267",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][8:10]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "length",
            "remove": False,
        },
        {
            "type": "267",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][10:12]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "first_message_offset",
            "remove": False,
        },
        {
            "type": "267",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 12 : i + 14]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 498, 2)
            ],
            "name": "data",
            "remove": False,
        },
        {
            "type": "268",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][0:4]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "sequence",
            "remove": False,
        },
        {
            "type": "268",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][4:6]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "268",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][6:8]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "269",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "framerate",
            "remove": False,
        },
        {
            "type": "269",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "bitrate",
            "remove": False,
        },
        {
            "type": "269",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][16:20]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "flags(VIDEO_STREAM_STATUS_FLAGS)",
            "remove": False,
        },
        {
            "type": "269",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][20:24]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "resolution_h",
            "remove": False,
        },
        {
            "type": "269",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][24:28]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "resolution_v",
            "remove": False,
        },
        {
            "type": "269",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][28:32]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "rotation",
            "remove": False,
        },
        {
            "type": "269",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][32:36]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "hfov",
            "remove": False,
        },
        {
            "type": "269",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][36:38]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "stream_id",
            "remove": False,
        },
        {
            "type": "269",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][38:40]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "count",
            "remove": False,
        },
        {
            "type": "269",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][40:42]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "type(VIDEO_STREAM_TYPE)",
            "remove": False,
        },
        {
            "type": "269",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 42 : i + 44]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 64, 2)
                ]
            ).rstrip("\x00"),
            "name": "name",
            "remove": False,
        },
        {
            "type": "269",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 106 : i + 108]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 320, 2)
                ]
            ).rstrip("\x00"),
            "name": "uri",
            "remove": False,
        },
        {
            "type": "270",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "framerate",
            "remove": False,
        },
        {
            "type": "270",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "bitrate",
            "remove": False,
        },
        {
            "type": "270",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][16:20]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "flags(VIDEO_STREAM_STATUS_FLAGS)",
            "remove": False,
        },
        {
            "type": "270",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][20:24]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "resolution_h",
            "remove": False,
        },
        {
            "type": "270",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][24:28]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "resolution_v",
            "remove": False,
        },
        {
            "type": "270",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][28:32]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "rotation",
            "remove": False,
        },
        {
            "type": "270",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][32:36]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "hfov",
            "remove": False,
        },
        {
            "type": "270",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][36:38]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "stream_id",
            "remove": False,
        },
        {
            "type": "271",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "271",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lat_camera",
            "remove": False,
        },
        {
            "type": "271",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lon_camera",
            "remove": False,
        },
        {
            "type": "271",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "alt_camera",
            "remove": False,
        },
        {
            "type": "271",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lat_image",
            "remove": False,
        },
        {
            "type": "271",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lon_image",
            "remove": False,
        },
        {
            "type": "271",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "alt_image",
            "remove": False,
        },
        {
            "type": "271",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 56 : i + 64]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 32, 8)
            ],
            "name": "q",
            "remove": False,
        },
        {
            "type": "271",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][88:96]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "hfov",
            "remove": False,
        },
        {
            "type": "271",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][96:104]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vfov",
            "remove": False,
        },
        {
            "type": "275",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "point_x",
            "remove": False,
        },
        {
            "type": "275",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "point_y",
            "remove": False,
        },
        {
            "type": "275",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "radius",
            "remove": False,
        },
        {
            "type": "275",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "rec_top_x",
            "remove": False,
        },
        {
            "type": "275",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "rec_top_y",
            "remove": False,
        },
        {
            "type": "275",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "rec_bottom_x",
            "remove": False,
        },
        {
            "type": "275",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "rec_bottom_y",
            "remove": False,
        },
        {
            "type": "275",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][56:58]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "tracking_status(CAMERA_TRACKING_STATUS_FLAGS)",
            "remove": False,
        },
        {
            "type": "275",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][58:60]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "tracking_mode(CAMERA_TRACKING_MODE)",
            "remove": False,
        },
        {
            "type": "275",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][60:62]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_data(CAMERA_TRACKING_TARGET_DATA)",
            "remove": False,
        },
        {
            "type": "276",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lat",
            "remove": False,
        },
        {
            "type": "276",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lon",
            "remove": False,
        },
        {
            "type": "276",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "alt",
            "remove": False,
        },
        {
            "type": "276",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "h_acc",
            "remove": False,
        },
        {
            "type": "276",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "v_acc",
            "remove": False,
        },
        {
            "type": "276",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vel_n",
            "remove": False,
        },
        {
            "type": "276",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vel_e",
            "remove": False,
        },
        {
            "type": "276",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vel_d",
            "remove": False,
        },
        {
            "type": "276",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][64:72]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vel_acc",
            "remove": False,
        },
        {
            "type": "276",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][72:80]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "dist",
            "remove": False,
        },
        {
            "type": "276",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][80:88]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "hdg",
            "remove": False,
        },
        {
            "type": "276",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][88:96]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "hdg_acc",
            "remove": False,
        },
        {
            "type": "276",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][96:98]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "tracking_status(CAMERA_TRACKING_STATUS_FLAGS)",
            "remove": False,
        },
        {
            "type": "280",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "280",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "cap_flags(GIMBAL_MANAGER_CAP_FLAGS)",
            "remove": False,
        },
        {
            "type": "280",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "roll_min",
            "remove": False,
        },
        {
            "type": "280",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "roll_max",
            "remove": False,
        },
        {
            "type": "280",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "pitch_min",
            "remove": False,
        },
        {
            "type": "280",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "pitch_max",
            "remove": False,
        },
        {
            "type": "280",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yaw_min",
            "remove": False,
        },
        {
            "type": "280",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yaw_max",
            "remove": False,
        },
        {
            "type": "280",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][64:66]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "gimbal_device_id",
            "remove": False,
        },
        {
            "type": "281",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "281",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "flags(GIMBAL_MANAGER_FLAGS)",
            "remove": False,
        },
        {
            "type": "281",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][16:18]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "gimbal_device_id",
            "remove": False,
        },
        {
            "type": "281",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][18:20]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "primary_control_sysid",
            "remove": False,
        },
        {
            "type": "281",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][20:22]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "primary_control_compid",
            "remove": False,
        },
        {
            "type": "281",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][22:24]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "secondary_control_sysid",
            "remove": False,
        },
        {
            "type": "281",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][24:26]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "secondary_control_compid",
            "remove": False,
        },
        {
            "type": "282",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "flags(GIMBAL_MANAGER_FLAGS)",
            "remove": False,
        },
        {
            "type": "282",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 8 : i + 16]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 32, 8)
            ],
            "name": "q",
            "remove": False,
        },
        {
            "type": "282",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "angular_velocity_x",
            "remove": False,
        },
        {
            "type": "282",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "angular_velocity_y",
            "remove": False,
        },
        {
            "type": "282",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "angular_velocity_z",
            "remove": False,
        },
        {
            "type": "282",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][64:66]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "282",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][66:68]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "282",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][68:70]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "gimbal_device_id",
            "remove": False,
        },
        {
            "type": "283",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "uid",
            "remove": False,
        },
        {
            "type": "283",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "283",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "firmware_version",
            "remove": False,
        },
        {
            "type": "283",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "hardware_version",
            "remove": False,
        },
        {
            "type": "283",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "roll_min",
            "remove": False,
        },
        {
            "type": "283",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "roll_max",
            "remove": False,
        },
        {
            "type": "283",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "pitch_min",
            "remove": False,
        },
        {
            "type": "283",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][64:72]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "pitch_max",
            "remove": False,
        },
        {
            "type": "283",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][72:80]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yaw_min",
            "remove": False,
        },
        {
            "type": "283",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][80:88]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yaw_max",
            "remove": False,
        },
        {
            "type": "283",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][88:92]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "cap_flags(GIMBAL_DEVICE_CAP_FLAGS)",
            "remove": False,
        },
        {
            "type": "283",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][92:96]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "custom_cap_flags",
            "remove": False,
        },
        {
            "type": "283",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 96 : i + 98]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 64, 2)
                ]
            ).rstrip("\x00"),
            "name": "vendor_name",
            "remove": False,
        },
        {
            "type": "283",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 160 : i + 162]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 64, 2)
                ]
            ).rstrip("\x00"),
            "name": "model_name",
            "remove": False,
        },
        {
            "type": "283",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 224 : i + 226]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 64, 2)
                ]
            ).rstrip("\x00"),
            "name": "custom_name",
            "remove": False,
        },
        {
            "type": "284",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 0 : i + 8]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 32, 8)
            ],
            "name": "q",
            "remove": False,
        },
        {
            "type": "284",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "angular_velocity_x",
            "remove": False,
        },
        {
            "type": "284",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "angular_velocity_y",
            "remove": False,
        },
        {
            "type": "284",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "angular_velocity_z",
            "remove": False,
        },
        {
            "type": "284",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][56:60]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "flags(GIMBAL_DEVICE_FLAGS)",
            "remove": False,
        },
        {
            "type": "284",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][60:62]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "284",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][62:64]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "285",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "285",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 8 : i + 16]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 32, 8)
            ],
            "name": "q",
            "remove": False,
        },
        {
            "type": "285",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "angular_velocity_x",
            "remove": False,
        },
        {
            "type": "285",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "angular_velocity_y",
            "remove": False,
        },
        {
            "type": "285",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "angular_velocity_z",
            "remove": False,
        },
        {
            "type": "285",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][64:72]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "failure_flags(GIMBAL_DEVICE_ERROR_FLAGS)",
            "remove": False,
        },
        {
            "type": "285",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][72:80]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "delta_yaw",
            "remove": False,
        },
        {
            "type": "285",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][80:88]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "delta_yaw_velocity",
            "remove": False,
        },
        {
            "type": "285",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][88:92]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "flags(GIMBAL_DEVICE_FLAGS)",
            "remove": False,
        },
        {
            "type": "285",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][92:94]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "285",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][94:96]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "286",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_boot_us",
            "remove": False,
        },
        {
            "type": "286",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 16 : i + 24]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 32, 8)
            ],
            "name": "q",
            "remove": False,
        },
        {
            "type": "286",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "q_estimated_delay_us",
            "remove": False,
        },
        {
            "type": "286",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vx",
            "remove": False,
        },
        {
            "type": "286",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][64:72]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vy",
            "remove": False,
        },
        {
            "type": "286",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][72:80]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vz",
            "remove": False,
        },
        {
            "type": "286",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][80:88]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "v_estimated_delay_us",
            "remove": False,
        },
        {
            "type": "286",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][88:96]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "feed_forward_angular_velocity_z",
            "remove": False,
        },
        {
            "type": "286",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][96:104]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "angular_velocity_z",
            "remove": False,
        },
        {
            "type": "286",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][104:108]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "estimator_status(ESTIMATOR_STATUS_FLAGS)",
            "remove": False,
        },
        {
            "type": "286",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][108:110]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "286",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][110:112]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "286",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][112:114]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "landed_state(MAV_LANDED_STATE)",
            "remove": False,
        },
        {
            "type": "287",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "flags(GIMBAL_MANAGER_FLAGS)",
            "remove": False,
        },
        {
            "type": "287",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "pitch",
            "remove": False,
        },
        {
            "type": "287",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yaw",
            "remove": False,
        },
        {
            "type": "287",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "pitch_rate",
            "remove": False,
        },
        {
            "type": "287",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yaw_rate",
            "remove": False,
        },
        {
            "type": "287",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][40:42]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "287",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][42:44]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "287",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][44:46]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "gimbal_device_id",
            "remove": False,
        },
        {
            "type": "288",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "flags(GIMBAL_MANAGER_FLAGS)",
            "remove": False,
        },
        {
            "type": "288",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "pitch",
            "remove": False,
        },
        {
            "type": "288",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yaw",
            "remove": False,
        },
        {
            "type": "288",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "pitch_rate",
            "remove": False,
        },
        {
            "type": "288",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yaw_rate",
            "remove": False,
        },
        {
            "type": "288",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][40:42]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "288",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][42:44]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "288",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][44:46]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "gimbal_device_id",
            "remove": False,
        },
        {
            "type": "290",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "290",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<I",
                    bytes.fromhex(x[0][i + 16 : i + 24]).ljust(
                        struct.calcsize("<I"), b"\x00"
                    ),
                )[0]
                for i in range(0, 32, 8)
            ],
            "name": "error_count",
            "remove": False,
        },
        {
            "type": "290",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][48:52]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "counter",
            "remove": False,
        },
        {
            "type": "290",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<H",
                    bytes.fromhex(x[0][i + 52 : i + 56]).ljust(
                        struct.calcsize("<H"), b"\x00"
                    ),
                )[0]
                for i in range(0, 16, 4)
            ],
            "name": "failure_flags(ESC_FAILURE_FLAGS)",
            "remove": False,
        },
        {
            "type": "290",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<h",
                    bytes.fromhex(x[0][i + 68 : i + 72]).ljust(
                        struct.calcsize("<h"), b"\x00"
                    ),
                )[0]
                for i in range(0, 16, 4)
            ],
            "name": "temperature",
            "remove": False,
        },
        {
            "type": "290",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][84:86]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "index",
            "remove": False,
        },
        {
            "type": "290",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][86:88]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "count",
            "remove": False,
        },
        {
            "type": "290",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][88:90]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "connection_type(ESC_CONNECTION_TYPE)",
            "remove": False,
        },
        {
            "type": "290",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][90:92]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "info",
            "remove": False,
        },
        {
            "type": "291",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "291",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<i",
                    bytes.fromhex(x[0][i + 16 : i + 24]).ljust(
                        struct.calcsize("<i"), b"\x00"
                    ),
                )[0]
                for i in range(0, 32, 8)
            ],
            "name": "rpm",
            "remove": False,
        },
        {
            "type": "291",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 48 : i + 56]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 32, 8)
            ],
            "name": "voltage",
            "remove": False,
        },
        {
            "type": "291",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 80 : i + 88]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 32, 8)
            ],
            "name": "current",
            "remove": False,
        },
        {
            "type": "291",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][112:114]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "index",
            "remove": False,
        },
        {
            "type": "299",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 0 : i + 2]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 64, 2)
                ]
            ).rstrip("\x00"),
            "name": "ssid",
            "remove": False,
        },
        {
            "type": "299",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 64 : i + 66]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 128, 2)
                ]
            ).rstrip("\x00"),
            "name": "password",
            "remove": False,
        },
        {
            "type": "299",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<b", bytes.fromhex(x[0][192:194]).ljust(struct.calcsize("<b"), b"\x00")
            )[0],
            "name": "mode(WIFI_CONFIG_AP_MODE)",
            "remove": False,
        },
        {
            "type": "299",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<b", bytes.fromhex(x[0][194:196]).ljust(struct.calcsize("<b"), b"\x00")
            )[0],
            "name": "response(WIFI_CONFIG_AP_RESPONSE)",
            "remove": False,
        },
        {
            "type": "301",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "MMSI",
            "remove": False,
        },
        {
            "type": "301",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lat",
            "remove": False,
        },
        {
            "type": "301",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lon",
            "remove": False,
        },
        {
            "type": "301",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][24:28]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "COG",
            "remove": False,
        },
        {
            "type": "301",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][28:32]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "heading",
            "remove": False,
        },
        {
            "type": "301",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][32:36]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "velocity",
            "remove": False,
        },
        {
            "type": "301",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][36:40]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "dimension_bow",
            "remove": False,
        },
        {
            "type": "301",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][40:44]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "dimension_stern",
            "remove": False,
        },
        {
            "type": "301",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][44:48]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "tslc",
            "remove": False,
        },
        {
            "type": "301",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][48:52]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "flags(AIS_FLAGS)",
            "remove": False,
        },
        {
            "type": "301",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<b", bytes.fromhex(x[0][52:54]).ljust(struct.calcsize("<b"), b"\x00")
            )[0],
            "name": "turn_rate",
            "remove": False,
        },
        {
            "type": "301",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][54:56]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "navigational_status(AIS_NAV_STATUS)",
            "remove": False,
        },
        {
            "type": "301",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][56:58]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "type(AIS_TYPE)",
            "remove": False,
        },
        {
            "type": "301",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][58:60]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "dimension_port",
            "remove": False,
        },
        {
            "type": "301",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][60:62]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "dimension_starboard",
            "remove": False,
        },
        {
            "type": "301",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 62 : i + 64]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 14, 2)
                ]
            ).rstrip("\x00"),
            "name": "callsign",
            "remove": False,
        },
        {
            "type": "301",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 76 : i + 78]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 40, 2)
                ]
            ).rstrip("\x00"),
            "name": "name",
            "remove": False,
        },
        {
            "type": "310",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "310",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "uptime_sec",
            "remove": False,
        },
        {
            "type": "310",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][24:28]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "vendor_specific_status_code",
            "remove": False,
        },
        {
            "type": "310",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][28:30]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "health(UAVCAN_NODE_HEALTH)",
            "remove": False,
        },
        {
            "type": "310",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][30:32]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "mode(UAVCAN_NODE_MODE)",
            "remove": False,
        },
        {
            "type": "310",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][32:34]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "sub_mode",
            "remove": False,
        },
        {
            "type": "311",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "311",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "uptime_sec",
            "remove": False,
        },
        {
            "type": "311",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "sw_vcs_commit",
            "remove": False,
        },
        {
            "type": "311",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 32 : i + 34]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 160, 2)
                ]
            ).rstrip("\x00"),
            "name": "name",
            "remove": False,
        },
        {
            "type": "311",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][192:194]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "hw_version_major",
            "remove": False,
        },
        {
            "type": "311",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][194:196]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "hw_version_minor",
            "remove": False,
        },
        {
            "type": "311",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 196 : i + 198]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 32, 2)
            ],
            "name": "hw_unique_id",
            "remove": False,
        },
        {
            "type": "311",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][228:230]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "sw_version_major",
            "remove": False,
        },
        {
            "type": "311",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][230:232]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "sw_version_minor",
            "remove": False,
        },
        {
            "type": "320",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][0:4]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "param_index",
            "remove": False,
        },
        {
            "type": "320",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][4:6]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "320",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][6:8]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "320",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 8 : i + 10]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 32, 2)
                ]
            ).rstrip("\x00"),
            "name": "param_id",
            "remove": False,
        },
        {
            "type": "321",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][0:2]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "321",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][2:4]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "322",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][0:4]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "param_count",
            "remove": False,
        },
        {
            "type": "322",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][4:8]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "param_index",
            "remove": False,
        },
        {
            "type": "322",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 8 : i + 10]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 32, 2)
                ]
            ).rstrip("\x00"),
            "name": "param_id",
            "remove": False,
        },
        {
            "type": "322",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 40 : i + 42]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 256, 2)
                ]
            ).rstrip("\x00"),
            "name": "param_value",
            "remove": False,
        },
        {
            "type": "322",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][296:298]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "param_type(MAV_PARAM_EXT_TYPE)",
            "remove": False,
        },
        {
            "type": "323",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][0:2]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "323",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][2:4]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "323",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 4 : i + 6]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 32, 2)
                ]
            ).rstrip("\x00"),
            "name": "param_id",
            "remove": False,
        },
        {
            "type": "323",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 36 : i + 38]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 256, 2)
                ]
            ).rstrip("\x00"),
            "name": "param_value",
            "remove": False,
        },
        {
            "type": "323",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][292:294]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "param_type(MAV_PARAM_EXT_TYPE)",
            "remove": False,
        },
        {
            "type": "324",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 0 : i + 2]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 32, 2)
                ]
            ).rstrip("\x00"),
            "name": "param_id",
            "remove": False,
        },
        {
            "type": "324",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 32 : i + 34]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 256, 2)
                ]
            ).rstrip("\x00"),
            "name": "param_value",
            "remove": False,
        },
        {
            "type": "324",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][288:290]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "param_type(MAV_PARAM_EXT_TYPE)",
            "remove": False,
        },
        {
            "type": "324",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][290:292]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "param_result(PARAM_ACK)",
            "remove": False,
        },
        {
            "type": "330",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "330",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "increment_f",
            "remove": False,
        },
        {
            "type": "330",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "angle_offset",
            "remove": False,
        },
        {
            "type": "330",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<H",
                    bytes.fromhex(x[0][i + 32 : i + 36]).ljust(
                        struct.calcsize("<H"), b"\x00"
                    ),
                )[0]
                for i in range(0, 288, 4)
            ],
            "name": "distances",
            "remove": False,
        },
        {
            "type": "330",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][320:324]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "min_distance",
            "remove": False,
        },
        {
            "type": "330",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][324:328]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "max_distance",
            "remove": False,
        },
        {
            "type": "330",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][328:330]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "sensor_type(MAV_DISTANCE_SENSOR)",
            "remove": False,
        },
        {
            "type": "330",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][330:332]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "increment",
            "remove": False,
        },
        {
            "type": "330",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][332:334]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "frame(MAV_FRAME)",
            "remove": False,
        },
        {
            "type": "331",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "331",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "x",
            "remove": False,
        },
        {
            "type": "331",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "y",
            "remove": False,
        },
        {
            "type": "331",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "z",
            "remove": False,
        },
        {
            "type": "331",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 40 : i + 48]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 32, 8)
            ],
            "name": "q",
            "remove": False,
        },
        {
            "type": "331",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][72:80]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vx",
            "remove": False,
        },
        {
            "type": "331",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][80:88]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vy",
            "remove": False,
        },
        {
            "type": "331",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][88:96]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "vz",
            "remove": False,
        },
        {
            "type": "331",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][96:104]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "rollspeed",
            "remove": False,
        },
        {
            "type": "331",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][104:112]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "pitchspeed",
            "remove": False,
        },
        {
            "type": "331",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][112:120]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "yawspeed",
            "remove": False,
        },
        {
            "type": "331",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 120 : i + 128]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 168, 8)
            ],
            "name": "pose_covariance",
            "remove": False,
        },
        {
            "type": "331",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 288 : i + 296]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 168, 8)
            ],
            "name": "velocity_covariance",
            "remove": False,
        },
        {
            "type": "331",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][456:458]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "frame_id(MAV_FRAME)",
            "remove": False,
        },
        {
            "type": "331",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][458:460]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "child_frame_id(MAV_FRAME)",
            "remove": False,
        },
        {
            "type": "331",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][460:462]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "reset_counter",
            "remove": False,
        },
        {
            "type": "331",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][462:464]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "estimator_type(MAV_ESTIMATOR_TYPE)",
            "remove": False,
        },
        {
            "type": "331",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<b", bytes.fromhex(x[0][464:466]).ljust(struct.calcsize("<b"), b"\x00")
            )[0],
            "name": "quality",
            "remove": False,
        },
        {
            "type": "332",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "332",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 16 : i + 24]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 40, 8)
            ],
            "name": "pos_x",
            "remove": False,
        },
        {
            "type": "332",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 56 : i + 64]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 40, 8)
            ],
            "name": "pos_y",
            "remove": False,
        },
        {
            "type": "332",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 96 : i + 104]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 40, 8)
            ],
            "name": "pos_z",
            "remove": False,
        },
        {
            "type": "332",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 136 : i + 144]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 40, 8)
            ],
            "name": "vel_x",
            "remove": False,
        },
        {
            "type": "332",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 176 : i + 184]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 40, 8)
            ],
            "name": "vel_y",
            "remove": False,
        },
        {
            "type": "332",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 216 : i + 224]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 40, 8)
            ],
            "name": "vel_z",
            "remove": False,
        },
        {
            "type": "332",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 256 : i + 264]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 40, 8)
            ],
            "name": "acc_x",
            "remove": False,
        },
        {
            "type": "332",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 296 : i + 304]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 40, 8)
            ],
            "name": "acc_y",
            "remove": False,
        },
        {
            "type": "332",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 336 : i + 344]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 40, 8)
            ],
            "name": "acc_z",
            "remove": False,
        },
        {
            "type": "332",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 376 : i + 384]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 40, 8)
            ],
            "name": "pos_yaw",
            "remove": False,
        },
        {
            "type": "332",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 416 : i + 424]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 40, 8)
            ],
            "name": "vel_yaw",
            "remove": False,
        },
        {
            "type": "332",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<H",
                    bytes.fromhex(x[0][i + 456 : i + 460]).ljust(
                        struct.calcsize("<H"), b"\x00"
                    ),
                )[0]
                for i in range(0, 20, 4)
            ],
            "name": "command(MAV_CMD)",
            "remove": False,
        },
        {
            "type": "332",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][476:478]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "valid_points",
            "remove": False,
        },
        {
            "type": "333",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "333",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 16 : i + 24]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 40, 8)
            ],
            "name": "pos_x",
            "remove": False,
        },
        {
            "type": "333",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 56 : i + 64]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 40, 8)
            ],
            "name": "pos_y",
            "remove": False,
        },
        {
            "type": "333",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 96 : i + 104]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 40, 8)
            ],
            "name": "pos_z",
            "remove": False,
        },
        {
            "type": "333",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 136 : i + 144]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 40, 8)
            ],
            "name": "delta",
            "remove": False,
        },
        {
            "type": "333",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 176 : i + 184]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 40, 8)
            ],
            "name": "pos_yaw",
            "remove": False,
        },
        {
            "type": "333",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][216:218]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "valid_points",
            "remove": False,
        },
        {
            "type": "334",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][0:4]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "mcc",
            "remove": False,
        },
        {
            "type": "334",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][4:8]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "mnc",
            "remove": False,
        },
        {
            "type": "334",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][8:12]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "lac",
            "remove": False,
        },
        {
            "type": "334",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][12:14]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "status(CELLULAR_STATUS_FLAG)",
            "remove": False,
        },
        {
            "type": "334",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][14:16]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "failure_reason(CELLULAR_NETWORK_FAILED_REASON)",
            "remove": False,
        },
        {
            "type": "334",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][16:18]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "type(CELLULAR_NETWORK_RADIO_TYPE)",
            "remove": False,
        },
        {
            "type": "334",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][18:20]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "quality",
            "remove": False,
        },
        {
            "type": "335",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "timestamp",
            "remove": False,
        },
        {
            "type": "335",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][16:32]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "last_heartbeat",
            "remove": False,
        },
        {
            "type": "335",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][32:36]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "failed_sessions",
            "remove": False,
        },
        {
            "type": "335",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][36:40]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "successful_sessions",
            "remove": False,
        },
        {
            "type": "335",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][40:42]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "signal_quality",
            "remove": False,
        },
        {
            "type": "335",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][42:44]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "ring_pending",
            "remove": False,
        },
        {
            "type": "335",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][44:46]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "tx_session_pending",
            "remove": False,
        },
        {
            "type": "335",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][46:48]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "rx_session_pending",
            "remove": False,
        },
        {
            "type": "336",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][0:2]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "enable_lte",
            "remove": False,
        },
        {
            "type": "336",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][2:4]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "enable_pin",
            "remove": False,
        },
        {
            "type": "336",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 4 : i + 6]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 32, 2)
                ]
            ).rstrip("\x00"),
            "name": "pin",
            "remove": False,
        },
        {
            "type": "336",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 36 : i + 38]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 32, 2)
                ]
            ).rstrip("\x00"),
            "name": "new_pin",
            "remove": False,
        },
        {
            "type": "336",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 68 : i + 70]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 64, 2)
                ]
            ).rstrip("\x00"),
            "name": "apn",
            "remove": False,
        },
        {
            "type": "336",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 132 : i + 134]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 32, 2)
                ]
            ).rstrip("\x00"),
            "name": "puk",
            "remove": False,
        },
        {
            "type": "336",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][164:166]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "roaming",
            "remove": False,
        },
        {
            "type": "336",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][166:168]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "response(CELLULAR_CONFIG_RESPONSE)",
            "remove": False,
        },
        {
            "type": "339",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "frequency",
            "remove": False,
        },
        {
            "type": "339",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][8:10]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "index",
            "remove": False,
        },
        {
            "type": "340",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time",
            "remove": False,
        },
        {
            "type": "340",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lat",
            "remove": False,
        },
        {
            "type": "340",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "lon",
            "remove": False,
        },
        {
            "type": "340",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "alt",
            "remove": False,
        },
        {
            "type": "340",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "relative_alt",
            "remove": False,
        },
        {
            "type": "340",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "next_lat",
            "remove": False,
        },
        {
            "type": "340",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "next_lon",
            "remove": False,
        },
        {
            "type": "340",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][64:72]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "next_alt",
            "remove": False,
        },
        {
            "type": "340",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][72:76]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "vx",
            "remove": False,
        },
        {
            "type": "340",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][76:80]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "vy",
            "remove": False,
        },
        {
            "type": "340",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][80:84]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "vz",
            "remove": False,
        },
        {
            "type": "340",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][84:88]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "h_acc",
            "remove": False,
        },
        {
            "type": "340",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][88:92]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "v_acc",
            "remove": False,
        },
        {
            "type": "340",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][92:96]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "vel_acc",
            "remove": False,
        },
        {
            "type": "340",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][96:100]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "update_rate",
            "remove": False,
        },
        {
            "type": "340",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 100 : i + 102]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 36, 2)
            ],
            "name": "uas_id",
            "remove": False,
        },
        {
            "type": "340",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][136:138]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "flight_state(UTM_FLIGHT_STATE)",
            "remove": False,
        },
        {
            "type": "340",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][138:140]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "flags(UTM_DATA_AVAIL_FLAGS)",
            "remove": False,
        },
        {
            "type": "350",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "350",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 16 : i + 24]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 464, 8)
            ],
            "name": "data",
            "remove": False,
        },
        {
            "type": "350",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][480:484]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "array_id",
            "remove": False,
        },
        {
            "type": "350",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 484 : i + 486]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 20, 2)
                ]
            ).rstrip("\x00"),
            "name": "name",
            "remove": False,
        },
        {
            "type": "360",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "360",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "radius",
            "remove": False,
        },
        {
            "type": "360",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "x",
            "remove": False,
        },
        {
            "type": "360",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "y",
            "remove": False,
        },
        {
            "type": "360",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "z",
            "remove": False,
        },
        {
            "type": "360",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][48:50]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "frame(MAV_FRAME)",
            "remove": False,
        },
        {
            "type": "370",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "capacity_full_specification",
            "remove": False,
        },
        {
            "type": "370",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "capacity_full",
            "remove": False,
        },
        {
            "type": "370",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "discharge_maximum_current",
            "remove": False,
        },
        {
            "type": "370",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "discharge_maximum_burst_current",
            "remove": False,
        },
        {
            "type": "370",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][32:36]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "cycle_count",
            "remove": False,
        },
        {
            "type": "370",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][36:40]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "weight",
            "remove": False,
        },
        {
            "type": "370",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][40:44]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "discharge_minimum_voltage",
            "remove": False,
        },
        {
            "type": "370",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][44:48]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "charging_minimum_voltage",
            "remove": False,
        },
        {
            "type": "370",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][48:52]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "resting_minimum_voltage",
            "remove": False,
        },
        {
            "type": "370",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][52:56]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "charging_maximum_voltage",
            "remove": False,
        },
        {
            "type": "370",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][56:58]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "id",
            "remove": False,
        },
        {
            "type": "370",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][58:60]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "battery_function(MAV_BATTERY_FUNCTION)",
            "remove": False,
        },
        {
            "type": "370",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][60:62]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "type(MAV_BATTERY_TYPE)",
            "remove": False,
        },
        {
            "type": "370",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 62 : i + 64]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 32, 2)
                ]
            ).rstrip("\x00"),
            "name": "serial_number",
            "remove": False,
        },
        {
            "type": "370",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 94 : i + 96]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 100, 2)
                ]
            ).rstrip("\x00"),
            "name": "device_name",
            "remove": False,
        },
        {
            "type": "370",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][194:196]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "cells_in_series",
            "remove": False,
        },
        {
            "type": "370",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 196 : i + 198]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 22, 2)
                ]
            ).rstrip("\x00"),
            "name": "manufacture_date",
            "remove": False,
        },
        {
            "type": "373",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "status(MAV_GENERATOR_STATUS_FLAG)",
            "remove": False,
        },
        {
            "type": "373",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "battery_current",
            "remove": False,
        },
        {
            "type": "373",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "load_current",
            "remove": False,
        },
        {
            "type": "373",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "power_generated",
            "remove": False,
        },
        {
            "type": "373",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "bus_voltage",
            "remove": False,
        },
        {
            "type": "373",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "bat_current_setpoint",
            "remove": False,
        },
        {
            "type": "373",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "runtime",
            "remove": False,
        },
        {
            "type": "373",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][64:72]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "time_until_maintenance",
            "remove": False,
        },
        {
            "type": "373",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][72:76]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "generator_speed",
            "remove": False,
        },
        {
            "type": "373",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][76:80]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "rectifier_temperature",
            "remove": False,
        },
        {
            "type": "373",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][80:84]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "generator_temperature",
            "remove": False,
        },
        {
            "type": "375",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "375",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "active",
            "remove": False,
        },
        {
            "type": "375",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<f",
                    bytes.fromhex(x[0][i + 24 : i + 32]).ljust(
                        struct.calcsize("<f"), b"\x00"
                    ),
                )[0]
                for i in range(0, 256, 8)
            ],
            "name": "actuator",
            "remove": False,
        },
        {
            "type": "380",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "safe_return",
            "remove": False,
        },
        {
            "type": "380",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "land",
            "remove": False,
        },
        {
            "type": "380",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "mission_next_item",
            "remove": False,
        },
        {
            "type": "380",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "mission_end",
            "remove": False,
        },
        {
            "type": "380",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "commanded_action",
            "remove": False,
        },
        {
            "type": "385",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][0:4]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "payload_type(MAV_TUNNEL_PAYLOAD_TYPE)",
            "remove": False,
        },
        {
            "type": "385",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][4:6]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "385",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][6:8]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "385",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][8:10]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "payload_length",
            "remove": False,
        },
        {
            "type": "385",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 10 : i + 12]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 256, 2)
            ],
            "name": "payload",
            "remove": False,
        },
        {
            "type": "386",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "id",
            "remove": False,
        },
        {
            "type": "386",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][8:10]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "386",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][10:12]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "386",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][12:14]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "bus",
            "remove": False,
        },
        {
            "type": "386",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][14:16]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "len",
            "remove": False,
        },
        {
            "type": "386",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 16 : i + 18]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 16, 2)
            ],
            "name": "data",
            "remove": False,
        },
        {
            "type": "390",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "390",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "uptime",
            "remove": False,
        },
        {
            "type": "390",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "ram_usage",
            "remove": False,
        },
        {
            "type": "390",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "ram_total",
            "remove": False,
        },
        {
            "type": "390",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<I",
                    bytes.fromhex(x[0][i + 40 : i + 48]).ljust(
                        struct.calcsize("<I"), b"\x00"
                    ),
                )[0]
                for i in range(0, 32, 8)
            ],
            "name": "storage_type",
            "remove": False,
        },
        {
            "type": "390",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<I",
                    bytes.fromhex(x[0][i + 72 : i + 80]).ljust(
                        struct.calcsize("<I"), b"\x00"
                    ),
                )[0]
                for i in range(0, 32, 8)
            ],
            "name": "storage_usage",
            "remove": False,
        },
        {
            "type": "390",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<I",
                    bytes.fromhex(x[0][i + 104 : i + 112]).ljust(
                        struct.calcsize("<I"), b"\x00"
                    ),
                )[0]
                for i in range(0, 32, 8)
            ],
            "name": "storage_total",
            "remove": False,
        },
        {
            "type": "390",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<I",
                    bytes.fromhex(x[0][i + 136 : i + 144]).ljust(
                        struct.calcsize("<I"), b"\x00"
                    ),
                )[0]
                for i in range(0, 48, 8)
            ],
            "name": "link_type",
            "remove": False,
        },
        {
            "type": "390",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<I",
                    bytes.fromhex(x[0][i + 184 : i + 192]).ljust(
                        struct.calcsize("<I"), b"\x00"
                    ),
                )[0]
                for i in range(0, 48, 8)
            ],
            "name": "link_tx_rate",
            "remove": False,
        },
        {
            "type": "390",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<I",
                    bytes.fromhex(x[0][i + 232 : i + 240]).ljust(
                        struct.calcsize("<I"), b"\x00"
                    ),
                )[0]
                for i in range(0, 48, 8)
            ],
            "name": "link_rx_rate",
            "remove": False,
        },
        {
            "type": "390",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<I",
                    bytes.fromhex(x[0][i + 280 : i + 288]).ljust(
                        struct.calcsize("<I"), b"\x00"
                    ),
                )[0]
                for i in range(0, 48, 8)
            ],
            "name": "link_tx_max",
            "remove": False,
        },
        {
            "type": "390",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<I",
                    bytes.fromhex(x[0][i + 328 : i + 336]).ljust(
                        struct.calcsize("<I"), b"\x00"
                    ),
                )[0]
                for i in range(0, 48, 8)
            ],
            "name": "link_rx_max",
            "remove": False,
        },
        {
            "type": "390",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<h",
                    bytes.fromhex(x[0][i + 376 : i + 380]).ljust(
                        struct.calcsize("<h"), b"\x00"
                    ),
                )[0]
                for i in range(0, 16, 4)
            ],
            "name": "fan_speed",
            "remove": False,
        },
        {
            "type": "390",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][392:394]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "type",
            "remove": False,
        },
        {
            "type": "390",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 394 : i + 396]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 16, 2)
            ],
            "name": "cpu_cores",
            "remove": False,
        },
        {
            "type": "390",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 410 : i + 412]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 20, 2)
            ],
            "name": "cpu_combined",
            "remove": False,
        },
        {
            "type": "390",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 430 : i + 432]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 8, 2)
            ],
            "name": "gpu_cores",
            "remove": False,
        },
        {
            "type": "390",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 438 : i + 440]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 20, 2)
            ],
            "name": "gpu_combined",
            "remove": False,
        },
        {
            "type": "390",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<b", bytes.fromhex(x[0][458:460]).ljust(struct.calcsize("<b"), b"\x00")
            )[0],
            "name": "temperature_board",
            "remove": False,
        },
        {
            "type": "390",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<b",
                    bytes.fromhex(x[0][i + 460 : i + 462]).ljust(
                        struct.calcsize("<b"), b"\x00"
                    ),
                )[0]
                for i in range(0, 16, 2)
            ],
            "name": "temperature_core",
            "remove": False,
        },
        {
            "type": "395",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "395",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "general_metadata_file_crc",
            "remove": False,
        },
        {
            "type": "395",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "peripherals_metadata_file_crc",
            "remove": False,
        },
        {
            "type": "395",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 24 : i + 26]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 200, 2)
                ]
            ).rstrip("\x00"),
            "name": "general_metadata_uri",
            "remove": False,
        },
        {
            "type": "395",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 224 : i + 226]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 200, 2)
                ]
            ).rstrip("\x00"),
            "name": "peripherals_metadata_uri",
            "remove": False,
        },
        {
            "type": "397",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "time_boot_ms",
            "remove": False,
        },
        {
            "type": "397",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "file_crc",
            "remove": False,
        },
        {
            "type": "397",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 16 : i + 18]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 200, 2)
                ]
            ).rstrip("\x00"),
            "name": "uri",
            "remove": False,
        },
        {
            "type": "400",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "format(TUNE_FORMAT)",
            "remove": False,
        },
        {
            "type": "400",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][8:10]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "400",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][10:12]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "400",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 12 : i + 14]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 496, 2)
                ]
            ).rstrip("\x00"),
            "name": "tune",
            "remove": False,
        },
        {
            "type": "401",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "format(TUNE_FORMAT)",
            "remove": False,
        },
        {
            "type": "401",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][8:10]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "401",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][10:12]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "410",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "id",
            "remove": False,
        },
        {
            "type": "410",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "event_time_boot_ms",
            "remove": False,
        },
        {
            "type": "410",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][16:20]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "sequence",
            "remove": False,
        },
        {
            "type": "410",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][20:22]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "destination_component",
            "remove": False,
        },
        {
            "type": "410",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][22:24]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "destination_system",
            "remove": False,
        },
        {
            "type": "410",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][24:26]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "log_levels",
            "remove": False,
        },
        {
            "type": "410",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 26 : i + 28]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 80, 2)
            ],
            "name": "arguments",
            "remove": False,
        },
        {
            "type": "411",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][0:4]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "sequence",
            "remove": False,
        },
        {
            "type": "411",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][4:6]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "flags(MAV_EVENT_CURRENT_SEQUENCE_FLAGS)",
            "remove": False,
        },
        {
            "type": "412",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][0:4]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "first_sequence",
            "remove": False,
        },
        {
            "type": "412",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][4:8]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "last_sequence",
            "remove": False,
        },
        {
            "type": "412",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][8:10]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "412",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][10:12]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "413",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][0:4]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "sequence",
            "remove": False,
        },
        {
            "type": "413",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][4:8]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "sequence_oldest_available",
            "remove": False,
        },
        {
            "type": "413",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][8:10]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "413",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][10:12]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "413",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][12:14]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "reason(MAV_EVENT_ERROR_REASON)",
            "remove": False,
        },
        {
            "type": "387",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "id",
            "remove": False,
        },
        {
            "type": "387",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][8:10]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "387",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][10:12]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "387",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][12:14]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "bus",
            "remove": False,
        },
        {
            "type": "387",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][14:16]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "len",
            "remove": False,
        },
        {
            "type": "387",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 16 : i + 18]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 128, 2)
            ],
            "name": "data",
            "remove": False,
        },
        {
            "type": "388",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<H",
                    bytes.fromhex(x[0][i + 0 : i + 4]).ljust(
                        struct.calcsize("<H"), b"\x00"
                    ),
                )[0]
                for i in range(0, 64, 4)
            ],
            "name": "ids",
            "remove": False,
        },
        {
            "type": "388",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][64:66]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "388",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][66:68]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "388",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][68:70]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "bus",
            "remove": False,
        },
        {
            "type": "388",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][70:72]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "operation(CAN_FILTER_OP)",
            "remove": False,
        },
        {
            "type": "388",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][72:74]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "num_ids",
            "remove": False,
        },
        {
            "type": "9000",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "9000",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<d",
                    bytes.fromhex(x[0][i + 16 : i + 32]).ljust(
                        struct.calcsize("<d"), b"\x00"
                    ),
                )[0]
                for i in range(0, 256, 16)
            ],
            "name": "distance",
            "remove": False,
        },
        {
            "type": "9000",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][272:274]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "count",
            "remove": False,
        },
        {
            "type": "9005",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<Q", bytes.fromhex(x[0][0:16]).ljust(struct.calcsize("<Q"), b"\x00")
            )[0],
            "name": "time_usec",
            "remove": False,
        },
        {
            "type": "9005",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "line_length",
            "remove": False,
        },
        {
            "type": "9005",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "speed",
            "remove": False,
        },
        {
            "type": "9005",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "tension",
            "remove": False,
        },
        {
            "type": "9005",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "voltage",
            "remove": False,
        },
        {
            "type": "9005",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][48:56]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "current",
            "remove": False,
        },
        {
            "type": "9005",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][56:64]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "status(MAV_WINCH_STATUS_FLAG)",
            "remove": False,
        },
        {
            "type": "9005",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][64:68]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "temperature",
            "remove": False,
        },
        {
            "type": "12900",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][0:2]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "12900",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][2:4]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "12900",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 4 : i + 6]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 40, 2)
            ],
            "name": "id_or_mac",
            "remove": False,
        },
        {
            "type": "12900",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][44:46]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "id_type(MAV_ODID_ID_TYPE)",
            "remove": False,
        },
        {
            "type": "12900",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][46:48]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "ua_type(MAV_ODID_UA_TYPE)",
            "remove": False,
        },
        {
            "type": "12900",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 48 : i + 50]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 40, 2)
            ],
            "name": "uas_id",
            "remove": False,
        },
        {
            "type": "12901",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "latitude",
            "remove": False,
        },
        {
            "type": "12901",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "longitude",
            "remove": False,
        },
        {
            "type": "12901",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "altitude_barometric",
            "remove": False,
        },
        {
            "type": "12901",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "altitude_geodetic",
            "remove": False,
        },
        {
            "type": "12901",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "height",
            "remove": False,
        },
        {
            "type": "12901",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "timestamp",
            "remove": False,
        },
        {
            "type": "12901",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][48:52]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "direction",
            "remove": False,
        },
        {
            "type": "12901",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][52:56]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "speed_horizontal",
            "remove": False,
        },
        {
            "type": "12901",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][56:60]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "speed_vertical",
            "remove": False,
        },
        {
            "type": "12901",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][60:62]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "12901",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][62:64]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "12901",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 64 : i + 66]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 40, 2)
            ],
            "name": "id_or_mac",
            "remove": False,
        },
        {
            "type": "12901",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][104:106]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "status(MAV_ODID_STATUS)",
            "remove": False,
        },
        {
            "type": "12901",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][106:108]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "height_reference(MAV_ODID_HEIGHT_REF)",
            "remove": False,
        },
        {
            "type": "12901",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][108:110]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "horizontal_accuracy(MAV_ODID_HOR_ACC)",
            "remove": False,
        },
        {
            "type": "12901",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][110:112]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "vertical_accuracy(MAV_ODID_VER_ACC)",
            "remove": False,
        },
        {
            "type": "12901",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][112:114]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "barometer_accuracy(MAV_ODID_VER_ACC)",
            "remove": False,
        },
        {
            "type": "12901",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][114:116]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "speed_accuracy(MAV_ODID_SPEED_ACC)",
            "remove": False,
        },
        {
            "type": "12901",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][116:118]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "timestamp_accuracy(MAV_ODID_TIME_ACC)",
            "remove": False,
        },
        {
            "type": "12902",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "timestamp",
            "remove": False,
        },
        {
            "type": "12902",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][8:10]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "12902",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][10:12]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "12902",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 12 : i + 14]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 40, 2)
            ],
            "name": "id_or_mac",
            "remove": False,
        },
        {
            "type": "12902",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][52:54]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "authentication_type(MAV_ODID_AUTH_TYPE)",
            "remove": False,
        },
        {
            "type": "12902",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][54:56]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "data_page",
            "remove": False,
        },
        {
            "type": "12902",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][56:58]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "last_page_index",
            "remove": False,
        },
        {
            "type": "12902",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][58:60]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "length",
            "remove": False,
        },
        {
            "type": "12902",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 60 : i + 62]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 46, 2)
            ],
            "name": "authentication_data",
            "remove": False,
        },
        {
            "type": "12903",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][0:2]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "12903",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][2:4]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "12903",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 4 : i + 6]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 40, 2)
            ],
            "name": "id_or_mac",
            "remove": False,
        },
        {
            "type": "12903",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][44:46]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "description_type(MAV_ODID_DESC_TYPE)",
            "remove": False,
        },
        {
            "type": "12903",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 46 : i + 48]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 46, 2)
                ]
            ).rstrip("\x00"),
            "name": "description",
            "remove": False,
        },
        {
            "type": "12904",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "operator_latitude",
            "remove": False,
        },
        {
            "type": "12904",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "operator_longitude",
            "remove": False,
        },
        {
            "type": "12904",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "area_ceiling",
            "remove": False,
        },
        {
            "type": "12904",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "area_floor",
            "remove": False,
        },
        {
            "type": "12904",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][32:40]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "operator_altitude_geo",
            "remove": False,
        },
        {
            "type": "12904",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][40:48]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "timestamp",
            "remove": False,
        },
        {
            "type": "12904",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][48:52]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "area_count",
            "remove": False,
        },
        {
            "type": "12904",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][52:56]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "area_radius",
            "remove": False,
        },
        {
            "type": "12904",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][56:58]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "12904",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][58:60]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "12904",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 60 : i + 62]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 40, 2)
            ],
            "name": "id_or_mac",
            "remove": False,
        },
        {
            "type": "12904",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][100:102]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "operator_location_type(MAV_ODID_OPERATOR_LOCATION_TYPE)",
            "remove": False,
        },
        {
            "type": "12904",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][102:104]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "classification_type(MAV_ODID_CLASSIFICATION_TYPE)",
            "remove": False,
        },
        {
            "type": "12904",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][104:106]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "category_eu(MAV_ODID_CATEGORY_EU)",
            "remove": False,
        },
        {
            "type": "12904",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][106:108]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "class_eu(MAV_ODID_CLASS_EU)",
            "remove": False,
        },
        {
            "type": "12905",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][0:2]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "12905",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][2:4]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "12905",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 4 : i + 6]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 40, 2)
            ],
            "name": "id_or_mac",
            "remove": False,
        },
        {
            "type": "12905",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][44:46]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "operator_id_type(MAV_ODID_OPERATOR_ID_TYPE)",
            "remove": False,
        },
        {
            "type": "12905",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 46 : i + 48]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 40, 2)
                ]
            ).rstrip("\x00"),
            "name": "operator_id",
            "remove": False,
        },
        {
            "type": "12915",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][0:2]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "12915",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][2:4]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "12915",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 4 : i + 6]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 40, 2)
            ],
            "name": "id_or_mac",
            "remove": False,
        },
        {
            "type": "12915",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][44:46]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "single_message_size",
            "remove": False,
        },
        {
            "type": "12915",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][46:48]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "msg_pack_size",
            "remove": False,
        },
        {
            "type": "12915",
            "var": ["_raw"],
            "method": lambda x: [
                struct.unpack(
                    "<B",
                    bytes.fromhex(x[0][i + 48 : i + 50]).ljust(
                        struct.calcsize("<B"), b"\x00"
                    ),
                )[0]
                for i in range(0, 450, 2)
            ],
            "name": "messages",
            "remove": False,
        },
        {
            "type": "12918",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][0:2]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "status(MAV_ODID_ARM_STATUS)",
            "remove": False,
        },
        {
            "type": "12918",
            "var": ["_raw"],
            "method": lambda x: "".join(
                [
                    struct.unpack(
                        "<c",
                        bytes.fromhex(x[0][i + 2 : i + 4]).ljust(
                            struct.calcsize("<c"), b"\x00"
                        ),
                    )[0].decode()
                    for i in range(0, 100, 2)
                ]
            ).rstrip("\x00"),
            "name": "error",
            "remove": False,
        },
        {
            "type": "12919",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][0:8]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "operator_latitude",
            "remove": False,
        },
        {
            "type": "12919",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<i", bytes.fromhex(x[0][8:16]).ljust(struct.calcsize("<i"), b"\x00")
            )[0],
            "name": "operator_longitude",
            "remove": False,
        },
        {
            "type": "12919",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<f", bytes.fromhex(x[0][16:24]).ljust(struct.calcsize("<f"), b"\x00")
            )[0],
            "name": "operator_altitude_geo",
            "remove": False,
        },
        {
            "type": "12919",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<I", bytes.fromhex(x[0][24:32]).ljust(struct.calcsize("<I"), b"\x00")
            )[0],
            "name": "timestamp",
            "remove": False,
        },
        {
            "type": "12919",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][32:34]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_system",
            "remove": False,
        },
        {
            "type": "12919",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][34:36]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "target_component",
            "remove": False,
        },
        {
            "type": "12920",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<h", bytes.fromhex(x[0][0:4]).ljust(struct.calcsize("<h"), b"\x00")
            )[0],
            "name": "temperature",
            "remove": False,
        },
        {
            "type": "12920",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<H", bytes.fromhex(x[0][4:8]).ljust(struct.calcsize("<H"), b"\x00")
            )[0],
            "name": "humidity",
            "remove": False,
        },
        {
            "type": "12920",
            "var": ["_raw"],
            "method": lambda x: struct.unpack(
                "<B", bytes.fromhex(x[0][8:10]).ljust(struct.calcsize("<B"), b"\x00")
            )[0],
            "name": "id",
            "remove": False,
        },
    ],
}
