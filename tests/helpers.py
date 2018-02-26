import os


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


def is_process_active(pid):
    try:
        os.kill(pid, 0)
    except OSError:
        return False

    return True
