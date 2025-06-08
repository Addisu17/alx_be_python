"""# This is main.py

from arithmetic_operations import perform_operation

def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()"""

# main.py

# Import the perform_operation function for arithmetic operations
from arithmetic_operations import perform_operation

# Function for the first assignment: Arithmetic Operations
def arithmetic_operations():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

# Function for the second assignment: Shopping List Manager
# Import the display_menu function and any other required functions from shopping_list_manager.py
from shopping_list_manager import display_menu

def main():
    shopping_list = []  # Initialize an empty shopping list
    
    while True:
        display_menu()  # Show the menu
        choice = input("Enter your choice: ")  # Get the user's choice
        
        if choice == '1':  # Add Item
            item = input("Enter the item to add: ")
            shopping_list.append(item)  # Add item to the list
            print(f"'{item}' has been added to your shopping list.")
        
        elif choice == '2':  # Remove Item
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)  # Remove item from the list
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")
        
        elif choice == '3':  # View List
            if shopping_list:
                print("\nYour shopping list:")
                for idx, item in enumerate(shopping_list, 1):  # Display items with numbering
                    print(f"{idx}. {item}")
            else:
                print("Your shopping list is empty.")
        
        elif choice == '4':  # Exit
            print("Goodbye!")  # Display exit message
            break  # Exit the loop
        
        else:
            print("Invalid choice. Please try again.")  # Handle invalid input

if __name__ == "__main__":
    main()  # Start the program
