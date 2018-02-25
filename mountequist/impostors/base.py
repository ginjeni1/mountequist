import abc


class Impostor(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def as_dict(self):
        pass
