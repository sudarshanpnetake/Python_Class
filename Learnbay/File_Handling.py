#  ============ file handling ===========

def add_product(product_id, name, price):
    file = open("products_new.txt", 'w')  # open the file

# specify the format inwhcih data will be added into file
    record = f"{product_id}, {name}, {price}\n"
    file.write(record)

    file.close()


add_product(101, "Laptop", 45000)
add_product(102, "Watch", 3000)
add_product(103, "Headphones", 1000)

print("============= reading all the data from the file=================")


def read_products():
    file = open("products_new.txt", 'r')  # open the file in read mode

    data = file.read()  # this will read all the data from the file
    print(data)

    file.close()


read_products()


# ==========Read============================


def read_first_product():
    file = open("products_new.txt", 'r')  # open the file in read mode

    line = file.readlines()
    print(line)

    file.close()


read_first_product()

print("========= read the data line by line ====================")


def disp():
    file = open("products_new.txt", 'r')

    for line in file:
        print(line.strip())

    file.close()


disp()
