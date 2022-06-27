#!/usr/bin/env python3
import json

import transcriber.settings as settings
from transcribers.utils import get_all_transcribers


class StateExtractor:

    _name = None
    _description = None
    _options = None

    def __init__(self, args):
        self.transcribers = get_all_transcribers()

        self._state = {}
        self._first = True

    def _get_identifier(self, msg, key):
        return self.transcribers[msg.protocol].state_identifier(msg, key)

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
            output[
                "_state_extractor-config"
            ] = settings.state_extractor_settings_to_dict()
            output["_state_extractor-config"]["options"] = self._options
            self._first = False

        settings.stateoutfd.write(json.dumps(output) + "\n")

    @classmethod
    def add_arguments_to_parser(cls, subparser):
        raise NotImplementedError

    def update_state(self, msg):
        raise NotImplementedError

    def finalize(self):
        raise NotImplementedError
