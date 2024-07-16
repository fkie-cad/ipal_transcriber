from enum import Enum, IntEnum
from typing import List, Optional, Union

from pyshark.packet.packet import Packet

from transcriber.messages import Activity, IpalMessage
from transcribers.transcriber import Transcriber


class _RegCMD(IntEnum):
    WRITE = 0xC1
    READ = 0xC2


class _RegisterPacketType(IntEnum):
    REG_RADAR_OPS_A = 0x00
    REG_RADAR_OPS_B = 0x01
    REG_ZOOM_LEVEL = 0x03
    REG_UNKNOWN_04 = 0x04  # might be firmware
    REG_BEARING_ALIGNMENT = 0x05
    REG_FILTERS = 0x06
    REG_IF_REJ = 0x08
    REG_TARGET_EXP = 0x09
    REG_TARGET_BOOST = 0x0A
    REG_LOCAL_IF_REJ = 0x0E
    REG_SCAN_SPEED = 0x0F
    REG_NOISE_REJ = 0x21
    REG_TARGET_SEP = 0x22
    REG_DOPPLER = 0x23
    REG_ANTENNA_HEIGHT = 0x30
    REG_KEEP_ALIVE = 0x10
    REG_UNDETERMINED = 0xFF


class _ReportPacketType(IntEnum):
    REP_STATUS = 0x01C4
    REP_SETTINGS = 0x02C4
    REP_FIRMWARE = 0x03C4
    REP_BEARING = 0x04C4
    REP_SCAN = 0x08C4
    REP_UNDETERMINED = 0xFFFF


class _ImagePacketType(IntEnum):
    IMG_DEFAULT = 0xFFFFFF


_RadarPacketType = Union[_RegisterPacketType, _ReportPacketType, _ImagePacketType]


