#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_recognizer_handler
----------------------------------

Tests for `recognizer_handler` module.
"""

from smartrcs.web.server import Server
from smartrcs.configurable.configurable import Configurable
from twisted.trial.unittest import TestCase
from twisted.internet import defer, reactor
from cyclone import httpclient, httputil
from PIL import Image
import io
import json

CONFIG_VALUE = None

# Sample recognizer configuration
SAMPLE_RECOGNIZER_CONFIG = {'radius': 3, 'order': ['U', 'L', 'F', 'R', 'B', 'D'],
                            'facelet': [[840, 192], [1188, 171], [1527, 165], [864, 552],
                                        [1203, 543], [1542, 522], [879, 888], [1218, 876], [1548, 864]]}


class TestCameraHandler(TestCase):

    @staticmethod
    def get_http_port():
        """
        Get a HTTP port
        """

        return 8080

    @staticmethod
    def get_app(host, port):
        """
        Get HTTP server application

        :param str host: Host or IP for interface
        :param int port: Port number
        """

        server = Server(host, port)
        return server.get_application()

    @staticmethod
    def load(obj):
        global SAMPLE_RECOGNIZER_CONFIG
        obj._config = SAMPLE_RECOGNIZER_CONFIG

    @staticmethod
    def save(obj):
        global CONFIG_VALUE
        CONFIG_VALUE = obj._config

    def setUp(self, *args, **kwargs):

        # Mocking methods
        Configurable.load = self.load
        Configurable.save = self.save

        self.__host = 'localhost'
        self.__port = self.get_http_port()
        self.__app = self.get_app(self.__host, self.__port)
        self.__listener = reactor.listenTCP(self.__port, self.__app)

        return TestCase.setUp(self, *args, **kwargs)

    def tearDown(self):
        if self.__listener:
            self.__listener.stopListening()

    @defer.inlineCallbacks
    def fetch(self, url, *args, **kwargs):
        response = yield httpclient.fetch('http://%s:%s%s' % (self.__host, self.__port, url), *args, **kwargs)
        defer.returnValue(response)

    @defer.inlineCallbacks
    def test_get(self):
        """
        Test GET request (configuration getter)
        """

        global SAMPLE_RECOGNIZER_CONFIG

        # JSON configuration test
        res = yield self.fetch('/api/recognizer?type=json')
        self.failUnlessEqual(json.loads(res.body), SAMPLE_RECOGNIZER_CONFIG)

        # Image test
        res = yield self.fetch('/api/recognizer?type=img')
        try:
            img = Image.open(io.BytesIO(res.body))
        except IOError:
            self.fail('Should receive a valid image from /api/recognizer?type=img.')

    @defer.inlineCallbacks
    def test_post(self):
        """
        Test POST request (configuration setter)
        """

        global CONFIG_VALUE

        # Invalid post data test
        res = yield self.fetch('/api/recognizer', method='POST', postdata='garbage data')
        self.failUnlessEqual(json.loads(res.body), {'error': 1})

        # Valid post data test
        postdata = {'test_prop1': 1, 'test_prop2': True, 'test_prop3': ['a', 'b', 'c']}
        res = yield self.fetch('/api/recognizer', method='POST', postdata=json.dumps(postdata))
        self.failUnlessEqual(json.loads(res.body), {'error': 0})
        self.failUnlessEqual(CONFIG_VALUE, postdata)
