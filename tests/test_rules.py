import pytest

from .conftest import check_command_output, check_with_validation_file, transcriber

RAW_FILES = [
    ("misc/pcaps/cip.pcapng", "cip.ipal", "cip", "misc/rules/minicps.py"),
    (
        "misc/pcaps/nmea0183udp.pcapng",
        "nmea0183udp.ipal",
        "nmea0183udp",
        "misc/rules/nmea.py",
    ),
    ("misc/pcaps/iec450-nmea.pcap", "iec450-nmea.ipal", "iec450", "misc/rules/nmea.py"),
    (
        "misc/pcaps/MAVLink.pcap",
        "mavlink.ipal",
        "MAVLink",
        "misc/rules/mavlink_common.py",
    ),
    ("misc/pcaps/BR24.pcap.gz", "BR24.ipal", "Navico-BR24", "misc/rules/br24.py"),
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

    expected_stderr = [
        b"",
        r"WARNING:asyncio:Unknown child process pid \d+, will report returncode 255\n?",
    ]

    check_command_output(
        errno,
        args,
        stdout,
        stderr,
        expectedcode=0,
        expected_stderr=expected_stderr,
        check_for=["ERROR"],
    )
    check_with_validation_file(
        filename, stdout.decode("utf-8"), test_transcriber_rules.__name__
    )
