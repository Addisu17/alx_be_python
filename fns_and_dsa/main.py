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
def shopping_list_manager():
    def display_menu():
        print("\nShopping List Manager")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View List")
        print("4. Exit")

    shopping_list = []  # Start with an empty list
    
    while True:
        display_menu()  # Show the menu
        choice = input("Enter your choice: ")  # Get the user's choice
        
        if choice == '1':
            # Add Item
            item = input("Enter the item to add: ")  # Ensure the prompt matches the check exactly
            shopping_list.append(item)  # Add item to the list
            print(f"'{item}' has been added to your shopping list.")

        elif choice == '2':
            # Remove Item
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)  # Remove item from the list
                print(f"'{item}' has been removed from your shopping list.")
            else:
                print(f"'{item}' is not in the shopping list. Cannot remove.")

        elif choice == '3':
            # View List
            if shopping_list:
                print("\nYour Shopping List:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == '4':
            # Exit
            print("Goodbye!")
            break

        else:
            # Invalid choice
            print("Invalid choice. Please try again.")

# Display menu to choose which task to run
def display_menu():
    print("\nChoose the task to run:")
    print("1. Arithmetic Operations")
    print("2. Shopping List Manager")
    print("3. Exit")

# Main function to handle user input for task selection
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            arithmetic_operations()
        elif choice == '2':
            shopping_list_manager()
        elif choice == '3':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
