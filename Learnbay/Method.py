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


# =========================== Multiple ======================

class Product:
    def __init__(self, name, price, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.price = price
        print("We are into the Product Constructor")

    def display_basic(self):
        print(f"Product :{self.name} has the price as INR.{self.price}")


class Electronics(Product):
    def __init__(self, category, **kwargs):
        super().__init__(**kwargs)
        self.category = category
        print("We are into the Electronics Constructor")

    def display_category(self):
        print(f"Product :{self.name} has the price as INR.{self.price} with cateogry as {self.category}")


class Brand(Product):
    def __init__(self, brand, **kwargs):
        super().__init__(**kwargs)
        self.brand = brand
        print("We are into the Brand Constructor")

    def display_brand(self):
        print(f"Product :{self.name} has the price as INR.{self.price} with brand as {self.brand}")


class MyProduct(Electronics, Brand):
    def __init__(self, name, price, category, brand, discount):
        super().__init__(name=name, price=price, category=category, brand=brand)
        self.discount = discount

    def all_destails(self):
        print("we are into the all details method")
        self.display_category()
        self.display_brand()
        # self.display_basic()


mypro = MyProduct("Laptop", 45000, "Electronics", "DELL", 3000)
mypro.all_details()
