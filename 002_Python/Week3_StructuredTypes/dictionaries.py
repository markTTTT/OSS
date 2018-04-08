#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 21:54:36 2018

@author: markt
"""

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    
    numValues = 0
    
    numKeys = len(aDict.keys())
    
    for k, v in aDict.items():
        numValues += len(aDict[k])
        
    return numValues

aDict = {'a':['book', 'read'], 'b':['cat']}

print(how_many(aDict))