#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    x = list(map(lambda n: list(map(lambda s: s ** 2, n)), matrix))
    return x
