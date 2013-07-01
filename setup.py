#!/usr/bin/env python
import os
import urllib

from setuptools import setup, find_packages, Command

from cmsplugin_rst import __version__

setup(
    name = "cmsplugin_rst",
    version = __version__,
    packages = find_packages(),
    author = "Chris Spencer",
    author_email = "chrisspen@gmail.com",
    description = "A django-cms plugin for supporting Restructured Text.",
    license = "BSD",
    url = "https://github.com/chrisspen/cmsplugin_rst",
    classifiers = [
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    install_requires = [
        'django-cms>=2.0.0',
    ],
)
