#!/usr/bin/python3

def remove_char_at(str, n):
    return str if n < 0 else str[0:n] + str[n+1:]
