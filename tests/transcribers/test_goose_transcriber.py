import json
from pathlib import Path

import pyshark
import pytest
from pyshark.packet.fields import LayerField

import transcriber.settings as settings
from tests.conftest import check_with_validation_file
from transcribers.goose import (
    GooseTranscriber,
    UnknownValueTypeException,
    TimeQuality,
    Quality,
)
from transcribers.utils import IpalIdCounter


def get_goose_packet(pcapfile):
    capture = pyshark.FileCapture(
        input_file=str(
            Path(__file__).parent.parent.parent / "misc" / "pcaps" / pcapfile
        ),
        keep_packets=False,
        custom_parameters=settings.pyshark_options,
    )
    capture.load_packets()
    packet = capture.next_packet()
    return packet


def test_parse_packet():
    packet = get_goose_packet("goose-single.pcapng")
    goose_transcriber = GooseTranscriber(IpalIdCounter())

    ipalmessages = goose_transcriber.parse_packet(packet)
    assert len(ipalmessages) == 1
    check_with_validation_file(
        "goose-single.ipal",
        json.dumps(ipalmessages[0].export_json()),
        test_parse_packet.__name__,
    )


def test_parse_different_packet():
    packet = get_goose_packet("goose-single-schweitz-1.pcap")
    goose_transcriber = GooseTranscriber(IpalIdCounter())

    ipalmessages = goose_transcriber.parse_packet(packet)
    assert len(ipalmessages) == 1
    check_with_validation_file(
        "goose-single-schweitz-1.ipal",
        json.dumps(ipalmessages[0].export_json()),
        test_parse_packet.__name__,
    )


def test_parse_incompatible_int_packet():
    packet = get_goose_packet("goose-single-incompatible-int.pcap")
    goose_transcriber = GooseTranscriber(IpalIdCounter())

    ipalmessages = goose_transcriber.parse_packet(packet)
    assert len(ipalmessages) == 1
    check_with_validation_file(
        "goose-single-incompatible-int.ipal",
        json.dumps(ipalmessages[0].export_json()),
        test_parse_incompatible_int_packet.__name__,
    )


def test_parse_float():
    assert GooseTranscriber.parse_float(b"\x08\x43\x73\x28\xf8") == 243.1600341796875


def test_parse_float_invalid_first_byte():
    with pytest.raises(NotImplementedError):
        GooseTranscriber.parse_float(b"\x09\x43\x73\x28\xf8")


def test_parse_bitstring():
    assert GooseTranscriber.parse_bitstring(b"\x07\x43\x73\x80") == "01000011011100111"


def test_to_value_unknown():
    goose_transcriber = GooseTranscriber(IpalIdCounter())
    layer_field = LayerField("some-field", "some field (11)")
    with pytest.raises(UnknownValueTypeException):
        goose_transcriber.to_value(layer_field)


def test_parse_utc_time():
    assert (
        GooseTranscriber.parse_utc_time(b"\x4f\x6c\x2e\x60\x4a\x58\x0d\x9f")
        == 1332489824.290406
    )


def test_parse_utc_time_ignores_last_byte():
    assert GooseTranscriber.parse_utc_time(
        b"\x4f\x6c\x2e\x60\x4a\x58\x0d\x9f"
    ) == GooseTranscriber.parse_utc_time(b"\x4f\x6c\x2e\x60\x4a\x58\x0d\x01")


def test_parse_utc_time_quality():
    assert GooseTranscriber.parse_utc_time_quality(
        b"\x4f\x6c\x2e\x60\x4a\x58\x0d\x9f"
    ) == TimeQuality(
        leap_second_known=True,
        clock_failure=False,
        clock_not_synchronized=False,
        time_accuracy_of_fractions_of_second=None,
    )


def test_parse_quality():
    assert GooseTranscriber.parse_quality(b"\x03\xff\xff") == Quality(
        validity="Questionable",
        overflow=True,
        out_of_range=True,
        bad_reference=True,
        oscillatory=True,
        failure=True,
        old_data=True,
        inconsistent=True,
        inaccurate=True,
        source="Substituted",
        test=True,
        operator_blocked=True,
        raw_bitstring="1111111111111",
    )


def test_parse_bitstring_quality():
    assert GooseTranscriber.parse_bitstring(b"\x03\xff\xff") == "1111111111111"
