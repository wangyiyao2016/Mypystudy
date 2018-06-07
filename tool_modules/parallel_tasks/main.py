#!/usr/bin/env python
# encoding: utf-8
'''
Created on Oct 9, 2017

@author: Jack
'''
import concurrent.futures
from multiprocessing import Pool, TimeoutError
import time


def gen_data(path):
    with open(path) as f:
        progress_point = 0
        for i in f:
            progress_point += 1
            i = i.rstrip("\n")
            data = i.split(",")
            data.append(progress_point)
            data = (tuple(data))
            yield (data)


def test(v):
    if v % 3 == 0:
        time.sleep(3)
    #     raise TypeError
    return ("----", v)


def _main():
    f = open('data.txt')
    _ = list(range(1000))
    with concurrent.futures.ProcessPoolExecutor(max_workers=None) as executor:
        results = executor.map(test, _, chunksize=10)
        for i in results:
            print(i)
    f.close()
    print(f.closed)


def callback(a):
    print("callback called", a)
    return "not callable"


def error_callback(a):
    print("error_callback called")


def main():
    processes = None
    with Pool(processes=processes, maxtasksperchild=20) as pool:
        ids = range(1000)
        for i in ids:
            res = pool.apply_async(
                func=test, args=(i,), callback=callback,
                error_callback=error_callback
            )
            print(res.get(timeout=10))


if __name__ == '__main__':
    main()
    pass
