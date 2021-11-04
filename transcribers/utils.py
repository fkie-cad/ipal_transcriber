import threading

from transcribers.cip import CIPTranscriber
from transcribers.goose import GooseTranscriber
from transcribers.iec104 import IEC104Transcriber
from transcribers.iec450 import IEC450Transcriber
from transcribers.modbus import ModbusTranscriber
from transcribers.nmea0183 import NMEA0183UDPTranscriber
from transcribers.s7 import S7Transcriber


class IpalIdCounter:
    # Used to assign a uniqe ID to each message. These IDs are used
    # e.g. as references for responses.

    def __init__(self):
        self._id = 0
        self._threadLock = threading.Lock()

    def get_next_id(self):
        with self._threadLock:
            res = self._id
            self._id += 1
        return res


# Keep list up-to-date with all implemented transcribers!
all_transcribers = [
    CIPTranscriber,
    GooseTranscriber,
    IEC104Transcriber,
    IEC450Transcriber,
    ModbusTranscriber,
    NMEA0183UDPTranscriber,
    S7Transcriber,
]


def get_all_transcribers():
    return {transcriber._name: transcriber for transcriber in all_transcribers}
