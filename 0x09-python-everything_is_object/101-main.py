#!/usr/bin/python3

class LockedClass:
    """A locked class that only allows the creation of certain attributes."""
    __slots__ = ['first_name', 'last_name']

# Usage
lc = LockedClass()
lc.first_name = "John"

try:
    lc.last_name = "Snow"
except AttributeError as e:
    print("[{}] {}".format(e.__class__.__name__, e))