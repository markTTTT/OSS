#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 21:44:04 2018

@author: markt
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    tupLen = len(aTup)
    outTup = ()
    i = 0
    while i < tupLen:
        outTup = outTup + (aTup[i],)
        i += 2
    return outTup

