#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 21:38:42 2017

@author: markt
"""

# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal

balance = 320000
annualInterestRate = 0.2

monthlyIntRate = annualInterestRate / 12.0
lowerBound = balance / 12.0
upperBound = (balance * (1 + monthlyIntRate)**12) / 12.0
lowestPay = (lowerBound + upperBound) / 2

while True:
    testBalance = balance
    for i in range(12):
        testBalance = testBalance - lowestPay
        testBalance = testBalance + (monthlyIntRate * testBalance)
    if round(testBalance, 3) == 0.000:
        break
    elif testBalance > 0.0:
        lowerBound = lowestPay
        lowestPay = (lowerBound + upperBound) / 2
    else:
        upperBound = lowestPay
        lowestPay = (lowerBound + upperBound) / 2

roundLowestPay = round(lowestPay, 2)
print("Lowest Payment: " + str(roundLowestPay))
