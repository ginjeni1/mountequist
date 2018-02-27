import requests

from mountequist.clients.base import MountebankClient
from mountequist.util import list_or_none


class Http(MountebankClient):
    __slots__ = ("base_url", "port", "impostors", "active_impostors")

    def __init__(self, base_url, impostors, port=2525):
        self.base_url = base_url
        self.port = port
        self.impostors = list_or_none(impostors)
        self.active_impostors = set()

    @property
    def imposters_url(self):
        return "{}:{}/imposters".format(self.base_url, self.port)

    def activate_impostor(self, impostor):
        if impostor in self.active_impostors:
            return

        result = requests.post(self.imposters_url, json=impostor.as_dict())
        if result.ok:
            port = result.json()["port"]
            impostor.port = port
            self.active_impostors.add(impostor)

    def deactivate_impostor(self, impostor):
        if impostor not in self.active_impostors:
            return

        impostor_url = "{}/{}".format(self.imposters_url, impostor.port)

        result = requests.delete(impostor_url)
        if result.ok:
            self.active_impostors.remove(impostor)

    def send_to_impostor(self, impostor, **kwargs):
        self.post_to_impostor(impostor, **kwargs)

    def post_to_impostor(self, impostor, **kwargs):
        impostor_url = "{}:{}".format(self.base_url, impostor.port)
        return requests.post(impostor_url, **kwargs)

    def get_impostor(self, impostor):
        impostor_url = "{}/{}".format(self.imposters_url, impostor.port)
        return requests.get(impostor_url)

    def __enter__(self):
        for impostor in self.impostors:
            self.activate_impostor(impostor)

        return self

    def __exit__(self, *args, **kwargs):
        for impostor in self.impostors:
            self.deactivate_impostor(impostor)

    # TODO Currently, a client does not support Server Made Impostors
    # TODO It should be possible to import Server impostors upon initializing the client
