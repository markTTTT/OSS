#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 21:07:07 2018

@author: markt
"""

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    
    returns: list of keys mapped to unique integer values, in ascending order
    '''
    output = []
    copyDict = aDict.copy()
    
    for k, v in aDict.items():
        del copyDict[k]
        if v not in copyDict.values():
            output.append(k)
        copyDict[k] = v
        
    output.sort()
    return output
    
print(uniqueValues({1: 1, 2: 1, 3: 3}))