from mountequist.installers.base import Installer
from mountequist.installers.web import WindowsWeb


def get_default_installer():
    """
    :return: An instance of the default installer.
    :rtype: Installer
    """
    # TODO Currently only supports Windows
    return WindowsWeb()
