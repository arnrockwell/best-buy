"""
A class that manages the store
"""
class Store:

    def __init__(self, product_list):
        try:
            self.product_list = product_list
            check = isinstance(self.product_list, list)
            if not check:
                raise TypeError
        except TypeError:
            print("Product information must be in a list!")


    def add_product(self, product):
        """
        Adds one or more products to the store
        """
        try:
            self.product_list.append(product)
            if product in self.product_list:
                raise ValueError
        except ValueError:
            print("Product already exists!")


    def remove_product(self, product):
        """
        Removes a product from the store
        """
        try:
            self.product_list.remove(product)
            if product not in self.product_list:
                raise ValueError
        except ValueError:
            print("Product not in the database!")


    def get_total_quantity(self) -> int:
        """
        Returns how many items are in the store in total
        """
        quantity = []
        for item in self.product_list:
            quantity.append(item.get_quantity())
        return sum(quantity)


    def get_all_products(self):
        """
        Returns all products in the store that are active
        """
        active_products = []
        for item in self.product_list:
            if item.is_active() == True:
                active_products.append(item.show())
        return active_products


    def order(self, shopping_list) -> float:
        """
        Gets a list of tuples, where each tuple has 2 items:
        Product (from Product class) and quantity (int).
        Buys the products and returns the total price of the order.
        """
        return sum(item[0].buy(item[1]) or 0 for item in shopping_list)
