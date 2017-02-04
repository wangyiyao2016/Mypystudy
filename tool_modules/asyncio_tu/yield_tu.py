#!/usr/bin/env python
# encoding: utf-8
'''
Created on Feb 4, 2017

@author: Jack
'''


def g(x):
    yield from range(x, 0, -1)
    yield from range(x)

def tt():
    while True:
        y = yield
        print("tt called", type(y), y)


def ttt():
    l = []
    while True:
        e = yield from tt()
        l.append(e)
        print(l)

# l = list(r)
# for i in r:
#     print(i)

def accumulate():
    tally = 0
    while True:
        next = yield
        if next is None:
            return tally
        tally += next


def gather_tallies(tallies):
    while True:
        tally = yield from accumulate()
        print(tally)
        tallies.append(tally)
        print(tallies)


if __name__ == '__main__':
#     a = ttt()
#     for i in a:
#         print(i)
    tallies = []
    acc = gather_tallies(tallies)
    next(acc)
    acc.send(5)
    for i in range(4):
        acc.send(i)
    pass
