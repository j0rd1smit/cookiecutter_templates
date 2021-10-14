import os

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

_PATH_ROOT = os.path.dirname(__file__)


setup(
    name="src",
    version="0.0.0",
    packages=find_packages(exclude=[]),
    long_description_content_type="text/markdown",
    license="Creative Commons Attribution-Noncommercial-Share Alike license",
    long_description="",
)
