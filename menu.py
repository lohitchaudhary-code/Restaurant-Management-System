class MenuItem:
    """
    Represents a menu item in the restaurant.
    Stores name, price, and category of the item.
    """

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def display(self):
        """Returns formatted string of menu item."""
        return f"{self.name} ({self.category}) - €{self.price}"

    def update_price(self, new_price):
        """Updates the price of the item."""
        if new_price > 0:
            self.price = new_price

    def to_file(self):
        """Converts object to string for file storage."""
        return f"{self.name},{self.price},{self.category}\n"

    @staticmethod
    def from_file(line):
        """Creates MenuItem object from file line."""
        name, price, category = line.strip().split(",")
        return MenuItem(name, float(price), category)