import os
import shutil

from mountequist import exceptions
from mountequist.installers.base import Installer


class WindowsLocal(Installer):
    def __init__(self, zip_file_path):
        self.zip_file_path = zip_file_path

    def install(self, mountebank_path):
        if not os.path.exists(mountebank_path):
            os.makedirs(mountebank_path)

        zip_file_path = self._copy_zip_file(self.zip_file_path, mountebank_path)
        self._extract(zip_file_path, mountebank_path)
        os.remove(zip_file_path)
        exe_path = self.find_exe(mountebank_path)
        if exe_path is None:
            raise exceptions.InstallError("Could not install Mountebank.")

        return exe_path

    @classmethod
    def _copy_zip_file(cls, zip_file_path, mountebank_path):
        zip_file_name = os.path.split(zip_file_path)[-1]
        new_file_path = os.path.join(mountebank_path, zip_file_name)
        if new_file_path != zip_file_path:
            shutil.copyfile(zip_file_path, new_file_path)

        return new_file_path
