#!/usr/bin/env python
# coding=utf-8
import os
import re

from setuptools import setup, find_packages


version = re.compile(r'VERSION\s*=\s*\((.*?)\)')


def get_package_version():
    "returns package version without importing it"
    base = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(base, "myext/__init__.py")) as initf:
        for line in initf:
            m = version.match(line.strip())
            if not m:
                continue
            return ".".join(m.groups()[0].split(", "))


def get_requirements():
    return open('requirements.txt').read().splitlines()


classes = """
    Development Status :: 4 - Beta
    Intended Audience :: Developers
    License :: OSI Approved :: BSD License
    Topic :: System :: Distributed Computing
    Programming Language :: Python
    Programming Language :: Python :: 2
    Programming Language :: Python :: 2.7
    Programming Language :: Python :: 3
    Programming Language :: Python :: 3.3
    Programming Language :: Python :: 3.4
    Programming Language :: Python :: 3.5
    Programming Language :: Python :: 3.6
    Programming Language :: Python :: Implementation :: CPython
    Programming Language :: Python :: Implementation :: PyPy
    Operating System :: OS Independent
"""
classifiers = [s.strip() for s in classes.split('\n') if s]


install_requires = get_requirements()


setup(
    name='myext',
    version=get_package_version(),
    description='Celery Myext',
    long_description=open('README.rst').read(),
    author='garenchan',
    classifiers=classifiers,
    packages=['myext'],
    install_requires=install_requires,
    package_data={'myext': []},
    entry_points={
        'console_scripts': [
            'myext = myext.__main__:main',
        ],
        'celery.commands': [
            'myext = myext.command:MyextCommand',
        ],
    },
)
