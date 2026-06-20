class Order:
    """
    Handles customer orders including adding items,
    removing items, calculating total, and displaying order.
    """

    def __init__(self):
        self.items = []

    def add_item(self, item, quantity):
        """Adds item and quantity to order."""
        if quantity > 0:
            self.items.append((item, quantity))
        else:
            print("Quantity must be greater than 0.")

    def remove_item(self, item_name):
        """Removes item from order by name."""
        self.items = [i for i in self.items if i[0].name != item_name]

    def calculate_total(self):
        """Calculates total cost of order."""
        return sum(item.price * qty for item, qty in self.items)

    def display_order(self):
        """Displays all items in the order."""
        if not self.items:
            print("Order is empty.")
            return

        print("\n--- Current Order ---")
        for item, qty in self.items:
            print(f"{item.name} x{qty} = €{item.price * qty}")
        print(f"Total = €{self.calculate_total()}")

    def clear_order(self):
        """Clears the order."""
        self.items = []