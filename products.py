"""
A class that manages products
"""
class Product:

    def __init__(self, name, price, quantity=0):
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
        
        self.promotion = None

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


    def get_promotion(self):
        """
        Get active promotion(s)
        """
        return self.promotion


    def set_promotion(self, promotion):
        """
        Set one or more promotion(s)
        """
        self.promotion = promotion


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
        if self.promotion:
            return (f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, "
                    f"{self.promotion.name}")
        else:
            return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity) -> float:
        """
        Buys a given quantity of a product.
        Return a total price of the purchase as a float.
        Updates the quantity of the product.
        In case of a problem, raises an exception.
        """
        try:
            subtotal = self.price * quantity

            if self.promotion:
                total = self.promotion.apply_promotion(self, quantity)
            else:
                total = subtotal

            if quantity > self.quantity:
                raise ValueError
            self.quantity -= quantity
            if self.quantity == 0:
                self.deactivate()
            
            return total
        except ValueError:
            print("You cannot buy more product than what is available.")
            return None


class NonStockedProduct(Product):

    def __init__(self, name, price):
        super().__init__(name, price)

        try:
            self.name = name
            if not name:
                raise ValueError
        except ValueError:
            print("Product name cannot be empty!")

        try:
            self.price = price
            if price < 0:
                raise ValueError
        except ValueError:
            print("Price cannot be a negative number!")


    def show(self) -> str:
        """
        Returns a string representing the product.
        """
        if self.promotion:
            return (f"{self.name}, Price: {self.price}, Quantity: Unlimited! "
                    f"{self.promotion.name}")
        else:
            return f"{self.name}, Price: {self.price}, Quantity: Unlimited!"


    def buy(self, quantity) -> float:
        """
        Buys a given quantity of a product.
        Return a total price of the purchase as a float.
        """
        subtotal = self.price * quantity

        if self.promotion:
            total = self.promotion.apply_promotion(self, quantity)
        else:
            total = subtotal
        
        return total


class LimitedProduct(Product):

    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

        try:
            self.name = name
            if not name:
                raise ValueError
        except ValueError:
            print("Product name cannot be empty!")

        try:
            self.price = price
            self.quantity = quantity
            self.maximum = maximum
            if price < 0:
                raise ValueError
            if quantity < 0:
                raise ValueError
            if maximum < 0:
                raise ValueError
        except ValueError:
            print("Price, quantity, or maximum cannot be a negative number.")


    def show(self) -> str:
        """
        Returns a string representing the product.
        """
        if self.promotion:
            return (f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, "
                   f"Limited {self.maximum} per order! {self.promotion.name}")
        else:
            return (f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, "
                    f"Limited {self.maximum} per order!")


    def buy(self, quantity) -> float:
        """
        Buys a given quantity of a product.
        Return a total price of the purchase as a float.
        Updates the quantity of the product.
        In case of a problem, raises an exception.
        """
        try:
            subtotal = self.price * quantity

            if self.promotion:
                total = self.promotion.apply_promotion(self, quantity)
            else:
                total = subtotal

            if quantity > self.quantity:
                raise ValueError
            if quantity > self.maximum:
                raise ValueError
            self.quantity -= quantity
            if self.quantity == 0:
                self.deactivate()
            
            return total
        except ValueError:
            print("You have exceed the order limit or ordered more than what is available.")
            return None
