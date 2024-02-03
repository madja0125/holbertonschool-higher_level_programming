#!/usr/bin/python3
"""text_indentation function"""


def text_indentation(text):
    """function that prints 2 new lines after [., ?, :] """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    s = text[:]

    for d in ".?:":
        list_text = s.split(d)
        s = ""
        for i in list_text:
            i = i.strip(" ")
            s = i + d if s == "" else s + "\n\n" + i + d

    print(s[:-3], end="")
