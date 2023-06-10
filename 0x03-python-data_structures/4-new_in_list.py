#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx in range(len(my_list)):
        local_list = list(my_list)
        local_list[idx] = element
        return local_list
    return my_list
