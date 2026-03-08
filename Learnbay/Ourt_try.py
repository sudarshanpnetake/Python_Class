import json

product_stream = None

try:
    product_stream = open("products.json", "r")

    # ✅ Correct function
    products = json.load(product_stream)

    print("Product file is loaded\n")

    for p in products:
        try:
            assert "id" in p, "Product id is missing"
            assert "price" in p, "Price is missing"
            assert "stock" in p, "Stock is missing"

            assert p["price"] > 0, "Product price is negative"
            assert p["stock"] >= 0, "Product stock is negative"

            print("Product is ordered", p["id"])

        except AssertionError as ae:
            print("Skipping the product", p.get("id"), "--->", ae)

        except ValueError as ve:
            print("Value Error", ve)

        except Exception as e:
            print("Inner try exception for", p.get("id"), "--->", e)

except FileNotFoundError as fe:
    print("JSON file is missing", fe)

except json.JSONDecodeError:
    print("JSON file is having wrong format")

except Exception as e:
    print("Outer try exception:", e)

finally:
    if product_stream:
        product_stream.close()
        print("\nProduct file stream is closed now....")