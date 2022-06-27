# This DNP3 Transcriber was implemented by
# Olav Lamberts, RWTH Aachen, 2022

from __future__ import annotations
import struct

import math
from enum import IntEnum, Enum
from typing import Union

import transcriber.settings as settings
from transcriber.messages import IpalMessage, Activity
from transcribers.transcriber import Transcriber
from transcribers.auxiliary_enums.dnp3 import (
    _FunctionCodes,
    _ObjectTypes,
    _CastingTypes,
    _ObjectHeader,
    _ObjectValueFields,
    _Qualifier,
    _DnpMsgType,
)


# General transcriber extension possibilities through special makers/ flags:
# - object doesn't exist/ is inactive/ disabled
# - function code (/ TypeID/ Modbus function code) is not supported
# - value-format is unsupported
# - outstation is busy, but queued req/cmd
# - outstation is busy, had to drop req/cmd
# - invalid msg. format (*not* unsupported, but not allowed by standard)
# - uses reserved bits
# - uses deprecated/ obsolete bits
# - ??? Some basic authentication stuff (challenge, response, error, ...) ???
# - real-value greater than what requested format allows
#     (e.g. a true 17-bit nr should be reported as 16-bit); as in 11.6.1.1. Rule 2
# - probably could make a mini-survey about the status-codes, qualifiers, flags
#    set by each of the protocols and see which are shared across (most)
# - various types of parameters that are common but may not be shared across all protocols,
#    e.g., deadband values
# - If multiple different protocols are deployed in the same setting, it could be useful
# - outside of expected implementation level flag:
#   some devices will be set to not cover all "additional" non-mandatory functionality
#   while in DNP3, this is stated in a more structured approach, i.e., the implementation levels,
#   it could be useful to mark a packet as being outside the normal operational support of the resp. device
#   DNP3 clearly states that a stated implementation level always only sets the "minimum" and more can always
#   be supported, packets outside of the expected implementation level might be more correlated to
#   attacks, e.g., if the MITM injects pkts not supported by the IED/outstation/...


# A general issue w/ the current transcriber architecture:
#   as soon as we have an attacker who injects packets which do not correspond
#   directly to the standard, e.g., by sending a msg. in master direction which only is allowed
#   in outstation direction, the flow direction etc. will be false.
#   Since no "track record" of use of an IP/... is kept, it's not clear at all
#   what is the true direction upon such "illegal" pkt.
#   The current transcriber will just flip the direction since he assumes the pkt is a legal pkt.

# This Transcriber assumes an implementation of function codes, groups & qualifiers combinations as shown in the
# tables of section 12, §2:
# The standard itself allows for other combinations outside of these specifications;
#   however, since the tables provide the various baselines, these are the focus of this implementation
# c.f.12.2.:
# "
# These tables do not provide an exhaustive list of all valid DNP3 object / function code / qualifier
# combinations. Devices may implement different combinations to those shown in the tables and still use
# DNP3 in a valid way.
# "


