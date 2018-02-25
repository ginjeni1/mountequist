import abc


class Installer(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def install(self, path):
        pass
