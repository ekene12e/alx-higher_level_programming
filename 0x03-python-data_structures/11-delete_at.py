#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if len(my_list) == 0 or idx >= len(my_list) or idx < 0:
        return my_list
    new_list = []
    count = 0
    for item in my_list:
        if idx != count:
            count += 1
            new_list.append(item)
    return new_list
