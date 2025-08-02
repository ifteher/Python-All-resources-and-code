# Program to convert temperature from Celsius to Fahrenheit

# Taking input from the user
celsius = input("Enter temperature in Celsius: ")

# Converting the input to float type
try:
    celsius = float(celsius)
    fahrenheit = (celsius * 9/5) + 32
    # Displaying the result
    print(f"{celsius}°C is equal to {fahrenheit}°F")

except ValueError:
    print("Please enter a valid number.")

    '''
    # Example Output:
    25.0°C is equal to 77.0°F
    
    0.0°C is equal to 32.0°F
    -20.0°C is equal to -4.0°F
    100.0°C is equal to 212.0°F
    '''
