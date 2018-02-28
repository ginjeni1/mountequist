import os
import subprocess
import sys

import pytest

from mountequist import exceptions
from mountequist.servers import windows
from mountequist.util import get_root_mountebank_path
from tests.defaults import DEFAULT_TEST_PATH
from tests.helpers import is_process_active

windows_only = pytest.mark.skipif(sys.platform != "win32", reason="Windows Only")


@windows_only
def test_can_find_config(mark_for_removal, mountebank_install):
    config_file_path = os.path.join(mountebank_install, "test.json")
    with open(config_file_path, "w") as temp_file:
        temp_file.write("TEST")
    mark_for_removal(config_file_path)
    result = windows.WindowsServer._find_config(mountebank_install, "test.json")

    assert result == config_file_path


@windows_only
def test_properly_prepares_basic_argument(mountebank_install):
    args = windows.WindowsServer._prepare_arguments(
        mountebank_install,
        local_host_only=False)

    assert args[0] == os.path.join(mountebank_install, windows.BIN_FILE)
    assert len(args) == 1


@windows_only
def test_properly_prepares_all_arguments(mark_for_removal, mountebank_install):
    config_file_path = os.path.join(mountebank_install, "test")
    with open(config_file_path, "w") as temp_file:
        temp_file.write("TEST")

    mark_for_removal(config_file_path)

    args = windows.WindowsServer._prepare_arguments(
        mountebank_path=mountebank_install,
        config_file_name="test",
        port=3636)

    assert args[0] == os.path.join(mountebank_install, windows.BIN_FILE)
    assert "--configfile test" in args
    assert "--localOnly" in args
    assert "--port 3636" in args
    assert len(args) == 4


@windows_only
def test_can_start_and_stop_mountebank(mountebank_install):
    server = windows.WindowsServer(DEFAULT_TEST_PATH)
    with server:
        pid = server.process.pid
        assert server.process is not None
        assert server.process.poll() is None

    assert server.process is None
    assert is_process_active(pid) is False


@windows_only
def test_can_find_bin_file(mountebank_install):
    server = windows.WindowsServer(DEFAULT_TEST_PATH)
    with server:
        assert "mountebank/bin/mb" in server._find_bin_file(server.mountebank_path)


@windows_only
def test_can_save_config(mountebank_install):
    server = windows.WindowsServer(DEFAULT_TEST_PATH)
    with server:
        server.save_config_file("TEST.json")
        assert server._find_config(server.mountebank_path, "TEST.json")


@windows_only
def test_can_load_new_config(mountebank_install, mark_for_removal, sample_config):
    root = get_root_mountebank_path(DEFAULT_TEST_PATH)
    config_file_path = os.path.join(root, "example.json")
    mark_for_removal(config_file_path)
    with open(config_file_path, 'w') as config_file:
        config_file.write(sample_config)

    server = windows.WindowsServer(DEFAULT_TEST_PATH)
    with server:
        server.load_config_file("example.json")
        assert server.process.poll() is None


@windows_only
def test_succeeds_polling():
    process = subprocess.Popen("cmd")
    return_code = windows.WindowsServer._poll_and_timeout(process)
    assert return_code == 0


@windows_only
def test_properly_times_out_polling():
    process = subprocess.Popen("cmd /K")
    with pytest.raises(exceptions.TimeoutError):
        windows.WindowsServer._poll_and_timeout(process, 0.1)
    process.kill()


@pytest.fixture
def sample_config(mark_for_removal):
    return ('{"imposters": [{"protocol": "http","port": 61486,'
            '"stubs": [{"responses": [{"is": {"body": "All Ok","headers":'
            '{"Connection": "close"},"_mode": "text","statusCode": 200}}]}]}]}')
