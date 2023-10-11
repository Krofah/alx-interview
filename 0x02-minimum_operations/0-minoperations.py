#!/usr/bin/python3
"""
Module for calculating the fewest number of operations needed to result in exactly n H characters
"""

def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters
    """
    if n < 2:
        return 0
    
    ops = 0
    divisor = 2
    
    while n > 1:
        if n % divisor == 0:
            ops += divisor
            n //= divisor
        else:
            divisor += 1
    
    return ops

if __name__ == "__main__":
    n = 9
    result = minOperations(n)
    print("Number of operations:", result)
