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

        # Getting user id and group id
        uid = int(os.getuid())
        gid = int(os.getgid())

        # sudo?
        if uid == 0:
            uid = int(os.environ.get('SUDO_UID'))
            gid = int(os.environ.get('SUDO_GID'))

        # Home directory
        directory = os.path.expanduser('~') + '/.smartrcs'

        # Recreating home directory
        if os.path.exists(directory):
            shutil.rmtree(directory)
        os.mkdir(directory)

        # Copy stuffs
        shutil.copytree('./config', directory + '/config')
        shutil.copytree('./web', directory + '/web')

        # Set permissions
        os.system('chown -R %d:%d %s' % (uid, gid, directory))
