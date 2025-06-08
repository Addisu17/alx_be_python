# shopping_list_manager.py

def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Start with an empty list

    while True:
        display_menu()  # Show the menu
        choice = input("Enter your choice: ")  # Get the user's choice

        if choice == '1':
            # Add Item
            item = input("Enter the item to add: ")  # Exact prompt required
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

# Run the program
if __name__ == "__main__":
    main()
