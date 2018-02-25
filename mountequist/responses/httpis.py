class HttpIs(object):
    __slots__ = ("status_code", "headers", "body", "mode")

    response_type = "is"

    def __init__(self, status_code=200, headers=None, body=None, mode="text"):
        self.status_code = status_code
        self.headers = headers if headers is not None else {"Connection": "close"}
        self.body = body if body is not None else ""
        self.mode = mode

    def as_dict(self):
        return {
            self.response_type: {
                "statusCode": self.status_code,
                "headers": self.headers,
                "body": self.body,
                "_mode": self.mode}}
