#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 21:55:10 2018

@author: markt
"""

def max_val(t):
    if type(t) == int:
        return t
    elif type(t) == tuple:
        return fn_for_tuple(t)
    else:
        return fn_for_loe(t)

def fn_for_tuple(t):
    if t == ():
        return 0
    elif t[0:1] == int:
        return max(t[0:1], fn_for_tuple(t[1:]))
    elif t[0:1] == list:
        return max(fn_for_loe(t[0:1]), fn_for_tuple(t[1:]))
    else:
        return max(fn_for_tuple(t[0:1]), fn_for_tuple(t[1:]))
   
def fn_for_loe(loe):
    if loe == []:
        return 0
    elif loe[0:1] == int:
        return max(loe[0:1], fn_for_loe(loe[1:]))
    elif loe[0:1] == list:
        return max(fn_for_loe(loe[0:1]), fn_for_loe(loe[1:]))
    else:
        return max(fn_for_tuple(loe[0:1]), fn_for_loe(loe[1:]))

max_val((1,4))




