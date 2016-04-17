#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_distancetable
----------------------------------

Tests for `distancetable` module.
"""

import unittest
from smartrcs.configurable.configurable import Configurable


class TestConfigurable(unittest.TestCase):

    def test___init__(self):

        # Create an object
        conf = Configurable()

        # Test
        try:
            config_path = conf._Configurable__config_path
        except AttributeError:
            self.assertTrue(False, 'Config path not set')

    def test___get_config_path(self):

        # Need this to get home dir
        from os.path import expanduser

        # Create a new object
        conf = Configurable()

        # Get path and correct path
        path = conf._Configurable__get_config_path()
        correct_path = expanduser("~") + '/.smartrcs/config/configurable.yaml'

        # Test
        self.assertEqual(path, correct_path, 'Invalid config path')

    def test_save(self):

        # Create a new object
        conf = Configurable()

        # Set protected variable
        conf._config = 'Test config'

        # Mock file write method
        def __write_to_config(data):
            # Test
            self.assertTrue(data.count('Test config') == 1)

        # Set mocked method
        conf._Configurable__write_to_config = __write_to_config

        # Save method testing
        conf.save()


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
