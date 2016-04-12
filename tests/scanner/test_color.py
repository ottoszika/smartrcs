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

    def test___init__(self):

        # Test invalid red data (-1)
        with self.assertRaises(AttributeError):
            color = Color(-1, 241, 42)

        # Test invalid red data (256)
        with self.assertRaises(AttributeError):
            color = Color(256, 241, 42)

        # Test invalid red data (3.14)
        with self.assertRaises(AttributeError):
            color = Color(3.14, 241, 42)

        # Test invalid green data (-1)
        with self.assertRaises(AttributeError):
            color = Color(121, -1, 42)

        # Test invalid green data (256)
        with self.assertRaises(AttributeError):
            color = Color(121, 256, 42)

        # Test invalid green data (3.14)
        with self.assertRaises(AttributeError):
            color = Color(121, 3.14, 42)

        # Test invalid blue data (-1)
        with self.assertRaises(AttributeError):
            color = Color(121, 241, -1)

        # Test invalid blue data (256)
        with self.assertRaises(AttributeError):
            color = Color(121, 241, 256)

        # Test invalid blue data (3.14)
        with self.assertRaises(AttributeError):
            color = Color(121, 241, 3.14)

    def test_distance_to(self):

        # Create 2 colors
        color1 = Color(121, 241, 42)
        color2 = Color(24, 59, 122)

        # Calculate the distance between them
        dist = color1.distance_to(color2)

        # Float assertion
        self.assertAlmostEqual(dist, 221.20804687, 6, 'Invalid distance')

        # Test invalid attribute
        with self.assertRaises(AttributeError):
            color1.distance_to(3.14)

    def test_inverse(self):

        # Create a color and invert it
        color = Color(121, 241, 42)
        color = color.inverse()

        # RGB component assertions
        self.assertEqual(color.red, 134, 'Invalid red component')
        self.assertEqual(color.green, 14, 'Invalid green component')
        self.assertEqual(color.blue, 213, 'Invalid blue component')

    def test_grayscale(self):

        # Create a color and convert it to grayscale
        color = Color(121, 241, 42)
        color = color.grayscale()

        # Asserstions
        self.assertEqual(color.red, 134, 'Invalid red component')
        self.assertEqual(color.green, 134, 'Invalid green component')
        self.assertEqual(color.blue, 134, 'Invalid blue component')

    def test___str__(self):

        # Create a color
        color = Color(121, 241, 42)

        # Assertion
        self.assertEqual(str(color), '(r: 121, g: 241, b: 42)', 'Invalid __str__ conversion')

    def test_getters(self):
        color = Color(121, 241, 42)

        self.assertEqual(color.red, 121, 'Invalid red component')
        self.assertEqual(color.green, 241, 'Invalid green component')
        self.assertEqual(color.blue, 42, 'Invalid blue component')

    def test_setters(self):

        # Create an uninitialized color object
        color = Color()

        # Test red with valid data
        color.red = 121
        self.assertEqual(color.red, 121)

        # Test green with valid data
        color.green = 241
        self.assertEqual(color.green, 241)

        # Test blue with valid data
        color.blue = 42
        self.assertEqual(color.blue, 42)

        # Test red with invalid values
        self.assertRaises(AttributeError, setattr, color, 'red', -1)
        self.assertRaises(AttributeError, setattr, color, 'red', 256)
        self.assertRaises(AttributeError, setattr, color, 'red', 3.14)

        # Test green with invalid values
        self.assertRaises(AttributeError, setattr, color, 'green', -1)
        self.assertRaises(AttributeError, setattr, color, 'green', 256)
        self.assertRaises(AttributeError, setattr, color, 'green', 3.14)

        # Test blue with invalid values
        self.assertRaises(AttributeError, setattr, color, 'blue', -1)
        self.assertRaises(AttributeError, setattr, color, 'blue', 256)
        self.assertRaises(AttributeError, setattr, color, 'blue', 3.14)

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
