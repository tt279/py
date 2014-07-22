#-*-coding:utf-8-*- 
'''
Created on 2014年7月1日

@author: amssy
'''
dict8 = dict(x=1,y=2)
dict9 = dict8.copy()
#print dict8.setdefault('x',5)    #没有键添加，不做操作
#print   dict8  
s=set(['c','e','h','o','p','s','z'])
s.update('pypi')
print s

s.remove('z')
print s

s-=set('pypi')
print s

print 'k' in s
print 'z' not in s

print set('posh')== set('shop')
print len(s)

for eachLetter in 'Names':
    print 'current letter:',eachLetter
for eachVal in range(2,19,3):
    print "value is:" ,eachVal
f=open(r'E:\nginx.conf')
#print sum([len(word) for line in f for word in line.split()])
print sum(len(word) for line in f for word in line.split())

