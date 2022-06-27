import pytest

from .conftest import check_with_validation_file
from .conftest import transcriber

RAW_FILES = [
    ("misc/pcaps/iec104.pcap", "iec104.state", "iec104"),
    ("misc/pcaps/iec450-nmea.pcap", "iec450-nmea.state", "iec450"),
    ("misc/pcaps/modbus.pcap", "modbus.state", "modbus"),
    (
        "misc/pcaps/nmea0183udp.pcapng",
        "nmea0183udp.state",
        "nmea0183udp",
    ),
    ("misc/pcaps/s7.pcap", "s7.state", "s7"),
]


@pytest.mark.parametrize("pcap,filename,protocol", RAW_FILES)
def test_transcriber_combined(pcap, filename, protocol):
    args = [
        "--pcap",
        pcap,
        "--protocol",
        protocol,
        "--crc",
        "and",
        "--state.output",
        "-",
        "default",
    ]
    errno, stdout, stderr = transcriber(args)
    assert stderr == b"" or b"WARNING:asyncio:Unknown child process" in stderr
    assert errno == 0
    check_with_validation_file(
        filename, stdout.decode("utf-8"), test_transcriber_combined.__name__
    )
