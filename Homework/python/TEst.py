#!/usr/bin/env python
#-*- coding:utf-8 -*-







#3 定义一个方法test_list(l), 参数l类型是列表，如何才能保证在函数体内对参数l进行修改，不影响原来   原始的列表a。
#
# (也就是说，传入可变参数a，函数内进行操作，如何不影响函数外的列表。)


#def test_list(l):
#    '''
#    listtest .doc
#    '''
#    a = l[:]
#    return a
#
#l = ['4', '1', '5', '4', '5', '1', '8', '9', '4', '5', '1', '6', '4', '9', '8']
#print test_list(l)

#2 定义一个方法get_sum(),求1-100范围内的所有数的平方和, 返回结果为整数类型。
#  做好断言。
#
#
#def get_sum(a):
#    '''
#    quadratic sum
#    '''
#    for i in xrang(a+1):
#        i == i ** 2
#        
#        
#        assert x == int, 'calculation wrong'
        


        
    
    



#1 定义一个方法get_doc(func),func参数为任意一个函数对象，返回该函数对象的描述文档，
#  如果该函数没有描述文档，则返回"Not found."


#def get_doc(func):
#    '''
#    get   fgffgdoc
#    '''    
#
#    if func.__doc__ != None:
#        return func.__doc__
#    else:
#        return 'Not found'        
#
#print get_doc(get_doc)
    



def get_num(n):
    '''
    ddddd
    '''
    l = []
    for i in n:
        if isinstance(i, int) == True and i%2 == 0:
            l.append(i)
        else:
            print 'non integer'
    return l
x = ['4', '1', '5', 4, '5', '1', '8', 9, '4', '5', '1', '6', 4, '9', 8]
print get_num(x)