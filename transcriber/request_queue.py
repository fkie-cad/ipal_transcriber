import collections
import threading
from copy import deepcopy

import transcriber.settings as settings


class RequestQueue:
    # Stores past requests to match responses against. Assumes chronological correctness!

    def __init__(self, transcribers):
        self.messages = {}
        self.queue = collections.deque()
        self.transcribers = transcribers
        self.threadLock = threading.Lock()

    # Remove all requests whose deadline for a response has passed
    def __remove_old_messages(self, current_time):
        if not self.queue:  # empty check
            return

        oldest_message = self.queue[0]
        while oldest_message.queue_timeout < current_time:

            # assumes chronological correctness
            del self.messages[oldest_message._flow][0]

            if len(self.messages[oldest_message._flow]) == 0:
                del self.messages[oldest_message._flow]

            self.queue.popleft()
            if not self.queue:  # empty check
                break

            oldest_message = self.queue[0]

    def __add_to_queue(self, request):
        # Deepcopy requests since the rule processor might alter values while requests are in the queue
        data = deepcopy(request.data)
        request = deepcopy(request)
        request.data = data

        # Calculate when this message times out in the queue
        request.queue_timeout = request.timestamp + settings.timeout

        if request._flow not in self.messages:
            self.messages[request._flow] = [request]
        else:
            self.messages[request._flow].append(request)
        self.queue.append(request)

    def __match_response(self, response):
        if response._flow in self.messages:

            # Match response with individual protocol transcriber
            to_remove = self.transcribers[response.protocol].match_response(
                self.messages[response._flow], response
            )

            # Remove used messages from queue
            for req in to_remove:
                self.messages[response._flow].remove(req)
                if len(self.messages[response._flow]) == 0:
                    del self.messages[response._flow]
                self.queue.remove(req)

    def update_queue(self, messages):
        with self.threadLock:
            # Remove messages first, as the last invocation of this method might
            # be a while ago already.
            self.__remove_old_messages(messages[-1].timestamp)

            for message in messages:
                if message._add_to_request_queue:
                    self.__add_to_queue(message)
                if message._match_to_requests:
                    self.__match_response(message)
