# -*- coding: utf-8 -*-
from smartrcs.configurable.configurable import Configurable
import numpy as np
import textwrap
from .color import Color
from .distancetable import DistanceTable


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

        # Notation face order
        self.__notation_keys = ['U', 'R', 'F', 'D', 'L', 'B']

    def load(self, config=None):
        """
        Load configuration from YAML
        :param dict config: Configuration value
        """

        Configurable.load(self, config)
        self.__cast_config()

    def __cast_config(self):
        """
        Cast configuration to match types
        """

        # Converting radius to integer
        self._config['radius'] = int(self._config['radius'])

        # Convert facelet cubie coordinates to integer
        for i in range(0, len(self._config['facelet'])):
            self._config['facelet'][i][0] = int(self._config['facelet'][i][0])
            self._config['facelet'][i][1] = int(self._config['facelet'][i][1])

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

    def __read_images(self):
        """
        Read all images

        :return: List of dominant colors
        :rtype: dict
        """

        # Here we will store dominant colors
        values = {}

        self.__facelets_values = []

        # Getting radius and coords from config
        radius = self._config['radius']
        facelet = self._config['facelet']

        # Loop over each face
        for index in self._config['order']:

            image = self.__face_images[index]

            # Initialize an empty list at index
            values[index] = []

            # Loop over each coords
            for cubie in facelet:

                # Crop image
                cubie_img = image.crop((cubie[0] - radius, cubie[1] - radius, cubie[0] + radius, cubie[1] + radius))

                # Calculate histogram
                cubie_hist = cubie_img.histogram()

                # Getting dominant color
                red = np.argmax(cubie_hist[0: 256])
                green = np.argmax(cubie_hist[256: 512])
                blue = np.argmax(cubie_hist[512: 768])

                # Create color and add to hash table
                color = Color(red, green, blue)
                values[index].append(color)

            self.__facelets_values.append(values[index])

        # Set property and return value
        self.__facelets = values
        return values

    def __create_distance_table(self):
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
        distance_table = DistanceTable(len(self._config['order']) * len(self._config['facelet']))

        # Fill distance table
        for i in range(0, len(colors_list)):
            for j in range(0, len(colors_list)):
                distance_table.add(i, j, colors_list[i].distance_to(colors_list[j]))

        # Set property and return
        self.__distance_table = distance_table
        return distance_table

    def __sort_colors(self):
        """
        Sort colors by distance

        :return: Sorted color indices
        :rtype: list
        """

        # Create an empty list
        sorted_colors = []

        # We start with the first color
        start_val = 0
        sorted_colors.append(start_val)

        # Getting distance table length
        dist_len = len(self.__distance_table)

        # Loop distance_table_size times
        i = 0
        while i < dist_len:

            # Getting the closest color
            next_val = self.__distance_table.nearest(start_val, sorted_colors)

            # Break if there are no more colors
            if next_val is None:
                break

            # Add the next color
            sorted_colors.append(next_val)

            # Change the starting value
            start_val = next_val

            i += 1

        # Set property and return it's value
        self.__sorted_colors = sorted_colors
        return sorted_colors

    def to_notation(self):
        """
        Convert to notation string

        :return: Notation string
        :rtype: str
        """

        # Read, create distance table and sort
        self.__read_images()
        self.__create_distance_table()
        self.__sort_colors()

        # Grouping obtained values from sort colors
        s_limit = int(len(self.__sorted_colors) / len(self._config['order']))
        s_range = range(0, len(self.__sorted_colors), s_limit)
        group_values = [self.__sorted_colors[x: x + s_limit] for x in s_range]

        # Getting each center value
        center_values = [x + int(s_limit / 2) for x in range(0, len(self.__sorted_colors), s_limit)]

        # Create center and group dict to store a key <-> value pair together with faces
        centers = {}
        groups = {}

        # Fill centers and groups
        for i in range(0, len(center_values)):
            centers[self.__notation_keys[i]] = center_values[i]
            for j in range(0, len(group_values)):
                if center_values[i] in group_values[j]:
                    groups[self.__notation_keys[i]] = group_values[j]
                    break

        # Build up notation
        notation = ''
        for i in range(0, len(self.__sorted_colors)):
            for index in self.__notation_keys:
                if i in groups[index]:
                    notation += index

        # Translate from order -> Notation keys
        trans_notation = ''
        for i in range(0, len(notation)):
            c = notation[i]
            c = self._config['order'][self.__notation_keys.index(c)]
            trans_notation += c

        # Create s_limit sized groups
        notation_groups = textwrap.wrap(trans_notation, s_limit)

        # Reorder notation
        notation = ''
        for index in self.__notation_keys:
            for i in range(0, len(notation_groups)):
                notation_chunk = notation_groups[i]
                if notation_chunk[int(s_limit / 2)] == index:
                    notation += notation_chunk
                    del notation_groups[i]
                    break

        return notation
