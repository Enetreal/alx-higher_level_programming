#!/usr/bin/python3
"""This module defines a Pascal's Triangle"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle of n rows.

    Args:
    n (int): Number of rows for Pascal's triangle

    Returns:
    list: List of lists representing Pascal's triangle
    """

    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]
        for j in range(1, i):
            new_row.append(prev_row[j-1] + prev_row[j])
        new_row.append(1)
        triangle.append(new_row)

    return triangle