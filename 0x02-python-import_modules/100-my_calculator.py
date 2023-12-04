#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

def main():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    if choice not in ('1', '2', '3', '4'):
        print("Invalid choice. Please choose a valid operation.")
        return

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == '1':
        result = add(a, b)
    elif choice == '2':
        result = sub(a, b)
    elif choice == '3':
        result = mul(a, b)
    elif choice == '4':
        try:
            result = div(a, b)
        except ValueError as e:
            print(f"Error: {e}")
            return

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
