#-*-coding:utf-8-*- 
class Student(object):
    pass
def set_age(self,age):
    self.age=age
    
s = Student()
s.name='Michael'
print s.name

from types import MethodType
s.set_age = MethodType(set_age,s,Student)
s.set_age(25)
print s.age