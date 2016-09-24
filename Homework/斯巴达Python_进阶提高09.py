#!/usr/bin/env python
#coding=utf-8

'''
斯巴达Python_进阶提高09_高级抽象_面对对象_类 Class03 
==================================================== 

一：Python是一门面向_对象___的编程语言。 
'''


'''
二： 写一个网页数据操作类，完成下面的功能： 

提示：网址为http://www.iplaypython.com/ ,需要用到urllib模块 

get_httpcode()获取网页的状态码，返回结果例如：200 类型要为int 

get_htmlcontent() 获取网页的内容。返回类型:str 

get_linknum()计算网页的链接数目。(可选题)
'''


import urllib 

a = 'http://www.iplaypython.com/' 

class get_content_from_website(object): 

    def get_htmlcontent(self, a): 
        content = urllib.urlopen(a) 
        return content.read()

t = get_content_from_website() 

print t.get_htmlcontent(a)

#其他的不会做诶

'''
三：类中的方法，第一个参数永远都是？ 
'''
self


'''
四：举例说明，类的继承关系，做好代码的注释。 
'''
class test(object):pass    

#test 就是object的子类

'''
五：怎么判断一个类是否为另一个类的子类？ 
'''

#issubclass(subclass, class) --> bull
'''
六：如何确定一个对象是否是一个类的实例？ 
'''
isinstance(instance, class)

'''
七：何谓封装？ 
'''
def  class  还有module 都是封装

'''
八：何谓多态？ 

'''
好像讲过 

