import pytest

from .conftest import check_command_output, check_with_validation_file, transcriber

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
    ("misc/pcaps/cip.pcapng", "cip.state", "cip"),
    ("misc/pcaps/dnp3.pcap", "dnp3.state", "dnp3"),
    ("misc/pcaps/mqtt.pcap", "mqtt.state", "mqtt"),
    ("misc/pcaps/ethercat.pcapng", "ethercat.state", "ethercat"),
    ("misc/pcaps/MAVLink.pcap", "MAVLink.state", "MAVLink"),
    ("misc/pcaps/BR24.pcap.gz", "BR24.state", "Navico-BR24"),
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
        filename, stdout.decode("utf-8"), test_transcriber_combined.__name__
    )
