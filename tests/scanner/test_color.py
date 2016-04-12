#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_color
----------------------------------

Tests for `color` module.
"""

import unittest
from smartrcs.scanner.color import Color


class TestColor(unittest.TestCase):

    def test_distance_to(self):

        # Create 2 colors
        color1 = Color(121, 241, 42)
        color2 = Color(24, 59, 122)

        # Calculare the distance between them
        dist = color1.distance_to(color2)

        # Float assertion
        self.assertAlmostEqual(dist, 221.20804687, 6, 'Invalid distance')

    def test_inverse(self):

        # Create a color and invert it
        color = Color(121, 241, 42)
        color = color.inverse()

        # RGB component assertions
        self.assertEqual(color.get_red(), 134, 'Invalid red component')
        self.assertEqual(color.get_green(), 14, 'Invalid green component')
        self.assertEqual(color.get_blue(), 213, 'Invalid blue component')

    def test_grayscale(self):
        color = Color(121, 241, 42)
        color = color.grayscale()

        self.assertEqual(color.get_red(), 134, 'Invalid red component')
        self.assertEqual(color.get_green(), 134, 'Invalid green component')
        self.assertEqual(color.get_blue(), 134, 'Invalid blue component')


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
