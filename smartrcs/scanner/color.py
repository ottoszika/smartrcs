# -*- coding: utf-8 -*-
import math


class Color(object):
    """
    The :class:`Color <Color>` class.
    Defines a color by it's components (R, G, B)
    """

    def __init__(self, red=0xff, green=0xff, blue=0xff):

        # Check for invalid attributes
        if not isinstance(red, int) or red < 0x00 or red > 0xff:
            raise AttributeError('Invalid value for red property: %d' % red)
        elif not isinstance(green, int) or green < 0x00 or green > 0xff:
            raise AttributeError('Invalid value for green property: %d' % green)
        elif not isinstance(blue, int) or blue < 0x00 or blue > 0xff:
            raise AttributeError('Invalid value for blue property: %d' % blue)
        else:
            # Set attributes
            self.__red = red
            self.__green = green
            self.__blue = blue

    def distance_to(self, color):
        """
        Calculates distance between two colors.

        :param Color color: The second color
        :return: The distance
        :rtype: int
        """

        # Check for color attribute
        if not isinstance(color, Color):
            raise AttributeError('Attribute is not a color')

        # Calculating the square for each component
        red_sqr = (color.__red - self.__red) ** 2
        green_sqr = (color.__green - self.__green) ** 2
        blue_sqr = (color.__blue - self.__blue) ** 2

        # Formula for distance between two 3D points
        return math.sqrt(red_sqr + green_sqr + blue_sqr)

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

    def __str__(self):
        """
        Converts to string

        :return: The string representation
        :rtype: str
        """
        return '(r: %d, g: %d, b: %d)' % (self.__red, self.__green, self.__blue)

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

        if not isinstance(value, int) or value < 0x00 or value > 0xff:
            raise AttributeError('Invalid value for red property: %d' % value)
        else:
            self.__red = value

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

        if not isinstance(value, int) or value < 0x00 or value > 0xff:
            raise AttributeError('Invalid value for green property: %d' % value)
        else:
            self.__green = value

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

        if not isinstance(value, int) or value < 0x00 or value > 0xff:
            raise AttributeError('Invalid value for blue property: %d' % value)
        else:
            self.__blue = value
