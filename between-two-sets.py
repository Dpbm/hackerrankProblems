#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getFactors(a, target):
    numbers = []
    
    firstValue =  a[-1]
    step = 2 if len(a) % 2 == 0 else 1
    
    for num in range(firstValue, target + 1, step):
    
        divide = list(filter(None, [num % actualNumber == 0 for actualNumber in a]))
        
        if(len(divide) == len(a)): numbers.append(num)
        
    return numbers
    

def getDivisors(factors, b):
    numbers = []
    
    for factor in factors:
        totalNumbers = 0
        
        for num in b:
            if(num % factor == 0): totalNumbers += 1
        
        if(totalNumbers == len(b)): numbers.append(factor)
        
    return numbers
        
    
def getTotalX(a, b):
    a, b = sorted(a), sorted(b)

    factors = getFactors(a, b[0])
    total = len(getDivisors(factors, b))
    return total

if __name__ == '__main__':

    total = getTotalX([1], [72, 48])
    print(total)
