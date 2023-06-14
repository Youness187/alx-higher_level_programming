#!/usr/bin/python3
def roman_to_int(roman_string):
    romanN = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    my_sum = 0
    timp = 0
    if type(roman_string) != str or not roman_string:
        return my_sum
    for i in range(len(roman_string)):
        if romanN.get(roman_string[i], 0) == 0:
            return 0

        if romanN[roman_string[i]] <= timp or timp == 0:
            timp = romanN[roman_string[i]]
            my_sum += timp
        else:
            timp = romanN[roman_string[i]]
            my_sum = abs(my_sum - timp)
    return my_sum
