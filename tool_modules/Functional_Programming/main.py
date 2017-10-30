#!/usr/bin/env python
# encoding: utf-8
'''
Created on Jan 30, 2017

@author: Jack
'''
from itertools import zip_longest
import functools


l = [0, 1, 2, 3, 4, 5, 6]
lr = iter(l)
ll = [1, 2, 3, 4, 5, 6]
l_null = []
r = all(l_null)
rv = any(l)


def tesfuc():
    pass


c = "ddddd21123"
c = "我身边有个  后天结巴的同学以前都不敢和他多说话"
ac = ascii(c)
i = 3
bi = bin(i)
cc = callable(tesfuc)

bc = c.encode(encoding='utf_8', errors='strict')
m_obj = memoryview(bc)

m = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 'Jun': 6,
     'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12}
mi = iter(m)

S = {2, 3, 5, 7, 11, 13}
si = iter(S)

line_list = ['  line 1\n', 'line 2  \n', ]

stripped_iter = (line.strip() for line in line_list)
stripped_list = [line.strip() for line in line_list]
stripped_list = [line.strip() for line in line_list
                 if line == ""]
seq1 = 'abc'
seq2 = (1, 2, 3)
a = [{x, y} for x in seq1 for y in seq2]


def generate_ints(N):
    for i in range(N):
        yield i


gen = generate_ints(3)
a, b, c = generate_ints(3)


# A recursive generator that generates Tree leaves in in-order.
def inorder(t):
    if t:
        for x in inorder(t.left):
            yield x

        yield t.label

        for x in inorder(t.right):
            yield x


def counter(maximum):
    i = 0
    while i < maximum:
        val = (yield i)
        # If value provided, change counter
        if val is not None:
            i = val
        else:
            i += 1


it = counter(5)


def log(message, subsystem):
    """Write the contents of 'message' to the specified subsystem."""
    print('%s: %s' % (subsystem, message))


x = [1, 2, 3]
y = [5, 6, 7]

xy = zip_longest(x, y)
if __name__ == '__main__':
    for i in xy:
        print(i)
    print(xy)
    server_log = functools.partial(log, subsystem='server')
    server_log('Unable to open socket')
