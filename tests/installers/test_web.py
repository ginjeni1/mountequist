import os
import sys
import zipfile

import pytest

from mountequist import installers
from mountequist.installers.web import NODE_FILENAME
from mountequist.util import get_root_mountebank_path
from tests.defaults import DEFAULT_TEST_PATH

windows_only = pytest.mark.skipif(sys.platform != "win32", reason="Windows Only")


@windows_only
def test_windows_can_download(mark_for_removal):
    installer = installers.WindowsWeb()
    zip_file_path = installer._download(installer.link, DEFAULT_TEST_PATH)

    mark_for_removal(zip_file_path)
    assert zip_file_path
    assert os.path.exists(zip_file_path)
    with zipfile.ZipFile(zip_file_path) as zip_file:
        assert zip_file.testzip() is None


@windows_only
def test_windows_can_extract(mountebank_zipfile):
    installer = installers.WindowsWeb()
    installer._extract(mountebank_zipfile, DEFAULT_TEST_PATH)
    root_path = get_root_mountebank_path(DEFAULT_TEST_PATH)

    assert NODE_FILENAME in os.listdir(root_path)


@windows_only
def test_windows_can_find_exe(mountebank_install):
    exe_path = installers.WindowsWeb.find_exe(DEFAULT_TEST_PATH)

    assert NODE_FILENAME in exe_path


@windows_only
def test_windows_can_install():
    installer = installers.WindowsWeb()
    installer.install(DEFAULT_TEST_PATH)
    root_path = get_root_mountebank_path(DEFAULT_TEST_PATH)

    assert NODE_FILENAME in os.listdir(root_path)


@windows_only
def test_windows_can_detect_installation(mountebank_install):
    assert installers.WindowsWeb.is_installed(DEFAULT_TEST_PATH)
