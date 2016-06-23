import cyclone.web
import json


class Handler(cyclone.web.RequestHandler):
    """
    The :class:`Handler <Handler>` class.
    Generic handler for REST
    """

    def initialize(self):
        """
        Set header
        """

        self.set_header('Content-Type', 'application/json')

    def write(self, chunk):
        """
        Generate a compact JSON string from dict and write it to stream

        :param dict chunk: The data to be write to stream
        """

        chunk = json.dumps(chunk, separators=(',', ':'))
        super(Handler, self).write(chunk)
