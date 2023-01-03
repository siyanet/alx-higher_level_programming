#!/usr/bin/python3
def remove_char_at(str, n):
    for letter in str:
        if letter == str[n]:
            continue
        else:
            s = letter
    return s
