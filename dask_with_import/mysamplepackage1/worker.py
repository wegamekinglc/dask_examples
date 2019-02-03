# -*- coding: utf-8 -*-
u"""
Created on 2019-2-3

@author: cheng.li
"""

from mysamplepackage1.globaldata import Data

GLOBAL_DATA = Data(25)


def worker(i):
    print(GLOBAL_DATA[i])


if __name__ == '__main__':
    from dask.distributed import Client

    client = Client('127.0.0.1:8786')

    results = []
    for i in range(25):
        results.append(client.submit(worker, i))

    results = client.gather(results)


