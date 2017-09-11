#!/usr/bin/env python
import os, sys
from setuptools import setup, find_packages

setup(
    name = 'django-tidy',
    version = '0.1',
    url = 'https://github.com/JaapJoris/django-tidy',
    author = 'Jaap Joris Vens',
    author_email = 'jj@rtts.eu',
    license = 'GPL3',
    packages = find_packages(),
    include_package_data = True,
    install_requires = [
        'django >= 1.7.7',
        'pytidylib >= 0.3.2',
    ],
)
