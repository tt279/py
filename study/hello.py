#-*-coding:utf-8-*- 
'''
Created on 2014年6月27日

@author: amssy
'''
class FooClass(object):
    """my very first class"""
    version = 0.1
    def __init__(self,nm='John Doe'):
            """constructor"""
            self.__name__=nm 
            print 'Created a class insstance for',nm
    def showname(self):
        print 'Your name is ', self.__name__
        print 'My name is', self.__class__.__name__
    def shower(self):
        "display class(static) attribute"
        print self.version
    def addMe2Me(self,x):
        """apply + operation to arguement"""
        return x+x
fool = FooClass()
x=fool.showname()
print x

