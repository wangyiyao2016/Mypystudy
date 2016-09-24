#!/usr/bin/env python
#coding=utf-8

"""
1.定义一个cap_str(name)，该函数效果如下(提示用到字符串的内置方法).

# assert cap_str("xiaoming") == "Xiaoming"
# assert cap_str("dashagua") == "Dashagua"
# assert cap_str("Xiaoxigua") == "Xiaoxigua"
"""
#def cap_str(a):
#    '''
#    cap_str(name)
#    '''
#    if not isinstance(a,str):
#        return 'Error'
#    else:
#        b = a.capitalize()
#        return b
#
#assert cap_str("xiaoming") == "Xiaoming"
#assert cap_str("dashagua") == "Dashagua"
#assert cap_str("Xiaoxigua") == "Xiaoxigua"
#





"""
2.定义一个函数,需要实现效果如下。

#迭代函数后，实现如下效果输出

l = func(1,2,3,4,5)
for i in l:
    print i,
#输出 1 2 3 4 5

l = func(5,3,4,5,6)
for i in l:
    print i,

#输出 5 3 4 5 6
"""

def func(*a):
    '''
    doc
    '''
    return a

l = func(1,2,3,4,5)
for i in l:
    print i,
#输出 1 2 3 4 5

l = func(5,3,4,5,6)
for i in l:
    print i,

#输出 5 3 4 5 6


"""
3.定义一个func(*kargs)，该函数要实现下面 断言 中的各个条件.

# assert func(213,356,'mypython','hello world') == 'mypython'
# assert func(888,666,'mynamepy','ABC') == 'mynamepy'
# assert func(1,2,3,4) == None
"""



#def func(*kargs):
#    
#    a = filter(lambda x:isinstance(x,str),kargs)
#    
#    if not a:
#        return None
#    
#    else:
#        return a[0]
#assert func(213,356,'mypython','hello world') == 'mypython'
#assert func(888,666,'mynamepy','ABC') == 'mynamepy'
#assert func(1,2,3,4) == None



"""
4.定义一个func(name=None,**kargs),该函数效果如下

# assert func("xiaoming") == "xiaoming"
# assert func("xiaoming",years=4) == "xiaoming,years:4"
# assert func("lilei", years=4,weight=20) == "lilei,weight:20,years:4"
"""

#def func(name=None,**kargs):
#    '''
#    Doc
#    '''
#    a = ['%s:%s' % (p,o) for p,o in kargs.items()]
#    a.insert(0,name)
#    return ','.join(a)
#assert func("xiaoming") == "xiaoming"
#assert func("xiaoming",years=4) == "xiaoming,years:4"
#assert func("lilei", years=4,weight=20) == "lilei,weight:20,years:4"





"""
5.举一个小例子，说明 函数位置参数，默认参数， 元组匹配收集，字典匹配收集方法，
就是一个函数，上面参数全要用到，举例说明一下。
"""






"""
6. 首先查看 range(-10,10)返回的是什么？
     再用 filter 和 lambda 实现结果为 [6, 7, 8, 9]
"""

#print range(-10,10)
#
#a = filter(lambda x:x>=6,xrange(-10,10))
#
#print a