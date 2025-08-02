# Program to sort a list in ascending order

# Taking input from the user and converting it to a list of integers
user_input = input("Enter numbers separated by spaces: ")
num_list = [int(x) for x in user_input.split()]

# Sorting the list in ascending order
num_list.sort()

# Displaying the sorted list
print("Sorted list in ascending order:", num_list)

'''
# Example Output:
Enter numbers separated by spaces: 34 12 5 67 23
Sorted list in ascending order: [5, 12, 23, 34, 67]
'''
