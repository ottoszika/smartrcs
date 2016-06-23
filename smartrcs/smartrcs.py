# -*- coding: utf-8 -*-
from web import Server


class SmartRCS(object):
    """
    The :class:`SmartRCS <SmartRCS>` class.
    Defines the main process
    """

    def __init__(self, **kwargs):
        """
        Initialize object

        :param kwargs: Initializer arguments
        """
        self.__server = None
        self.__server_thread = None
        self.__kwargs = kwargs

    def run(self):
        """
        Run the solver
        """

        # Server argument
        if self.__kwargs.get('server'):
            host = '0.0.0.0'
            port = 8080

            # Override host
            if self.__kwargs.get('host') is not None:
                host = self.__kwargs.get('host')

            # Override port
            if self.__kwargs.get('port') is not None:
                port = self.__kwargs.get('port')

            # Start server
            self.start_server(host, port)

    def start_server(self, host, port):
        """
        Start web server

        :param str host: Host of the server (interface)
        :param int port: Port number
        :return:
        """

        self.__server = Server(host, port)
        self.__server.start()


# Main function
def __main__():
    s = SmartRCS(server=1)
    s.run()

if __name__ == '__main__':
    smartrcs.__main__()
