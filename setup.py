#!/usr/bin/env python
import os, sys
from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name = 'django-tidy',
    version = '0.1',
    author = 'Jaap Joris Vens',
    author_email = 'jj@rtts.eu',
    url = 'https://github.com/rtts/django-tidy',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    packages = find_packages(),
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
    ],
    python_requires = '>=3.8',
    install_requires = [
        'django >= 1.7.7',
        'pytidylib >= 0.3.2',
    ],
)
