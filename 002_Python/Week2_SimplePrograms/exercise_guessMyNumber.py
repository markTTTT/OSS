#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 13:02:02 2017

@author: markt
"""

# 0 inclusive, 100 not inclusive
low = 0
high = 100
guess = int((low + high) / 2)
inputChar = ''

print("Please think of a number between 0 and 100!")
while (True):
    print("Is your secret number " + str(guess) + "?")
    inputChar = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if inputChar == 'h':
        high = guess
        guess = int((low + high) / 2)
    elif inputChar == 'l':
        low = guess
        guess = int((low + high) / 2)
    elif inputChar == 'c':
        print("Game over. Your secret number was: " + str(guess))
        break
    else:
        print("Sorry, I did not understand your input.")
        