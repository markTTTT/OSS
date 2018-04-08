# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def fancy_divide(list_of_numbers, index):
    try:
        try:
            raise Exception("0")
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
    except Exception as ex:
        print(ex)
        
fancy_divide([0,2,4],0)