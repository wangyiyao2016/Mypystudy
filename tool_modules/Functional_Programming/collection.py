#!/usr/bin/env python
# encoding: utf-8
'''
Created on Sep 5, 2017

@author: Jack

'''
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y', 'x'], rename=True)
p = Point(11, 1, 22)
print(p)

if __name__ == '__main__':
    for i in p:
        print(i)
    pass
