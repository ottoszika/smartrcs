# -*- coding: utf-8 -*-
from smartrcs.configurable.configurable import Configurable
from handler import Handler
import json


class CameraHandler(Handler):
    """
    The :class:`CameraHandler <CameraHandler>` class.
    Handle camera configuration GET and POST requests
    """

    class Camera(Configurable):
        """
        Fake :class:`Camera <Camera>` class.
        Just to simulate configs
        """

        def __init__(self):
            """
            Initialize fake camera and config
            """

            # Initialize and load superclass
            Configurable.__init__(self)
            Configurable.load(self)

    def __init__(self, application, request, **kwargs):
        Handler.__init__(self, application, request, **kwargs)
        self.__camera = self.Camera()

    def get(self):
        """
        Handle GET request
        Write camera configuration to stream
        """

        config = self.__camera.get_config()
        self.write(config)

    def post(self):
        """
        Handle POST request
        Write camera configuration to config file
        """

        try:

            # Read body json and save it
            config = json.loads(self.request.body)
            self.__camera.set_config(config)
            self.__camera.save()

            # Success code
            self.write({'error': 0})
        except ValueError:

            # Error code
            self.write({'error': 1})
