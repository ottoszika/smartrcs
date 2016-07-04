#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_camera_handler
----------------------------------

Tests for `camera_handler` module.
"""

from smartrcs.web.server import Server
from smartrcs.configurable.configurable import Configurable
from twisted.trial.unittest import TestCase
from twisted.internet import defer, reactor
from cyclone import httpclient, httputil
import json

CONFIG_VALUE = None

# Sample camera configuration
SAMPLE_CAMERA_CONFIG = {'meter_mode': 'average', 'saturation': 0, 'image_effect': 'none', 'brightness': 50,
                        'exposure_mode': 'auto', 'sharpness': 0, 'crop': [0.0, 0.0, 1.0, 1.0], 'awb_mode': 'auto',
                        'ISO': 0, 'vflip': False, 'video_stabilization': False, 'color_effects': None, 'hflip': False,
                        'rotation': 0, 'resolution': [2592, 1944], 'exposure_compensation': 0, 'contrast': 0}


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
        global SAMPLE_CAMERA_CONFIG
        obj._config = SAMPLE_CAMERA_CONFIG

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

        global SAMPLE_CAMERA_CONFIG

        res = yield self.fetch('/api/camera')
        self.failUnlessEqual(json.loads(res.body), SAMPLE_CAMERA_CONFIG)

    @defer.inlineCallbacks
    def test_post(self):
        """
        Test POST request (configuration setter)
        """

        global CONFIG_VALUE

        # Invalid post data test
        res = yield self.fetch('/api/camera', method='POST', postdata='garbage data')
        self.failUnlessEqual(json.loads(res.body), {'error': 1})

        # Valid post data test
        postdata = {'test_prop1': 1, 'test_prop2': True, 'test_prop3': ['a', 'b', 'c']}
        res = yield self.fetch('/api/camera', method='POST', postdata=json.dumps(postdata))
        self.failUnlessEqual(json.loads(res.body), {'error': 0})
        self.failUnlessEqual(CONFIG_VALUE, postdata)
