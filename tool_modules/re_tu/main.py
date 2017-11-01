#!/usr/bin/env python
# encoding: utf-8
'''
Created on Aug 6, 2017

@author: Jack
'''
import re

string = "hdfs://host:8020/user/hive/warehouse/test.db/test"


pattern = r"host"

pattern_test = r"hdfs://"
#         """

prog = re.compile(pattern)
prog_test = re.compile(pattern_test)
result_s = prog.search(string)
result_m = prog_test.match(string)
result_sub = prog.sub("tsoh", string)


def main():
    print(result_s)
    print(result_m)
    print(result_sub)


line = 'asdf fjdk; afed, fjek,asdf, foo'

fields = re.split(r'([;,\s])\s*', line)
values = fields[::2]
delimiters = fields[1::2] + ['']

test = ''.join(v + d for v, d in zip(values, delimiters))

if __name__ == '__main__':
    main()
    pass
