
def applydiscountdecorator(function):

    def wrapper(base_price):
        price = function(base_price)
        discounted_price = price - (price * 0.1)
        print("discounted_price=", discounted_price)
        return discounted_price

    return wrapper


def taxdecorator(function):

    def wrapper(base_price):
        price = function(base_price)
        final_price = price + (price * 0.18)
        print("final price=", final_price)
        return final_price

    return wrapper


@taxdecorator
@applydiscountdecorator
def calculate_flight_price(base_price):

    print(base_price)

    return (base_price)


print(calculate_flight_price(9000))
