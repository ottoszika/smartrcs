# -*- coding: utf-8 -*-
from smartrcs.configurable.configurable import Configurable
from smartrcs.hardware.camera import Camera
import cyclone
import json
import tempfile
import shutil
import uuid
from PIL import ImageDraw


class RecognizerHandler(cyclone.web.RequestHandler):
    """
    The :class:`RecognizerHandler <CameraHandler>` class.
    Handle recognizer configuration GET and POST requests
    """

    class Recognizer(Configurable):
        """
        Fake :class:`Recognizer <Camera>` class.
        Just to simulate configs
        """

        def __init__(self):
            """
            Initialize fake recognizer and config
            """

            # Initialize and load superclass
            Configurable.__init__(self)
            Configurable.load(self)

    def __init__(self, application, request, **kwargs):
        cyclone.web.RequestHandler.__init__(self, application, request, **kwargs)
        self.__recognizer = self.Recognizer()
        self.__camera = Camera()

    def get(self):
        """
        Handle GET request
        Write recognizer configuration or camera sample image to stream
        """

        # Get configuration type (img or json)
        conf_type = self.get_argument('type')

        if conf_type == 'json':
            # Write configuration to stream
            config = self.__recognizer.get_config()
            self.write(config)
        elif conf_type == 'img':
            # Write camera sample to stream
            self.set_header('Content-Type', 'image/jpg')

            data = self.__get_snapshot_data()

            # Write image to stream
            self.write(data)

            self.finish()

    def post(self):
        """
        Handle POST request
        Write recognizer configuration to config file
        """

        try:

            # Read body json and save it
            config = json.loads(self.request.body)
            self.__recognizer.set_config(config)
            self.__recognizer.save()

            # Success code
            self.write({'error': 0})
        except ValueError:

            # Error code
            self.write({'error': 1})

    def __get_snapshot_data(self):
        self.__camera.load()
        image = self.__camera.snapshot()

        # Draw marked facelet
        draw = ImageDraw.Draw(image)
        radius = int(self.__recognizer.get_config()['radius'])
        for cubie in self.__recognizer.get_config()['facelet']:
            draw.rectangle(((int(cubie[0]) - radius, int(cubie[1]) - radius),
                            (int(cubie[0]) + radius, int(cubie[1]) + radius)), fill=0)
        del draw

        # Creating temp paths
        dirpath = tempfile.mkdtemp()
        filepath = dirpath + '/' + str(uuid.uuid4()) + '.jpg'

        # Save image
        image.save(filepath)

        # Reopen file
        f = open(filepath, 'r')
        jpg_image = f.read()

        # Delete temp folder
        shutil.rmtree(dirpath)

        return jpg_image
