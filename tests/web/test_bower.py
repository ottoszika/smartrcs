#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_bower
----------------------------------

Tests for `bower` module.
"""

import unittest
from smartrcs.configurable.configurable import Configurable
from smartrcs.web.bower import Bower
import os


CONFIG_VALUE = None
SAMPLE_BOWER_CONFIG = {'installed': False}


class TestBower(unittest.TestCase):

    @staticmethod
    def load(obj):
        global SAMPLE_BOWER_CONFIG
        obj._config = SAMPLE_BOWER_CONFIG

    @staticmethod
    def save(obj):
        global CONFIG_VALUE
        CONFIG_VALUE = obj._config

    def setUp(self):

        # Mocking methods
        Configurable.load = self.load
        Configurable.save = self.save

    def test___init__(self):
        global SAMPLE_BOWER_CONFIG

        bower = Bower()

        # Check if fields were set
        self.assertEqual(bower._Bower__web_path, os.path.expanduser("~") + '/.smartrcs/web')
        self.assertEqual(bower._config, SAMPLE_BOWER_CONFIG)

    def test_check_installed(self):

        global SAMPLE_BOWER_CONFIG

        # Check with installed: false
        SAMPLE_BOWER_CONFIG['installed'] = False
        bower = Bower()
        self.assertFalse(bower.check_installed())

        # Check with installed: true
        SAMPLE_BOWER_CONFIG['installed'] = True
        bower = Bower()
        self.assertTrue(bower.check_installed())

    def test_mark_installed(self):

        global SAMPLE_BOWER_CONFIG

        # Set config 'installed' to false to see changes
        SAMPLE_BOWER_CONFIG['installed'] = False

        bower = Bower()
        bower.mark_installed()

        self.assertEqual(CONFIG_VALUE, {'installed': True})
