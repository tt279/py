#-*-coding:utf-8-*- 
'''
Created on 2014年7月23日

@author: amssy
'''
class Animal(object):
    def run(self):
        print 'Animal is running...'

class Dog(Animal):
    def run(self):
        print 'Dog is running...'

class Cat(Animal):
    def run(self):
        print 'Cat is running...'

dog = Dog()
dog.run()

cat = Cat()
cat.run()
fact = lambda x: reduce(int.__mul__, xrange(2, x + 1), 1)  
print fact(6) 