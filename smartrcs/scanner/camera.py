# -*- coding: utf-8 -*-
import picamera
import io
from PIL import Image
from smartrcs.configurable.configurable import Configurable


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
        self.__camera = picamera.PiCamera()

    def load(self):
        """
        Load configuration from YAML
        """

        # Load configuration
        Configurable.load(self)

        # Set attributes from config
        for key, value in self._config.iteritems():
            setattr(self.__camera, key, value)

    def snapshot(self):
        """
        Take a snapshot

        :return: The snaphot image
        :rtype: Image
        """

        # Capture to stream
        stream = io.BytesIO()
        self.__camera.capture(stream, format='jpeg')

        # "Rewind" the stream to the beginning so we can read its content
        stream.seek(0)

        # Create image from stream
        image = Image.open(stream)

        return image
