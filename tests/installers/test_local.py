import os
import sys
import zipfile

import pytest

from mountequist import installers
from mountequist.util import get_root_mountebank_path
from tests.defaults import DEFAULT_TEST_PATH

windows_only = pytest.mark.skipif(sys.platform != "win32", reason="Windows Only")


@windows_only
def test_windows_can_copy(mark_for_removal, mountebank_zipfile):
    copy_folder = os.path.join(DEFAULT_TEST_PATH, "zipcopy")
    if not os.path.exists(copy_folder):
        os.mkdir(copy_folder)

    installer = installers.WindowsLocal(mountebank_zipfile)
    zip_file_path = installer._copy_zip_file(mountebank_zipfile, copy_folder)

    mark_for_removal(zip_file_path)
    assert zip_file_path
    assert os.path.exists(zip_file_path)
    with zipfile.ZipFile(zip_file_path) as zip_file:
        assert zip_file.testzip() is None


@windows_only
def test_windows_can_extract(mountebank_zipfile):
    installer = installers.WindowsLocal(mountebank_zipfile)
    installer._extract(mountebank_zipfile, DEFAULT_TEST_PATH)
    root_path = get_root_mountebank_path(DEFAULT_TEST_PATH)

    assert installer.NODE_FILENAME in os.listdir(root_path)


@windows_only
def test_windows_can_find_exe(mountebank_install):
    exe_path = installers.WindowsLocal.find_exe(DEFAULT_TEST_PATH)

    assert installers.WindowsLocal.NODE_FILENAME in exe_path


@windows_only
def test_windows_can_install(mountebank_zipfile):
    installer = installers.WindowsLocal(mountebank_zipfile)
    installer.install(DEFAULT_TEST_PATH)
    root_path = get_root_mountebank_path(DEFAULT_TEST_PATH)

    assert installer.NODE_FILENAME in os.listdir(root_path)


@windows_only
def test_windows_can_detect_installation(mountebank_install):
    assert installers.WindowsLocal.is_installed(DEFAULT_TEST_PATH)
