import pytest

from .conftest import check_with_validation_file
from .conftest import transcriber


def test_transcriber_empty():
    errno, stdout, stderr = transcriber([])
    assert errno == 1
    assert (
        stderr
        == b"ERROR:ipal-transcriber:Use either --pcap or --interface to indicate source of transcribed traffic\n"
    )


RAW_FILES = [
    ("misc/pcaps/iec104.pcap", "iec104.ipal", "iec104"),
    ("misc/pcaps/iec450-nmea.pcap", "iec450-nmea.ipal", "iec450"),
    ("misc/pcaps/modbus.pcap", "modbus.ipal", "modbus"),
    ("misc/pcaps/nmea0183udp.pcapng", "nmea0183udp.ipal", "nmea0183udp"),
    ("misc/pcaps/s7.pcap", "s7.ipal", "s7"),
    ("misc/pcaps/goose-single.pcapng", "goose-single.ipal", "goose"),
    (
        "misc/pcaps/goose-single-schweitz-1.pcap",
        "goose-single-schweitz-1.ipal",
        "goose",
    ),
    ("misc/pcaps/cip.pcapng", "cip.ipal", "cip"),
    ("misc/pcaps/dnp3.pcap", "dnp3.ipal", "dnp3"),
]


@pytest.mark.parametrize("pcap,filename,protocol", RAW_FILES)
def test_transcriber_raw(pcap, filename, protocol):

    args = [
        "--pcap",
        pcap,
        "--protocol",
        protocol,
        "--ipal.output",
        "-",
        "--crc",
        "and",
        "--timeout",
        "1000",
    ]
    errno, stdout, stderr = transcriber(args)
    assert stderr == b"" or b"WARNING:asyncio:Unknown child process" in stderr
    assert errno == 0
    check_with_validation_file(
        filename, stdout.decode("utf-8"), test_transcriber_raw.__name__
    )
