#!/usr/bin/env python3
import socket

import orjson

import transcriber.settings as settings
from transcribers.transcriber import Transcriber
from transcribers.utils import get_all_transcribers


class StateExtractor:
    _name = None
    _description = None
    _options = None

    def __init__(self, args):
        self.transcribers = get_all_transcribers()

        self._state = {}
        self._first = True
        self._warned_protocol = False

    def _get_identifier(self, msg, key):
        try:
            return self.transcribers[msg.protocol].state_identifier(msg, key)
        except KeyError:
            if not self._write_state:
                settings.logger.warning(
                    "Protocol unknown, using default state_identifier"
                )
                self._write_state = True
            return Transcriber.state_identifier(msg, key)

    def _write_state(self, msg, malicious=None, timestamp=None):
        if not settings.stateout:
            return

        # Apply filter if necessary
        state = self._state
        if settings.filter is not None:
            state = {k: v for k, v in state.items() if k in settings.filter}

        # Output only non-empty states
        if len(state) == 0:
            return

        # Output only if state is complete
        if settings.completeonly and settings.filter is not None:
            if len(state) != len(settings.filter):
                return

        # Add output to message or output as state
        if settings.stateinmessage:
            output = msg.export_json()
            output["state"] = state
        else:
            output = {
                "timestamp": timestamp,
                "state": state,
                "malicious": malicious,
            }

        if self._first:
            output["_state_extractor-config"] = (
                settings.state_extractor_settings_to_dict()
            )
            output["_state_extractor-config"]["options"] = self._options
            self._first = False

        if settings.hostname:
            output["hostname"] = socket.gethostname()

        settings.stateoutfd.write(
            orjson.dumps(
                output,
                option=orjson.OPT_SERIALIZE_NUMPY
                | orjson.OPT_APPEND_NEWLINE
                | orjson.OPT_NON_STR_KEYS,
            ).decode("utf-8")
        )

        # flushing for all output formats (not just pipes) results in performance losses, and larger file sizes
        if settings.stateout == "-" or settings.stateout == "stdout":
            settings.stateoutfd.flush()

    @classmethod
    def add_arguments_to_parser(cls, subparser):
        raise NotImplementedError

    def update_state(self, msg):
        raise NotImplementedError

    def finalize(self):
        raise NotImplementedError
