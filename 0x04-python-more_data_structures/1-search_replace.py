def search_replace(my_list, search, replace):


    new_list = []
    for item in my_list:
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)
    return new_list


print(search_replace([4, 5, 5, 6, 9, 0, 5, 5], 0, 'badass'))