def read_file(filename=""):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
read_file("example.txt")
