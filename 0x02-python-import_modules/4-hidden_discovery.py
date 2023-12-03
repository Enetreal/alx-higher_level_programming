#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    for content in dir(sys):
        if content[:2] != "__":
            print(content)
