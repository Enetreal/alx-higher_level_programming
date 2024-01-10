#!/usr/bin/python3

def append_write(filename="", text=""):
    """Appends a string to the end of UTF8 text file"""
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            num_characters_added = file.write(text)
            return num_characters_added
    except Exception as e:
        # Handle the exception here if needed
        return 0
