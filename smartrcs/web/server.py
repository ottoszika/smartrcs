# -*- coding: utf-8 -*-
import cyclone.web
import sys
from os.path import expanduser

from twisted.internet import reactor
from twisted.python import log


# Handlers
from camera_handler import CameraHandler
from recognizer_handler import RecognizerHandler
from bower import Bower


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
                {'path': home + '/.smartrcs/web', 'default_filename': 'index.html'}),
        ])

        # Log to console
        log.startLogging(sys.stdout)

        # Creating a bower object for further installation (if it's necessary)
        self.__bower = Bower()

    def start(self):
        """
        Start web server
        """

        # Install bower dependencies (only if it were not install)
        if not self.__bower.check_installed():
            print 'Bower dependencies will be installed...'
            self.__bower.install_dependencies()

        reactor.listenTCP(self.__port, self.__application, interface=self.__host)
        reactor.run()

    @staticmethod
    def stop():
        """
        Stop web server
        """

        reactor.stop()
