# Program to display all numbers from 1 to 100 that are divisible by 5
print("Numbers between 1 and 100 that are divisible by 5:")

# Looping from 1 to 100
for number in range(1, 101):
    if number % 5 == 0:
        print(number, end=" ")


'''
# Example Output:
Numbers between 1 and 100 that are divisible by 5:
5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100
'''
