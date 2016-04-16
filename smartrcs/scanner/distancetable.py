# -*- coding: utf-8 -*-
import numpy as np


class DistanceTable(object):
    """
    The :class:`DistanceTable <DistanceTable>` class.
    Defines a 2D matrix to calculate distances between 2 nodes
    """

    def __init__(self, size):
        """
        Initialize a table (size x size)

        :param int size: The size of the table
        """

        # Checking size limit
        self.__check_limits(size, 1)

        self.__size = size

        # Create table
        self.__table = np.zeros(shape=(size, size))

        # Reset all to None
        for i in range(0, size):
            for j in range(0, size):
                self.__table[i, j] = None

    def add(self, from_loc, to_loc, distance):
        """
        Add a distance between 2 locations

        :param int from_loc: From location
        :param int to_loc: To location
        :param int distance: Distance value
        """

        self.__check_limits(from_loc, 0, self.__size - 1)
        self.__check_limits(to_loc, 0, self.__size - 1)

        # Add distance for (from -> to) and (to -> from)
        self.__table[from_loc, to_loc] = distance
        self.__table[to_loc, from_loc] = distance

    def get(self, from_loc, to_loc):
        """
        Get distance between 2 locations

        :param int from_loc: From location
        :param int to_loc: To location
        :return: Distance value
        :rtype: int
        """

        self.__check_limits(from_loc, 0, self.__size - 1)
        self.__check_limits(to_loc, 0, self.__size - 1)

        return self.__table[from_loc, to_loc]

    def nearest(self, loc):
        """
        Get the nearest location

        :param int loc: The starting location
        :return: The nearest location
        :rtype: int
        """

        # Checking loc param
        self.__check_limits(loc, 0, self.__size - 1)

        # Set min value on the first not None value
        min_value = None
        min_value_index = 0
        for i in range(0, self.__size):

            # Check for the first number
            if not np.isnan(self.__table[loc, i]):
                min_value = self.__table[loc, i]
                min_value_index = i
                break

        # Return None if no min value assigned
        if min_value is None:
            return None

        # Find the min value
        for i in range(min_value_index, self.__size):

            # Store value
            value = self.__table[loc, i]

            # Check if there was a lower value than min value and reset it
            if min_value > value:
                min_value = value
                min_value_index = i

        return min_value_index

    @staticmethod
    def __check_limits(value, lower=None, upper=None):
        """
        Check if value is between lower and upper

        :param value: The value to be checked
        :raise: ValueError
        """

        # Check bounds
        if value < lower or (upper is not None and value > upper):
            raise ValueError('Invalid value: %s' % value)