class DNP3Transcriber(Transcriber):
    # Assumes non-encrypted traffic.
    # Independent on underlying TCP/IP, UDP/IP, ... that are placed below
    # DNP3's data link layer, DNP3 deploys TLS on top if security is applied.

    # Possible global parameter which should be added for better
    # cross-dataset support: Timeout parameters, e.g., for confirmations
    # to better handle retries of the original packet which, depending on the specific packet,
    # don't need to increment the sequence nr.
    # Same goes for the #unsolicited response retries (e.g. for better handling 4.6.6 rule 12)

    # Further, if authentication is deployed, the transcriber would probably fare easier
    # if the resp. settings could be given as input since then responses can occur to
    # functions codes which would never get responses if no authentication is deployed

    _name = "dnp3"

    @classmethod
    def state_identifier(cls, msg, key):
        if msg.activity in [
            Activity.INTERROGATE,
            Activity.COMMAND,
            Activity.CONFIRMATION,
        ]:
            # Confirmation Activity should never address a datapoint though.
            return "{}:{}".format(msg.dest, key)
        elif msg.activity in [Activity.INFORM, Activity.ACTION]:
            return "{}:{}".format(msg.src, key)
        else:
            settings.logger.critical("Unknown activity {}".format(msg.activity))
            return "{}:{}".format(msg.src, key)

    @staticmethod
    def matches_protocol(pkt):
        return "dnp3" in pkt

    def parse_packet(self, pkt):
        """
        :param pkt: to be parsed
        :return: [ipal msg: each msg represents a complete entity in DNP3]
        """
        msgs = []

        # Limitation:
        #  for broadcasting UDP may be used.
        #  Thus, TCP does not always happen
        #  In QUT-DNP3 it's TCP-only though
        #  ref: definition of "listening end point" in 3.1
        # UDP can also be used entirely instead of TCP in case of highly reliable links
        # to reduce the overhead from TCP (ref. 13.2.3.2)
        # Generally, DNP3 is defined also for serial communication (e.g., RS-232) but we assume
        #  for now that TCP/IP is used until a dataset w/ other characteristics becomes available
        l4_proto = "TCP" if "TCP" in pkt else "UDP"
        src = "{}:{}".format(pkt["IP"].src, pkt[l4_proto].srcport)
        dest = "{}:{}".format(pkt["IP"].dst, pkt[l4_proto].dstport)
        timestamp = float(pkt.sniff_time.timestamp())

        dnp3_layers = pkt.get_multiple_layers("dnp3")
        for dnp in dnp3_layers:

            if not hasattr(dnp, "al_func"):
                # Layer 2/3/4 only and contains no real
                # change of state etc., therefore ignore for now at least.
                continue

            # each DNP3 packet-stack (L2, Transportation, Application Layer, objects)
            # is contained in this single layer
            try:
                msgs.append(self.parse_dnp(src, dest, timestamp, dnp))
            except BaseException as e:
                # assumes TCP
                settings.logger.critical(
                    f'DNP {e=}\n{src=} {dest=} {timestamp=} {pkt["TCP"].seq=} {pkt=}'
                )

        return msgs

    def parse_dnp(self, src, dest, timestamp, dnp) -> IpalMessage:
        # while for the special address "self-addr" (only allowed as dst-addr),
        # the src-addr will always include the true destination address,
        # it's still a relevant piece of data that the self-addr was used.
        # Therefore, I'm not going to replace the self-addr. with the other addr included
        # Broadcast addresses cannot be replaced with the true addr to my understanding
        # as that information is not given.
        dnp3_l2_src = int(dnp.src)
        dnp3_l2_dst = int(dnp.dst)
        data = {}

        func_code = _FunctionCodes(int(dnp.al_func))
        activity = self.define_activity(dnp)

        # These are purely APPLICATION LAYER requests/ responses!
        # Since we so far only focus on the AL data, no DNP3 Data link/ transport layer req/resp.
        #   messaging is kept track of and turned into IPAL messages.
        add_to_req_queue, match_to_requests = self._get_queue_info(dnp)

        if activity == Activity.CONFIRMATION or func_code.msg_type_is_request:
            # Only masters ever send a confirmation
            # ref. 4.4.1
            # if an outstation would send sth. with the same type of functionality,
            # it is a null-response
            flow = (src, dest)
            outstation_addr = dnp3_l2_dst
        else:
            flow = (dest, src)
            outstation_addr = dnp3_l2_src

        if func_code.data_contains_no_individual_obj:
            # if contains payload
            # # it only is which general things (classes/ groups) the signal is targeted at.
            data = self._parse_signals(dnp, outstation_addr)

        elif func_code in (
            _FunctionCodes.READ,
            _FunctionCodes.ENABLE_UNSOLICITED,
        ):
            # contains payloads that can be just group-objects
            # but also actual points to my understanding (QUT only has the group-objects though)
            # these points & groups do not contain further data, but are just the target of the
            # respective signal (e.g. to be read)

            # For read, enable & disable unsolicited resp. specifying individual points are *optional*;
            # the master can enable & disable entire groups/ classes (c.f. 4.4.13)
            # entire classes can be read as well
            data = self._parse_signals_with_mixed_class_and_point_targets(
                dnp, outstation_addr
            )

        elif func_code in (
            _FunctionCodes.WRITE,
            _FunctionCodes.RESPONSE,
            _FunctionCodes.UNSOLICITED_RESPONSE,
        ):
            data = self._parse_main_payload_data(dnp, outstation_addr)
        else:
            settings.logger.warning(f"[DNP3] Could not handle {func_code=}")

        # duplicate SEQ numbers can exist for:
        # - retries
        # - between unsolicited \& solicited responses,
        #    the former will always set the UNS bit though (c.f. 4.6.4)
        data["SEQ"] = int(dnp.al_seq)

        m = IpalMessage(
            id=self._id_counter.get_next_id(),
            src=src,  # add outstation_addr or dnp3_l2_src?
            dest=dest,  # add outstation_addr or dnp3_l2_dst?
            timestamp=timestamp,
            protocol=self._name,
            activity=activity,
            flow=flow,
            # 5 always added for uncounted L2 header in len-field
            # + CRC field of 2 octets per data-chunk (max 16 octets per data-chunk)
            length=int(dnp.len) + 5 + 2 * math.ceil(int(dnp.dnp_data_chunk_len) / 16),
            type=func_code.value,
        )
        m.data = data
        m._add_to_request_queue = add_to_req_queue
        m._match_to_requests = match_to_requests

        return m

    @staticmethod
    def define_activity(dnp) -> Activity:
        func_code = _FunctionCodes(int(dnp.al_func))
        activity = func_code.get_activity()

        if activity == Activity.UNKNOWN:
            if not DNP3Transcriber._is_null_response(dnp):
                headers = _ObjectHeader.parse_all_headers(dnp).values()
                tmp = list({h.group.activity_in_response for h in headers})
                if len(tmp) == 1 and tmp[0] != Activity.UNKNOWN:
                    activity = tmp[0]
                elif tmp == [Activity.UNKNOWN]:
                    settings.logger.warning(
                        f"[DNP3] No activity clearly defined; only UNKNOWN; is null resp: "
                        f"{DNP3Transcriber._is_null_response(dnp)}\n{dnp}",
                    )
                else:
                    tmp = [t for t in tmp if t != Activity.UNKNOWN]
                    if len(tmp) == 1:
                        activity = tmp[0]
                    elif len(tmp) > 1:
                        settings.logger.warning(
                            f"[DNP3] No unique activity: {tmp}\nMeans fault in activity for response definition."
                        )
        return activity

    @staticmethod
    def _parse_signals(
        dnp, outstation_addr
    ) -> Union[dict[str, int], dict[str, list[int]], dict[str, list[str]]]:
        f = int(dnp.al_func)
        if f in (
            _FunctionCodes.WARM_RESTART,
            _FunctionCodes.COLD_RESTART,
            _FunctionCodes.RECORD_CURRENT_TIME,
        ):
            # function-code is signal of what happened.
            # doesn't refer to anything else.
            return {}

        target = None

        if f == _FunctionCodes.CONFIRM:
            # null payload; target is previously send package
            target = f"{outstation_addr}:{int(dnp.al_seq)}"

        elif f in (
            _FunctionCodes.IMMED_FREEZE,
            _FunctionCodes.IMMED_FREEZE_NR,
        ):
            # Ref.
            # variation will always be 0, bc. the freezing does not depend on a data format
            # *all* objects of the same group will be frozen (and potentially cleared, depending on the func-code)
            # thus, no single point is referred to in the dnp-msgs.
            groups_to_freeze = _ObjectHeader.parse_all_headers(dnp).values()
            target = [
                f"{outstation_addr}:{header.group.value}" for header in groups_to_freeze
            ]

        if target is not None:
            return {_SignalKeys.SIGNAL_TARGET: target}

        raise RuntimeError(f"Couldn't handle {dnp}")

    @staticmethod
    def _parse_signals_with_mixed_class_and_point_targets(
        dnp, outstation_addr
    ) -> dict[str, list[str]]:
        # For now designed at read & enable spontaneous msging cmds
        # to be extended for non-QUT datasets
        signal_targets = []
        headers = _ObjectHeader.parse_all_headers(dnp)
        assert len(headers) >= 1
        for h in headers.values():
            if h.group == 60:
                # stands for addressing an entire "Class"
                # Class x => var == x+1
                # For consistency to the other signal-targeting options,
                # I choose the raw variation instead

                # class 0 = static data; class 1-3 = events
                # events can be (re-)assigned to any of 1-3; assigning one to class 0
                # stands for disabling the assignment/event generation (c.f. 4.4.14)
                # every point that supports events shall have a default class assignment
                signal_targets.append(f"{outstation_addr}:60:{h.variation}")
            else:
                # QUT-DNP3 only applies Read w/ group 60
                # Group 60 asks the outstation simply for all updates of the resp. class
                raise NotImplementedError("Cannot handle read-cmd to non-60 group yet.")

            # For things like authentication, file-handling, save-config
            # it would probably make most sense to set the signal target in a more
            # specific way; e.g. include the user-name for the first, file-name second,
            # and config-location for the last

        return {_SignalKeys.SIGNAL_TARGET: signal_targets}

    @staticmethod
    def _parse_main_payload_data(dnp, outstation_addr):
        point_data = {}
        count_status = _CountingStatus()

        if int(dnp.al_func) in (
            _FunctionCodes.RESPONSE,
            _FunctionCodes.UNSOLICITED_RESPONSE,
        ) and not hasattr(dnp, "al_obj"):
            # potentially need to fill with IIN bits, will see#
            # In case of "Unsolicited Response" there might still be another
            # "signal-bit" set, e.g. that the device restarted
            # if it were not for that signal bit, it wouldn't make too much sense to explicitly
            # send out an *unsolicited* response w/e payload
            return {}

        for i in range(len(dnp.al_obj.all_fields)):
            count_status.data_obj_main_index = i
            header = _ObjectHeader.from_index(dnp, i)

            point_indexes = DNP3Transcriber._parse_objects_indexes(
                dnp, count_status, header
            )

            # retrieves *main* value for each point-obj. and stores it.
            for point_id in point_indexes:
                # while the "point-id" is the true identity of a general point class (e.g. analog inputs)
                # since it *can* have additional event & freeze objects associated with it
                # that *do not* have to have equal value to the currently read analog input state,
                # it is important to include the group as part of the address. (c.f. 11.9)
                # Further, multiple point ids of the same group & variation can refer to the same
                #   semantic point, e.g. positive & negative accumulations through counters:
                #   11.9.5.4
                #
                # Further, as outlined below, a point can actually report different values for different
                # variations, even if it does not change in between, simply because the format
                # requested by var1 does not properly fit the current input point's state.
                # Therefore, adding the variation to the address allows to destinguish between
                # addressing schemes which have different reporting "capacities" (e.g. 16 bit vs. 32 bit values)
                #  besides also adding side-information like time-of-occurrence to the main value,
                #  dependent on the var chosen
                addr = f"{outstation_addr}:{header.group}:{header.variation}:{point_id}"

                val_field_index = count_status.index_for_value_field(
                    header.main_value_field
                )
                val_field = dnp.get_field(header.main_value_field).all_fields[
                    val_field_index
                ]

                # Note: Some values which will be reported here may not be the true
                # values of the field device; if a master requests a value as 16-bit nr,
                # but it is a true > 16 bit nr, special values are reported that signal this,
                # together with the resp. OVER_RANGE flag etc. (e.g. Table 11-6)
                val = DNP3Transcriber._parse_shark_val_field(
                    val_field, header.casting_type
                )

                if header.group.obj_type == _ObjectTypes.EVENT:
                    # multiple events for the same addr can exist
                    if addr in point_data:
                        point_data[addr].append(val)
                    else:
                        point_data[addr] = [val]
                else:
                    if addr in point_data:
                        raise RuntimeError(
                            f"Unexpected; {addr=} already in {point_data=}"
                        )
                    point_data[addr] = val

                count_status.increment_val_field_index(header.main_value_field)

            # update overall status
            if header.qual.prefixed_with_index:
                count_status.prefixed_objects_index += 1
                count_status.next_prefixed_obj_index += len(point_indexes)
            elif header.qual.range_contains_start_stop_index:
                # not supporting start-stop virt addresses here yet (diff. range qualifier)
                count_status.start_stop_index += 1

        return point_data

    @staticmethod
    def _parse_shark_val_field(shark_val_field, cast_type) -> Union[int, str]:
        if cast_type == _CastingTypes.INT:
            return shark_val_field.int_value
        if cast_type == _CastingTypes.INT_THROUGH_SHOW:
            # little-endianess, the #bits of the octets relevant for the actual main value
            # sometimes result in .{int,binary,...}_value
            # representing the wrong parsing of the data.
            return int(shark_val_field.show)
        if cast_type == _CastingTypes.TS_48_BIT_TO_SEC_MS:
            transmitted_val = shark_val_field.binary_value
            # 48-bit value; but for some reason formitted in a way
            # s.t. // 10^3 are *exactly* the epoch-seconds and mod 10^3 ms
            # even though 48-bit value would allow for more accurate measurements in the
            # part-nanosecond region
            # perhaps to circumvent the year 2038 problem of using only 32 bits for seconds
            # since epoch

            # struct does not support 48-bit unpacking
            # DNP3 always transmits in Little-Endian
            ms = struct.unpack("<q", transmitted_val + b"\x00\x00")[0]
            s = ms // 1000
            ms = ms % 1000
            return f"{s}.{ms}"
        if cast_type == _CastingTypes.MILLI_S_TS:
            ms = int(shark_val_field.show)
            s = ms // 1000
            ms = ms % 1000
            return f"{s}.{ms}"
        raise ValueError(f"bad {shark_val_field=} {cast_type=}")

    @staticmethod
    def match_response(requests, response):
        """
        Tries to find those requests which could cause this specific response.

        Note: We do not perform a data-obj. based checkup which requires far more
             in depth protocol parsing; the current checkup is based on
            function codes + sequence numbers alone.

        :param requests: dnp3 pkts which still need a response matched to them
        :param response: the dnp3 pkt for which we look-back to find the request-pkt
                        causing it to occur
        :return: list of requests that the response ?possibly? responds to.
        """
        for request in requests:
            # seq.numbers go only up to 2^4 - 1...
            # depending on how this is used by the transcriber I'll need to add some further checks
            # to limit accidental false matches
            if request.data["SEQ"] != response.data["SEQ"]:
                # potentially need to modify this for cmd post cmd
                continue

            # Future datasets: Possibly need statekeeping of unsol. resp conf seq numbers.
            #   late arriving confirmations to unsol. resp. with seq-nr lower than
            #   a previous confirmation should be discarded by the RTU
            #   while the late confirmations should in some way still be matched to
            #   the resp. unsol. resp, it maybe should at least be marked in some way
            #    as being neglected by the protocol (c.f. 4.6.6 Rule 10)
            # One could extend that discussion of marking "discarded" packets
            #    in other protocols for easier highlighting of some anomalies
            #    such as a dynamic latency ...

            if {response.type, request.type} <= {0x81, 0x82}:
                # both response/ unsol. resp; cannot match as both from outstation.
                continue

            if response.type in (_FunctionCodes.CONFIRM, _FunctionCodes.RESPONSE):
                response.responds_to.append(request.id)
                if response.type == _FunctionCodes.RESPONSE:
                    if response.activity == Activity.UNKNOWN:
                        # Null-response/ has content which can be used for both inform & action
                        # It's unclear to me if for every command that can lead to null-responses
                        # we can clearly differentiate between those cases where it serves a pure
                        # "ACK" function, e.g., bc. the outstation still is too busy and has to queue the cmd
                        # from a legit null-response for the same incoming cmd signalling that the cmd was actually
                        # performed.
                        # If that were the case, we could mark the first "too-busy" ACK as pure "Confirmation" Activity.
                        if request.activity == Activity.INTERROGATE:
                            response.activity = Activity.INFORM
                        elif request.activity == Activity.COMMAND:
                            response.activity = Activity.ACTION
                        else:
                            # It *may* be possible to re-evaluate the packet-flow after restart commands
                            # to not just include the g52v2 immediately send pre-restart, but also
                            # the *optional* unsolicited/ sol. response post-restart.
                            # The issue being that masters may optionally (and in QUT-DNP3 at least the attacker does)
                            # continue to send other cmds while the restart is in progress.
                            # Thus, it becomes tricky to find that *maybe send* post-restart pkt w/e taking it away
                            # from a different cmd send during the device restart.
                            # Since the g52v2 is only a very rough estimate, and in QUT-DNP3 doens't fit at all,
                            # of how long the outstation is busy, taking the g52v2 timestamp does not necessarily
                            # help.
                            settings.logger.warning(
                                f"Could not re-define response's activity from request! "
                                f"Req:\n{request}\nResp:\n{response}"
                            )
                return [request]

            # For cold/warm restart types could nail-down the response
            #  to one with a g52v{1/2} obj reply.

            # Potentially need to match outstation packets to
            #   Record current time cmds afterwards due to rule
            #   4.4.16.1 (IIN 1.4)
        settings.logger.debug(f"No request found for response\n{response}")
        return []

    @staticmethod
    def _is_null_response(dnp) -> bool:
        # Unsolicited responses can also be null-responses.
        # For instance, post device-restart, the outstation shall signal its new availability to the
        # master as null-response; c.f. 5.1.1.1.1 Rule 2
        return int(dnp.al_func) in (0x81, 0x82) and int(dnp.dnp_data_chunk_len) == 5

    @staticmethod
    def _get_queue_info(dnp) -> tuple[bool, bool]:
        """
        ret [add dnp to req queue, dnp needs to be matched to request]

        Note: Does *not* check if the pkt is an invalid dnp3 packet;
        for invalid dnp3 packets (e.g. unsupported variation for an included group id),
            a response might occur when for "its" correct version no response would occur

        In case of several types of errors, e.g., incorrectly formatted AL fragment,
            a response w/ IIN2.2 PARAMETER_ERROR Bit should be send (c.f. 4.5.11)
        """
        f = _FunctionCodes(int(dnp.al_func))

        # If the CON bit is set, a *confirmation* msg (func code 0x0) shall be returned,
        # if not set, it shall *not* be returned (ref. 4.2.2.4.3)
        # => Any msg with con bit set will be classified as "request" here
        conf_msg_requested = int(dnp.al_con) == 1

        if f.msg_type == _DnpMsgType.REQUEST:
            if f.always_requires_response:
                return True, False
            elif f.should_never_be_responded_to:
                return False, False
            else:
                # response is optional
                return conf_msg_requested, False

        if f.msg_type == _DnpMsgType.CONFIRMATION:
            # w/ the exception of custom authentication marking the Confirmation msg. as critical
            # and not providing an aggressive authentication obj. in the same msg...
            # if that would be the case, also needs to add this pkt to dnp req. queue
            return False, True

        # just dnp-responses left (not always responses to cmds/...)
        if f == _FunctionCodes.UNSOLICITED_RESPONSE:
            # always req. confirmation
            return True, False

        if f == _FunctionCodes.RESPONSE:
            return conf_msg_requested, True

        if f == _FunctionCodes.AUTHENTICATE_RESP:
            # latter argument dependent on what caused the resp...
            # Not entirely sure... also doesn't come up in QUT-DNP3
            return True, True

        settings.logger.warning(
            f"Couldn't determine the queue info for reserved/ obsolete/ deprecated func. code {f}"
        )
        return False, False

    @staticmethod
    def _parse_objects_indexes(dnp, count_status, header: _ObjectHeader) -> list[int]:
        """

        :param dnp: dnp3-stack
        :param count_status: statekeeping of how how much of dnp was parsed so far
        :param header: Obj. header wrapper as in 4.2.2.7
        :return: [i: i is index of point in following objs of packets]: sorted by order in pkt

        Note: Does *not* assume an attacker who might end up simply in/-decreasing the start/stop-index field
            s.t. we would end up ignoring some points/ having array-out-of-bound correspondence
        """
        if header.should_contain_single_obj_without_prefix:
            return [1]

        if header.qual.prefixed_with_index:
            cnt = int(
                dnp.al_range_quantity.all_fields[
                    count_status.prefixed_objects_index
                ].show
            )
            indexes = [
                int(dnp.al_index.all_fields[k].show)
                for k in range(
                    count_status.next_prefixed_obj_index,
                    count_status.next_prefixed_obj_index + cnt,
                )
            ]
            count_status.next_prefixed_obj_index += len(indexes)
            return indexes

        elif header.qual.range_contains_start_stop_index:
            start = int(
                dnp.al_range_start.all_fields[count_status.start_stop_index].show
            )
            stop = int(dnp.al_range_stop.all_fields[count_status.start_stop_index].show)
            return list(range(start, stop + 1))


