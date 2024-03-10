#!usr/bin/python3
"""
This module defines a function that return a list of
lists integers representing the Pascal's triangle of n
"""


def pascal_triangle(n):
    """
          Generate Pascal's triangle of n rows.
          :param n: number of rows.
          :return: A lists of list of integers  representing the Pascal's triangle.
    """

    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            diagonal_left = triangle[i - 1][j - 1]
            diagonal_right = triangle[i - 1][j]
            sum_diagonals = diagonal_left + diagonal_right
            row.append(sum_diagonals)
        row.append(1)
        triangle.append(row)

    return triangle
