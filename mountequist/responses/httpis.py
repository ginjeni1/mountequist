from mountequist.util import list_or_none


class HttpIs(object):
    __slots__ = ("status_code", "headers", "body", "mode", "behaviors")

    response_type = "is"

    def __init__(self, status_code=200, headers=None,
                 body=None, mode="text", behaviors=None):
        self.status_code = status_code
        self.headers = headers if headers is not None else {"Connection": "close"}
        self.body = body if body is not None else ""
        self.mode = mode
        self.behaviors = list_or_none(behaviors)

    def as_dict(self):
        result = {
            "statusCode": self.status_code,
            "headers": self.headers,
            "body": self.body,
            "_mode": self.mode}

        if self.behaviors is not None:
            behaviors = {}
            for behavior in self.behaviors:
                behaviors.update(behavior.as_dict())
            result["_behaviors"] = behaviors

        return {self.response_type: result}
