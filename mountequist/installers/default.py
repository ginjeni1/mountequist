import sys

from mountequist.installers.base import Installer
from mountequist.installers.web import WindowsWeb


def get_default_installer():
    """
    :return: An instance of the default installer.
    :rtype: Installer
    """

    if sys.platform == "win32":
        return WindowsWeb()
    elif "linux" in sys.platform:
        raise NotImplementedError("Linux not yet supported.")
    else:
        raise NotImplementedError("OS not supported.")
