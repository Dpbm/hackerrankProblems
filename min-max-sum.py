#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    sorted_array = sorted(arr)
    
    min_sum = sum(sorted_array[:4])
    max_sum = sum(sorted_array[1:])
    
    print(min_sum, max_sum)
    # Write your code here

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

