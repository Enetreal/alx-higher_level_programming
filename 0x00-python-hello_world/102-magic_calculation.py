#!/usr/bin/python3
import dis

def magic_calculation(a, b):
    return 98 + (a ** b)

# Display the bytecode of the function
dis.dis(magic_calculation)
