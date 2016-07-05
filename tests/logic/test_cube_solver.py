#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_cube_solver
----------------------------------

Tests for `cube_solver` module.
"""

import unittest
from smartrcs.logic.cube_solver import CubeSolver
import kociemba


class TestCubeSolver(unittest.TestCase):

    @staticmethod
    def solve(notation):
        return 'D2 R\' D\' F2 B D R2 D2 R\' F2 D\' F2 U\' B2 L2 U2 D R2 U'

    def setUp(self):

        # Mockup kociemba solving function
        kociemba.solve = self.solve

    def test__init__(self):
        cube_solver = CubeSolver('DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD')

        # Check for correct property value
        self.assertEqual(cube_solver._CubeSolver__notation,
                         'DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD')

    def test_solve(self):
        cube_solver = CubeSolver('DRLUUBFBRBLURRLRUBLRDDFDLFUFUFFDBRDUBRUFLLFDDBFLUBLRBD')

        # Check for correct splitting
        result = cube_solver.solve()
        expected = ['D2', 'R\'', 'D\'', 'F2', 'B', 'D', 'R2', 'D2', 'R\'',
                    'F2', 'D\'', 'F2', 'U\'', 'B2', 'L2', 'U2', 'D', 'R2', 'U']

        self.assertListEqual(result, expected)
