from restaurant import RestaurantSystem


# Main function 
def main():
    # Create an object of RestaurantSystem
    system = RestaurantSystem()

    # Infinite loop to keep the program running until user exits
    while True:
        # Display menu options to the user
        print("\n===== Restaurant System =====")
        print("1. Add Menu Item")
        print("2. View Menu")
        print("3. Add Item to Order")
        print("4. View Order")
        print("5. Checkout / Generate Bill")
        print("6. Exit")

        # Take user input safely
        user_input = input("Enter your choice: ").strip()

        # Validate input before converting
        if not user_input.isdigit():
            print("Please enter a valid number!")
            continue

        choice = int(user_input)

        # Call corresponding function 
        if choice == 1:
            system.add_menu_item()

        elif choice == 2:
            system.view_menu()

        elif choice == 3:
            system.add_to_order()

        elif choice == 4:
            system.view_order()

        elif choice == 5:
            system.checkout()

        elif choice == 6:
            # Exit the program
            print("Exiting system...")
            break

        else:
            # Handle invalid menu option
            print("Invalid choice!")


# Ensures the program runs only when executed directly
if __name__ == "__main__":
    # Starts the program when this file is executed directly
    main()