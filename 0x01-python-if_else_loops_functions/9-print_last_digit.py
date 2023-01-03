#!/usr/bin/python3
def print_last_digit(number):
    n = str(number)
    last_digit = n[-1]
    print("{}".format(last_digit), end = '')
    return last_digit
