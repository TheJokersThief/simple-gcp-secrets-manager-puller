#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='simple-gcp-secrets-manager-puller',
    version='1.0.0',
    description='Small abstraction for pulling secret values from GCP secrets manager',
    long_description='Small abstraction for pulling secret values from GCP secrets manager',
    author='Evan Smith',
    author_email='',
    url='https://github.com/TheJokersThief/simple-gcp-secrets-manager-puller',
    py_modules=['secretpuller'],
    packages=[
       'secretpuller',
    ],
    package_dir={'secretpuller': 'src'},
    scripts=[],
    test_suite='tests',
    include_package_data=True,
    zip_safe=False,
    keywords='',
    classifiers=[],
)
