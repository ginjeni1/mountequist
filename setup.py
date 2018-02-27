from setuptools import setup, find_packages

from mountequist import __version__

setup(
    name="Mountequist",
    version=__version__,
    description="Utility to help using Mountebank in automated testing.",
    packages=find_packages(
        exclude=[
            "*.tests",
            "*.tests.*",
            "tests.*",
            "tests"]),
    install_requires=["requests"])
