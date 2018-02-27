import abc
import os
import zipfile

from mountequist.util import get_root_mountebank_path


class Installer(object):
    __metaclass__ = abc.ABCMeta

    NODE_FILENAME = "node.exe"

    @classmethod
    def is_installed(cls, mountebank_path):
        return cls.find_exe(mountebank_path) is not None

    @abc.abstractmethod
    def install(self, mountebank_path):
        pass

    @classmethod
    def find_exe(cls, mountebank_path):
        elements = os.listdir(mountebank_path)
        if not elements:
            return

        root_path = get_root_mountebank_path(mountebank_path)
        if cls.NODE_FILENAME in os.listdir(root_path):
            return os.path.join(root_path, cls.NODE_FILENAME)

    @classmethod
    def _extract(cls, zip_file_path, mountebank_path):
        with zipfile.ZipFile(zip_file_path) as zip_file:
            zip_file.extractall(mountebank_path)
