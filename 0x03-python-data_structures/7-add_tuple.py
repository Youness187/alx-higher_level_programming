#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    tuple_a = list(tuple_a)
    for i in range(len_a):
        if i < len_b:
            tuple_a[i] += tuple_b[i]
    return tuple(tuple_a)
