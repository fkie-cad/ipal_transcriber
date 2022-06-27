import pytest

from .conftest import check_with_validation_file
from .conftest import extractor


def test_extractor_empty():
    errno, stdout, stderr = extractor([])
    assert errno == 1
    assert stderr == b"ERROR:ipal-state-extractor:Define a state_extractor!\n"


RAW_FILES = [
    ("misc/ipal/iec104.ipal", "iec104.state"),
    ("misc/ipal/iec450-nmea.ipal", "iec450-nmea.state"),
    ("misc/ipal/modbus.ipal", "modbus.state"),
    ("misc/ipal/nmea0183udp.ipal", "nmea0183udp.state"),
    ("misc/ipal/s7.ipal", "s7.state"),
]


@pytest.mark.parametrize("ipal,filename", RAW_FILES)
def test_extractor_default(ipal, filename):

    args = ["--ipal.input", ipal, "--state.output", "-", "default"]
    errno, stdout, stderr = extractor(args)
    assert stderr == b"" or b"WARNING:asyncio:Unknown child process" in stderr
    assert errno == 0
    check_with_validation_file(
        filename, stdout.decode("utf-8"), test_extractor_default.__name__
    )
