import json

with open("Horse.jpg", "rb") as Product_stream:
    image_bytes = Product_stream.read.read()
    print(type(image_bytes))
    print(len(image_bytes))