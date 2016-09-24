#!/usr/bin/python
#!/usr/bin/env python
#coding:utf-8


H = {"name":"xiaoming", "age":"25", "address":"Beijing", "phone":"13008565432"}

#H.pop('age')
#del H['address']
#H.pop('sss','bucuozai')
##print H.keys()
#print H['name']
#print H.get('name','bucunzai')
#print H.get('nam','bucunzai')
#print H
#
#H.pop('name')
#H['address'] = 'Beijing'

#H['age'] = ''
#h = {'age':''}
#H.update(h)
#print H

f = open('/home/jack/abc/test1.txt','w')

f.write('I like python')

f.close()
f = open('/home/jack/abc/test1.txt','a')

f.write('\nhello python')
f.close()




