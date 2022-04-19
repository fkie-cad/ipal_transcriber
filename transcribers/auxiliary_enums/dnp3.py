from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum, Enum

from transcriber import settings as settings
from transcriber.messages import Activity


class _FunctionCodes(IntEnum):
    """
    Function codes are the identifier of what general action
    the remaining contents of the pkt are for.

    Names are as in Table 4-2

    Fully supported function codes are noted in the Readme.md

    Any FC which is marked as one of: obsolete, reserved, deprecated
        is supported in properties other than those that check if a fc
        actually is obsolete etc.
    """

    # 4.4.1
    CONFIRM = 0x0

    # 4.4.2
    READ = 0x1

    # 4.4.3
    WRITE = 0x2

    # 4.4.4
    # Function code 3 should not occur in TCP/UDP transmissions
    # ref. 9.2.6.3, 13.2.1.1
    SELECT = 0x3
    OPERATE = 0x4

    # 4.4.5
    DIRECT_OPERATE = 0x5
    DIRECT_OPERATE_NR = 0x6

    # 4.4.6
    IMMED_FREEZE = 0x07
    IMMED_FREEZE_NR = 0x08
    # 4.4.7
    FREEZE_CLEAR = 0x9
    FREEZE_CLEAR_NR = 0xA
    # 4.4.8
    FREEZE_AT_TIME = 0xB
    FREEZE_AT_TIME_NR = 0xC

    # 4.4.9
    COLD_RESTART = 0x0D
    WARM_RESTART = 0x0E

    # 4.4.10 ; OBSOLETE
    # INITIALIZE_DATA = 0xF

    # 4.4.11
    INITIALIZE_APPL = 0x10
    START_APPL = 0x11
    STOP_APPL = 0x12

    # 4.4.12; DEPRECATED
    # SAVE_CONFIG = 0x13

    # 4.4.13
    ENABLE_UNSOLICITED = 0x14
    DISABLE_UNSOLICITED = 0x15

    # 4.4.14
    ASSIGN_CLASS = 0x16

    # 4.4.15; mostly for non-LAN channels
    DELAY_MEASURE = 0x17

    # 4.4.16; for LAN channels
    RECORD_CURRENT_TIME = 0x18

    # 4.4.17
    OPEN_FILE = 0x19
    CLOSE_FILE = 0x1A
    DELETE_FILE = 0x1B
    ABORT_FILE = 0x1E

    # 4.4.18
    GET_FILE_INFO = 0x1C

    # 4.4.19
    AUTHENTICATE_FILE = 0x1D

    # 4.4.20
    ACTIVATE_CONFIG = 0x1F

    # 4.4.21
    AUTHENTICATE_REQ = 0x20

    # 4.4.22
    AUTH_REQ_NR = 0x21

    # 0x22 to 0x80 are reserved

    # 4.4.23 (false entry in Table 4-2)
    RESPONSE = 0x81

    # 4.4.24
    UNSOLICITED_RESPONSE = 0x82

    # 4.4.25
    # I find the name can be a bit mislead
    # With "response" they simply signify, that this is solely
    # send by the outstation and upon finding that e.g. a select ASDU must be authenticated
    # to be actually performed
    # the "response" then "requests" an authentication challenge to be solved
    # a masters "Authentication Request" ASDU (0x20) thus means that the master wishes
    # to be authenticated by the outstation w/ the challenge-response provided in his answer
    # The request/response naming must be separated from the objects actually contained
    # since the outstation might also need to authenticate itself to the master w/e using this FC
    #   (e.g. Table 7-4 Aggr. Mode request)
    AUTHENTICATE_RESP = 0x83

    # remaining 0x84 to 0xFF are reserved

    @property
    def always_requires_response(self) -> bool:
        """
        Even if an outstation does not support the resp. function code/ the func. for a given object,
            it should still response but just with the IIN2.0 [NO_FUNC_CODE_SUPPORT] bit set. (c.f. 4.5.9)
        This might *not* occur for function codes for which no response should occur (e.g. IMMED_FREEZE_NR)

        Note: except for 0x10-0x12 fully implemented
        """
        return self in (
            _FunctionCodes.READ,
            _FunctionCodes.WRITE,
            # Select response by outstation will only be responded to
            # if no error occurred during either select req/resp transmission
            _FunctionCodes.SELECT,
            # see ex. 4.4.4.4; the operate msg. response is
            # either the standard copy of the operate req. msg (if successful)
            # or an error msg.
            _FunctionCodes.OPERATE,
            _FunctionCodes.DIRECT_OPERATE,
            _FunctionCodes.IMMED_FREEZE,
            _FunctionCodes.FREEZE_CLEAR,
            _FunctionCodes.FREEZE_AT_TIME,
            _FunctionCodes.COLD_RESTART,
            _FunctionCodes.WARM_RESTART,
            # not clear from 4.4.11 if 0x10 - 0x12 always need a response
            _FunctionCodes.ENABLE_UNSOLICITED,
            _FunctionCodes.DISABLE_UNSOLICITED,
            _FunctionCodes.ASSIGN_CLASS,
            _FunctionCodes.DELAY_MEASURE,
            _FunctionCodes.RECORD_CURRENT_TIME,
            # c.f. 4.4.17.{1,2}.2; §2...
            _FunctionCodes.OPERATE,
            _FunctionCodes.CLOSE_FILE,
            _FunctionCodes.DELETE_FILE,
            _FunctionCodes.ABORT_FILE,
            _FunctionCodes.GET_FILE_INFO,
            _FunctionCodes.AUTHENTICATE_FILE,
            _FunctionCodes.ACTIVATE_CONFIG,
            # According to 4.6.4, all unsolicited responses shall set
            # the CON bit and thereby request AL-confirmation; 4.6.6 Rule 6
            _FunctionCodes.UNSOLICITED_RESPONSE,
        )

    @property
    def should_never_be_responded_to(self) -> bool:
        """
        Identifies FCs for which a direct response *shall never* be send

        Note: Except for unclear things regarding 0x0, fully implemented
        Note 2: In case that Authentication is required *and* that
            no aggressive authentication mode is deployed,
            all of those below except AUTH_REQ_NR  can (and in the case of DIRECT_OPERATE_NR *must()
            require an authentication response from the outstation first.
        Therefore, the return value assumes no authentication is deployed
            c.f. Table 7-7, 7.5.2.3.2
        """
        return self in (
            # Not sure if Confirmation must never be responded to since some execution flows
            # are over multiple pkt (e.g., select & operate)
            # Actually not sure what occurs if one would send the NR
            # versions w/ a BROADCAST_SHALL_CONFIRM address
            # which would take precedence? (Doesn't occur in QUT-DNP3)
            _FunctionCodes.IMMED_FREEZE_NR,
            _FunctionCodes.FREEZE_CLEAR_NR,
            _FunctionCodes.FREEZE_AT_TIME_NR,
            _FunctionCodes.DIRECT_OPERATE_NR,
            _FunctionCodes.AUTH_REQ_NR,
        )

    @property
    def response_is_optional(self) -> bool:
        """
        Identifies FCs for which a response *may* be send

        Note: Except for unclear things regarding 0x0, 0x81 fully implemented
        """
        return self in (
            # for failures, the challenger may choose not to reply
            # e.g. to protect again DoS attacks (c.f. 7.4.1.5, Fig. 7-4)
            _FunctionCodes.AUTHENTICATE_RESP,
            # In the case of aggressive mode request which fails the authentication
            # and maximum error count already exceeded, the challenger may not
            # send an auth-error pkg (c.f. Fig. 7-6)
            _FunctionCodes.AUTHENTICATE_REQ,
            # example of both confirmed and not-confirmed response: 4.4.18  Ex 4-33
            # unconfirmed responses often are "null-responses" which serve a similar
            # function to confirmation *but* also contain the internal indication bits
            _FunctionCodes.RESPONSE,
        )

    @property
    def msg_type_is_request(self) -> bool:
        # As defined in Table 4-2
        # Is the "Message Type" further defined somewhere?
        return 1 <= self <= 0x80

    @property
    def msg_type(self) -> _DnpMsgType:
        if self == _FunctionCodes.CONFIRM:
            return _DnpMsgType.CONFIRMATION
        if 1 <= self <= 0x80:
            return _DnpMsgType.REQUEST
        return _DnpMsgType.RESPONSE

    @property
    def data_contains_no_individual_obj(self) -> bool:
        """
        True iff function code is for pure signaling behaviour,
        contains no further data other than (potentially) object group headers

        Can still be command though, e.g., Immediate freeze

        Note: this function is fully implemented
        """
        return self in (
            _FunctionCodes.CONFIRM,
            # *NOT* FREEZE_AT_TIME; that will contain a g50v2 obj!
            _FunctionCodes.IMMED_FREEZE,
            _FunctionCodes.IMMED_FREEZE_NR,
            _FunctionCodes.FREEZE_CLEAR,
            _FunctionCodes.FREEZE_CLEAR_NR,
            _FunctionCodes.COLD_RESTART,
            _FunctionCodes.WARM_RESTART,
            _FunctionCodes.DELAY_MEASURE,
            _FunctionCodes.RECORD_CURRENT_TIME,
        )

    @property
    def contains_no_data(self) -> bool:
        """
        True iff the fc is never used w/ even an object group header

        c.f. Table 12-64
        """
        return (
            self
            in (
                _FunctionCodes.CONFIRM,
                _FunctionCodes.DELAY_MEASURE,
                _FunctionCodes.RECORD_CURRENT_TIME,
            )
            or self.is_for_restart
        )

    @property
    def is_reserved(self) -> bool:
        return 0x22 <= self <= 0x80 or 0x84 <= self <= 0xFF

    @property
    def obsolete_or_deprecated(self) -> bool:
        return self in (0x13, 0xF)

    @property
    def is_for_file_operation(self) -> bool:
        return self in (
            _FunctionCodes.OPEN_FILE,
            _FunctionCodes.CLOSE_FILE,
            _FunctionCodes.ABORT_FILE,
            _FunctionCodes.DELETE_FILE,
        )

    @property
    def is_for_freeze(self) -> bool:
        return self in (
            _FunctionCodes.IMMED_FREEZE,
            _FunctionCodes.IMMED_FREEZE_NR,
            _FunctionCodes.FREEZE_CLEAR,
            _FunctionCodes.FREEZE_CLEAR_NR,
        )

    @property
    def is_for_application(self) -> bool:
        return self in (
            _FunctionCodes.INITIALIZE_APPL,
            _FunctionCodes.START_APPL,
            _FunctionCodes.STOP_APPL,
        )

    @property
    def is_for_restart(self) -> bool:
        return self in (
            _FunctionCodes.COLD_RESTART,
            _FunctionCodes.WARM_RESTART,
        )

    @property
    def is_for_select_or_type_of_operate(self) -> bool:
        return self in (
            _FunctionCodes.SELECT,
            _FunctionCodes.OPERATE,
            _FunctionCodes.DIRECT_OPERATE,
            _FunctionCodes.DIRECT_OPERATE_NR,
        )

    @property
    def is_for_channel_time_measurement(self) -> bool:
        return self in (
            _FunctionCodes.DELAY_MEASURE,
            _FunctionCodes.RECORD_CURRENT_TIME,
        )

    @property
    def is_for_authentication(self) -> bool:
        return self in (
            _FunctionCodes.AUTHENTICATE_FILE,
            _FunctionCodes.AUTHENTICATE_RESP,
            _FunctionCodes.AUTHENTICATE_REQ,
            _FunctionCodes.AUTH_REQ_NR,
        )

    @property
    def is_for_mod_unsolicited_responses(self) -> bool:
        return self in (
            _FunctionCodes.ENABLE_UNSOLICITED,
            _FunctionCodes.DISABLE_UNSOLICITED,
        )

    def get_activity(self) -> Activity:
        if self == _FunctionCodes.CONFIRM:
            return Activity.CONFIRMATION

        # check if these also could be send by outstation for some reason - don't think so
        # but whatever...
        if self in (
            _FunctionCodes.READ,
            _FunctionCodes.GET_FILE_INFO,
            # Send by the master to request a temporary (single-transaction)
            # authentication key for opening or deleting a file;
            # I thereby interpret it as "Request for Data" which is the
            # description of Interrogate activity;
            # Nonetheless, the master needs to submit user, pw etc.
            # in his key-request
            _FunctionCodes.AUTHENTICATE_FILE,
        ):
            return Activity.INTERROGATE

        if (
            self
            in (
                _FunctionCodes.WRITE,
                _FunctionCodes.ASSIGN_CLASS,
                _FunctionCodes.ACTIVATE_CONFIG,
            )
            or self.is_for_file_operation
            or self.is_for_application
            or self.is_for_freeze
            or self.is_for_restart
            or self.is_for_select_or_type_of_operate
            or self.is_for_channel_time_measurement
            or self.is_for_mod_unsolicited_responses
        ):
            return Activity.COMMAND

        if self in (
            _FunctionCodes.RESPONSE,
            _FunctionCodes.UNSOLICITED_RESPONSE,
        ):
            # Can be either inform or action
            # c.f. Table 12-33 ff.
            # Since a response can be a null response both for read
            # and command actions, it is necessary to assign the activity
            # *later* by trying to match sequence numbers between response &
            # request
            # but for unsolicited response, the activity can be read from
            # its content; an unsolicited response should never be a real none
            # response with no error bits etc. set
            return Activity.UNKNOWN

        if self == _FunctionCodes.AUTHENTICATE_REQ:
            # Could be interrogation (e.g. Key status request)
            # or command (e.g., Key Change) c.f. Table 7-3
            # Activity is defined by the object contained.
            return Activity.UNKNOWN

        if self == _FunctionCodes.AUTHENTICATE_RESP:
            # same argumentation as above, since this fc is
            # used for both the interrogation-style & command-style
            # authentication request ASDUs
            return Activity.UNKNOWN

        if self == _FunctionCodes.AUTH_REQ_NR:
            # Its full use not yet clearly understood by me
            return Activity.UNKNOWN

        return Activity.UNKNOWN


