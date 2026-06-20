class Customer:
    """
    Represents a customer placing an order.
    """

    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

    def display_customer(self):
        """Displays customer details."""
        print(f"Customer ID: {self.customer_id}, Name: {self.name}")

    def update_name(self, new_name):
        """Updates customer name."""
        self.name = new_name

    def get_details(self):
        """Returns customer details as string."""
        return f"{self.customer_id},{self.name}"