from abc import ABC, abstractmethod


class Product(ABC):

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def calculate_price(self):
        pass

    @abstractmethod
    def deliver_product(self):
        pass


class PyhsicalProduct(Product):

    def calculate_price(self):
        shipping = 100
        tax = self.price * 0.18
        return self.price + tax + shipping

    def deliver_product(self):
        print("Product will be shipped to the customer via courier service..")


class DigitalProduct(Product):

    def calculate_price(self):
        tax = self.price * 0.18
        return self.price + tax

    def deliver_product(self):

        print("Download link is being sent to your email. check it to proceed further")


class SubscriptionProduct(Product):

    def calculate_price(self):
        discount = self.price * 0.10
        return self.price - discount

    def deliver_product(self):
        print("Subscription is added here")


p1 = PyhsicalProduct("Laptop", 40000)
print(p1.calculate_price())
p1.deliver_product()

d1 = DigitalProduct("Python course", 1000)
print(d1.calculate_price())
d1.deliver_product()

s1 = SubscriptionProduct("Software", 2000)
print(s1.calculate_price())
s1.deliver_product()
