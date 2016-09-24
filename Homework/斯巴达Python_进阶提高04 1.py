#!/usr/bin/env python
#coding=utf-8
'''
斯巴达Python_进阶提高04_抽象 函数_第三节课
==================================================

1 定义一个方法get_doc(func),func参数为任意一个函数对象，返回该函数对象的描述文档，
  如果该函数没有描述文档，则返回"Not found."
'''

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


'''
2 定义一个方法get_sum(),求1-100范围内的所有数的平方和, 返回结果为整数类型。
  做好断言。

'''

#def get_sum(a):
#    '''
#    quadratic sum
#    '''
#    l = []
#    for i in xrange(a+1):
#        l.append(i**2)
#    return sum(l)
#a = input('dddd :   ')
#x = get_sum(a)
#print x
#assert type(x) == int, 'calculation wrong'



'''
3 定义一个方法test_list(l), 参数l类型是列表，如何才能保证在函数体内对参数l进行修改，不影响原来   原始的列表a。

 (也就是说，传入可变参数a，函数内进行操作，如何不影响函数外的列表。)
'''


#def test_list(l):
#    '''
#    listtest .doc
#    '''
#    a = l[:]
#    a.insert(2,5)
#    return a
#
#l = ['4', '1', '5', '4', '5', '1', '8', '9', '4', '5', '1', '6', '4', '9', '8']
#print test_list(l)
#print l


'''
4 定义一个方法get_name(a),a参数为任意一个函数对象，判断函数是否可以调用，
  如果可调用，则返回该函数名(断言类型为str)，否则返回 “Error."。
'''

#def get_name(a):
#    '''
#    doc
#    '''
#    if callable(a):
#        return a.__name__
#    else:
#        return 'Error'
#    
#assert type(get_name(len)) == str,'not a function'
#
#print get_name(dir)
#print get_name(max)
'''
  (判断函数是否可调用，可以搜索或查询资料。)


========================================
玩蛇网 www.iplaypython.com
斯巴达 QQ: 315799180
'''