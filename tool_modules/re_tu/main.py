#!/usr/bin/env python
# encoding: utf-8
'''
Created on Aug 6, 2017

@author: Jack
'''
import re

string = "hdfs://host:8020/user/hive/warehouse/test.db/test"


pattern = r"host"

#         """

prog = re.compile(pattern)
result_s = prog.search(string)
result_m = prog.match(string)


def main():
    print(result_s)
    print(result_m)


if __name__ == '__main__':
    main()
    pass
