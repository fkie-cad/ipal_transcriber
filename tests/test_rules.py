import pytest

from .conftest import check_with_validation_file
from .conftest import transcriber


RAW_FILES = [
    ("misc/pcaps/cip.pcapng", "cip.ipal", "cip", "misc/rules/minicps.py"),
    (
        "misc/pcaps/nmea0183udp.pcapng",
        "nmea0183udp.ipal",
        "nmea0183udp",
        "misc/rules/nmea.py",
    ),
    ("misc/pcaps/iec450-nmea.pcap", "iec450-nmea.ipal", "iec450", "misc/rules/nmea.py"),
]


@pytest.mark.parametrize("pcap,filename,protocol,rules", RAW_FILES)
def test_transcriber_rules(pcap, filename, protocol, rules):

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
        "--rules",
        rules,
    ]
    errno, stdout, stderr = transcriber(args)
    assert stderr == b"" or b"WARNING:asyncio:Unknown child process" in stderr
    assert errno == 0
    check_with_validation_file(
        filename, stdout.decode("utf-8"), test_transcriber_rules.__name__
    )
