# Function to calculate factorial using a loop
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i  # Multiply result by i
    return result

# Taking input from the user
num = input("Enter a non-negative integer: ")

# Checking if the input is valid
if num.isdigit():
    num = int(num)
    # Calling the function and displaying the result
    print(f"Factorial of {num} is: {factorial(num)}")
else:
    print("Invalid input! Please enter a non-negative integer.")

'''
বাংলা ব্যাখ্যা:
factorial(n) নামের একটি ফাংশন বানানো হয়েছে যা loop ব্যবহার করে factorial হিসাব করে।

ইউজার থেকে ইনপুট নেওয়া হয়, সেটা digit কিনা চেক করা হয়।

যদি ঠিক হয়, তাহলে সেই ইনপুট ফাংশনে পাঠিয়ে ফলাফল প্রিন্ট করা হয়।
# Example Output:
Enter a non-negative integer: 5
Factorial of 5 is: 120
'''
