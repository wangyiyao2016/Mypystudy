#!/usr/bin/env python
#coding:utf-8

def Fibonacci(a):
	'''
	Doc
	'''
	n, x, y = 0, 0, 1
	while n < a:
		z = yield y
		x, y = y, x+y
		n = n+1


x = input('type into a integer: ')
F1 = Fibonacci(x)

for i in F1:
	print i

'''

斯巴达Python_进阶篇18_Python协程yield生成器'''