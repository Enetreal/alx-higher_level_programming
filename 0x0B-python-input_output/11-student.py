#!/usr/bin/python3
"""Defines a class Student."""

class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Gets a dictionary representation of the Student.

        If attrs is a list of strings, represents only those attributes
        included in the list.
        """
        if isinstance(attrs, list) and all(isinstance(ele, str) for ele in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json_data):
        """Replaces all attributes of the Student."""
        for key, value in json_data.items():
            setattr(self, key, value)
