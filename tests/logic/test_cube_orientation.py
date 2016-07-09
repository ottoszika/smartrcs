#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_cube_orientation
----------------------------------

Tests for `cube_orientation` module.
"""

import unittest
from smartrcs.logic.cube_orientation import CubeOrientation


class TestCubeOrientation(unittest.TestCase):

    def setUp(self):
        self.__initial_faces = {
            'U': 'U',
            'L': 'L',
            'F': 'F',
            'R': 'R',
            'B': 'B',
            'D': 'D'
        }

    def test___init__(self):

        # Test with no parameters
        cube_orientation = CubeOrientation()
        self.assertDictEqual(cube_orientation._CubeOrientation__faces, self.__initial_faces)

        # Test with parameters
        cube_orientation = CubeOrientation({
            'U': 'F',
            'L': 'L',
            'F': 'D',
            'R': 'R',
            'B': 'U',
            'D': 'B'})
        self.assertDictEqual(cube_orientation._CubeOrientation__faces, {
            'U': 'F',
            'L': 'L',
            'F': 'D',
            'R': 'R',
            'B': 'U',
            'D': 'B'
        })

    def test_rotate_ox_cw(self):
        cube_orientation = CubeOrientation()

        # Check for one rotation
        cube_orientation.rotate_ox_cw()
        self.assertDictEqual(cube_orientation._CubeOrientation__faces, {
            'U': 'F',
            'L': 'L',
            'F': 'D',
            'R': 'R',
            'B': 'U',
            'D': 'B'
        })

        # Rotate 3 times and should go back into the initial position
        cube_orientation.rotate_ox_cw()
        cube_orientation.rotate_ox_cw()
        cube_orientation.rotate_ox_cw()
        self.assertDictEqual(cube_orientation._CubeOrientation__faces, self.__initial_faces)

    def test_rotate_ox_ccw(self):
        cube_orientation = CubeOrientation()

        # Check for one rotation
        cube_orientation.rotate_ox_ccw()
        self.assertDictEqual(cube_orientation._CubeOrientation__faces, {
            'U': 'B',
            'L': 'L',
            'F': 'U',
            'R': 'R',
            'B': 'D',
            'D': 'F'
        })

        # Rotate 3 times and should go back into the initial position
        cube_orientation.rotate_ox_ccw()
        cube_orientation.rotate_ox_ccw()
        cube_orientation.rotate_ox_ccw()
        self.assertDictEqual(cube_orientation._CubeOrientation__faces, self.__initial_faces)

    def test_rotate_oy_cw(self):
        cube_orientation = CubeOrientation()

        # Check for one rotation
        cube_orientation.rotate_oy_cw()
        self.assertDictEqual(cube_orientation._CubeOrientation__faces, {
            'U': 'U',
            'L': 'F',
            'F': 'R',
            'R': 'B',
            'B': 'L',
            'D': 'D'
        })

        # Rotate 3 times and should go back into the initial position
        cube_orientation.rotate_oy_cw()
        cube_orientation.rotate_oy_cw()
        cube_orientation.rotate_oy_cw()
        self.assertDictEqual(cube_orientation._CubeOrientation__faces, self.__initial_faces)

    def test_rotate_oy_ccw(self):
        cube_orientation = CubeOrientation()

        # Check for one rotation
        cube_orientation.rotate_oy_ccw()
        self.assertDictEqual(cube_orientation._CubeOrientation__faces, {
            'U': 'U',
            'L': 'B',
            'F': 'L',
            'R': 'F',
            'B': 'R',
            'D': 'D'
        })

        # Rotate 3 times and should go back into the initial position
        cube_orientation.rotate_oy_ccw()
        cube_orientation.rotate_oy_ccw()
        cube_orientation.rotate_oy_ccw()
        self.assertDictEqual(cube_orientation._CubeOrientation__faces, self.__initial_faces)

    def test_rotate_oz_cw(self):
        cube_orientation = CubeOrientation()

        # Check for one rotation
        cube_orientation.rotate_oz_cw()
        self.assertDictEqual(cube_orientation._CubeOrientation__faces, {
            'U': 'L',
            'L': 'D',
            'F': 'F',
            'R': 'U',
            'B': 'B',
            'D': 'R'
        })

        # Rotate 3 times and should go back into the initial position
        cube_orientation.rotate_oz_cw()
        cube_orientation.rotate_oz_cw()
        cube_orientation.rotate_oz_cw()
        self.assertDictEqual(cube_orientation._CubeOrientation__faces, self.__initial_faces)

    def test_rotate_oz_ccw(self):
        cube_orientation = CubeOrientation()

        # Check for one rotation
        cube_orientation.rotate_oz_ccw()
        self.assertDictEqual(cube_orientation._CubeOrientation__faces, {
            'U': 'R',
            'L': 'U',
            'F': 'F',
            'R': 'D',
            'B': 'B',
            'D': 'L'
        })

        # Rotate 3 times and should go back into the initial position
        cube_orientation.rotate_oz_ccw()
        cube_orientation.rotate_oz_ccw()
        cube_orientation.rotate_oz_ccw()
        self.assertDictEqual(cube_orientation._CubeOrientation__faces, self.__initial_faces)

    def test_faces(self):
        cube_orientation = CubeOrientation()
        self.assertDictEqual(cube_orientation.faces, self.__initial_faces)
