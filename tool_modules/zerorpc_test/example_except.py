'''
Created on Dec 26, 2016

@author: jack
'''

import zerorpc

class ExceptionalRPC(object):
    def bad(self):
        print("bad method called")
        raise Exception(":P")


if __name__ == '__main__':
    s = zerorpc.Server(ExceptionalRPC())
    s.bind("tcp://0.0.0.0:4242")
    s.run()