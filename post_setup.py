try:
    from setuptools.command.install import install
except ImportError:
    from distutils.command.install import install
import os
import shutil


class PostInstallCommand(install):
    """
    Post-installation for installation mode.
    """

    def run(self):
        """
        Run post-installation
        """

        install.run(self)
        self.create_home_path()

    def create_home_path(self):
        """
        Create home directory with config and web files
        """

        # Home directory
        directory = os.path.expanduser('~') + '/.smartrcs'

        # Recreating home directory
        if os.path.exists(directory):
            shutil.rmtree(directory)
        os.mkdir(directory)

        # Copy stuffs
        shutil.copytree('./config', directory + '/config')
        shutil.copytree('./web', directory + '/web')
