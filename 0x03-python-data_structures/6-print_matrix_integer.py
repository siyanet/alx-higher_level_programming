#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            if col == matrix[-1][-1]:
                print(col, end="")
            else:
                print(col,end=" ")
        print("")