class _ObjectTypes(str, Enum):
    """
    As defined in 11.5;
    they broadly divide objects based on what they represent, what role they play
    """

    ATTRIBUTE = "Attribute Type"
    EVENT = "Event Type"
    STATIC = "Static Type"
    COMMAND = "Command Type"
    DEADBAND = "Deadband Type"
    STATUS = "Status Type"
    INFORMATION = "Information Type"


class _ObjectValueFields(str, Enum):
    """
    Strings that represent pdml-xml's keys for accessing
        the value already parsed by tshark
    These are *not* unique per group!
    """

    BINARY = "al_biq_b7"
    COUNTER = "al_cnt"
    BIT = "al_bit"
    STRING_TS = "al_timestamp"
    TIME_DELAY = "al_time_delay"


class _CastingTypes(Enum):
    """
    Internal transcriber identifiers for how
        values from an object value field should be casted in python.

    One cannot generally access the pdml-xml value in the final
        datatype/ format in which it should be stored in IPAL
    """

    INT = "ints"
    FLOAT = "floats"
    STRING = "string"

    # use int(field.show) because .int_value for some reason
    # throws "nonetype' error' in some cases
    INT_THROUGH_SHOW = "int through show"
    TS_48_BIT_TO_SEC_MS = "raw 48-bit ts to seconds.float"
    MILLI_S_TS = "millisecond time"


