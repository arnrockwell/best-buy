from abc import ABC, abstractmethod

"""
An abstract class for product promotions
"""
class Promotion(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity) -> float:
        pass


"""
Promotion: Get the second item at half price
"""
class SecondHalfPrice(Promotion):

    def __init__(self, name):
        super().__init__(name)

    # If the quantity is more than 1, apply the promotion
    def apply_promotion(self, product, quantity) -> float:
        full_price = quantity - quantity // 2
        half_price = quantity // 2
        return full_price * product.price + half_price * (product.price / 2)


"""
Promotion: Buy two, get the third item free
"""
class ThirdOneFree(Promotion):

    def __inti__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity) -> float:
        third_free = quantity - quantity // 3
        return third_free * product.price


"""
Promotion: Percent off the price of an item
"""
class PercentDiscount(Promotion):

    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity) -> float:
        return product.price * (1 - self.percent / 100) * quantity
