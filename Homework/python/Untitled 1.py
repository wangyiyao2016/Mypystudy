#!/usr/bin/env python
#coding=utf-8


def get_content(f):
    """
    #4
    """
    with open(f,'r') as fl:
        return fl.read()
a = raw_input('enter the file path: ')    
print get_content(a)


#def get_doc(module):
#    """
#    #3
#    """
#    return module.__doc__
#
#a = raw_input('please enter an module name:\n')
#print get_doc(a)

#def test2(*args):
#    """
#    #2
#    """
#    return  max(args,key=len)
#x = ('ffdff4', 'ggnjnvjvn', '5', '4', '5', '1fffff12212', '11118', '9', '4', '5', '1', '6', '4', '9', '8')
##print test2('ffdff4', 'ggnjnvjvn', '5', '4', '5', '1fffff12212', '11118', '9', '4', '5', '1', '6', '4', '9', '8')
#
#print test2(x)
#name = raw_input('please enter your name: ')
#
#age = raw_input('your age: ')
#
#hobby = raw_input('what\'s your hobby: ')
#
#welcome = "My name is %s, %s years old, I like %s." % (name,age,hobby)
#
#print welcome


#a = 123 
#b = 234
#
#if b > a:
#    print "b > a"

#a = 123 
#b = 234  
#
#c = b is 234
#
#print a if c else b

#def test(a):
#    '''dfdfdfd
#    
#    fdfdf
#    '''
#    
#    l=[]
#	
#	l.append(a)
#	mx = max(l)
#    mi = min(l)
#    
#    return mx
#    return mi
#a = input('please enter integer: ')
#print test(a)
#
#help(test)
#hel