class _ObjectGroups(IntEnum):
    """
    Object Groups as represented in DNP3;
    Each group represents a collection of "objects", certain types of input-dps, internal counters, time-stamps, etc.

    If a "frozen" version for group-id=x exists, the frozen version is addressed as x+1
    One example of use of frozen registers is to perform a cmd/ read synchronously across multiple outstations
    and then read the frozen registers while the outstation's normal operation can continue on the normal registers.

    Similarly, if a group x exists with an "event" group as well, the latter will be x+1

    Special cases are represented by:
    - group ID 60, which references an outstation's internal 4 sets of objects
        which were manually assigned to one (?or more?) of these classes.

    - group ID 0: device attributes, such as: names, supported security parameters, support for specific sub-groups,
        - maximum per-group index controllable by station (may not be equal to the resp. #dps)
        - #per-group points controllable by the station
        - supported group-id variations (~ value-formats, size (16 bit vs. 32 bit), additional info)
        ...

    Commented out are those not yet supported at all

    """

    # DEVICE_ATTRIBUTES = 0

    BINARY_INPUT = 1
    BINARY_INPUT_EVENT = 2

    # Double bit binary = On, off, in-transit states
    # DOUBLE_BIT_BINARY_INPUT = 3
    # DOUBLE_BIT_BINARY_INPUT_EVENT = 4

    # BINARY_OUTPUT = 10
    # BINARY_OUTPUT_EVENTS = 11
    # BINARY_OUTPUT_COMMAND = 12
    # BINARY_OUTPUT_COMMAND_EVENTS = 13

    COUNTER = 20
    # FROZEN_COUNTER = 21
    # COUNTER_EVENT = 22
    # FROZEN_COUNTER_EVENT = 23

    # ANALOG_INPUT = 30
    # FROZEN_ANALOG_INPUT = 31
    # ANALOG_INPUT_EVENT = 32
    # FROZEN_ANALOG_INPUT_EVENT = 33
    # ANALOG_INPUT_REPORTING_DEADBAND = 34

    # ANALOG_OUTPUT_STATUS = 40
    # ANALOG_OUTPUT = 41
    # ANALOG_OUTPUT_EVENT = 42
    # ANALOG_OUTPUT_COMMAND_EVENT = 43

    TIME_AND_DATE = 50
    # TIME_AND_DATE_COMMON_TIME_OF_OCCURRENCE = 51
    TIME_DELAYS = 52

    CLASS_OBJECTS = 60

    # FILE_CONTROL = 70

    INTERNAL_INDICATIONS = 80
    # DEVICE_STORAGE = 81
    # DEVICE_PROFILES = 82
    # DATA_SET = 83
    # DATA_SET_PROTOTYPE = 85
    # DATA_SET_DESCRIPTOR = 86
    # DATA_SET_PRESENT_VALUE = 87
    # DATA_SET_EVENT = 88

    # APPLICATION = 90
    # STATUS_OF_REQ_OPERATION = 91

    # FLOATING_POINT = 100
    # BINARY_CODED_DECIMAL_INT = 101
    # UNSIGNED_INT = 102

    # OCTET_STRING = 110
    # OCTET_STRING_EVENT = 111

    # VIRTUAL_TERMINAL_OUTPUT_BLOCK = 112
    # VIRTUAL_TERMINAL_EVENT_DATA = 113

    # AUTHENTICATION = 120
    # SECURITY_STATISTICS = 121
    # SECURITY_STATISTIC_EVENTS = 122

    @property
    def obj_type(self):
        return {
            _ObjectGroups.BINARY_INPUT: _ObjectTypes.STATIC,
            _ObjectGroups.BINARY_INPUT_EVENT: _ObjectTypes.EVENT,
            _ObjectGroups.COUNTER: _ObjectTypes.STATIC,
            _ObjectGroups.TIME_AND_DATE: _ObjectTypes.INFORMATION,
            _ObjectGroups.TIME_DELAYS: _ObjectTypes.INFORMATION,
            _ObjectGroups.CLASS_OBJECTS: _ObjectTypes.INFORMATION,
            _ObjectGroups.INTERNAL_INDICATIONS: _ObjectTypes.STATIC,
        }[self]

    @property
    def value_field(self) -> _ObjectValueFields:
        """
        Returns the identifier of the field in which the points *main* value
            is stored.

        Note: secondary values, such as timestamps that *may* be added in some
            variations are not returned.
        """
        if self in (1, 2):
            return _ObjectValueFields.BINARY
        if self in (20,):
            return _ObjectValueFields.COUNTER
        if self in (50,):
            return _ObjectValueFields.STRING_TS
        if self in (52,):
            return _ObjectValueFields.TIME_DELAY
        if self in (80,):
            return _ObjectValueFields.BIT
        raise NotImplementedError(f"Value field for group {self} not known.")

    @property
    def use_special_data_parser(self) -> bool:
        return self == _ObjectGroups.TIME_AND_DATE

    @property
    def point_type(self) -> _PointType:
        if self in (1, 2):
            return _PointType.SINGLE_BIT_BINARY_INPUT

        if self in (3, 4):
            return _PointType.DOUBLE_BIT_BINARY_INPUT

        if 10 <= self <= 13:
            return _PointType.BINARY_OUTPUT

        if 20 <= self <= 23:
            return _PointType.COUNTER

        if 30 <= self <= 34:
            return _PointType.ANALOG_INPUT

        if 40 <= self <= 43:
            return _PointType.ANALOG_OUTPUT

        if 50 <= self <= 52:
            # Time-objects
            return _PointType.HAS_NO_POINT_TYPE

        if self == 101:
            return _PointType.BCD

        if self in (110, 111):
            return _PointType.OCTET_STRING

        if self in (112, 113):
            return _PointType.VIRTUAL_TERMINAL

        if self in (121, 122):
            return _PointType.SECURITY_STATISTICS

    @property
    def activity_in_response(self) -> Activity:
        """

        Note: Considering "reporting present value" of outputs
            as inform activity, even though the point's main
            function is not monitoring (which would be an input dp)

        Note 2: The CHATTER_FILTER Flag (Table 11-5)
            is assumed either *not set* or interpreted as not having
            an influence on the activity chosen.
            Issue: Events can be generated once a flag changes and the
                chatter filter signifies that the outstation by itself
                decides to not send new updates for each input/output change
                because the frequency of these changes got too high.
                The event (and event-including pkt) generated once
                the chatter filter is set or cleared
                therefor can be interpreted as ACTION Activity
                (Does not occur in QUT-DNP3 to my knowledge)

            For the ONLINE Flag, the analysis becomes on the one side
                more complicated, since we cannot know from this pkt
                what caused a change in the flag.
                Since we have a variety of causes, there is an argument
                to be made that this flag is a pure "monitoring" flag
                stating whether or whether not the resp. point
                is available for use.

        :return: Activity a != UNKNOWN if this obj. group can be given
                this activity independent of other data in an outstation's response
        """
        if self.point_type in (
            _PointType.ANALOG_INPUT,
            _PointType.SINGLE_BIT_BINARY_INPUT,
            _PointType.DOUBLE_BIT_BINARY_INPUT,
            _PointType.SECURITY_STATISTICS,
            # These are *not* returned after
            # Freeze counter function code!
            # but must be read/ send as unsol. resp. afterwards
            _PointType.COUNTER,
        ):
            return Activity.INFORM

        elif self.point_type == _PointType.ANALOG_OUTPUT:
            if self == 40:
                return Activity.INFORM
            return Activity.ACTION

        if self.point_type == _PointType.BCD:
            # Not further limited in input/ output direction
            # c.f. 11.9.3.1
            # could be further defined if
            # dataset-metadata is provided
            return Activity.UNKNOWN

        elif self.point_type == _PointType.BINARY_OUTPUT:
            if self == 10:
                # While in *theory* writing to group 10
                # is possible, the standard does not recommend
                # it bc. devices may not support this type of operation
                # and the resp. a device would give would not
                # indicate the success of the operation (c.f. 11.9.4.6)
                # therefore assuming that this is used
                # for unsolicited resp./ read-resp
                return Activity.INFORM
            return Activity.ACTION

        if self.point_type == _PointType.OCTET_STRING:
            # can be used for both read & write
            # and... basically whatever the operator
            # wants to do with it
            return Activity.UNKNOWN

        if self.point_type == _PointType.VIRTUAL_TERMINAL:
            if self == 112:
                # Not entirely sure if outsatation
                # ever responds with this obj.
                # not further defined in DNP3
                # but when, it should be action
                return Activity.ACTION
            if self == 113:
                return Activity.INFORM

        if self.point_type == _PointType.HAS_NO_POINT_TYPE:
            if self == _ObjectGroups.TIME_DELAYS:
                # at least when searching for its code "g52",
                # it only comes up as responses for: restarts, save cfg, delay measure
                # these are all commands
                return Activity.ACTION

        settings.logger.warning(
            f"Could not resolve group {self} w/ point type {self.point_type} to any activity/ knowingly set it to UNKNOWN"
        )
        return Activity.UNKNOWN


