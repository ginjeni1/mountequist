from collections import Iterable


def list_or_none(value):
    if value is not None:
        if isinstance(value, Iterable):
            return value
        else:
            return [value]

    return None
