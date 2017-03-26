#!/usr/bin/env python
# encoding: utf-8
'''
Created on Feb 26, 2017

@author: Jack
'''


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b"Hello World"]


if __name__ == '__main__':
    pass
