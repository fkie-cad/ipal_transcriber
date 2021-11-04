from pathlib import Path

import pyshark

import transcriber.settings as settings
from transcribers.iec450 import IEC450Transcriber
from transcribers.utils import IpalIdCounter


def get_dhcp_packet():
    capture = pyshark.FileCapture(
        input_file=str(
            Path(__file__).parent.parent.parent / "misc/pcaps/dhcp-single.pcapng"
        ),
        keep_packets=False,
        custom_parameters=settings.pyshark_options,
    )
    capture.load_packets()
    packet = capture.next_packet()
    return packet


def test_does_not_match_dhcp_packet():
    packet = get_dhcp_packet()
    transcriber = IEC450Transcriber(IpalIdCounter())
    assert not transcriber.matches_protocol(packet)
