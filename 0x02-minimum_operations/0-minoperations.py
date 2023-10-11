#!/usr/bin/python3
""" Module for 0-minoperations"""


def minOperations(n):
    """
    minOperations
    Gets the fewest number of operations needed to result in exactly n H characters
    """
    if n < 2:
        return 0
    ops, root = 0, 2
    while root <= n:
        if n % root == 0:
            ops += root
            n = n // root  # Use integer division instead of regular division
            root -= 1
        root += 1
    return ops