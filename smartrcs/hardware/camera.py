# -*- coding: utf-8 -*-
try:
    import cv2
    from cv2 import cv
except ImportError:
    print 'OpneCV not installed!'

from PIL import Image
from ..configurable.configurable import Configurable


class Camera(Configurable):
    """
    The :class:`Camera <Camera>` class.
    Defines a camera module for Raspberry Pi
    """

    def __init__(self):
        """
        Initialize camera and config
        """

        # Initialize superclass
        Configurable.__init__(self)

        # Create camera instance
        self.__camera = None

    def load(self, config=None):
        """
        Load configuration from YAML
        :param dict config: Configuration value
        """

        # Load configuration
        Configurable.load(self, config)

        # Creating camera
        self.__camera = cv2.VideoCapture(int(self._config['port']))

        # Setting other attributes
        self.__camera.set(cv.CV_CAP_PROP_FRAME_WIDTH, int(self._config['resolution'][0]))
        self.__camera.set(cv.CV_CAP_PROP_FRAME_HEIGHT, int(self._config['resolution'][1]))

    def snapshot(self):
        """
        Take a snapshot

        :return: The snapshot image
        :rtype: Image
        """

        # Capture from camera and convert to PIL Image
        _, cv2_im = self.__camera.read()
        cv2_im = cv2.cvtColor(cv2_im, cv2.COLOR_BGR2RGB)
        pil_im = Image.fromarray(cv2_im)

        return pil_im
