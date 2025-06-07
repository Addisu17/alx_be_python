# This is explore_datetime.py

# Part 1: Display the Current Date and Time
from datetime import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_date

print(f"Current date and time: {display_current_datetime()}")

# Part 2: Calculate a Future Date

def calculate_future_date(number_of_days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=number_of_days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d %H:%M:%S')}")

number_of_days = int(input("Enter the number of days to add to the current date: "))
calculate_future_date(number_of_days)