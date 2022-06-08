def common_elements(set_1, set_2):
    new_set = []
    for item in set_1:
        if item in set_2 and item not in new_set:
            new_set.append(item)
    print(new_set)

common_elements({'h', 56, 56, 'hello', 9, 56, 'h'}, {'hello', 56, 66, 8})