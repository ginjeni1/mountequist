import abc

from mountequist.installers.base import Installer
from mountequist.installers.default import get_default_installer


class Server(object):
    __metaclass__ = abc.ABCMeta
    __slots__ = (
        "mountebank_path", "port", "config_file_name",
        "local_host_only", "process", "installer")

    DEFAULT_PORT = 2525

    def __init__(self, mountebank_path, port=DEFAULT_PORT,
                 config_file_name=None, local_host_only=True, installer=None):
        """
        A Mountebank Server Instance
        :param mountebank_path: The Folder path of the Mountebank installation.
        :type mountebank_path: str
        :param port: The port to use for the server.
        :type port: int
        :param config_file_name: The name of the config file
        :type config_file_name: str
        :param local_host_only: If True Mountebank only accepts requests from localhost.
        :type local_host_only: bool
        :param installer: The installer to use when install is required.
        :type installer: Installer
        """
        self.mountebank_path = mountebank_path
        self.port = port
        self.config_file_name = config_file_name
        self.local_host_only = local_host_only
        self.process = None
        self.installer = installer if installer is not None else get_default_installer()

    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass

    @abc.abstractmethod
    def save_config_file(self):
        pass

    @abc.abstractmethod
    def load_config_file(self):
        pass
