import os

import requests

from mountequist.exceptions import InstallError
from mountequist.installers.base import Installer

WINDOWS_LINK = (
    "https://s3.amazonaws.com/mountebank/v1.14/mountebank-v1.14.0-win-x64.zip")


class WindowsWeb(Installer):
    def __init__(self, link=None):
        self.link = link if link is not None else WINDOWS_LINK

    def install(self, mountebank_path):
        if not os.path.exists(mountebank_path):
            os.makedirs(mountebank_path)

        zip_file_path = self._download(self.link, mountebank_path)
        self._extract(zip_file_path, mountebank_path)
        os.remove(zip_file_path)
        exe_path = self.find_exe(mountebank_path)
        if exe_path is None:
            raise InstallError("Could not install Mountebank.")

        return exe_path

    @classmethod
    def _download(cls, link, mountebank_path):
        file_name = link.split('/')[-1]
        request = requests.get(link, stream=True)
        zip_file_path = os.path.join(mountebank_path, file_name)
        with open(zip_file_path, 'wb') as zip_file:
            for chunk in request.iter_content(1024):
                if chunk:
                    zip_file.write(chunk)

        return zip_file_path

    @classmethod
    def _install(cls, link, mountebank_path):
        zip_file_path = cls._download(link, mountebank_path)
        cls._extract(zip_file_path, mountebank_path)

        return cls.find_exe(mountebank_path)
