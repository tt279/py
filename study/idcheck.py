#-*-coding:utf-8-*- 
'''
Created on 2014年6月27日

@author: amssy
'''
import string
alphas =string.letters+'_'
nums=string.digits
print 'Welcome to the Identifier Checker v1.0'
print 'Testees must be at least 2 chars long.'
myInput = raw_input('Identifirer to test?\n')
if len(myInput)>1:
    if myInput[0] not in alphas:
        print '''invalid: first symbol must be alphabetic'''
    else:
        for otherChar in myInput[1:]:
            if otherChar not in alphas+nums:
                print '''invalid:remaining
                    sybmols mustbe alphanumeric'''
                break
        else:
            print "okay as an identifier"
            
            