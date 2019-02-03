# -*- coding: utf-8 -*-
u"""
Created on 2019-2-3

@author: cheng.li
"""

import io
from setuptools import setup
from setuptools import find_packages

setup(
    name='mysamplepackage1',
    version='0.1.0',
    description='',
    author='Cheng Li',
    author_email='wegamekinglc@hotmail.com',
    packages=find_packages(),
    include_package_data=False,
    install_requires=io.open("requirements.txt", encoding='utf8').read(),
)