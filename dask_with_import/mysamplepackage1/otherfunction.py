# -*- coding: utf-8 -*-
u"""
Created on 2019-2-3

@author: cheng.li
"""

from mysamplepackage1.globaldata import fetch_data


def internal_func(i):
    return fetch_data()[i]
