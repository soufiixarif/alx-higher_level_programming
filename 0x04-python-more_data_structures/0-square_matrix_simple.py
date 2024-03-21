#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for line in matrix:
        squared_line = []
        for num in line:
            squared_line.append(num * num)
        squared_matrix.append(squared_line)
    return squared_matrix
