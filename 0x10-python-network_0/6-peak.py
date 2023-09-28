#!/usr/bin/python3
"""
Find a peak
"""


def find_peak(list_of_integers):
    """
    finds a peak in a list of unsorted integers.
    """
    if not list_of_integers:
        return None

    lng = len(list_of_integers)
    m = int(lng / 2)
    lst = list_of_integers

    if m + 1 >= lng:
        if m - 1 < 0:
            return lst[m]
        elif lst[m] > lst[m - 1]:
            return lst[m]
        else:
            return lst[m - 1]
    elif m - 1 < 0:
        if lst[m] > lst[m + 1]:
            return lst[m]
        else:
            return lst[m + 1]
    elif lst[m - 1] < lst[m] > lst[m + 1]:
        return lst[m]
    elif lst[m + 1] > lst[m - 1]:
        return find_peak(lst[m:])
    return find_peak(lst[:m])
