from mountequist.installers.base import Installer


windows_mountebank_link = (
    "https://s3.amazonaws.com/mountebank/v1.14/mountebank-v1.14.0-win-x64.zip")


class WindowsWeb(Installer):
    def __init__(self):
        pass

    def install(self, path):
        pass

    @classmethod
    def _download(cls, mountebank_link):
        pass

    @classmethod
    def _extract(cls, zip_file_path, mountebank_path):
        pass

    @classmethod
    def _install(cls, mountebank_link, mountebank_path):
        zip_file_path = cls._download(mountebank_link)
        cls._extract(zip_file_path, mountebank_path)

        return cls._find_exe(mountebank_path)
