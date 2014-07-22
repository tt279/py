# -*- coding: UTF-8 -*- 
'''
Created on 2014年6月30日

@author: amssy
'''
def line(file):
    for line in file:yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []