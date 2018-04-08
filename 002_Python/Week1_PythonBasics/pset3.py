#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 22:00:02 2017

@author: markt
"""

s = 'abcdefghijklmnopqrstuvwxyz'
s = s + ' '
prevLtr = '' 
curWord = '' 
longest = '' 

for letter in s:
    if prevLtr == '':
        prevLtr = letter 
        curWord += letter 
    else:
        if prevLtr <= letter:
            curWord += letter
        elif len(curWord) > len(longest):
            longest = curWord
            curWord = letter
        else:
            curWord = letter
        prevLtr = letter
            
print("Longest substring in alphabetical order is: " + longest)