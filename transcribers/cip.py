import transcriber.settings as settings
from transcriber.messages import Activity, IpalMessage
from transcribers.transcriber import Transcriber


class CIPTranscriber(Transcriber):
    _name = "cip"

    @classmethod
    def state_identifier(cls, msg, key):
        if msg.activity in [Activity.INTERROGATE, Activity.COMMAND]:
            return f"{msg.dest}:{key}"
        elif msg.activity in [Activity.INFORM, Activity.ACTION]:
            return f"{msg.src}:{key}"
        else:
            settings.logger.critical(f"Unknown activity {msg.activity}")
            return f"{msg.src}:{key}"

    def matches_protocol(self, pkt):
        return "CIP" in pkt

    def parse_packet(self, pkt):
        res = []

        enip_layers = pkt.get_multiple_layers("ENIP")

        cip_layers = pkt.get_multiple_layers("CIP")

        cipcm_layers = pkt.get_multiple_layers("CIPCM")

        src = f"{pkt['IP'].src}:{pkt['TCP'].srcport}"
        dest = f"{pkt['IP'].dst}:{pkt['TCP'].dstport}"

        for i in range(len(cip_layers)):
            enip = enip_layers[i]
            cip = cip_layers[i]
            cipcm = cipcm_layers[i]

            length = int(enip.length)

            if int(pkt["TCP"].dstport) == settings.ENIP_PORT:  # Request
                code = int(cipcm.cip_service, 16)

                flow = (dest, src, int(enip.session, 16), code)

                m = IpalMessage(
                    id=self._id_counter.get_next_id(),
                    src=src,
                    dest=dest,
                    timestamp=float(pkt.sniff_time.timestamp()),
                    protocol=self._name,
                    flow=flow,
                    length=length,
                    type=code,
                )

                if code == 76:
                    # (0x4C) CIP data table read: read a block of consecutive DINT data
                    self.transcribe_read_request(m, cip, cipcm)
                elif code == 77:
                    # (0x4D) CIP data table write: write a block of consecutive DINT data
                    self.transcribe_write_request(m, cip, cipcm)
                else:
                    m.activity = (
                        Activity.INTERROGATE
                    )  # NOTE maybe not an accurate activity
                    settings.logger.warning(
                        f"Not implemented request function code {cip.service}"
                    )

                res.append(m)

            elif int(pkt["TCP"].srcport) == settings.ENIP_PORT:  # Response
                code = int(cip.sc, 16)

                flow = (src, dest, int(enip.session, 16), code)

                m = IpalMessage(
                    id=self._id_counter.get_next_id(),
                    src=src,
                    dest=dest,
                    timestamp=float(pkt.sniff_time.timestamp()),
                    protocol=self._name,
                    flow=flow,
                    length=length,
                    type=code,
                )

                if code == 76:
                    # (0x4C) CIP data table read: read a block of consecutive DINT data
                    self.transcribe_read_response(m, cip, cipcm)
                elif code == 77:
                    # (0x4D) CIP data table write: write a block of consecutive DINT data
                    self.transcribe_write_response(m, cip, cipcm)
                else:
                    m.activity = Activity.INFORM  # NOTE maybe not an accurate activity
                    settings.logger.warning(
                        f"Not implemented response function code {cip.service}"
                    )

                res.append(m)

            else:
                settings.logger.critical(
                    f"Unknown ports for CIP ({pkt['TCP'].srcport}, {pkt['TCP'].dstport})"
                )

        return res

    def transcribe_read_request(self, m, cip, cipcm):
        m.activity = Activity.INTERROGATE
        m._add_to_request_queue = True
        m.data = {}

        code = int(cipcm.cip_service, 16)

        if code == 76:
            m.data[cipcm.cip_symbol.split(":")[0]] = None

        else:
            settings.logger.warning(
                f"Not implemented request code {cip.service} in transcribe_read_request"
            )

    def transcribe_read_response(self, m, cip, cipcm):
        m.activity = Activity.INFORM
        m._match_to_requests = True
        m.data = {}

        code = int(cip.sc, 16)

        if code == 76:
            m.data[cipcm.cip_symbol.split(":")[0]] = "".join(
                cipcm.cip_data.split(":")[2:]
            )  # ca:00:cd:cc:1c:40 => cdcc1c40

        else:
            settings.logger.warning(
                f"Not implemented response code {cip.service} in transcribe_read_response"
            )

    def transcribe_write_request(self, m, cip, cipcm):
        pass  # TODO

    def transcribe_write_response(self, m, cip, cipcm):
        pass  # TODO

    def match_response(self, requests, response):
        remove_from_queue = []

        if len(set([r.type for r in requests])) != 1 or (
            requests[0].type != response.type
        ):
            settings.logger.critical("Matching with different function codes!")
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
                            "CIP response carries more data than was requested."
                        )
        else:
            settings.logger.critical("Unhandled CIP response activity")

        return remove_from_queue
