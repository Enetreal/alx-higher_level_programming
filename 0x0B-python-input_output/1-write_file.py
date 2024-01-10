#!/usr/bin/python3
"""
Defines a file-writing function.
"""

def write_file(filename="", text=""):
    """
    Writes the specified text to the given filename.

    Parameters:
    - filename (str): The name of the file to write to.
    - text (str): The text to be written to the file.

    Returns:
    int: The number of characters written to the file.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            num_characters_written = file.write(text)
            return num_characters_written
    except Exception as e:
        return 0
