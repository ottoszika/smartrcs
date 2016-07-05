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
import subprocess


CONFIG_VALUE = None
SAMPLE_BOWER_CONFIG = {'installed': False}
CHECK_OUTPUT_RESULT = None
SYSTEM_RESULT = None


class TestBower(unittest.TestCase):

    @staticmethod
    def load(obj):
        global SAMPLE_BOWER_CONFIG
        obj._config = SAMPLE_BOWER_CONFIG

    @staticmethod
    def save(obj):
        global CONFIG_VALUE
        CONFIG_VALUE = obj._config

    @staticmethod
    def check_output(data):
        global CHECK_OUTPUT_RESULT
        CHECK_OUTPUT_RESULT = data

    @staticmethod
    def system(data):
        global SYSTEM_RESULT
        SYSTEM_RESULT = data

    def setUp(self):

        # Mocking methods
        Configurable.load = self.load
        Configurable.save = self.save
        os.system = self.system
        subprocess.check_output = self.check_output

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

    def test_install_dependencies(self):

        global CHECK_OUTPUT_RESULT
        global SYSTEM_RESULT

        bower = Bower()
        bower.install_dependencies()

        # Test two shell command results
        self.assertEqual(CHECK_OUTPUT_RESULT, ['bower', '--version'])
        self.assertEqual(SYSTEM_RESULT, 'cd %s && bower install' % (os.path.expanduser("~") + '/.smartrcs/web'))

    def test_mark_installed(self):

        global SAMPLE_BOWER_CONFIG

        # Set config 'installed' to false to see changes
        SAMPLE_BOWER_CONFIG['installed'] = False

        bower = Bower()
        bower.mark_installed()

        self.assertEqual(CONFIG_VALUE, {'installed': True})
