#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_number = 0
    for i in my_list:
        if max_number >= i:
            continue
        else:
            max_number = i
    return max_number
