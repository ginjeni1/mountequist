import abc


class Predicate(object):
    __slots__ = ("parameters", )
    __metaclass__ = abc.ABCMeta
    operator = None

    def __init__(self, parameters=None):
        self.parameters = parameters

    def as_dict(self):
        result = {self.operator: self.get_value_as_dict()}
        if self.parameters is not None:
            parameters = [parameter.as_dict() for parameter in self.parameters]
            for parameter in parameters:
                result.update(parameter)

        return result

    @abc.abstractmethod
    def get_value_as_dict(self):
        pass
