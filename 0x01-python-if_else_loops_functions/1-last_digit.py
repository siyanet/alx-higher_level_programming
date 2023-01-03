#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
s = str(number)
last_digit = s[-1]
last_digit = int(last_digit)
if number < -1:
    last_digit = -last_digit
if last_digit > 5:
    stra = "and is greater than 5"
elif last_digit == 0:
    stra = "and is 0"
elif last_digit < 6 and last_digit:
    stra = "and is less than 6 and not 0"
print("Last digit of {} is {} {}".format(number, last_digit, stra))
