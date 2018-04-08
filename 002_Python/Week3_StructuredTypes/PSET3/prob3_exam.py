#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 23:50:50 2018

@author: markt
"""

def count7(N):
    '''
    N: a non-negative integer
    '''
    if N < 10:
        if N % 10 == 7:
            return 1
        else:
            return 0
    elif N % 10 == 7:
        return 1 + count7(N // 10)
    else:
        return count7(N // 10)
    
x = count7(7747)
print(x)