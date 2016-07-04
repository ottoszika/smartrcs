import subprocess
import logging
import os
import yaml


class Bower:
    """
    The :class:`Bower <Bower>` class.
    Bower dependency checker and installer
    """

    def __init__(self):
        """
        Initializer (paths)
        """

        # Getting home path
        home = os.path.expanduser('~')

        # Config and web path
        self.__config_file = home + '/.smartrcs/config/bower.yaml'
        self.__web_path = home + '/.smartrcs/web'

    def check_installed(self):
        """
        Check if dependencies were installed

        :return: True - if dependencies were installed, False - if not
        :rtype: bool
        """

        stream = open(self.__config_file, 'r')
        bower_config = yaml.load(stream)
        return bower_config['installed']

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

        with open(self.__config_file, 'w') as outfile:
            data = yaml.dump({'installed': True}, default_flow_style=True)
            outfile.write(data)
