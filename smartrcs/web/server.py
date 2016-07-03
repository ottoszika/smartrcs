# -*- coding: utf-8 -*-
import cyclone.web
import sys
from os.path import expanduser

from twisted.internet import reactor
from twisted.python import log


# Handlers
from camera_handler import CameraHandler
from recognizer_handler import RecognizerHandler

class Server:
    """
    The :class:`Server <Server>` class.
    Defines a REST API server
    """

    def __init__(self, host, port):
        """
        Initialize and configure web server application

        :param str host: Host or IP for interface
        :param int port: Port number
        """

        # Setting properties
        self.__host = host
        self.__port = port

        self.__api_path = '/api'

        home = expanduser("~")

        self.__application = cyclone.web.Application([

            # API
            (self.__api_path + '/camera', CameraHandler),
            (self.__api_path + '/recognizer', RecognizerHandler),

            # Static files
            ('/(.*)', cyclone.web.StaticFileHandler,
                {'path': home + '/.smartrcs/web/static', 'default_filename': 'index.html'}),
        ])

        # Log to console
        log.startLogging(sys.stdout)

    def start(self):
        """
        Start web server
        """

        reactor.listenTCP(self.__port, self.__application, interface=self.__host)
        reactor.run()

    def stop(self):
        """
        Stop web server
        """

        reactor.stop()
