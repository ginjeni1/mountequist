import subprocess

from mountequist.servers.base import Server


class WindowsServer(Server):
    __slots__ = Server.__slots__

    @classmethod
    def _find_exe(cls, mountebank_path):
        pass

    @classmethod
    def _find_config(cls, config_file_name):
        pass

    @classmethod
    def _get_exe_path(cls, mountebank_link, mountebank_path):
        try:
            exe_path = cls._find_exe(mountebank_path)
        except WindowsError:
            exe_path = cls._install(mountebank_link, mountebank_path)

        return exe_path

    @classmethod
    def _prepare_arguments(cls, config_file_name, port, local_host_only):
        args = tuple()
        if config_file_name and cls._find_config(config_file_name):
            args += "--configfile {}.ejs".format(config_file_name),

        if port != cls.DEFAULT_PORT:
            args += "--port {}".format(port),

        if local_host_only:
            args += "--localOnly",

        return args

    def start(self):
        exe_path = self._get_exe_path(
            self.mountebank_link,
            self.mountebank_path)

        args = self._prepare_arguments(
            self.config_file_name,
            self.port,
            self.local_host_only)

        process = subprocess.Popen()

    def stop(self):
        pass

    def save_config_file(self):
        pass

    def load_config_file(self):
        pass

