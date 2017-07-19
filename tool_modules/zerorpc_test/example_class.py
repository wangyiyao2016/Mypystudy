'''
Created on Dec 25, 2016

@author: jack
'''
import zerorpc


class Cooler(object):
    """ Various convenience methods to make things cooler. """

    def add_man(self, sentence):
        """ End a sentence with ", man!" to make it sound cooler, and
        return the result. """
        return sentence + ", man!"

    def add_42(self, n):
        """ Add 42 to an integer argument to make it cooler, and return the
        result. """
        return n + 42

    def boat(self, sentence):
        """ Replace a sentence with "I'm on a boat!", and return that,
        because it's cooler. """
        return "I'm on a boat!"


if __name__ == '__main__':
    s = zerorpc.Server(Cooler())
    s.bind("tcp://0.0.0.0:4242")
    s.run()

    pass

"""$ zerorpc -j tcp://localhost:4242 add_42 1
43
$ zerorpc tcp://localhost:4242 add_man 'I own a mint-condition Volkswagen Golf'
"I own a mint-condition Volkswagen Golf, man!"
$ zerorpc tcp://localhost:4242 boat 'I own a mint-condition Volkswagen Golf, man!'
"I'm on a boat!"
"""
