#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not  None:
        values_list = []
        for key, value in a_dictionary:
            values_list.append(value)
        return max(values_list)
    return None
