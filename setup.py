"""Python setup.py for cli_gw package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("cli_gw", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="cli_gw",
    version=read("cli_gw", "VERSION"),
    description="Awesome cli_gw created by CaravanaCloud",
    url="https://github.com/CaravanaCloud/cli_gw/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="CaravanaCloud",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["cli_gw = cli_gw.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
