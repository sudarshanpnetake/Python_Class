class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        print("We are into the Product Constructor")

    def get_price(self):
        return self.price


class DiscountedProduct(Product):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount
        print("We are into the DiscountedProduct Constructor")

    def get_price(self):
        # calling the parent class method with same name
        base_price = super().get_price()
        return base_price - self.discount


class SeasonalProduct(DiscountedProduct):
    def __init__(self, name, price, discount, offer):
        super().__init__(name, price, discount)
        self.offer = offer
        print("We are into the Seasonal Product Constructor")

    def get_price(self):
        price_after_discount = super().get_price()
        return price_after_discount - self.offer


p1 = SeasonalProduct("Laptop", 45000, 3000, 1000)


print(" Final price after discounts nad offers is ", p1.get_price())