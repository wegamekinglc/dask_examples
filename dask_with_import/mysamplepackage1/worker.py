# -*- coding: utf-8 -*-
u"""
Created on 2019-2-3

@author: cheng.li
"""

from mysamplepackage1.globaldata import register_data
from mysamplepackage1.otherfunction import internal_func


def worker(i, data):
    register_data(data)
    print(internal_func(i))
