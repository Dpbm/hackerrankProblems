#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def check_in_house(s, t, tree_point, update):
    new_fruit_position = tree_point + update
    
    if(new_fruit_position >= s and new_fruit_position <= t):
        return 1
    
    return 0
    
def countApplesAndOranges(s, t, a, b, apples, oranges):
    
    total_house_apples  = (sum([ check_in_house(s, t, a, apple)  for apple  in apples  ]))
    total_house_oranges = (sum([ check_in_house(s, t, b, orange) for orange in oranges ]))
    
    print(total_house_apples)
    print(total_house_oranges)
    
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

