def uniq_add(my_list=[]):
    sum = 0
    new_list = []
    for item in my_list:
        if item not in new_list:
            new_list.append(item)
    for item in new_list:
        sum += item
    return sum

print(uniq_add([1,2,2,2,2,2,2,2,2,1]))