#!/usr/bin/env python
# encoding: utf-8
'''
Created on Nov 6, 2017

@author: Jack
@note: https://blog.filippo.io/building-python-modules-with-go-1-5/
my test module not working yet, need more reading from the above blog
'''
import ctypes
lib_go = ctypes.cdll.LoadLibrary("sum.so")
print(lib_go.Sum(7, 11))


if __name__ == '__main__':
    pass