@dataclass(frozen=True)
class _ObjectHeader:
    """
    A collection of Object Headers is created at the start for each
        object group+var combination existent in the pkt.

    With these it is decided how to retrieve the actual values of points.

    Maybe add qualifier here in future extensions?
    Would allow better parsing of what to expect from the point indexes.

    Note: That a master requests a point in a specific format,
    """

    group: _ObjectGroups
    variation: int
    qual: _Qualifier

    @property
    def casting_type(self) -> _CastingTypes:
        # Anything which is possible to be communicated in a > 1 hex-value field
        # must not be directly interpreted through base16_value
        # because DNP3 transports them packed as little-endian.
        # Linux does not apply little-endian as standard in contrast to Windows.
        if self.group in (
            _ObjectGroups.BINARY_INPUT,
            _ObjectGroups.BINARY_INPUT_EVENT,
            _ObjectGroups.INTERNAL_INDICATIONS,
        ):
            return _CastingTypes.INT
        if self.group == _ObjectGroups.COUNTER:
            return _CastingTypes.INT_THROUGH_SHOW
        if self.group in (_ObjectGroups.TIME_AND_DATE,):
            return _CastingTypes.TS_48_BIT_TO_SEC_MS
        if self.group in (_ObjectGroups.TIME_DELAYS,):
            if self.variation == 1:
                return _CastingTypes.INT_THROUGH_SHOW
            elif self.variation == 2:
                return _CastingTypes.MILLI_S_TS
            else:
                raise ValueError("Bad variation for time-delay gorup")
        raise ValueError(f"casting type not known for {self=}")

    @property
    def main_value_field(self) -> _ObjectValueFields:
        return self.group.value_field

    @property
    def should_contain_single_obj_without_prefix(self) -> bool:
        # Can only hold for group-var combinations for which 0x07 is the only valid qualifier code.
        # For qualifiers, c.f. 4.2.2.7.3
        # For group-var combinations, c.f. Table 12-33 to 12-64
        if self.group == _ObjectGroups.TIME_AND_DATE:
            # c.f. Table 12-55; var 4 timing objects are addressed to actual points
            return self.variation in (1, 2, 3)
        if self.group == _ObjectGroups.TIME_DELAYS:
            # only two variations exist and according to all examples etc.
            # they are never send by the master to outstation by only in reverse direction
            return True
        if self.group == 120:
            # c.f. Table 12-63
            return self.variation in (3, 4)
        return False

    @staticmethod
    def from_index(dnp, i: int) -> "_ObjectHeader":
        """
        :param dnp: packet from which to extract a header
        :param i: the header's index in dnp
        :return: i'th header in dnp
        """
        obj_group_and_var = int(dnp.al_obj.all_fields[i].show, 16)
        qual_prefix = int(dnp.al_objq_prefix.all_fields[i].show)
        qual_range = int(dnp.al_objq_range.all_fields[i].show)
        qual = _Qualifier(qual_prefix, qual_range)
        return _ObjectHeader.from_dnp_obj_header(obj_group_and_var, qual)

    @staticmethod
    def from_dnp_obj_header(obj_main_header: int, qual: _Qualifier) -> "_ObjectHeader":
        """
        :param obj_main_header: DWORD representing the obj header
        :param qual: parsed qualifier octet of this header
        :return: group:var parsed header
        """
        obj_group = obj_main_header // 0x100
        obj_variation = obj_main_header % 0x100
        return _ObjectHeader(_ObjectGroups(obj_group), obj_variation, qual)

    @staticmethod
    def parse_all_headers(dnp) -> dict[int, "_ObjectHeader"]:
        """
        :param dnp: dnp3-pkt
        :return: {index of group in pkt -> obj header}
        """
        if not hasattr(dnp, "al_obj"):
            # null-response
            return {}
        tmp = {
            i: _ObjectHeader.from_index(dnp, i)
            for i in range(len(dnp.al_obj.all_fields))
        }
        return tmp


