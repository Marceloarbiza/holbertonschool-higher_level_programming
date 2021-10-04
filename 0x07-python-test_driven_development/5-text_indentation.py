#!/usr/bin/python3
"""
    Write a function that prints a text with 2 new \
        lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
        prints a text with 2 new lines after each \
            of these characters: ., ? and :

        This function mus replace ., ? and : with
        the char plus two line breaks and print it

        The last line must no have a line break
    """
    flag = 0
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    else:
        text = text.replace('.', '.\n\n')
        text = text.replace('?', '?\n\n').replace(':', ':\n\n')
        textL = text.split('\n\n')
        last = len(textL)
        for i in textL:
            flag += 1
            h = i.lstrip()
            if flag < last:
                print(h + '\n')
            else:
                print(h, end="")