class BR24Transcriber(Transcriber):
    _name = "Navico-BR24"

    def _match_packet_type(self, pkt: Packet) -> Optional[_RadarPacketType]:
        ip = pkt["IP"]
        udp = pkt["UDP"]

        if str(ip.dst) == "236.6.7.8" and int(udp.dstport) == 6678:
            # IMG packet
            return _ImagePacketType.IMG_DEFAULT
        if str(ip.dst) == "236.6.7.9" and int(udp.dstport) == 6679:
            # REP packet
            return _ReportPacketType.REP_UNDETERMINED
        if str(ip.dst) == "236.6.7.10" and int(udp.dstport) == 6680:
            # REG packet
            return _RegisterPacketType.REG_UNDETERMINED
        return None

    def matches_protocol(self, pkt: Packet) -> bool:
        if "UDP" not in pkt:
            return False

        if self._match_packet_type(pkt) is not None:
            return True

        return False

    def _parse_img(self, raw_message: bytes, res: IpalMessage) -> IpalMessage:
        res.activity = Activity.INFORM
        res._match_to_requests = False
        res.type = _ImagePacketType.IMG_DEFAULT

        data = {}
        # frame header
        data["scanline_count"] = raw_message[5]
        data["scanline_len"] = raw_message[6] | raw_message[7] << 8

        # scanlines
        # for i in range(data["scanline_count"]) -> always 32
        index = 8
        for scanline in range(32):
            sl_name = f"scanline_{scanline}"
            # header_len = raw_message[index + 0]
            radar_status = raw_message[index + 1]
            raw_counter = raw_message[index + 2] | raw_message[index + 3] << 8
            angle = raw_message[index + 8] | raw_message[index + 9] << 8
            # heading
            scale = (
                raw_message[index + 12]
                | raw_message[index + 13] << 8
                | raw_message[index + 14] << 24
            )
            pixels = [int(b) for b in raw_message[index + 24 : index + 24 + 512]]

            data[f"{sl_name}:raw_counter"] = raw_counter
            data[f"{sl_name}:status"] = radar_status
            data[f"{sl_name}:angle"] = angle
            data[f"{sl_name}:range"] = scale
            data[f"{sl_name}:pixels"] = pixels
            index += 24 + 512

        res.data = data
        return res

    def _parse_rep(self, raw_message: bytes, res: IpalMessage) -> IpalMessage:
        rep_prefix = raw_message[0]
        rep_cmd = raw_message[1]

        rep_type = (rep_prefix << 8) | rep_cmd
        if rep_cmd != 0xC4:
            # typically 0xF5 reports which are undocumented so far
            res.type = _ReportPacketType.REP_UNDETERMINED
            return res

        res.activity = Activity.INFORM

        match rep_type:
            case _ReportPacketType.REP_STATUS:
                # can be triggered by radar_ops reg
                res._match_to_requests = True
                res.type = _ReportPacketType.REP_STATUS
                res.data = {"status": raw_message[2]}

            case _ReportPacketType.REP_SETTINGS:
                # can be triggered by zoom and filter reg
                res._match_to_requests = True
                res.type = _ReportPacketType.REP_SETTINGS

                # report vals
                rep_range = (
                    raw_message[2]
                    | raw_message[3] << 8
                    | raw_message[4] << 16
                    | raw_message[5] << 24
                )
                gain_auto = (
                    raw_message[8]
                    | raw_message[9] << 8
                    | raw_message[10] << 16
                    | raw_message[11] << 24
                )
                gain = raw_message[12]
                sea_clutter_auto = raw_message[13]
                sea_clutter = raw_message[17]
                rain_clutter = raw_message[22]
                if_rej = raw_message[34]
                tgt_exp = raw_message[38]
                tgt_boost = raw_message[42]

                res.data = {
                    "rep_range": rep_range,
                    "gain_auto": gain_auto,
                    "gain": gain,
                    "sea_clutter_auto": sea_clutter_auto,
                    "sea_clutter": sea_clutter,
                    "rain_clutter": rain_clutter,
                    "if_rej": if_rej,
                    "tgt_exp": tgt_exp,
                    "tgt_boost": tgt_boost,
                }

            case _ReportPacketType.REP_FIRMWARE:
                # can be triggered by firmware reg(?)
                res._match_to_requests = True
                res.type = _ReportPacketType.REP_FIRMWARE

                # store the data fields as sequence of ints instead of bytes
                # so that they are json-serializable
                radar_type = raw_message[2]
                firmware_date = [int(b) for b in raw_message[58:90]]
                firmware_time = [int(b) for b in raw_message[90:122]]
                res.data = {
                    "radar_type": radar_type,
                    "firmware_date": firmware_date,
                    "firmware_time": firmware_time,
                }

            case _ReportPacketType.REP_BEARING:
                # can be triggered by bearing and antenna reg
                res._match_to_requests = True
                res.type = _ReportPacketType.REP_BEARING

                bearing_alignment = raw_message[6] | raw_message[7] << 8
                antenna_height = (
                    raw_message[10]
                    | raw_message[11] << 8
                    | raw_message[12] << 16
                    | raw_message[13] << 24
                )
                res.data = {
                    "bearing_alignment": bearing_alignment,
                    "antenna_height": antenna_height,
                }

            case _ReportPacketType.REP_SCAN:
                # can be triggered by at least scan speed reg
                res._match_to_requests = True
                res.type = _ReportPacketType.REP_SCAN

                local_ir = raw_message[3]
                scan_speed = raw_message[4]
                sls_auto = raw_message[5]
                sls = raw_message[9]
                noise_rej = raw_message[12]
                tgt_sep = raw_message[13]

                res.data = {
                    "local_ir": local_ir,
                    "scan_speed": scan_speed,
                    "sls_auto": sls_auto,
                    "sls": sls,
                    "noise_rej": noise_rej,
                    "tgt_sep": tgt_sep,
                }

            case _:
                # an unknown 0xC4 report, don't try matching, don't speculate on activity
                res.type = _ReportPacketType.REP_UNDETERMINED
                res._match_to_requests = False
                res.activity = Activity.UNKNOWN
        return res

    def _parse_reg(self, raw_message: bytes, res: IpalMessage) -> IpalMessage:
        register = raw_message[0]
        command = raw_message[1]

        # mark the message as request for req-rep matching
        res._add_to_request_queue = True
        res._match_to_requests = False
        if command == _RegCMD.WRITE:
            res.activity = Activity.COMMAND
        elif command == _RegCMD.READ:
            res.activity = Activity.INTERROGATE
        else:
            # malformed packet, don't guess activity
            pass

        match register:
            case _RegisterPacketType.REG_RADAR_OPS_A:
                res.type = _RegisterPacketType.REG_RADAR_OPS_A
                if len(raw_message) >= 3:
                    res.data = {"reg_radar_ops_A": raw_message[2]}

            case _RegisterPacketType.REG_RADAR_OPS_B:
                res.type = _RegisterPacketType.REG_RADAR_OPS_B
                if len(raw_message) >= 3:
                    res.data = {"reg_radar_ops_B": raw_message[2]}

            case _RegisterPacketType.REG_ZOOM_LEVEL:
                res.type = _RegisterPacketType.REG_ZOOM_LEVEL
                if len(raw_message) >= 6:
                    range = (
                        raw_message[2]
                        | raw_message[3] << 8
                        | raw_message[4] << 16
                        | raw_message[5] << 24
                    )
                    res.data = {"range": range}

            case _RegisterPacketType.REG_UNKNOWN_04:
                res.type = _RegisterPacketType.REG_UNKNOWN_04

            case _RegisterPacketType.REG_BEARING_ALIGNMENT:
                res.type = _RegisterPacketType.REG_BEARING_ALIGNMENT
                if len(raw_message) >= 4:
                    bearing_alignment = raw_message[2] | raw_message[3] << 8
                    res.data = {"bearing_alignment": bearing_alignment}

            case _RegisterPacketType.REG_FILTERS:
                res.type = _RegisterPacketType.REG_FILTERS

                if len(raw_message) >= 11:
                    filter_selector = raw_message[2]
                    auto_flag = raw_message[6]
                    filter_value = raw_message[10]

                    res.data = {
                        "filter_selector": filter_selector,
                        "auto_flag": auto_flag,
                        "filter_value": filter_value,
                    }

            case _RegisterPacketType.REG_IF_REJ:
                res.type = _RegisterPacketType.REG_IF_REJ
                if len(raw_message) >= 3:
                    res.data = {"if_rej": raw_message[2]}

            case _RegisterPacketType.REG_TARGET_EXP:
                res.type = _RegisterPacketType.REG_TARGET_EXP
                # not used in BR24?

            case _RegisterPacketType.REG_TARGET_BOOST:
                res.type = _RegisterPacketType.REG_TARGET_BOOST
                if len(raw_message) >= 3:
                    res.data = {"tgt_boost": raw_message[2]}

            case _RegisterPacketType.REG_LOCAL_IF_REJ:
                res.type = _RegisterPacketType.REG_LOCAL_IF_REJ
                if len(raw_message) >= 3:
                    res.data = {"local_ir": raw_message[2]}

            case _RegisterPacketType.REG_SCAN_SPEED:
                res.type = _RegisterPacketType.REG_SCAN_SPEED
                if len(raw_message) >= 3:
                    res.data = {"scan_speed": raw_message[2]}

            case _RegisterPacketType.REG_NOISE_REJ:
                res.type = _RegisterPacketType.REG_NOISE_REJ
                # not used in BR24?

            case _RegisterPacketType.REG_TARGET_SEP:
                res.type = _RegisterPacketType.REG_TARGET_BOOST
                # not used in BR24?

            case _RegisterPacketType.REG_DOPPLER:
                res.type = _RegisterPacketType.REG_DOPPLER
                # not used in BR24?

            case _RegisterPacketType.REG_ANTENNA_HEIGHT:
                res.type = _RegisterPacketType.REG_ANTENNA_HEIGHT
                if len(raw_message) >= 3:
                    res.data = {"antenna_height": raw_message[2]}

            case _RegisterPacketType.REG_KEEP_ALIVE:
                res.type = _RegisterPacketType.REG_KEEP_ALIVE

            case _:
                res.type = _RegisterPacketType.REG_UNDETERMINED

        return res

    def match_response(
        self, requests: List[IpalMessage], response: IpalMessage
    ) -> List[IpalMessage]:

        if response.responds_to is None:
            return []

        match response.type:
            case _ReportPacketType.REP_STATUS:
                # might be a response to REG radar_ops
                for req in requests:
                    if req.type in (
                        _RegisterPacketType.REG_RADAR_OPS_B,
                        _RegisterPacketType.REG_RADAR_OPS_A,
                        _RegisterPacketType.REG_KEEP_ALIVE,
                    ):
                        response.responds_to.append(req.id)
                        if req.activity == Activity.COMMAND:
                            response.activity = Activity.ACTION

            case _ReportPacketType.REP_SETTINGS:
                # might be a response to many REG types
                for req in requests:
                    if req.type in (
                        _RegisterPacketType.REG_ZOOM_LEVEL,
                        _RegisterPacketType.REG_FILTERS,
                        _RegisterPacketType.REG_IF_REJ,
                        _RegisterPacketType.REG_TARGET_BOOST,
                    ):
                        response.responds_to.append(req.id)
                        if req.activity == Activity.COMMAND:
                            response.activity = Activity.ACTION

            case _ReportPacketType.REP_FIRMWARE:
                # only ever sent in response to 0x04 REG reqs(?)
                for req in requests:
                    if req.type == _RegisterPacketType.REG_UNKNOWN_04:
                        response.responds_to.append(req.id)
                        if req.activity == Activity.COMMAND:
                            response.activity = Activity.ACTION

            case _ReportPacketType.REP_BEARING:
                # might be a response to a bearing req
                for req in requests:
                    if req.type == _RegisterPacketType.REG_BEARING_ALIGNMENT:
                        response.responds_to.append(req.id)
                        if req.activity == Activity.COMMAND:
                            response.activity = Activity.ACTION

            case _ReportPacketType.REP_SCAN:
                # might be a response to many REG types
                for req in requests:
                    if req.type in (
                        # in real pcaps 0x03/0x04/0x05 reg salvos trigger a
                        # REP_SCAN, REP_SETTINGS, REP_FIRMWARE, REP_BEARING response.
                        # associating the unknown reg 0x04 to the firmware response
                        # leaves us with 0x03 (REG_ZOOM_LEVEL) as most likely trigger for the REP_SCAN
                        # response, although that is just a guess
                        _RegisterPacketType.REG_ZOOM_LEVEL,
                        # all other associations are evident because the register being acted upon
                        # is actually being reported by REP_SCAN
                        _RegisterPacketType.REG_FILTERS,
                        _RegisterPacketType.REG_LOCAL_IF_REJ,
                        _RegisterPacketType.REG_SCAN_SPEED,
                        _RegisterPacketType.REG_ANTENNA_HEIGHT,
                    ):
                        response.responds_to.append(req.id)
                        if req.activity == Activity.COMMAND:
                            response.activity = Activity.ACTION

            case _:
                assert False

        # FIXME: for most req types which only ever trigger a single response type
        #        we could remove them from queue
        return []

    def parse_packet(self, pkt: Packet) -> List[IpalMessage]:
        ip = pkt["IP"]
        udp = pkt["UDP"]

        raw_msg = bytes.fromhex(udp.payload.replace(":", ""))
        timestamp = float(pkt.sniff_time.timestamp())

        src = f"{ip.src}:{udp.srcport}"
        dest = f"{ip.dst}:{udp.dstport}"

        pkt_type = self._match_packet_type(pkt)

        length = len(raw_msg)

        ipal_message = IpalMessage(
            id=self._id_counter.get_next_id(),
            src=src,
            dest=dest,
            timestamp=timestamp,
            protocol=self._name,
            activity=Activity.UNKNOWN,
            length=length,
            flow="_",
        )

        match pkt_type:
            case _ImagePacketType.IMG_DEFAULT:
                ipal_message = self._parse_img(raw_msg, ipal_message)
            case _ReportPacketType.REP_UNDETERMINED:
                ipal_message = self._parse_rep(raw_msg, ipal_message)
            case _RegisterPacketType.REG_UNDETERMINED:
                ipal_message = self._parse_reg(raw_msg, ipal_message)
            case _:
                raise Exception(
                    f"unknown packet type, packet does not appear to match {self._name}"
                )

        return [ipal_message]
