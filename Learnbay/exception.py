class InvalidProductPriceError(Exception):
    pass


def save_product(id, price):

    if price <= 0:
        raise InvalidProductPriceError(f"Invalid price for product {id}")

    print("Product saved successfully")


try:
    save_product("P101", -4000)

except InvalidProductPriceError as e:
    print("Product validation errror ", e)
