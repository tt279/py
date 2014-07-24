#-*-coding:utf-8-*- 
'''
Created on 2014年7月23日

@author: amssy
'''
import json
try:
    import cPickle as pickle
except ImportError:
    import pickle

d = dict(name='Bob', age=20, score=88)   
pickle.dumps(d)
print json.dumps(d)

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print json.loads(json_str)