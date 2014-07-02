#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""A simple Django-like URL router for Tornado."""

from setuptools import setup


setup(
    name='torouter',
    version='0.0.1',
    author='RussellLuo',
    author_email='luopeng.he@gmail.com',
    description='URL router for Tornado',
    license='MIT',
    keywords='Tornado router',
    url='https://github.com/RussellLuo/torouter',
    py_modules=['torouter'],
    long_description=__doc__,
    install_requires=['tornado'],
)
