from mountequist.util import list_or_none
from mountequist.impostors.base import Impostor


class Http(Impostor):
    __slots__ = ("default_response", "port", "name", "stubs")

    protocol = "http"

    def __init__(self, stubs=None, default_response=None, port=None, name=None, record_requests=False):
        self.default_response = default_response
        self.port = port
        self.name = name
        self.stubs = list_or_none(stubs)
        self.record_requests = record_requests

    def as_dict(self):
        result = {"protocol": self.protocol}

        if self.stubs:
            result["stubs"] = [stub.as_dict() for stub in self.stubs]

        if self.default_response is not None:
            result["defaultResponse"] = self.default_response.as_dict()

        if self.port is not None:
            result["port"] = self.port

        result['recordRequests'] = self.record_requests

        return result
