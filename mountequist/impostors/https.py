from mountequist.impostors import Http


class Https(Http):
    protocol = 'https'

    def __init__(self, mutual_authentication=False, **kwargs):
        super(Https, self).__init__(**kwargs)
        self.mutual_authentication = mutual_authentication

    def as_dict(self):
        result = super(Https, self).as_dict()

        if self.mutual_authentication:
            result['mutualAuth'] = True

        return result
