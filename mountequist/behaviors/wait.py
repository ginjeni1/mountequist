from mountequist.behaviors.base import Behavior
from datetime import timedelta


class Wait(Behavior):
    def __init__(self, latency):
        self.latency = latency

    def as_dict(self):
        if isinstance(self.latency, timedelta):
            return {"wait": self._convert_timedelta()}
        else:
            return {"wait": self.latency}

    def _convert_timedelta(self):
        return self.latency.total_seconds() * 1000
