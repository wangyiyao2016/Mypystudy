'''
Created on Dec 26, 2016

@author: jack
'''

import zerorpc

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4242")


if __name__ == '__main__':
    try:
        c.bad()
    except Exception as e:
        print("An error occurred: %r" % e)
    pass
