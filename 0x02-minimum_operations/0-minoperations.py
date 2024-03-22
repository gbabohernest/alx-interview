#!/usr/bin/python3
"""
This module contains a function to calculate the fewest number
of operations needed to generate a specified number of 'H'
characters in a text file using Copy All and Paste operations.
"""


def minOperations(n):
    """
     Calculates the fewest number of operations needed
     to generate 'n' 'H' characters.

    :param n: (int) The target number of 'H' characters to generate.
    :return: (int)  The fewest number of operations needed to achieve
                    'n' 'H' characters. If 'n' is impossible to achieve,
                    returns 0.
    """

    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
            operations += factor
        else:
            factor += 1

    if n > 1:
        operations += n

    return operations
