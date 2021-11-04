from transcriber.messages import IpalMessage, Activity
from transcribers.transcriber import Transcriber
import transcriber.settings as settings


class S7Transcriber(Transcriber):
    # The S7 transcriber is only capable of transcribing the one dataset that we currently have
    _name = "s7"

    _id_to_area = {
        0x03: "system_info",  # System info of S200 family
        0x05: "system_flag",  # System flags of S200 family
        0x06: "analog_in",  # Analog inputs of S200 family
        0x07: "analog_out",  # Analog outputs of S200 family
        0x1C: "C",  # S7 counters (C)
        0x1D: "T",  # S7 timers (T)
        0x1E: "iec_counter",  # IEC counters (200 family)
        0x1F: "iec_timer",  # IEC timers (200 family)
        0x80: "P",  # Direct peripheral access (P)
        0x81: "I",  # Inputs (I)
        0x82: "Q",  # Outputs (Q)
        0x83: "M",  # Flags (M) (Merker)
        0x84: "DB",  # Data blocks (DB)
        0x85: "DI",  # Instance data blocks (DI)
        0x86: "L",  # local data
        0x87: "V",  # unknown
    }

    def matches_protocol(self, pkt):

        return "S7COMM" in pkt

    def parse_packet(self, pkt):  # noqa: C901
        ip = pkt["IP"]
        tcp = pkt["TCP"]
        s7_pkt = pkt["S7COMM"]

        src = "{}:{}".format(ip.src, tcp.srcport)
        dest = "{}:{}".format(ip.dst, tcp.dstport)
        length = int(s7_pkt.header_parlg) + int(s7_pkt.header_datlg)

        try:
            job = int(s7_pkt.header_rosctr)
            pduref = int(s7_pkt.header_pduref)
        except IndexError:
            settings.logger.warning("Error parsing job and pduref number")
            return []

        m = IpalMessage(
            id=self._id_counter.get_next_id(),
            src=src,
            dest=dest,
            timestamp=float(pkt.sniff_time.timestamp()),
            protocol=self._name,
            length=length,
            type=job,
        )

        if job == 0x01:

            funcCode = int(s7_pkt.param_func, 16)

            # activity read request
            m._flow = (src, dest, pduref)

            if funcCode == 0xF0:  # setup communication
                # can be ignored by us
                return []
            elif funcCode == 0x05:  # write variable

                m.activity = Activity.COMMAND
                m._add_to_request_queue = True

                data = {}
                itemcount = int(s7_pkt.param_itemcount)
                for i in range(itemcount):

                    syntax_id = int(s7_pkt.param_item_syntaxid, 16)

                    if syntax_id == 0xB2:  # 1200SYM
                        address = int(
                            s7_pkt.tiap_item_value.all_fields[i].showname_value
                        )
                    elif syntax_id == 0x10:  # S7ANY

                        area = self._id_to_area[
                            int(s7_pkt.param_item_area.all_fields[i].raw_value, 16)
                        ]
                        if area == "DB":
                            area += ".{}".format(
                                int(s7_pkt.param_item_db.all_fields[i].raw_value, 16)
                            )

                        address = (
                            area
                            + "."
                            + str(
                                int(
                                    s7_pkt.param_item_address.all_fields[i].raw_value,
                                    16,
                                )
                            )
                        )
                    else:
                        settings.logger.warning("Unknown Syntax ID")
                        return []

                    data[address] = int(
                        s7_pkt.resp_data.all_fields[i].showname_value, 16
                    )

                m.data = data

            elif funcCode == 0x04:  # read variable

                m.activity = Activity.INTERROGATE
                m._add_to_request_queue = True

                data = {}
                itemcount = int(s7_pkt.param_itemcount)
                for i in range(itemcount):

                    syntax_id = int(s7_pkt.param_item_syntaxid, 16)

                    if syntax_id == 0xB2:  # 1200SYM
                        address = int(
                            s7_pkt.tiap_item_value.all_fields[i].showname_value
                        )
                    elif syntax_id == 0x10:  # S7ANY

                        area = self._id_to_area[
                            int(s7_pkt.param_item_area.all_fields[i].raw_value, 16)
                        ]
                        if area == "DB":
                            area += ".{}".format(
                                int(s7_pkt.param_item_db.all_fields[i].raw_value, 16)
                            )

                        address = (
                            area
                            + "."
                            + str(
                                int(
                                    s7_pkt.param_item_address.all_fields[i].raw_value,
                                    16,
                                )
                            )
                        )
                    else:
                        settings.logger.warning("Unknown Syntax ID")
                        return []

                    data[address] = None

                m.data = data
            else:
                settings.logger.warning(
                    f"S7 Function Code {funcCode} has not been implemented for the transcriber, ignoring packet ..."
                )
                return []

        elif job == 0x03:

            funcCode = int(s7_pkt.param_func, 16)

            m._flow = (dest, src, pduref)

            if funcCode == 0xF0:  # setup communication
                # can be ignored by us
                return []
            elif funcCode == 0x05:  # write variable

                m.activity = Activity.ACTION
                m._match_to_requests = True

                itemcount = int(s7_pkt.param_itemcount)

                m.data = {None: []}
                for i in range(itemcount):
                    m.data[None].append(
                        int(s7_pkt.data_returncode.all_fields[i].raw_value, 16)
                    )

            elif funcCode == 0x04:  # read variable

                m.activity = Activity.INFORM
                m._match_to_requests = True

                itemcount = int(s7_pkt.param_itemcount)

                m.data = {None: []}
                for i in range(itemcount):
                    value = int(s7_pkt.resp_data.all_fields[i].showname_value, 16)
                    m.data[None].append(value)

            else:
                settings.logger.warning(
                    f"S7 Function Code {funcCode} has not been implemented for the transcriber, ignoring packet ..."
                )
                return []
        else:
            settings.logger.warning(
                f"S7 job {job} has not been implemented for the transcriber, ignoring packet ..."
            )
            return []

        return [m]

    def match_response(self, requests, response):

        req_to_remove = []

        if None in response.data and response.activity == Activity.INFORM:
            for request in requests:

                if request.activity != Activity.INTERROGATE:
                    continue

                keys = list(request.data.keys())[0]
                if keys is None:
                    continue

                unmatched_data = len(response.data[None])
                requested_data = len(request.data)

                if requested_data == unmatched_data:

                    matchable_data = requested_data

                    response.responds_to.append(request.id)

                    annotated_data = {}
                    for i in range(matchable_data):
                        key = list(request.data.keys())[i]
                        annotated_data[key] = response.data[None][i]
                    response.data = annotated_data

                    req_to_remove.append(request)

                    break

        elif None in response.data and response.activity == Activity.ACTION:

            for request in requests:
                if request.activity != Activity.COMMAND:
                    continue

                if len(request.data) == len(response.data[None]):

                    keys = list(request.data.keys())
                    for i in range(len(request.data)):

                        if response.data[None][i] == 0xFF:  # Success return code
                            response.data[keys[i]] = request.data[keys[i]]

                        del response.data[None]

                    req_to_remove.append(request)
                    break

        else:
            settings.logger.warning("Unknown match condition")

        return req_to_remove
