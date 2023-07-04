#!/usr/bin/python3

"""Creting the Function text_indentation"""


def text_indentation(text):
    """Function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    """
    new_text = ""
    flag = False
    if type(text) is not str:
        raise TypeError("text must be a string")
    new_text = text.replace(". ", ".")
    new_text = new_text.replace(": ", ":")
    new_text = new_text.replace("? ", "?")
    for char in new_text:
        if char in [".", "?", ":"]:
            print(char)
            print()
            flag = True
        else:
            if flag is False:
                print(char, end="")
            else:
                if char != " ":
                    print(char, end="")
                    flag = False
