#!/usr/bin/env python3
from state_extractors.state_extractor import StateExtractor


class DefaultStateExtractor(StateExtractor):
    # Keeps a buffer of the last value for each state variable and updates the buffer whenever a new message arrives. A state is malicious if at least one message is maliciious.

    _name = "default"
    _description = "Simple last value buffer of all variables"
    _options = {}

    def __init__(self, args):
        super().__init__(args)

    @classmethod
    def add_arguments_to_parser(cls, subparser):
        pass

    def update_state(self, msg):
        for key in msg.data:
            if msg.data[key] is not None:
                identifier = self._get_identifier(msg, key)
                self._state[identifier] = msg.data[key]

        self._write_state(msg, malicious=msg.malicious, timestamp=msg.timestamp)

    def finalize(self):
        pass
