import os
import shutil

import pytest

from mountequist.installers.default import get_default_installer
from mountequist.util import get_root_mountebank_path
from tests.defaults import DEFAULT_TEST_PATH


@pytest.fixture(scope="session")
def installer_zipfile():
    """
    This fixture allows to download the zip file only once per run.
    :return: Zip file Path
    """
    installer = get_default_installer()
    cache_path = os.path.join(DEFAULT_TEST_PATH, "CACHE")
    os.mkdir(cache_path)
    zip_file_path = installer._download(installer.link, cache_path)
    yield zip_file_path
    os.remove(zip_file_path)
    os.rmdir(cache_path)


@pytest.fixture(scope="session")
def mountebank_zipfile(installer_zipfile):
    file_name = os.path.split(installer_zipfile)[-1]
    zip_file_path = os.path.join(DEFAULT_TEST_PATH, file_name)
    shutil.copy(installer_zipfile, zip_file_path)
    yield zip_file_path
    try:
        os.remove(zip_file_path)
    except WindowsError:
        # Mountebank Install fixture may finish before this one.
        pass


@pytest.fixture(scope="session")
def mountebank_install(installer_zipfile):
    installer = get_default_installer()
    installer._extract(installer_zipfile, DEFAULT_TEST_PATH)
    folder_path = get_root_mountebank_path(DEFAULT_TEST_PATH)
    yield folder_path
    shutil.rmtree(folder_path)
