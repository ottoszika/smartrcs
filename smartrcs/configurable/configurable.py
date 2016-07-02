# -*- coding: utf-8 -*-
from os.path import expanduser
import yaml


class Configurable:
    """
    The :class:`Configurable <Configurable>` class.
    Defines a YAML configuration mapper
    """

    def __init__(self):
        """
        Initialize configuration file path
        """

        # Get full path of the config file
        self.__config_path = self.__get_config_path()
        self._config = None

    def load(self, config=None):
        """
        Load configuration and initialize the class
        :param dict config: Configuration value
        """

        # Set config with the parameter value
        self._config = config

        if config is None:
            # Store configuration in property
            stream = open(self.__config_path, 'r')
            self._config = yaml.load(stream)

    def __get_config_path(self):
        """
        Get full path of the config file

        :return: The YAML file full path
        :rtype: str
        """

        # Getting home path and config file from class name
        home = expanduser("~")
        config_file = self.__class__.__name__.lower() + '.yaml'

        # Build up config file fill path
        return home + '/.smartrcs/config/' + config_file

    def __write_to_config(self, data):
        """
        Write data to file
        :param str data: Data to be written to file
        """

        with open(self.__config_path, 'w') as outfile:
            outfile.write(data)

    def save(self):
        """
        Save to YAML
        """

        # Write to file
        self.__write_to_config(yaml.dump(self._config, default_flow_style=True))

    def get_config(self):
        """
        Getter for configuration
        """

        return self._config

    def set_config(self, config):
        """
        Setter for configuration
        """

        self._config = config
