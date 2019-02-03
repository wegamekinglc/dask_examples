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
