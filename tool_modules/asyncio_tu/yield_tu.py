#!/usr/bin/env python
# encoding: utf-8
'''
Created on Feb 4, 2017

@author: Jack
'''


def g(x):
    yield from range(x, 0, -1)
    yield from range(x)

g_obj = g(4)


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


def ytest(x):
    l = []
    while True:
        a = yield from range(x)
        l.append(a)
        yield l

if __name__ == '__main__':
    #  ===========================================================================
    # a = ttt()
    # r = next(a)
    # rs = a.send(1)
    # r2 = next(a)
    # for i in a:
    #     print(i)
    #  ===========================================================================
    tallies = []
    acc = gather_tallies(tallies)
    next(acc)
#     acc.send(5)
    for i in range(4):
        acc.send(i)
    acc.send(None)
    for i in range(5):
        acc.send(i)
    acc.send(None)
    print(tallies)
    pass
