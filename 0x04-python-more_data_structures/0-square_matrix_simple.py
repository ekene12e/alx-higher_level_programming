#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    for my_list in matrix:
        sub_list = []
        for i in my_list:
            sub_list.append(i * i)
        new_list.append(sub_list)
    return new_list
