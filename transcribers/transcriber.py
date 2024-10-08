class Transcriber:
    # A transcriber handles the transcription from network packets to
    # abstract messages. Optimally a Transcriber should be implemented
    # thread-safe even though this is not required currently.

    _name = None  # The name of the transcribers protocol

    def __init__(self, id_counter):
        self._id_counter = id_counter

    @classmethod
    def state_identifier(cls, msg, key):
        # Used to identify a single variable for the state. Since e.g.
        # in Modbus a specific coil.1 depends on the IP address and unitID,
        # whereas in NMEA 0183 a GLL measurement does not necessarily
        # depend on the source address.
        # Default is source and variable name separated by ':'.

        # INFO Same ip+port+key for different protocols unlikely
        return f"{msg.src}:{key}"

    def matches_protocol(self, pkt):
        # Returns true if a packet can be handled by this transcriber
        raise NotImplementedError

    def parse_packet(self, pkt):
        # Parse a single packet and return a list of transcribed messages
        raise NotImplementedError

    def match_response(self, requests, response):
        # Modifies a response by information derived from the corresponding request(s). This method may alter the
        # requests in the request array but not the request array! It may return a list of requests to delete from
        # the queue
        return []
