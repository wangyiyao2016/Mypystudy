# -*- coding: utf-8 -*-

class Count_instance(object):
    count = 0
    def __new__(cls, *args, **kwargs):
        cls._instance = super(Count_instance, cls).__new__(cls, *args, **kwargs)
        cls.count += 1
        return cls._instance

a = Count_instance()
b = Count_instance()
c = Count_instance()
print a.count
print b.count
print c.count
print Count_instance.count
a.count = 100
print Count_instance.count



class A(object):
    var1 = 0
    def __init__(self):
        self.var2 = 1
        print self.var2, A.var1

obja=A()
objectB=A()

assert obja.var1==objectB.var1
assert obja.var2==objectB.var2

obja.var1=100
obja.var2=100
objectB.var1 = 200
objectB.var2 = 200

assert obja.var2==objectB.var2
assert obja.var1==objectB.var1 
    
    
    
