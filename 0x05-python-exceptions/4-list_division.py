#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            # Handle IndexError first
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("Index out of range")

            division_result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            division_result = 0
        except (TypeError, IndexError) as e:
            print(f"Error: {e}")
            division_result = 0
        finally:
            result.append(division_result)

    return result
