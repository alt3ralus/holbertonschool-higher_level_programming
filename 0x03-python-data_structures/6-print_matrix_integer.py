#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    for fila in range(len(matrix)):
        for columna in range(len(matrix[fila])):
            if columna == (len(matrix[fila]) - 1):
                print("{:d}".format(matrix[fila][columna]), end="")
            else:
                print("{:d} ".format(matrix[fila][columna]), end="")
        print()
