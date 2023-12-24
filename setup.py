# Always prefer setuptools over distutils
from setuptools import setup

setup(
    name="lib",  # Required
    version="0.3",  # Required
    packages=["lib"],  # Required
    install_requirements=["discord.py==2.3.2"],
)
