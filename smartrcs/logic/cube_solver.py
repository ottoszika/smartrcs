# -*- coding: utf-8 -*-
import kociemba


class CubeSolver(object):
    """
    The :class:`CubeSolver <CubeSolver>` class.
    Wrapper over Herbert Kociemba's algorithm library
    """

    def __init__(self, notation):
        """
        Initialize solver with notation

        :param str notation: Standard cube notation
        """

        self.__notation = notation

    def solve(self):
        """
        Solve cube

        :return: The movements to be performed
        :rtype: list
        """

        result = kociemba.solve(self.__notation)
        return result.split(' ')
