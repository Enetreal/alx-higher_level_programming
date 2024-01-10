#!/usr/bin/python3
def append_write(filename="", text=""):
    try:
        with open(filename, 'a', encoding='utf-8') as file:
            num_characters_added = file.write(text)
            return num_characters_added
    except Exception as e:
        return 0

# Example usage:
text_to_append = "This is additional content."
characters_added = append_write("example.txt", text_to_append)
print(f"Number of characters added: {characters_added}")
