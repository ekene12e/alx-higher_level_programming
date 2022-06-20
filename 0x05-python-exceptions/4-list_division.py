#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_list = []
    for i in range(list_length):
        try:
            div = (my_list_1[i] / my_list_2[i])
        except (TypeError, ValueError):
            print("wrong type")
            div_list.append(0)
        except IndexError:
            print("out of range")
            div_list.append(0)
        except ZeroDivisionError:
            print("division by zero")
            div_list.append(0)
        finally:
            print()   
    return div_list
