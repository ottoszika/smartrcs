class CubeOrientation(object):
    """
    The :class:`CubeOrientation <CubeOrientation>` class.
    Rotations applied on the cube sometimes needs reorientation,
    so this class keeps tracking these orientation changes.
    """

    def __init__(self, faces=None):
        """
        Initialize a plain cube ore a reoriented one
        :param dict faces: Initial orientation
        """

        if faces is None:
            # Default orientation
            self.__faces = {
                'U': 'U',
                'L': 'L',
                'F': 'F',
                'R': 'R',
                'B': 'B',
                'D': 'D'
            }
        else:
            self.__faces = faces

    def rotate_ox_cw(self):
        """
        Rotate clockwise on OX axe

        :return: The new cube orientation
        :rtype: dict
        """

        self.__faces = {
            'U': self.__faces['F'],
            'L': self.__faces['L'],
            'F': self.__faces['D'],
            'R': self.__faces['R'],
            'B': self.__faces['U'],
            'D': self.__faces['B']
        }

        return self.__faces

    def rotate_ox_ccw(self):
        """
        Rotate counterclockwise on OX axe

        :return: The new cube orientation
        :rtype: dict
        """

        self.__faces = {
            'U': self.__faces['B'],
            'L': self.__faces['L'],
            'F': self.__faces['U'],
            'R': self.__faces['R'],
            'B': self.__faces['D'],
            'D': self.__faces['F']
        }

        return self.__faces

    def rotate_oy_cw(self):
        """
        Rotate clockwise on OY axe

        :return: The new cube orientation
        :rtype: dict
        """

        self.__faces = {
            'U': self.__faces['U'],
            'L': self.__faces['F'],
            'F': self.__faces['R'],
            'R': self.__faces['B'],
            'B': self.__faces['L'],
            'D': self.__faces['D']
        }

        return self.__faces

    def rotate_oy_ccw(self):
        """
        Rotate counterclockwise on OY axe

        :return: The new cube orientation
        :rtype: dict
        """

        self.__faces = {
            'U': self.__faces['U'],
            'L': self.__faces['B'],
            'F': self.__faces['L'],
            'R': self.__faces['F'],
            'B': self.__faces['R'],
            'D': self.__faces['D']
        }

        return self.__faces

    def rotate_oz_cw(self):
        """
        Rotate clockwise on OZ axe

        :return: The new cube orientation
        :rtype: dict
        """

        self.__faces = {
            'U': self.__faces['L'],
            'L': self.__faces['D'],
            'F': self.__faces['F'],
            'R': self.__faces['U'],
            'B': self.__faces['B'],
            'D': self.__faces['R']
        }

        return self.__faces

    def rotate_oz_ccw(self):
        """
        Rotate counterclockwise on OZ axe

        :return: The new cube orientation
        :rtype: dict
        """

        self.__faces = {
            'U': self.__faces['R'],
            'L': self.__faces['U'],
            'F': self.__faces['F'],
            'R': self.__faces['D'],
            'B': self.__faces['B'],
            'D': self.__faces['L']
        }

        return self.__faces

    @property
    def faces(self):
        """
        Get faces orientation

        :return: The cube faces orientation
        """
        return self.__faces
