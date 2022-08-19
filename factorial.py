#!/bin/python3

memo = {}

def extraLongFactorials(n):
    """
    factorial = 1
    
    for i in range(n, 1, -1):
        factorial *=  i
    print(factorial)
    """
    
    if n == 1:
        return 1

    if (n not in memo.keys()):
        memo[n] = n * extraLongFactorials(n - 1)

    
    return memo[n]
        
    
    
if __name__ == '__main__':
    n = 1200
    print(extraLongFactorials(n))

