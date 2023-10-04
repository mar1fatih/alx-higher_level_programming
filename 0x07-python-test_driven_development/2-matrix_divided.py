#!/usr/bin/python3
"""matrix devider"""


def matrix_divided(matrix, div):
    """matrix devider"""
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    length = set()
    for row in matrix:
        ln = len(row)
        length.add(ln)
    if len(length) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    new_matrix = []
    for row in matrix:
        new_row = []
        for x in row:
            new_row.append(round(x / div, 2))
        new_matrix.append(new_row)
    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
