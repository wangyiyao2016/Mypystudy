#!/usr/local/bin/python
# encoding: utf-8
'''
Created on Jun 21, 2017

@author: Jack

tool_modules.random_line.main is a description

'''
from linecache import getline
from random import uniform, randrange


degree = randrange(1, 10001)
file_path = "test.txt"


def main():
    while True:
        lino = randrange(1, 10001)
        unikey = getline(file_path, lino)
        print(unikey)


if __name__ == '__main__':
    main()
    pass
