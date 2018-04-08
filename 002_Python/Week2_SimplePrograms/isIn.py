#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 23:42:06 2017

@author: markt
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    lowC = 0
    highC = len(aStr)
    testC = int((lowC + highC)/2)
    
    if aStr == "":
        return False    
    else:
        if aStr[testC] == char:
            return True
        elif aStr[testC] < char:
            return isIn(char, aStr[testC+1:])
        else:
            return isIn(char, aStr[:testC])

print(isIn('o', 'aaaeffhjotuvzzz'))