import abc


class Installer(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def install(self, path):
        pass

    @abc.abstractmethod
    def find_exe(cls, mountebank_path):
        pass
