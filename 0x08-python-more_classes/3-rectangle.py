#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """This represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing this rectangle class
        Args:
            width: represents the width of the rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self._width = width
        self._height = height

    @property
    def width(self):
        """Retrieves width attribute"""
        return self._width

    @width.setter
    def width(self, value):
        """Sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Retrieves height attribute"""
        return self._height

    @height.setter
    def height(self, value):
        """Sets height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self._width * self._height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self._width == 0 or self._height == 0:
            return 0
        return (self._width * 2) + (self._height * 2)

    def __str__(self):
        """Presents a diagram of the rectangle defined for an object"""
        return '\n'.join(['#' * self._width for _ in range(self._height)])

