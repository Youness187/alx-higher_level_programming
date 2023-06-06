#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = number % 10
if number >= 0:
    print("Last digit of {0} is {1}".format(number, lastDigit), end=" ")
else:
    lastDigit = ((number * -1) % 10) * -1
    print("Last digit of {0} is {1}".format(number, lastDigit), end=" ")

if lastDigit == 0:
    print("and is 0")
elif lastDigit > 5:
    print("and is greater than 5")
else:
    print("and is less than 6 and not 0")
