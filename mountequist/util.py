import os
from collections import Iterable
from mountequist.exceptions import InstallError


def list_or_none(value):
    if value is not None:
        if isinstance(value, Iterable):
            return value
        else:
            return [value]

    return None


def get_root_mountebank_path(path):
    elements = os.listdir(path)
    if "node.exe" in elements:
        return path

    try:
        folder_name = next((name for name in elements if "mountebank-v" in name))
    except StopIteration:
        raise InstallError("Could not find Mountebank root folder.")

    return os.path.join(path, folder_name)
