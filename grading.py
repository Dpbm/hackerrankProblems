#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    for grade_index in range(len(grades)):
        grade = grades[grade_index]
        
        if( grade < 38 ):
            grades[grade_index] = grade
            continue
        
        next_multiple = 0
        last_number_of_grade = grade % 10
        
        if(last_number_of_grade in [0, 5]):
            next_multiple = grade + 5
        elif(last_number_of_grade < 5):
            next_multiple = grade + (5 - last_number_of_grade)
        else:
            next_multiple = grade + (10 - last_number_of_grade)
        
        difference = next_multiple - grade
        
        if(difference < 3):
            grades[grade_index] = next_multiple
        
    return grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

