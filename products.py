"""
A class that manages products
"""
class Product:

    def __init__(self, name, price, quantity):
        try:
            self.name = name
            if not name:
                raise ValueError
        except ValueError:
            print("Product name cannot be empty.")

        try:
            self.price = price
            self.quantity = quantity
            if price < 0:
                raise ValueError
            if quantity < 0:
                raise ValueError
        except ValueError:
            print("Price or quantity cannot be a negative number.")

        self.active = True


    def get_quantity(self) -> float:
        """
        Getter function for quantity. Returns quantity as a float.
        """
        return self.quantity


    def set_quantity(self, quantity):
        """
        Setter function for quantity.
        If quantity hits 0, deactivate the product.
        """
        self.quantity += quantity
        if self.active == False:
            self.activate()
        elif self.quantity == 0:
            self.deactivate()


    def is_active(self) -> bool:
        """
        Getter function for active.
        Returns True is product is active, otherwise False.
        """
        return self.active
    

    def activate(self):
        """
        Activates the product.
        """
        self.active = True


    def deactivate(self):
        """
        Deactivates the product.
        """
        self.active = False


    def show(self) -> str:
        """
        Returns a string the represents the product.
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity) -> float:
        """
        Buys a given quantity of a product.
        Return a total price of the purchase as a float.
        Updates the quantity of the product.
        In case of a problem, raises an exception.
        """
        try:
            if quantity > self.quantity:
                raise ValueError
            self.quantity -= quantity
            if self.quantity == 0:
                self.deactivate()
        except ValueError:
            print("You cannot buy more product than what is available.")

        return self.price * quantity
