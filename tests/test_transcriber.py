import pytest

from .conftest import check_command_output, check_with_validation_file, transcriber


def test_transcriber_empty():
    expected_stderr = [
        (
            b"ERROR:ipal-transcriber:Use either --pcap or "
            b"--interface to indicate source of transcribed traffic\n"
        )
    ]
    args = []
    errno, stdout, stderr = transcriber(args)
    check_command_output(
        errno, args, stdout, stderr, expectedcode=1, expected_stderr=expected_stderr
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
    ("misc/pcaps/mqtt.pcap", "mqtt.ipal", "mqtt"),
    ("misc/pcaps/ethercat.pcapng", "ethercat.ipal", "ethercat"),
    ("misc/pcaps/MAVLink.pcap", "mavlink.ipal", "MAVLink"),
    ("misc/pcaps/BR24.pcap.gz", "BR24.ipal", "Navico-BR24"),
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
        filename, stdout.decode("utf-8"), test_transcriber_raw.__name__
    )


@pytest.mark.parametrize("pcap", [x[0] for x in RAW_FILES])
def test_transcriber_all_protocols(pcap):
    args = [
        "--pcap",
        pcap,
        "--ipal.output",
        "-",
        "--crc",
        "and",
        "--timeout",
        "1000",
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


@pytest.mark.parametrize("pcap,protocol", [(x[0], x[2]) for x in RAW_FILES])
def test_transcriber_all_other_protocols(pcap, protocol):
    all_other_protocols = [x[2] for x in RAW_FILES if not x[2] == protocol]
    args = (
        [
            "--pcap",
            pcap,
            "--protocols",
        ]
        + all_other_protocols
        + [
            "--ipal.output",
            "-",
            "--crc",
            "and",
            "--timeout",
            "1000",
        ]
    )
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
