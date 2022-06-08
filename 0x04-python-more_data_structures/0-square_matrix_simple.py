def square_matrix_simple(matrix=[]):
    new_list = []
    for my_list in matrix:
        sub_list = []
        for i in my_list:
            sub_list.append(i * i)
        new_list.append(sub_list)
    return new_list


matrix = [
    
    [1, 2, 3], 
    [1, 2, 3],
    [3, 7, 8],
    [77, 66, 33]
]

print(square_matrix_simple(matrix))