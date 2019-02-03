# -*- coding: utf-8 -*-
u"""
Created on 2019-2-3

@author: cheng.li
"""


if __name__ == '__main__':
    from dask.distributed import Client
    from mysamplepackage1.globaldata import Data
    from mysamplepackage1.worker import worker

    data = Data(25)

    client = Client('127.0.0.1:8786')

    results = []

    worker(2, data)
    for i in range(25):
        results.append(client.submit(worker, i, data))

    results = client.gather(results)
