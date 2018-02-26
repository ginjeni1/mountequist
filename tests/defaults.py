import os
import sys


DEFAULT_TEST_PATH = (
    "C:\\temp\\mountest\\" if sys.platform == "win32" else "/test/mountest/")


if not os.path.exists(DEFAULT_TEST_PATH):
    os.makedirs(DEFAULT_TEST_PATH)
