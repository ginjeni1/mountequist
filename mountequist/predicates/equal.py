from mountequist.predicates.base import Predicate


class Equal(Predicate):
    __slots__ = ("fields", ) + Predicate.__slots__
    operator = "equals"

    def __init__(self, fields, parameters=None):
        super(Equal, self).__init__(parameters)
        self.fields = fields

    def _get_value_for_dict(self):
        return self.fields
