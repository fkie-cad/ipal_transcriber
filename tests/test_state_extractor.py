import pytest

from .conftest import check_command_output, check_with_validation_file, extractor


def test_extractor_empty():
    args = []
    errno, stdout, stderr = extractor(args)

    expected_stderr = [b"ERROR:ipal-state-extractor:Define a state_extractor!\n"]

    check_command_output(
        errno, args, stdout, stderr, expectedcode=1, expected_stderr=expected_stderr
    )


RAW_FILES = [
    ("misc/ipal/iec104.ipal", "iec104.state"),
    ("misc/ipal/iec450-nmea.ipal", "iec450-nmea.state"),
    ("misc/ipal/modbus.ipal", "modbus.state"),
    ("misc/ipal/nmea0183udp.ipal", "nmea0183udp.state"),
    ("misc/ipal/s7.ipal", "s7.state"),
    ("misc/ipal/cip.ipal", "cip.state"),
    ("misc/ipal/dnp3.ipal", "dnp3.state"),
    ("misc/ipal/mqtt.ipal", "mqtt.state"),
    ("misc/ipal/ethercat.ipal", "ethercat.state"),
    ("misc/ipal/MAVLink.ipal", "MAVLink.state"),
    ("misc/ipal/BR24.ipal.gz", "BR24.state"),
]


@pytest.mark.parametrize("ipal,filename", RAW_FILES)
def test_extractor_default(ipal, filename):
    args = ["--ipal.input", ipal, "--state.output", "-", "default"]
    errno, stdout, stderr = extractor(args)

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
        filename, stdout.decode("utf-8"), test_extractor_default.__name__
    )
