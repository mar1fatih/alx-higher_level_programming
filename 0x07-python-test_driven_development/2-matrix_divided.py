#!/usr/bin/python3
"""matrix divided"""



def matrix_divided(matrix, div):
    """matrix"""
    c = 0
    if len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for i in matrix:
        for j in i:
            if type(j) not in (int, float) or len(i) == 0:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    j = len(matrix[0])
    for i in matrix:
        if len(i) != j:
            raise TypeError("Each row of the matrix must have the same size")
    
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
        
    new_matrix = [[round((j / div), 2) for j in i] for i in matrix]
    print(new_matrix)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")

