#!/usr/bin/python
#!/usr/bin/env python
#coding:utf-8
#
print 'hello world'
d = '%(who)s %(verb)s %(what)s' % {'who':'i','verb':'play','what':'python'}
print d
d = '%(who)s%(verb)s%(what)s'% {'who':'i','verb':'play','what':'python'}
print d
a = 'i'
b = 'play'
c = 'pyhon'
d = '%s%s%s' % (a,b,c)
print d
d = '{0}{1}{2}'.format(a,b,c)
print d
d = '{x} {y}'.format(x='i',y='do')
print d