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
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# User Interaction with Input Validation:
def get_temperature_input():
    while True:
        try:
            temperature = float(input("Enter the temperature to convert: "))
            return temperature
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

def get_unit_input():
    while True:
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit in ['C', 'F']:
            return unit
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

# Main Program Logic:
def main():
    temperature = get_temperature_input()
    unit = get_unit_input()

    if unit == 'F':
        converted = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted}°C")
    elif unit == 'C':
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted}°F")

# Execute the program:
if __name__ == "__main__":
    main()