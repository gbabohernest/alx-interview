#!/usr/bin/python3
"""This module defines a function for rotating 2D matrix"""


def rotate_2d_matrix(matrix):
    """ Rotates an n x n 2D matrix 90
        degreee clockwise in-place

    Args:
        matrix: List of lists representing the 2D matrix to be rotated.
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for row in matrix:
        row.reverse()
