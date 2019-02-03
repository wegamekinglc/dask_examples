# -*- coding: utf-8 -*-
u"""
Created on 2019-2-3

@author: cheng.li
"""


class Data:

    def __init__(self, n):
        print(f"init data with {n}")
        self.data = list(range(n))

    def __getitem__(self, item):
        return self.data[item]


def register_data(data):
    global GLOBAL_DATA
    GLOBAL_DATA = data


def fetch_data():
    global GLOBAL_DATA
    return GLOBAL_DATA
