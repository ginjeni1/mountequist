from mountequist.util import list_or_none


class Stub(object):
    __slots__ = ("predicates", "responses")

    def __init__(self, responses, predicates=None):
        self.predicates = list_or_none(predicates)
        self.responses = list_or_none(responses)

    def as_dict(self):
        result = {"responses": [response.as_dict() for response in self.responses]}
        if self.predicates is not None:
            result["predicates"] = [predicate.as_dict() for predicate in self.predicates]

        return result
