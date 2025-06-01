# Simple Calculator with Match Case 
# prompt the user to enter two numbers 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask for the type of operation they’d like to perform: Choose the operation (+, -, *, /)

operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
    #addition = num1 + num2
        print(f"The result is {num1 + num2}")
    case "-":
    #subtraction = num1 - num2
        print(f"The result is {num1 - num2}")
    case "*":
    #multiply = num1 * num2
        print(f"The result is {num1 * num2}")
    case "/":
    #divide = num1 / num2
        if num2 != 0:
            print(f"The result is {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print(f"Please, enter the arthimetic operation listed above")