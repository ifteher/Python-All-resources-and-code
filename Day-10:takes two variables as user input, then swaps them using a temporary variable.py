# Program to swap two variables using a temporary variable

# Taking user input for both variables
a = input("Enter the value of a: ")
b = input("Enter the value of b: ")

# Displaying original values
print(f"\nBefore swapping: a = {a}, b = {b}")

# Swapping using a temporary variable
temp = a
a = b
b = temp

# Displaying swapped values
print(f"After swapping: a = {a}, b = {b}")



'''
# Example Output:
Before swapping: a = 5, b = 10
After swapping: a = 10, b = 5
'''
