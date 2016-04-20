# -*- coding: utf-8 -*-
from smartrcs.configurable.configurable import Configurable
from PIL import Image
import numpy as np
from color import Color
from distancetable import DistanceTable


class Recognizer(Configurable):
    """
    The :class:`Recognizer <Recognizer>` class.
    Color recognizer for cube facelets
    """

    def __init__(self):
        """
        Initialize config and properties
        """

        Configurable.__init__(self)

        # Storing images hash table
        self.__face_images = {}

        # Dict of all cubies
        self.__facelets = {}
        self.__facelets_values = []

        # Color distance table
        self.__distance_table = None

        # Sorted colors
        self.__sorted_colors = []

    def add_image(self, image):
        """
        Add image to recognizer

        :param Image image: The image to be added
        """

        # Face order
        order = self._config['order']

        # Check if there is space for an image
        img_count = len(self.__face_images)
        if img_count > len(order) - 1:
            raise OverflowError('No more images can be added')

        # Getting facelet index name
        next_name = order[img_count]

        # Add image
        self.__face_images[next_name] = image

    def read_images(self):
        """
        Read all images

        :return: List of dominant colors
        """

        # Here we will store dominant colors
        values = {}

        # Getting radius and coords from config
        radius = self._config['radius']
        facelet = self._config['facelet']

        # Loop over each face
        for index, image in self.__face_images.iteritems():

            # Initialize an empty list at index
            values[index] = []

            # Loop over each coords
            for cubie in facelet:

                # Crop image
                cubie_img = image.crop((cubie[0] - radius, cubie[1] - radius, cubie[0] + radius, cubie[1] + radius))

                # Calculate histogram
                cubie_hist = cubie_img.histogram()

                # Separate R, G, B from hist
                cubie_hist_red = cubie_hist[0: 256]
                cubie_hist_green = cubie_hist[256: 512]
                cubie_hist_blue = cubie_hist[512: 768]

                # Getting dominant color
                red = np.argmax(cubie_hist_red)
                green = np.argmax(cubie_hist_green)
                blue = np.argmax(cubie_hist_blue)

                # Create color and add to hash table
                color = Color(red, green, blue)
                values[index].append(color)

        # Set property and return value
        self.__facelets = values
        self.__facelets_values = self.__facelets.values()
        return values

    def create_distance_table(self):
        """
        Create a distance table for facelets obtained

        :return: The distance table
        :rtype: DistanceTable
        """

        # Here we will store colors
        colors_list = []

        # Fill colors list with colors
        for value in self.__facelets_values:
            for color in value:
                colors_list.append(color)

        # Initialize a distance table
        distance_table = DistanceTable(len(colors_list))

        # Fill distance table
        for i in range(0, len(colors_list)):
            for j in range(0, len(colors_list)):
                distance_table.add(i, j, colors_list[i].distance_to(colors_list[j]))

        # Set property and return
        self.__distance_table = distance_table
        return distance_table

    def sort_colors(self):
        """
        Sort colors by distance

        :return: Sorted color indices
        """

        # Create an empty list
        sorted_colors = []

        # We start with the first color
        start_val = 0
        sorted_colors.append(start_val)

        # Loop distance_table_size times
        for i in range(0, len(self.__distance_table)):

            # Getting the closest color
            next_val = self.__distance_table.nearest(start_val, sorted_colors)

            # Break if there are no more colors
            if next_val is None:
                break

            # Add the next color
            sorted_colors.append(next_val)

            # Change the starting value
            start_val = next_val

        # Set property and return it's value
        self.__sorted_colors = sorted_colors
        return sorted_colors

    def group_colors(self):
        """
        Group colors by distance

        :return: Grouped colors
        """

        dists = [0]

        # Loop over each color
        for i in range(0, len(self.__sorted_colors) - 1):

            # Get two consecutive colors
            color1_id = self.__sorted_colors[i]
            color2_id = self.__sorted_colors[i + 1]

            # Calculate distance between them
            dists.append(self.__distance_table.get(color1_id, color2_id))

        # TODO: Implement grouping (auto-way)
