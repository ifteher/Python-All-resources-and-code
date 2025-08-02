# Program to count the frequency of each character in a string using a dictionary
# Taking input from the user
text = input("Enter a string: ")
# Initializing an empty dictionary
char_freq = {}
# Loop through each character in the string
for char in text:
    if char in char_freq:
        char_freq[char] += 1  # If character already in dictionary, increment count
    else:
        char_freq[char] = 1   # If character not in dictionary, set count to 1
# Display the frequency of each character
print("\nCharacter Frequency:")
for char, freq in char_freq.items():
    print(f"'{char}': {freq}")


'''
# Example Output:
# Enter a string: hello world  
# Character Frequency:
# 'h': 1
# 'e': 1
# 'l': 3
# 'o': 2
# ' ': 2
# 'w': 1
# 'r': 1
# 'd': 1
# This program counts the frequency of each character in a string and displays the result.
'''
