import os

import pytest


@pytest.fixture
def mark_for_removal():
    temporary_file_handler = TemporaryFileHandler()
    with temporary_file_handler:
        yield temporary_file_handler.wrap


class TemporaryFileHandler(object):
    __slots__ = ("temporary_file_path",)

    def __init__(self):
        self.temporary_file_path = None

    def wrap(self, temporary_file_path):
        self.temporary_file_path = temporary_file_path

    def __enter__(self):
        pass

    def __exit__(self, *args, **kwargs):
        if self.temporary_file_path is not None:
            os.remove(self.temporary_file_path)
