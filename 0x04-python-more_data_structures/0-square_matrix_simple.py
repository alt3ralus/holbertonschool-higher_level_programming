#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    new = [list(map((lambda x: x * x), position)) for position in matrix]
    return new
