#!/usr/bin/python3
"""This module defines a text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing a specific string.

    Args:
    filename (str): The name of the file to be modified.
    search_string (str): The specific string to search for in each line.
    new_string (str): The line of text to be inserted after each line containing the search string.

    Returns:
    None
    """
    # Open the file in read mode and create a new file to write the modified content
    with open(filename, 'r') as file, open('temp_file.txt', 'w') as temp_file:
        # Iterate through each line in the file
        for line in file:
            # Write the original line to the new file
            temp_file.write(line)
            # Check if the search string is present in the line
            if search_string in line:
                # If the search string is found, write the new string after the line
                temp_file.write(new_string + '\n')
    
    # Replace the original file with the modified file
    import os
    os.replace('temp_file.txt', filename)
