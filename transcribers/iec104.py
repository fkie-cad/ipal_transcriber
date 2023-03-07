import struct

import transcriber.settings as settings
from transcriber.messages import Activity, IpalMessage
from transcribers.transcriber import Transcriber


class IEC104Transcriber(Transcriber):
    _name = "iec104"

    type_to_value_name = {
        1: "siq_spi",
        2: "siq_spi",
        3: "diq_dpi",
        4: "diq_dpi",
        5: "vti_v",
        6: "vti_v",
        7: "bitstring",
        8: "bitstring",
        9: "normval",
        10: "normval",
        11: "scalval",
        12: "scalval",
        13: "float",
        14: "float",
        # Not implemented yet
        21: "normval",
        # 22 - 29 reserved
        30: "siq_spi",
        31: "diq_dpi",
        32: "vti",
        33: "bitstring",
        34: "normval",
        35: "scalval",
        36: "float",
        # Not implemented yet
        # 41 - 44 reserved
        45: "sco",
        46: "dco",
        47: "rco",
        48: "normval",
        49: "scalval",
        50: "float",
        51: "bitstring",
        # 52 - 57 reserved
        58: "sco",
        59: "dco",
        60: "rco",
        61: "normval",
        62: "scalval",
        63: "float",
        64: "bitstring",
        # 65 - 69 reserved
        70: "coi",
        # 71 - 99 reserved
        100: "qoi",
        102: None,
        103: "cp56time",
    }

    def matches_protocol(self, pkt):
        return "IEC60870_104" in pkt

    def parse_packet(self, pkt):
        msgs = []

        src = "{}:{}".format(pkt["IP"].src, pkt["TCP"].srcport)
        dest = "{}:{}".format(pkt["IP"].dst, pkt["TCP"].dstport)
        timestamp = float(pkt.sniff_time.timestamp())
        iec104_layers = pkt.get_multiple_layers("IEC60870_104")

        for i in range(len(iec104_layers)):
            iec104 = iec104_layers[i]
            # type = int(iec104.type, 16)

            # Temporary fix to determine the packet type until MR is accepted
            # https://gitlab.com/wireshark/wireshark/-/merge_requests/6414

            # if type == 0x03:  # Type: U(0x11)
            if "iec60870_104.utype" in iec104._all_fields:
                msgs += self.parse_U_format(src, dest, timestamp, pkt, i)

            # elif type == 0x00:  # Type: I(0x00)
            elif (
                "iec60870_104.tx" in iec104._all_fields
                and "iec60870_104.rx" in iec104._all_fields
            ):
                msgs += self.parse_I_format(src, dest, timestamp, pkt, i)

            # elif type == 0x01:  # Type: S(0x01)
            elif (
                "iec60870_104.tx" not in iec104._all_fields
                and "iec60870_104.rx" in iec104._all_fields
            ):
                msgs += self.parse_S_format(src, dest, timestamp, pkt, i)

            else:
                settings.logger.warning(iec104._all_fields)
                settings.logger.warning("Unknown IEC-104 type")

        return msgs

    def parse_U_format(self, src, dest, timestamp, pkt, pkt_index):
        iec104 = pkt.get_multiple_layers("IEC60870_104")[pkt_index]
        utype = int(iec104.utype, 16)

        if utype == 0x01 or utype == 0x04 or utype == 0x10:
            activity = Activity.COMMAND
            flow = (src, dest)
        else:
            activity = Activity.ACTION
            flow = (dest, src)

        m = IpalMessage(
            id=self._id_counter.get_next_id(),
            src=src,
            dest=dest,
            timestamp=timestamp,
            protocol=self._name,
            activity=activity,
            flow=flow,
            length=int(iec104.apdulen) + 2,
            type="U",
        )

        if activity == Activity.COMMAND:
            m._add_to_request_queue = True
        else:
            m._match_to_requests = True

        if utype == 0x01 or utype == 0x02:
            m.data = {"start data transfer": True}
        elif utype == 0x04 or utype == 0x08:
            m.data = {"start data transfer": False}
        elif utype == 0x10 or utype == 0x20:
            m.data = {"test": 1}
        else:
            settings.logger.warning("[IEC-104] Unknown U format bit combination.")

        return [m]

    def parse_S_format(self, src, dest, timestamp, pkt, pkt_index):
        iec104 = pkt.get_multiple_layers("IEC60870_104")[pkt_index]

        m = IpalMessage(
            id=self._id_counter.get_next_id(),
            src=src,
            dest=dest,
            timestamp=timestamp,
            protocol=self._name,
            activity=Activity.CONFIRMATION,
            flow=(src, dest),
            length=int(iec104.apdulen) + 2,
            type="S",
        )

        return [m]

    def _cot_to_activity(self, cot, src, dest):
        add_to_request_queue = False
        match_to_requests = False

        if cot == 1:  # periodic,cyclic
            activity = Activity.INFORM
            flow = (dest, src)

        elif cot == 3:  # spontaneous
            activity = Activity.INFORM
            flow = (dest, src)

        elif cot == 4:  # initialized
            activity = Activity.ACTION
            flow = (dest, src)
            match_to_requests = True

        elif cot == 5:  # interrogation or interrogated
            activity = Activity.INTERROGATE
            flow = (src, dest)
            add_to_request_queue = True

        elif cot == 6:  # activation
            activity = Activity.COMMAND
            flow = (src, dest)
            add_to_request_queue = True

        elif cot == 7:  # confirmation activation
            activity = Activity.ACTION
            flow = (dest, src)
            match_to_requests = True

        elif cot == 10:  # termination activation
            activity = Activity.ACTION
            flow = (dest, src)
            match_to_requests = True

        elif 20 <= cot and cot <= 41:  # interrogated by ...
            activity = Activity.INFORM
            flow = (dest, src)
            match_to_requests = True

        else:
            settings.logger.warning("[IEC-104] CoT {} not implemented".format(cot))

        return activity, flow, add_to_request_queue, match_to_requests

    def _interpret_data(self, type, field):
        # https://infosys.beckhoff.com/english.php?content=../content/1033/tcplclibiec870_5_104/html/tcplclibiec870_5_104_objref_overview.htm&id

        if type in [1, 30, 45, 58]:  # single point (with time)
            return field.binary_value[0] & 0x01
        elif type in [3, 31, 46, 59]:  # double point (with time)
            return field.binary_value[0] & 0x03
        elif type in [5, 32]:  # step position (with time)
            return field.binary_value[0]
        elif type in [7, 33, 51, 64]:  # 32-bit bitstring (with time)
            return int.from_bytes(field.binary_value[:4], "big")
        elif type in [9, 34, 48, 61]:  # measured value, normalized (with time)
            return struct.unpack("<h", field.binary_value[:2])[0]
        elif type in [11, 35, 49, 62]:  # measured value, scaled (with time)
            return struct.unpack("<h", field.binary_value[:2])[0]
        elif type in [13, 36, 50, 63]:  # short float (with time)
            return struct.unpack("<f", field.binary_value[:4])[0]

        elif type in [47, 60]:  # regulating step (with time)
            return field.binary_value[0]

        else:
            settings.logger.warning(
                "Can not interpret data of type {}. Returning default format: {}".format(
                    type, field.showname_value
                )
            )
            return field.showname_value

    def parse_I_format(self, src, dest, timestamp, pkt, pkt_index):  # noqa: C901
        iec104 = pkt.get_multiple_layers("IEC60870_104")[pkt_index]
        asdu = pkt.get_multiple_layers("IEC60870_ASDU")[pkt_index]
        data = {}

        # Derive activity and flow from 'cause of transmission'
        cot = int(asdu.causetx)
        (
            activity,
            flow,
            _add_to_request_queue,
            _match_to_requests,
        ) = self._cot_to_activity(cot, src, dest)

        # Parse type
        type = int(asdu.typeid)
        value_name = self.type_to_value_name[type]

        # 0: not used
        # 1 - 21: Process information in monitor direction
        if 1 <= type and type <= 21:
            flow = (dest, src)
            _match_to_requests = True
            _add_to_request_queue = False
            activity = Activity.INFORM

            for i in range(len(getattr(asdu, value_name).fields)):
                field = getattr(asdu, value_name).fields[i]
                ioa = str(asdu.ioa.all_fields[i].showname_value)
                addr = "{}.{}".format(asdu.addr, ioa)
                data[addr] = self._interpret_data(type, field)

        # 22 - 29: Not defined

        # 30 - 40: Process telegrams with long time tag
        elif 30 <= type and type <= 40:
            for i in range(len(getattr(asdu, value_name).fields)):
                field = getattr(asdu, value_name).fields[i]
                ioa = str(asdu.ioa.all_fields[i].showname_value)
                addr = "{}.{}".format(asdu.addr, ioa)
                data[addr] = self._interpret_data(type, field)

        # 41 - 44: Not defined

        # 45 - 51: Process information in control direction
        elif 45 <= type and type <= 51:
            for i in range(len(getattr(asdu, value_name).fields)):
                field = getattr(asdu, value_name).fields[i]
                ioa = str(asdu.ioa.all_fields[i].showname_value)
                addr = "{}.{}".format(asdu.addr, ioa)
                data[addr] = self._interpret_data(type, field)

        # 52 - 57: Not defined

        # 58 - 64: Command telegrams with long time tag
        elif 58 <= type and type <= 64:
            for i in range(len(getattr(asdu, value_name).fields)):
                field = getattr(asdu, value_name).fields[i]
                ioa = str(asdu.ioa.all_fields[i].showname_value)
                addr = "{}.{}".format(asdu.addr, ioa)
                data[addr] = self._interpret_data(type, field)

        # 65 - 69: Not defined

        # 70: System information in monitoring direction
        elif type == 70:  # End of initialization
            pass  # No process data

        # 71 - 99:  Not defined

        # 100 - 107: System information in control direction
        elif type == 100:  # (General-) Interrogation command
            pass  # No process data

        elif type == 102:  # Read command
            for i in range(len(asdu.ioa.all_fields)):
                ioa = str(asdu.ioa.all_fields[i].showname_value)
                addr = "{}.{}".format(asdu.addr, ioa)
                data[addr] = None

        elif type == 103:  # Clock synchronization command
            pass  # No process data

        # 108 - 109: Not defined

        # 110 - 113: Parameter in control direction

        # 114 - 119: Not defined

        # 120 - 127: File transfer
        #
        # 128 - 135: Routing messages
        # 136 - 255: Special use

        else:
            settings.logger.warning("[IEC-104] TypeId {} not implemented".format(type))

        # Create IPAL message
        m = IpalMessage(
            id=self._id_counter.get_next_id(),
            src=src,
            dest=dest,
            timestamp=timestamp,
            protocol=self._name,
            activity=activity,
            flow=flow,
            length=int(iec104.apdulen) + 2,
            type="I-" + str(type),
        )

        m.data = data
        m._add_to_request_queue = _add_to_request_queue
        m._match_to_requests = _match_to_requests

        return [m]

    def match_response(self, requests, response):
        if response.type == "U":
            for request in requests:
                if request.data.keys() != response.data.keys():
                    continue

                response.responds_to.append(request.id)
                return [request]

        else:
            for request in requests[::-1]:
                not_written_variables = request.data.copy()
                not_requested_variables = []
                for var in response.data:
                    if var in not_written_variables:
                        del not_written_variables[var]
                    else:
                        not_requested_variables.append(var)

                if (
                    None in not_written_variables
                    and not_written_variables[None] is None
                ):
                    response.responds_to.append(request.id)
                    return []

                if len(not_requested_variables) != 0:
                    continue

                if len(not_written_variables) != 0:
                    continue

                response.responds_to.append(request.id)
                return [request]

        return []
