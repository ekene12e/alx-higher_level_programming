#!/usr/bin/python3
"""Takes in a matrix and divides by a given number

    Returns a new matrix
    args: matrix - input
          div - divisor to be used
"""


def matrix_divided(matrix, div):
    """Takes in a matrix and divides by a given number
        Args: matrix - input
              div - divisor to be used
    """

    for li in matrix:
        for j in li:
            if type(j) not in (int, float):
                raise TypeError('matrix must be a matrix (list of lists) \
of integers/floats')
    list_len = len(matrix[1])
    for li in matrix:
        if len(li) != list_len:
            raise TypeError('Each row of the matrix must have the same size')
    if type(div) not in (int, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = []
    for li in matrix:
        matx = []
        for j in li:
            matx.append(round((j / div), 2))
        new_matrix.append(matx)

    return new_matrix
