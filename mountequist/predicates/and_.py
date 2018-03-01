from mountequist.predicates.base import Predicate


class And(Predicate):
    __slots__ = ("child_predicates", ) + Predicate.__slots__
    operator = "and"

    def __init__(self, *child_predicates):
        super(And, self).__init__(None)
        self.child_predicates = child_predicates

    def _get_value_for_dict(self):
        return [child_predicate.as_dict() for child_predicate in self.child_predicates]
