#!/usr/bin/python3
for l in "abcdefghijklmnopqrstuvwxyz":
    if l == 'q' or l == 'e':
        continue
    else:
        print("{}".format(l), end = '')
