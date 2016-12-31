#!/usr/bin/env python
# encoding: utf-8
'''
Created on Dec 31, 2016

@author: Jack
'''

import zerorpc

class StreamingRPC(object):
    @zerorpc.stream
    def streaming_range(self, fr, to, step):
        print("fr:{}, to:{}, step:{}".format(fr, to, step))
        return xrange(fr, to, step)

s = zerorpc.Server(StreamingRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()