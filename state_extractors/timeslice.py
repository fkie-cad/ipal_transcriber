import transcriber.settings as settings
from state_extractors.state_extractor import StateExtractor


class TimeSliceStateExtractor(StateExtractor):
    _name = "timeslice"
    _description = "Outputs complete state in regular time slices."
    _options = {
        "interval": 1.0,  # output state every x seconds
    }

    def __init__(self, args):
        super().__init__(args)

        self.malicious = None
        self.nextslice = None

        # parse arguments
        if args.timeslice_interval:
            try:
                self._options["interval"] = int(args.timeslice_interval) * 0.001
            except ValueError:
                settings.logger.error(
                    "Option '--timeslice.interval' has to be a positive integer!"
                )
                exit(1)

        if self._options["interval"] <= 0:
            settings.logger.error(
                "Option '--timeslice.interval' has to be a positive integer!"
            )
            exit(1)

        if settings.stateinmessage:
            settings.logger.error(
                "Timeslice is incompatible with state-in-message being true!"
            )
            exit(1)

    @classmethod
    def add_arguments_to_parser(cls, subparser):
        subparser.add_argument(
            "--timeslice.interval",
            dest="timeslice_interval",
            metavar="INT",
            help="generate a new state every INT milliseconds. (Default: 1000ms)",
            required=False,
        )

    def update_state(self, msg):
        # Based on the current messages timestamp, we check whether
        # we should have output states since the last state update.
        # If so, we do this now before considering new state changes.
        # Assumption: Delays between messages are so short that this
        # does not introduce significant delays.
        # Otherwise, we would have to rely on timers and callback functions
        # to output states at the current times.

        if self.nextslice is None:  # Initial timestamp
            self.nextslice = msg.timestamp

        # If we should output a state every second, but 3 seconds have
        # passed since the last update, we have to output more than one state
        if self.nextslice < msg.timestamp:
            while self.nextslice < msg.timestamp:
                self._write_state(
                    None, malicious=self.malicious, timestamp=self.nextslice
                )
                self.nextslice += self._options["interval"]

            # Reset malicious for the next output
            self.malicious = None

        # At least one malicious suffices to be a malicious timeslice

        # We assume that there is only one malicious id for each timeslice!
        if self.malicious not in [None, False] and msg.malicious not in [None, False]:
            assert self.malicious == msg.malicious

        # None/False or False/True/"a" => False/True/"a"
        # True/"a" or False/True/"a" => True/"a"
        if msg.malicious is not None:  # Because False or None => None
            self.malicious = self.malicious or msg.malicious

        # Update state
        for key in msg.data:
            if msg.data[key] is not None:
                identifier = self._get_identifier(msg, key)
                self._state[identifier] = msg.data[key]

    def finalize(self):
        # Output last state regardless of the time difference
        self._write_state(None, malicious=self.malicious, timestamp=self.nextslice)
