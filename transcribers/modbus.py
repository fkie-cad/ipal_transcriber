import transcriber.settings as settings
from transcriber.messages import Activity, IpalMessage
from transcribers.transcriber import Transcriber


class ModbusTranscriber(Transcriber):
    _name = "modbus"

    _func_to_addr_space = {
        1: "coil",
        2: "discrete.input",
        3: "holding.register",
        4: "input.register",
        5: "coil",
        6: "holding.register",
        15: "coil",
        16: "holding.register"
        # only possible to request multiple holding registers at once, which is handled in another function
    }

    @classmethod
    def state_identifier(cls, msg, key):
        if msg.activity in [Activity.INTERROGATE, Activity.COMMAND]:
            return "{}:{}".format(msg.dest, key)
        elif msg.activity in [Activity.INFORM, Activity.ACTION]:
            return "{}:{}".format(msg.src, key)
        else:
            settings.logger.critical("Unknown activity {}".format(msg.activity))
            return "{}:{}".format(msg.src, key)

    def matches_protocol(self, pkt):
        return "MBTCP" in pkt

    def parse_packet(self, pkt):
        # INFO Bug of Modbus/Scapy: Multiple messages in one TCP packet
        res = []

        adu_layers = pkt.get_multiple_layers("MBTCP")

        mb_layers = pkt.get_multiple_layers("MODBUS")

        src = "{}:{}".format(pkt["IP"].src, pkt["TCP"].srcport)
        dest = "{}:{}".format(pkt["IP"].dst, pkt["TCP"].dstport)

        for i in range(len(adu_layers)):
            adu = adu_layers[i]
            mb = mb_layers[i]

            length = 6 + int(adu.len)

            if int(pkt["TCP"].srcport) == settings.MBTCP_PORT:  # Response
                code = int(mb.func_code)

                flow = (src, dest, int(adu.trans_id), code)

                m = IpalMessage(
                    id=self._id_counter.get_next_id(),
                    src=src + ":{}".format(adu.unit_id),
                    dest=dest,
                    timestamp=float(pkt.sniff_time.timestamp()),
                    protocol=self._name,
                    flow=flow,
                    length=length,
                    type=code,
                )

                if "exception_code" in mb.field_names:
                    self.transcribe_error_response(m, mb)
                elif code in [1, 2, 3, 4]:
                    self.transcribe_read_response(m, mb)
                elif code in [5, 6, 15, 16]:
                    self.transcribe_write_response(m, mb)
                else:
                    m.activity = Activity.INFORM  # NOTE maybe not an accurate activity
                    settings.logger.warning(
                        "Not implemented response function code {}".format(mb.func_code)
                    )  # msg.pdfdump()
                res.append(m)

            elif int(pkt["TCP"].dstport) == settings.MBTCP_PORT:  # Request
                code = int(mb.func_code)

                flow = (dest, src, int(adu.trans_id), code)

                m = IpalMessage(
                    id=self._id_counter.get_next_id(),
                    src=src,
                    dest=dest + ":{}".format(adu.unit_Id),
                    timestamp=float(pkt.sniff_time.timestamp()),
                    protocol=self._name,
                    flow=flow,
                    length=length,
                    type=code,
                )

                if code in [1, 2, 3, 4]:
                    self.transcribe_read_request(m, mb)
                elif code in [5, 6, 15, 16]:
                    self.transcribe_write_request(m, mb)
                elif code == 8:
                    self.transcribe_diagnostic(m, mb)
                elif code == 43:
                    self.transcribe_encapsulated_interface_transport_request(m, mb)
                else:
                    m.activity = (
                        Activity.INTERROGATE
                    )  # NOTE maybe not an appropriate activity
                    settings.logger.warning(
                        "Not implemented request function code {}".format(mb.func_code)
                    )
                res.append(m)

            else:
                settings.logger.critical(
                    "Unknown ports for Modbus ({}, {})".format(
                        pkt["TCP"].srcport, pkt["TCP"].dstport
                    )
                )

        return res

    def transcribe_write_request(self, m, mb):
        m.activity = Activity.COMMAND
        m._add_to_request_queue = True

        data = {}

        code = int(mb.func_code)

        if code == 5:
            startAddr = int(mb.reference_num) + 1
            value = 0 if mb.data.all_fields[0].showname_value == "0000" else 1
            data[self._func_to_addr_space[code] + "." + str(startAddr)] = value

        elif code == 6:
            startAddr = int(mb.reference_num) + 1
            value = int(mb.data.all_fields[0].showname_value, 16)
            data[self._func_to_addr_space[code] + "." + str(startAddr)] = value

        elif code == 15:
            startAddr = int(mb.reference_num) + 1
            quantity = int(mb.bit_cnt)
            for i in range(quantity):
                b = int(mb.data.all_fields[i // 8].showname_value)
                bit = (b & (1 << (i % 8))) >> (i % 8)
                if bit == 1 or bit == 0:
                    value = bit
                else:
                    settings.logger.error(
                        "Something went wrong during parsing of coil write request"
                    )

                data[self._func_to_addr_space[code] + "." + str(startAddr + i)] = value

        elif code == 16:
            quantity = int(mb.word_cnt)

            for i in range(quantity):
                data[
                    self._func_to_addr_space[code]
                    + "."
                    + str(mb.regnum16.all_fields[i].showname_value)
                ] = int(mb.regval_uint16.all_fields[i].showname_value)

        else:
            settings.logger.warning(
                "Not implemented request code {} in transcribe_write_request".format(
                    mb.func_code
                )
            )
        m.data = data

    def transcribe_write_response(self, m, mb):
        m._match_to_requests = True
        m.activity = Activity.ACTION

        data = {}
        startAddr = int(mb.reference_num) + 1
        code = int(mb.func_code)

        if code == 5:
            data[self._func_to_addr_space[code] + "." + str(startAddr)] = None

        elif code == 6:
            data[self._func_to_addr_space[code] + "." + str(startAddr)] = None

        elif code == 15:
            quantity = int(mb.bit_cnt)
            for i in range(quantity):
                data[self._func_to_addr_space[code] + "." + str(startAddr + i)] = None

        elif code == 16:
            quantity = int(mb.word_cnt)

            for i in range(quantity):
                data[
                    self._func_to_addr_space[code]
                    + "."
                    + str(int(mb.reference_num) + i)
                ] = None

        else:
            settings.logger.warning(
                "Not implemented response code {} in transcribe_write_response".format(
                    mb.func_code
                )
            )  # mb.pdfdump()

        m.data = data

    def transcribe_read_request(self, m, mb):
        m.activity = Activity.INTERROGATE
        m._add_to_request_queue = True

        code = int(mb.func_code)

        startAddr = int(mb.reference_num)

        data = {}

        if code == 1 or code == 2:
            quantity = int(mb.bit_cnt)
            for i in range(quantity):
                data[self._func_to_addr_space[code] + "." + str(startAddr + i)] = None

        elif code == 3 or code == 4:
            quantity = int(mb.word_cnt)
            for i in range(quantity):
                data[self._func_to_addr_space[code] + "." + str(startAddr + i)] = None

        else:
            settings.logger.warning(
                "Not implemented request code {} in transcribe_read_request".format(
                    code
                )
            )
        m.data = data

    def transcribe_read_response(self, m, mb):
        m.activity = Activity.INFORM
        m._match_to_requests = True

        code = int(mb.func_code)

        m.data = {}

        if code == 4 or code == 3:
            for i in range(int(mb.byte_cnt) // 2):
                m.data[
                    self._func_to_addr_space[code]
                    + "."
                    + mb.regnum16.all_fields[i].showname_value
                ] = int(mb.regval_uint16.all_fields[i].showname_value)

        elif code == 2:
            for i in range(len(mb.bitnum.all_fields)):
                if mb.bitval.all_fields[i].showname_value == "True":
                    val = 1
                elif mb.bitval.all_fields[i].showname_value == "False":
                    val = 0
                else:
                    val = None
                    settings.logger.warning(
                        "Unknown coil value {}".format(
                            mb.bitval.all_fields[i].showname_value == "True"
                        )
                    )

                m.data[
                    self._func_to_addr_space[code]
                    + "."
                    + mb.bitnum.all_fields[i].showname_value
                ] = val

        elif code == 1:
            for i in range(len(mb.bitnum.all_fields)):
                if mb.bitval.all_fields[i].showname_value == "True":
                    val = 1
                elif mb.bitval.all_fields[i].showname_value == "False":
                    val = 0
                else:
                    val = None
                    settings.logger.warning(
                        "Unknown coil value {}".format(
                            mb.bitval.all_fields[i].showname_value == "True"
                        )
                    )
                m.data[
                    self._func_to_addr_space[code]
                    + "."
                    + mb.bitnum.all_fields[i].showname_value
                ] = val

        else:
            settings.logger.warning(
                "Not implemented response code {} in transcribe_read_response".format(
                    mb.func_code
                )
            )  # mb.pdfdump()

    def transcribe_diagnostic(self, m, mb):
        diagnostic_code = int(mb.get_field("diagnostic_code"))

        if diagnostic_code == 1:  # Restart Communication Option
            m.data["restart communication"] = None
            m.activity = Activity.COMMAND
            m._add_to_request_queue = True

        elif diagnostic_code == 4:  # Force listen only
            m.data["force listen only"] = None
            m.activity = Activity.COMMAND
            m._add_to_request_queue = True

        elif diagnostic_code == 10:  # Clear Counters and Diagnostic Register
            m.data["clear counters and diagnostic register"] = None
            m.activity = Activity.COMMAND
            m._add_to_request_queue = True

        else:
            m.activity = Activity.COMMAND  # NOTE maybe not an accurate activity
            settings.logger.warning(
                "Not implemented request code {}, {} in transcribe_diagnostic".format(
                    mb.func_code, diagnostic_code
                )
            )  # mb.pdfdump()

    def transcribe_encapsulated_interface_transport_request(self, m, mb):
        if int(mb.mei) == 14:  # read device identification
            m.data["read device identification"] = None
            m.activity = Activity.INTERROGATE
            m._add_to_request_queue = True

        else:
            settings.logger.warning(
                "Not implemented request code {}, {} in transcribe_encapsulated_interface_transport_request".format(
                    mb.func_code, mb.mei
                )
            )  # mb.pdfdump()

    def transcribe_error_response(self, m, mb):
        m.activity = Activity.INFORM
        m.type += 128
        m._match_to_requests = True

    def match_response(self, requests, response):  # noqa: C901
        remove_from_queue = []

        if len(set([r.type for r in requests])) != 1 or (
            requests[0].type != response.type
            and requests[0].type != response.type - 128
        ):
            settings.logger.critical("Matching with different function codes!")
            return []

        if response.type > 128:  # Handle errors
            response.responds_to = [r.id for r in requests]
            return []

        if response.activity == Activity.INFORM:
            # Response to requested data

            res_keys = list(response.data.keys())

            for request in requests:
                req_keys = list(request.data.keys())
                if req_keys[0] is None:
                    continue

                if (
                    res_keys == req_keys
                ):  # works since we can expect the lists to be ordered
                    response.responds_to.append(request.id)
                    remove_from_queue.append(request)
                else:
                    if set(res_keys).issubset(req_keys):
                        response.responds_to.append(request.id)
                        for key in res_keys:
                            request.pop(key)
                    else:  # more responses than requests
                        settings.logger.warning(
                            "Modbus response carries more data than was requested."
                        )

        elif response.activity == Activity.ACTION:
            # Response to requested action

            for request in requests:
                if request.data.keys() == response.data.keys():
                    for key in request.data.keys():
                        response.data[key] = None  # request.data[key]

                    response.responds_to.append(request.id)
                    remove_from_queue.append(request)
                    break
            else:
                settings.logger.warning(
                    "Received non-matching Modbus response to write request"
                )

        else:
            settings.logger.critical("Unhandled Modbus response activity")

        return remove_from_queue
