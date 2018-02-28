import os
import signal
import subprocess
import time

from mountequist import exceptions, util
from mountequist.servers.base import Server

BIN_FILE = "mountebank/bin/mb"
STOP_TIMEOUT = 5


class WindowsServer(Server):
    __slots__ = Server.__slots__

    def _find_exe(self, mountebank_path):
        return self.installer.find_exe(mountebank_path)

    @classmethod
    def _find_bin_file(cls, mountebank_path):
        possible_path = os.path.join(mountebank_path, BIN_FILE)
        if os.path.exists(possible_path):
            return possible_path

        raise ValueError("Could not find BIN_FILE.")

    @classmethod
    def _find_config(cls, mountebank_path, config_file_name):
        try:
            element = next((element for element in os.listdir(mountebank_path)
                            if config_file_name == element))
            return os.path.join(mountebank_path, element)
        except StopIteration:
            return

    def _get_exe_path(self, mountebank_path):
        try:
            exe_path = self._find_exe(mountebank_path)
        except (WindowsError, exceptions.InstallError):
            exe_path = self.installer.install(mountebank_path)
            self.mountebank_path = util.get_root_mountebank_path(
                os.path.split(exe_path)[0])

        return exe_path

    @classmethod
    def _prepare_arguments(cls, mountebank_path, config_file_name=None,
                           port=None, local_host_only=None):
        bin_file = cls._find_bin_file(mountebank_path)
        args = (bin_file, )

        if config_file_name:
            if cls._find_config(mountebank_path, config_file_name):
                args += "--configfile {}".format(config_file_name),
            else:
                raise ValueError(
                    "Could not find config file {}".format(config_file_name))

        if port != cls.DEFAULT_PORT and port is not None:
            args += "--port {}".format(port),

        if (local_host_only is None and cls.DEFAULT_LOCAL_HOST_ONLY) or local_host_only:
            args += "--localOnly",

        return args

    def start(self):
        exe_path = self._get_exe_path(self.mountebank_path)
        args = self._prepare_arguments(
            mountebank_path=self.mountebank_path,
            config_file_name=self.config_file_name,
            port=self.port,
            local_host_only=self.local_host_only
        )
        self.mountebank_command_path = exe_path, args[0]
        self.process = subprocess.Popen((exe_path,) + args, cwd=self.mountebank_path)

    def stop(self):
        self.process.send_signal(signal.SIGTERM)
        try:
            self._poll_and_timeout(self.process)
        except exceptions.TimeoutError:
            raise exceptions.ProcessUnstoppableError("Could not stop server process.")
        self.process = None

    def save_config_file(self, config_file_name):
        if not config_file_name:
            raise ValueError("A proper config file name is required")

        try:
            # In the case described below, we keep any existing saves intact.
            correct_file_path = os.path.join(self.mountebank_path, config_file_name)
            default_file_path = os.path.join(self.mountebank_path, "mb.json")
            temp_rename = default_file_path + "_old"
            if os.path.exists(default_file_path):
                os.rename(default_file_path, temp_rename)

            # Send the command to mountebank and make sure it has no errors.
            args = self.mountebank_command_path + (
                    "save", "--savefile {}".format(config_file_name))
            process = subprocess.Popen(args, cwd=self.mountebank_path)
            return_code = self._poll_and_timeout(process)
            if return_code == 0:
                # Mountebank seems to use mb.json by default,
                # not caring about the savefile arg.
                # While this is the case, we will rename the file ourselves.
                if os.path.exists(correct_file_path):
                    os.remove(correct_file_path)

                os.rename(default_file_path, correct_file_path)
                if os.path.exists(temp_rename):
                    os.rename(temp_rename, default_file_path)

                return

            raise exceptions.MountebankError(
                "Could not save config file, "
                "Mountebank return code {}".format(return_code))
        except exceptions.TimeoutError:
            raise exceptions.MountebankError(
                "Could not save config file, process timed out.")

    def load_config_file(self, new_config_file):
        self.config_file_name = new_config_file
        self.stop()
        self.start()

        return_code = self.process.poll()
        if return_code is None:
            return

        raise exceptions.MountebankError(
            "Mountebank ended prematurely, return code {}".format(return_code))

    @classmethod
    def _poll_and_timeout(cls, process, timeout=STOP_TIMEOUT):
        while timeout:
            return_code = process.poll()
            if return_code is not None:
                return return_code
            time.sleep(0.1)
            timeout -= 0.1

        raise exceptions.TimeoutError()
