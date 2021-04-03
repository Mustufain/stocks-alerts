#!/usr/bin/python
import os

from setuptools import setup, find_packages

SRC_DIR = os.path.dirname(__file__)
CHANGES_FILE = os.path.join(SRC_DIR, "CHANGES")

with open(CHANGES_FILE) as fil:
    VERSION = fil.readline().split()[0]


setup(
    name="stocks_alerting",
    provides=["stocks_alerting"],
    description="Job to get stocks data daily and generate alerts",
    version=VERSION,
    packages=find_packages(exclude=['test']),
    author="abbasmustufain@gmail.com",
    install_requires=['pyspark==3.0.0',
                      'python-json-logger==0.1.11'],
    entry_points={'console_scripts': [
        'stocks_alerting = stocks_alerting:main',
        'pyvertobuild = pyvertobuild.pyvertobuild:main']},
    include_package_data=True
)
