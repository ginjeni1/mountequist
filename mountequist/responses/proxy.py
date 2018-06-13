class Proxy(object):

    response_type = "proxy"

    def __init__(self, url, client_certificate=None, client_key=None):
        self.url = url
        self.certificate = client_certificate
        self.key = client_key

    def as_dict(self):
        proxy = {
            'to': self.url
        }
        if self.certificate:
            proxy['cert'] = self.certificate

        if self.key:
            proxy['key'] = self.key

        result = {
            self.response_type: proxy
        }

        return result
