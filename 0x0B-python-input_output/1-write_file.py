#!/usr/bin/python3
"""defines a file-writing function"""


def write_file(filename="", text=""):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            num_characters_written = file.write(text)
            return num_characters_written
    except Exception as e:
        print(f"Error: {e}")
        return 0