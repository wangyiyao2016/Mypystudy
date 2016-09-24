#!/usr/bin/env python
#coding=utf-8

'''
3 定义一个方法 func，该func引入任意多的列表参数，返回所有列表中最大的那个元素。

'''


def func(*a):
    l = []
    for i in a:
        l.append(i) 

    return max(i)

a = [1,2,3,4,56,7,8,94,544]
b = ['fdfd',454,'4554','ffg4545']

print func(a,b)
