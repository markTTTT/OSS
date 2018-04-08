#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 20:26:54 2017

@author: markt
"""

# area + square of perimeter

import math

def polysum(n, s):
    """
    input <- n (# of sides) and s (length)
    return -> (area) + (square of perimeter) [rounded to x.xxxx]
    """
    area = (0.25 * n * s**2) / (math.tan(math.pi / n))
    perimeter = (n * s)**2
    sumPoly = round(area + perimeter, 4)
    return sumPoly
    
    