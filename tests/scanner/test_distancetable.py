#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_distancetable
----------------------------------

Tests for `distancetable` module.
"""

import unittest
from smartrcs.scanner.distancetable import DistanceTable


class TestDistanceTable(unittest.TestCase):

    def test___init__(self):

        # Create a valid and common dt ad get inside table size
        dt = DistanceTable(54)
        size = len(dt._DistanceTable__table)

        self.assertEqual(size, 54, 'Invalid distance table size')


        # Create an invalid dt (with 0 size)
        with self.assertRaises(ValueError):
            DistanceTable(0)

        # Create an invalid dt (with negative size)
        with self.assertRaises(ValueError):
            DistanceTable(-1)

    def test_add(self):

        # Cteate a distance table and add a distance
        dt = DistanceTable(54)
        dt.add(4, 8, 11.5)

        # Test distance from A to B, and from B to A
        self.assertEqual(dt._DistanceTable__table[4, 8], 11.5, 'Distance not added to table')
        self.assertEqual(dt._DistanceTable__table[8, 4], 11.5, 'Distance from B to A not added to table')

    def test_get(self):

        # Cteate a distance table and add a distance
        dt = DistanceTable(54)
        dt.add(4, 8, 11.5)

        # Test distance from A to B, and from B to A (with get())
        self.assertEqual(dt.get(4, 8), 11.5, 'Invalid distance value')
        self.assertEqual(dt.get(8, 4), 11.5, 'Invalid distance value')

    def test_nearest(self):

        # Cteate a distance table and add some distances
        dt = DistanceTable(54)
        dt.add(2, 3, 14.21)
        dt.add(2, 7, 11.42)
        dt.add(2, 10, 17.22)
        dt.add(2, 5, 13.71)
        dt.add(1, 10, 10.10)

        # Test for nearest location
        self.assertEqual(dt.nearest(2), 7, 'Invalid nearest location')

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
