#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not  None:
        values_list = list(a_dictionary.values())
        keys_list = list(a_dictionary.keys())
        max_score = max(values_list)
        max_score_index = values_list.index(max_score)
        max_score_key = keys_list[max_score_index]
        return max_score_key
    return None