class _CountingStatus:
    """
    The "Counting Status" is applied for state-keeping during parsing
    of an individual packets.
    The transcriber parses the pkt-values differently dependent on if they the
    individual dp contents are bits, counters, timestamps, etc.

    In a DNP3 pkt parse by pyshark, i.e., parsed by tshark -> xml -> python
    these cannot simply be accessed through {addr -> value}
    But the address field is stored rather independent of the value

    If one does not want to parse the binary little-endian entries into whatever their value would be,
    one must access the tshark-parsed values through lists; 1 list for each datatype (binary, counter, etc.)

    We apply indexes to ensure cohesion between and per address block
        that is included in the pkt.
    """

    data_obj_main_index: int = 0
    start_stop_index: int = 0
    prefixed_objects_index: int = 0
    next_prefixed_obj_index: int = 0

    biq_7_index: int = 0
    counter_index: int = 0
    bit_index: int = 0
    ts_index: int = 0
    time_delay_index: int = 0

    def index_for_value_field(self, val_field: _ObjectValueFields) -> int:
        """
        Retrieves current index-state for an object's value field

        :param val_field: Type of Val field to know the state's index for
        :return: current index for list of values for the resp. type
        """
        if val_field == _ObjectValueFields.BINARY:
            return self.biq_7_index
        if val_field == _ObjectValueFields.COUNTER:
            return self.counter_index
        if val_field == _ObjectValueFields.BIT:
            return self.bit_index
        if val_field == _ObjectValueFields.STRING_TS:
            return self.ts_index
        if val_field == _ObjectValueFields.TIME_DELAY:
            return self.time_delay_index
        raise ValueError(f"Unknown {val_field=}")

    def increment_val_field_index(self, val_field: _ObjectValueFields):
        """Incrementing must be performed each value that is read!"""
        if val_field == _ObjectValueFields.BINARY:
            self.biq_7_index += 1
        elif val_field == _ObjectValueFields.COUNTER:
            self.counter_index += 1
        elif val_field == _ObjectValueFields.BIT:
            self.bit_index += 1
        elif val_field == _ObjectValueFields.STRING_TS:
            self.ts_index += 1
        elif val_field == _ObjectValueFields.TIME_DELAY:
            self.time_delay_index += 1
        else:
            raise ValueError(f"Unknown {val_field=}")


class _SignalKeys(str, Enum):
    SIGNAL_TARGET = "Signal Target"


class SpecialUseAddresses(IntEnum):
    # In Outstation replies, IIN1.0 stands for "Broadcast Msg rcvd"
    # and must only be reset according to Table 4-13
    # See 9.2.5.2
    BROADCAST_OPTIONAL_CONFIRM = 0xFFFF
    BROADCAST_SHALL_CONFIRM = 0xFFFE
    BROADCAST_DONT_CONFIRM = 0xFFFD
    SELF_ADDRESS = 0xFFFC

    @staticmethod
    def is_reserved_special_use_addr(addr: int) -> bool:
        return 0xFFF0 <= addr <= 0xFFFB

    @staticmethod
    def is_broadcast_addr(addr: int) -> bool:
        return addr in (
            SpecialUseAddresses.BROADCAST_DONT_CONFIRM,
            SpecialUseAddresses.BROADCAST_SHALL_CONFIRM,
            SpecialUseAddresses.BROADCAST_OPTIONAL_CONFIRM,
        )
