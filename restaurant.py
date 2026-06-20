import random
from menu import MenuItem
from order import Order
from customer import Customer


class RestaurantSystem:
    """
    Main system that manages menu, orders, and customers.
    """

    def __init__(self):
        self.menu = []
        self.order = Order()
        self.load_menu()

    # ---------- MENU FUNCTIONS ----------
    def add_menu_item(self):
        """Adds a new item to the menu."""
        try:
            name = input("Enter item name: ")
            price = float(input("Enter price: "))
            category = input("Enter category: ")

            if price <= 0:
                print("Price must be positive!")
                return

            item = MenuItem(name, price, category)
            self.menu.append(item)

            with open("menu.txt", "a", encoding="utf-8") as f:
                f.write(item.to_file())

            print("Item added successfully!")

        except ValueError:
            print("Invalid input!")

    def view_menu(self):
        """Displays all menu items."""
        if not self.menu:
            print("Menu is empty.")
            return

        print("\n--- MENU ---")
        for i, item in enumerate(self.menu, start=1):
            print(f"{i}. {item.display()}")

    # ---------- ORDER FUNCTIONS ----------
    def add_to_order(self):
        """Adds selected menu item to order."""
        if not self.menu:
            print("Menu is empty.")
            return

        self.view_menu()

        try:
            choice = int(input("Select item number: ")) - 1
            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than 0.")
                return

            if 0 <= choice < len(self.menu):
                self.order.add_item(self.menu[choice], quantity)
                print("Item added to order!")
            else:
                print("Invalid choice!")

        except ValueError:
            print("Invalid input!")

    def view_order(self):
        """Displays current order."""
        self.order.display_order()

    def checkout(self):
        """Generates bill, saves order, and clears it."""
        if not self.order.items:
            print("No items in order.")
            return

        # Create customer
        customer_name = input("Enter customer name: ")
        customer = Customer(random.randint(1000, 9999), customer_name)

        total = self.order.calculate_total()
        order_id = random.randint(100, 999)

        print("\n===== BILL =====")
        customer.display_customer()
        self.order.display_order()
        print(f"Final Total: €{total}")

        # Save order to file
        with open("orders.txt", "a", encoding="utf-8") as f:
            f.write(f"\n--- Order ID: {order_id} ---\n")
            f.write(f"Customer: {customer.name}\n")

            for item, qty in self.order.items:
                f.write(f"{item.name} x{qty} = €{item.price * qty}\n")

            f.write(f"Total: €{total}\n")

        self.order.clear_order()
        print("Order completed!")

    # ---------- FILE HANDLING ----------
    def load_menu(self):
        """Loads menu items from file."""
        try:
            with open("menu.txt", "r", encoding="utf-8") as f:
                for line in f:
                    self.menu.append(MenuItem.from_file(line))
        except FileNotFoundError:
            pass