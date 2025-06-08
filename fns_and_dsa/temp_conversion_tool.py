"""# This is temp_conversion_tool.py
# Define Global Conversion Factors:

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Implement Conversion Functions:
def convert_to_celsius(fahrenheit):
    Celsius = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
    return Celsius

fahrenheit = int(input("Enter your tempreture in Celsius: "))
#print(f"The Celsius equivalent for the fahrenheit is {fahrenheit}")
convert_to_celsius(fahrenheit)

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
    print("Please insert the exact number you want to convert!")    """

# This is temp_conversion_tool.py
"""Celsius to Fahrenheit:
F = 9/5 * C + 32

Fahrenheit to Celsius:
C = 5/9 * (F - 32)"""

# Define Global Conversion Factors:
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Implement Conversion Functions:
def convert_to_celsius(fahrenheit):
    celsius = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = CELSIUS_TO_FAHRENHEIT_FACTOR * celsius + 32
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
