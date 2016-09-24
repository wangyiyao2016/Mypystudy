#!/usr/bin/env python
#coding=utf-8
'''
斯巴达Python_进阶入门03_抽象 函数_第二节课
==============================================

以下所有题目，能做断言的，尽量都做好断言。:)

1 定义一个方法get_num(n),n参数是列表类型，判断列表里面的元素是否为数字类型，其他类型则报错，最  终返回一个偶数列表：（注：列表里面的元素为偶数)

'''

def get_num(n):
    
    l1 = []
    for i in n:
        if isinstance(i,int) or isinstance(i,float) or isinstance(i,long):
            if i%2 == 0:
                l1.append(i)
            else:
                print i,'is not an even integer'
        elif isinstance(i, str):
            print i , 'is Not number type, error'
        
        else:
            print str(i), 'is an error'
    return l1    
x = input('enter a list: ')
print get_num(x)






'''

2 定义一个方法get_page(url),url参数是需要获取网页内容的网址，返回网页的内容。
  提示（可以简单了解一下Python的urllib模块)
'''


#import urllib
#
#
#def get_page(url):
#    
#    if isinstance(url, str):
#        f = urllib.urlopen(url)
#        return f.read()
#    else:
#        s_url = str(url)
#        f1 = urllib.urlopen(s_url)
#        return f1.read()        
#
#
#url = raw_input('input an address: ')
#
#print get_page(url)







'''
3 定义一个方法 func，该func引入任意多的列表参数，返回所有列表中最大的那个元素。

'''



#def fun(*arg):
#    '''
#    maximum item in these list
#    '''
#    l = []
#    for i in arg:
#        if isinstance(i,list):
#            l.append(max(i))
#            
#        else:
#            pass
#    return max(l)
#
#
#a = [1,2,56,4,48,484,84,94,1.5,4848,5.555,989.0]
#b = [2,5,455,48.55,47]
#
#print fun(a,b)
#

'''
========================================
玩蛇网 www.iplaypython.com
斯巴达 QQ: 315799180

'''

