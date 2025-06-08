# This is temp_conversion_tool.py
"""Celsius to Fahrenheit:
F = 9/5 * C + 32

Fahrenheit to Celsius:
C = 5/9 * (F - 32)"""

# Define Global Conversion Factors:

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Implement Conversion Functions:
def convert_to_celsius(fahrenheit):
    Celsius = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
    return Celsius

"""fahrenheit = int(input("Enter your tempreture in Celsius: "))
#print(f"The Celsius equivalent for the fahrenheit is {fahrenheit}")
convert_to_celsius(fahrenheit)"""

def convert_to_fahrenheit(celsius):
    Fahrenheit = CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32
    return Fahrenheit

# User Interaction:
input_tempreture = float(input("Enter the temperature to convert: "))
celsius_or_fahrenheit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if celsius_or_fahrenheit == 'F':
    print(f"{input_tempreture}°F is {convert_to_celsius(float(input_tempreture))}°C")
elif celsius_or_fahrenheit == 'C':
    print(f"{input_tempreture}°C is {convert_to_fahrenheit(float(input_tempreture))}°F")
else:
    print("Please insert the exact number you want to convert!")    