@dataclass(frozen=True)
class _Qualifier:
    # 3 bits
    obj_prefix_code: int
    # 4 bits
    range_specifier_code: int
    # not keeping track of reserved bit #7

    @staticmethod
    def from_int(n: int, raise_on_reserved_number: bool = False) -> "_Qualifier":
        if n > 0xFF:
            raise ValueError(f"number for qualifier too big: {n}")
        pref = n // 0x10
        _range = n % 0x10
        if raise_on_reserved_number and (pref >= 7 or _range == 0xA or _range >= 0xC):
            raise ValueError(f"Qualifier applies reserved bit: {pref=} {_range=}")
        return _Qualifier(pref, _range)

    @property
    def as_hex_combination(self) -> int:
        return self.obj_prefix_code * 0x10 + self.range_specifier_code

    @property
    def prefixed_with_index(self) -> bool:
        return self.obj_prefix_code in (1, 2, 3)

    @property
    def prefixed_with_obj_size(self) -> bool:
        return self.obj_prefix_code in (4, 5, 6)

    @property
    def packed_without_prefix(self) -> bool:
        return self.obj_prefix_code == 0

    @property
    def range_contains_start_stop_index(self) -> bool:
        return self.range_specifier_code in (0, 1, 2)

    @property
    def range_contains_start_stop_virt_addr(self) -> bool:
        return self.range_specifier_code in (3, 4, 5)

    @property
    def no_range_field(self) -> bool:
        """True iff all values are addressed by this specific code"""
        return self.range_specifier_code == 6

    @property
    def range_contains_obj_count(self) -> bool:
        return self.range_specifier_code in (7, 8, 9)

    @property
    def var_format_and_obj_count(self) -> bool:
        return self.range_specifier_code == 0xB

    @property
    def contains_obj_with_size_unknown_to_receiver(self) -> bool:
        """
        Some objects, e.g., files, will not have a pre-defined size that is known
        to the receiver of the msg.
        """
        # c.f. Table 4-8
        return self.as_hex_combination == 0x5B


class _PointType(str, Enum):
    # 11.9
    # .1
    ANALOG_INPUT = "Analog Input"
    # .2
    ANALOG_OUTPUT = "Analog Output"
    # .3
    BCD = "Binary Coded Decimal"
    # .4
    BINARY_OUTPUT = "Binary Output"
    # .5
    COUNTER = "Counter"
    # .6
    DOUBLE_BIT_BINARY_INPUT = "Double Bit Binary Input"
    # .7
    OCTET_STRING = "Octet String"
    # .8
    SINGLE_BIT_BINARY_INPUT = "Single Bit Binary Input"
    # .9
    VIRTUAL_TERMINAL = "Virtual Terminal"
    # .10
    SECURITY_STATISTICS = "Security Statistics"
    #
    HAS_NO_POINT_TYPE = "Has no Point Type"


class _DnpMsgType(str, Enum):
    # => Master to outstation cmd/interro
    REQUEST = "Request"
    # =>  any Outstation to Master msg
    RESPONSE = "Response"
    # => Master to outstation ACK
    CONFIRMATION = "Confirmation"
