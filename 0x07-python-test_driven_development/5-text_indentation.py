#!/usr/bin/python3
"""Prints an indented string


  args:

"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ''
    final_text = ''

    new_text = ''
    for char in text:
        if char in ".?:":
            new_text += (char + "\n\n")
        else:
            new_text += char

    while (True):
        for i in [" \n ", " \n", "\n "]:
            if i in new_text:
                new_text = new_text.replace(i, "\n")
        break
    print(new_text)
