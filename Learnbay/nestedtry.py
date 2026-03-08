
products = [
    {
        "id": "P101",
        "name": "Laptop",
        "price": -5000,
        "stock": 10
    },
    {
        "id": "P102",
        "name": "LED TV",
        "price": 15000,
        "stock": 20
    }
]

try:    # outer try
    for p in products:

        try:     # inner try
            if p["price"] <= 0:
                raise ValueError("Invalid product price")

            print("Product is ordered ", p["id"])

        except ValueError as e:

            print("Product is not ordred ", p["id"], " raising the expcetion as ", e)

except Exception as e:
    print("System error is ", e)