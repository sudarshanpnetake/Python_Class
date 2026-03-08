def cal_price(price, quantity):

    try:
        assert price > 0, "Product price must be greater than zero"
        return price * quantity
    except AssertionError as e:
        print("The inner assertion error is ", e)

    try:
        assert quantity > 0, "Product quantity must be greater than zero"
        return price * quantity
    except AssertionError as e:
        print("The inner assertion error is ", e)


try:
    total = cal_price(-1000, -2)
    print(total)
except Exception as e:
    print("The outer assertion error is ", e)
