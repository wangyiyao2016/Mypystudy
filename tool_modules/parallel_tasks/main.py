#!/usr/bin/env python
# encoding: utf-8
'''
Created on Oct 9, 2017

@author: Jack
'''
from multiprocessing import Pool, TimeoutError
import concurrent.futures


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
    print("----", v)
#     raise TypeError
    return v


def _main():
    f = open('data.txt')
    _ = list(range(1000))
    with concurrent.futures.ProcessPoolExecutor(max_workers=None) as executor:
        results = executor.map(test, _, chunksize=10)
        for i in results:
            print(i)
    f.close()
    print(f.closed)


def main():
    with Pool(processes=4) as pool:
        _ = list(range(100))
        results = pool.apply_async(test, _,)
        print(results)
#         for i in results:
#             print(i)
#             pass
#             print(i)


if __name__ == '__main__':
    main()
    pass
