from mountequist.predicates.base import Predicate


class Not(Predicate):
    __slots__ = ("child_predicate", ) + Predicate.__slots__
    operator = "not"

    def __init__(self, child_predicate):
        super(Not, self).__init__(None)
        self.child_predicate = child_predicate

    def _get_value_for_dict(self):
        return self.child_predicate.as_dict()
