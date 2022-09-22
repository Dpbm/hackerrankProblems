#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    period_marker = s[8:]
    hours = int(s[:2])
    
    if (period_marker == 'AM' and hours >= 12):
        return f'{(hours - 12):02}:{s[3:8]}'
    elif (period_marker == 'PM' and hours < 12):
        return f'{(hours + 12):02}:{s[3:8]}'
    else:
        return s[:8]
        
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

