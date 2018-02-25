import abc


class MountebankClient(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def activate_impostor(self, impostor):
        pass

    @abc.abstractmethod
    def deactivate_impostor(self, impostor):
        pass

    @abc.abstractmethod
    def send_to_impostor(self, impostor, **kwargs):
        pass

    @abc.abstractmethod
    def get_impostor(self, impostor):
        pass

    @abc.abstractmethod
    def __enter__(self):
        pass

    @abc.abstractmethod
    def __exit__(self, *args, **kwargs):
        pass
