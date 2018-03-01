import abc


class Behavior(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def as_dict(self):
        pass
