class Flight:
    def calculate_price(self, base_price):
        return base_price


class DomesticFlight:
    def calculate_price(self, base_price):
        return base_price + 2000


class InternationalFlight:
    def calculate_price(self, base_price):
        return base_price + 5000


def printdisp(flight, base_price):
    print("Final price: ", flight.calculate_price(base_price))


dom = DomesticFlight()
inty = InternationalFlight()

printdisp(dom, 5000)
printdisp(inty, 5000)
