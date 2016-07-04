import subprocess
import logging
import os
from smartrcs.configurable.configurable import Configurable


class Bower(Configurable):
    """
    The :class:`Bower <Bower>` class.
    Bower dependency checker and installer
    """

    def __init__(self):
        """
        Initialize bower configuration and paths
        """

        # Initialize and load superclass
        Configurable.__init__(self)
        Configurable.load(self)

        self.__web_path = os.path.expanduser("~") + '/.smartrcs/web'

    def check_installed(self):
        """
        Check if dependencies were installed

        :return: True - if dependencies were installed, False - if not
        :rtype: bool
        """

        return self._config['installed']

    def install_dependencies(self):
        """
        Perform bower dependency installation
        """

        try:
            bower_version = subprocess.check_output(['bower', '--version'])
            print 'Using bower version: %s' % bower_version

            os.system('cd %s && bower install' % self.__web_path)

            self.mark_installed()
        except OSError:
            logging.error('Bower is not installed. Web UI won\'t work. Please install it using `npm install -g bower`.')

    def mark_installed(self):
        """
        Set installed to True in config file
        """

        self._config['installed'] = True
        self.save()
