# -*- coding: utf-8 -*-
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie1976


class Color(object):
    """
    The :class:`Color <Color>` class.
    Defines a color by it's components (R, G, B)
    """

    def __init__(self, red=0xff, green=0xff, blue=0xff):

        # Check for invalid attributes
        self.__check_limits(red)
        self.__check_limits(green)
        self.__check_limits(blue)

        # Set attributes
        self.__red = int(red)
        self.__green = int(green)
        self.__blue = int(blue)

    def distance_to(self, color):
        """
        Calculates distance between two colors.

        :param Color color: The second color
        :return: The distance
        :rtype: int
        """

        # Making up first color
        rgb_a = sRGBColor(float(self.red) / 0xff,
                          float(self.green) / 0xff,
                          float(self.blue) / 0xff)

        # Making up first color
        rgb_b = sRGBColor(float(color.red) / 0xff,
                          float(color.green) / 0xff,
                          float(color.blue) / 0xff)

        # RGB to Lab
        lab_a = convert_color(rgb_a, LabColor, target_illuminant='d50')
        lab_b = convert_color(rgb_b, LabColor, target_illuminant='d50')

        # Calculate Delta-E color distance
        delta_e = delta_e_cie1976(lab_a, lab_b)

        return delta_e

    def inverse(self):
        """
        Calculates the negative of the color

        :return: The negative color
        :rtype: Color
        """

        # Negate all components
        red = ~self.__red & 0xff
        green = ~self.__green & 0xff
        blue = ~self.__blue & 0xff

        # Create a new color and return it
        return Color(red, green, blue)

    def grayscale(self):
        """
        Calculates the grayscale value of the color

        :return: The grayscale color
        :rtype: Color
        """

        # Gray color formula
        gray = int((self.__red + self.__green + self.__blue) / 3)

        # Create and return the grayscaled color
        return Color(gray, gray, gray)

    @staticmethod
    def __check_limits(value):
        """
        Check if value is between 0 and 255

        :param int value: The value you want to check
        """

        if value < 0x00 or value > 0xff:
            raise ValueError('Invalid color component value: %d' % value)

    def __str__(self):
        """
        Converts to string

        :return: The string representation
        :rtype: str
        """
        return '(r: %d, g: %d, b: %d)' % (self.__red, self.__green, self.__blue)

    def __eq__(self, other):
        """
        Equals to

        :param Color other: The other color
        :return: True if the two color are equal, otherwise False
        :rtype: bool
        """

        return (isinstance(other, self.__class__) and
                self.__red == other.red and
                self.__green == other.green and
                self.__blue == other.blue)

    @property
    def red(self):
        """
        Getter for the red component

        :return: The red component value
        :rtype: int
        """

        return self.__red

    @red.setter
    def red(self, value):
        """
        Setter for the red component

        :param int value: The value to be set
        """

        self.__check_limits(value)
        self.__red = int(value)

    @property
    def green(self):
        """
        Getter for the green component

        :return: The green component value
        :rtype: int
        """

        return self.__green

    @green.setter
    def green(self, value):
        """
        Setter for the green component

        :param int value: The value to be set
        """

        self.__check_limits(value)
        self.__green = int(value)

    @property
    def blue(self):
        """
        Getter for the blue component

        :return: The blue component value
        :rtype: int
        """

        return self.__blue

    @blue.setter
    def blue(self, value):
        """
        Setter for the blue component

        :param int value: The value to be set
        """

        self.__check_limits(value)
        self.__blue = int(value)
