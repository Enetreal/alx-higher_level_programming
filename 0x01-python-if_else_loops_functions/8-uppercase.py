#!/usr/bin/python3
def uppercase(str):
    """Print a string in uppercase"""
    for u in str:
        if ord(u) >= 97 and oru(u) <= 122:
            u = chr(ord(u) - 32)
            pint("{}".format(u), end="")
            print("")