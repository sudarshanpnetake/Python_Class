try:
    price = 400
    quantity = 'a'

    total_price = price * quantity
except ValueError:
    print("Invalid pcroduct quantity")
else:
    print("Product saved successfully")

    