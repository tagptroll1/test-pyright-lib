# Always prefer setuptools over distutils
from setuptools import setup

setup(
    name="lib",  # Required
    version="0.2",  # Required
    packages=["lib"],  # Required
    install_requirements=["requests==2.31.0"],
)
