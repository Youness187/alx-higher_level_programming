#!/usr/bin/python3
def roman_to_int(roman_string):
    romanN = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    my_sum = 0
    length = len(roman_string)
    if type(roman_string) != str or not roman_string:
        return my_sum
    for i in range(length):
        if (i != length - 1) and romanN[roman_string[i]] < romanN[roman_string[i + 1]]:
            my_sum += romanN[roman_string[i]] * -1
        else:
            my_sum += romanN[roman_string[i]]
    return my_sum
