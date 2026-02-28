lst = [23, 45, 12, 90, 60]
lst.append(88)
lst.append(11)
lst.append(45)
print(lst)
lst.insert(3, 55)
print(lst)
lst.remove(90)
print(lst)
lst.pop()
print(lst)
lst.pop()
lst.pop()
print(lst)
del lst[3]
print(lst)
lst[2] = 100
print(lst)
lst.append(88)
lst.append(11)
lst.append(45)
print(lst)

print(60 in lst)   # search will return boolean

list("abc")   # str --> list
list((40, 30, 20))  # tuple --> list
list({30, 30, 90})  # set --> list

# convert list to set
my_list = [45, 67, 89, 34, 89, 45]
myset = set(my_list)
print(myset)

# convert list to tuple
mytuple = tuple(my_list)

print(mytuple)

##---------------------------------------------------------------------// tuple below

t = (90, 45, 23, 67, 90, 88, 90)
print(t)
print(t[4])

# search
print(90, int) # if value is there
print(t.count(90))  # no of times values is coming
print(t.index(88))  # what index value is there

#list to tuple
tuple(90, 67, 88, 34, 56, 90)

#string to tuple
tuple("Viren")

###===============================================================// set below

s={45,67,23,56,89,23,40,15,87}
print(s)

#s.add(77)
#s.add(88)
#s.add(67)
#print(s)

y = s.pop()
print(y)

s.discard(100)
print(s)

y = s.pop()
print(y)

#search
print(56 in s)

a = {1,6,3,9,8}
b = {30,20,78,3,1}
print(a | b)  # union
print(a & b)  # intesection
print(b - a)    # difference = all values of a but common elemnts of a and b will be removed

myset = {45,56,67,34,45}
mylist = list(myset)
print(mylist)
mylist.append(45)
print(mylist)

s1 = set(mylist)
print(s1)

# set to tuple
t = tuple(myset)
print(t)

set1 = {5,90,23,4,20}
sorted_list = sorted(set1)
sorted_tuple = tuple(sorted(set1))
print(sorted_list)
print(sorted_tuple)
set2=set(sorted_list)
print(set2)

###----------------------------------------------- frozenset

s={45,67,23,56,89,23,40,15,87}
print(s)

s.add(77)
s.add(88)
s.add(67)
print(s)

fs = frozenset(s)
print(fs)

print(67 in fs)

list1 = list(fs)
print(list1)
list1.append(100)
list1.append(10)
print(list1)
fs2 = frozenset(list1)
print(fs2)

tupl1 = tuple(fs)
print(tupl1)

###----------------------------------------- dictionary
d1 = [
     {
       "id":101,
       "name":"Ravi",
       "age":34
     },
     {
       "id":102,
       "name":"Reena",
       "age":34
     }
     ]
print(d1)

d1["city"]="Delhi"
print(d1)

d1["name"] = "Viren"
print(d1)

d1.pop("age")
print(d1)

del d1["name"]
print(d1)

print("city" in d1)

print(d1.keys())
print(d1.values())
print(d1.items())  # list of tuple items
print(d1)

###---------------------------


marks = 45

if marks > 60:
    if marks > 80:
        if marks > 90:
            print('grade A')
        else:
            print('grade B')
    else:
        print('grade C')
else:
    print('grade D')






# if-elif

    number = -78

if number > 0:
    print('positive number')
elif number < 0:
    print('negative number')
else:
    print('zero')

#-----------------------

languages = ['Java','Python','C','JS','React']
word = 'Python'

for l in languages:
    print(l)

for w in word:
    print(w)

sum=0
for i in range(0,6):    # 0 to 5
    sum = sum + i
print('sum is ', sum)

# ------ nested for loops

attributes = ['EV','Petrol','Diesel','CNG']
cars =['Tesla','Audi','Hyundai','Mahindra']

for a in attributes:
    for c in cars:
        print(a,c)

    print("------")


    #-------- while loop with break

    number = 10

while number >=1:
    if number == 5:
        break
    print(number)
    number = number - 1

##Assignment
##1) print the table of 5 using the for loop and range

###2) print all the even and odd numbers starting from 1 - 20


import math

def add_numbers(a=1,b=1,c=5):
    result = a+ b +c         # result is local variable
    print(result)

# calling functions below
add_numbers(4,5)
add_numbers(10)
add_numbers()

# calling the function with arbirtay arguments below
def find_sum(*n):
    res = 0                  # res is local variable

    for num in n:
         res = res + num

    print(res)

# calling  the function
find_sum(10,20)
find_sum(20,30,40,50,60)
find_sum(20,30,40)



# outside function
def outer():
    message = 'local'

    # nested function
    def inner():

        # declare nonlocal variable
        nonlocal message

        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)

outer()



###____________________________

message = "outer-variable"

# outside function
def outer():
    message = 'local'
    print("inner:", message)

    # nested function
    def inner():

        global message
        # declare nonlocal variable
        #nonlocal message

        #message = 'nonlocal'
        print("inner $$$$:", message)

    inner()
    print("outer:", message)

outer()
print("outside the outer_func", message)


message = "outer-variable"

# outside function
def outer():
    message = 'local'
    print("inner:", message)

    # nested function
    def inner():

        # declare nonlocal variable
        nonlocal message

        message = 'nonlocal'
        print("inner $$$$:", message)

    inner()
    print("outer:", message)

outer()
print("outside the outer_func", message)

##----------------------------------------------------


##Assignment:
##Create a function to display the product details like- Id, prodName, price inside the function
##(a) calculate the total price of the product by passing the discount variable as 'global variable'

##And also you need  create another function that takes the quantity of the product as an argument and calculate the total price after applying the discount  and return the total price from the function
##(Note**: quantity * price = price  and then apply the discount over the price)



##drive link: https://drive.google.com/drive/folders/1OzK-zTwJhL83wHH0YQiPhh4xpKWF2LHo

##____________________________________________________________________________________________
##Constructors:

class Bike:
    name = ""
    gear = 0

# create object of class
b1 = Bike()

b1.name = "Mountain Bike"
b1.gear = 3

print(f"Name : {b1.name} has gears {b1.gear}")

# 2nd example

class Room:
    #length = 0.0
    #breadth = 0.0

    #constrcutor below
    def __init__(self,length, breadth):
        self.length = length
        self.breadth = breadth

    def __init__(self,length, breadth, height):
        self.length = length
        self.breadth = breadth
        self.height = height

    # area calcualtion
    def calcualte_area(self,name):
        c = self.length * self.breadth
        print(f" Area of the {name} is {c}")


# 1st object of the class
study_room = Room(42.0,10.0)
study_room.calcualte_area("study_rooom");

# 2nd object
living_room = Room(80.0,50.0)
living_room.calcualte_area("living_rooom");

# 3rd object
bed_room = Room(180.0,20.0)
bed_room.calcualte_area("bed_rooom");


#--------------------------------------------------------------
#Single Inheritance:

class Animal:
    name = ""

    def eat(self):
        print(f"This method is eat of Animal class")

class Dog(Animal):

    def display(self):
        print(f"The {self.name} is an animal and inside display")

    def eat(self):
        super().eat() # caling the parent class method eat
        print(f"This method is eat of Dog Class")

labrador = Dog()
labrador.name = "ABC"
labrador.eat()
labrador.display()





#________________________________________

#Assignment:

Product(Parent)
name
price
brand
warranty
display()
calc_price()


Elctronics (Child)
type = "Electronics"
count = 10
displayAlldetails()


#Methods:
##displayAlldetails() - print all the variables of the child class and parent
##display() - print only the name, price and brand
##calc_price() - you need to print the total_price of the products pruchased
##(total_price= price * count)







##Multilevel Inheritance:

class Product:
    def __init__(self,name,price):
        self.name = name
        self.price= price
        print("We are into the Product Constructor")

    def get_price(self):
        return self.price

class DiscountedProduct(Product):
    def __init__(self, name, price,discount):
        super().__init__(name, price)
        self.discount = discount
        print("We are into the DiscountedProduct Constructor")

    def get_price(self):
        base_price = super().get_price()  # calling the parent class method with same name
        return base_price - self.discount

class SeasonalProduct(DiscountedProduct):
    def __init__(self, name, price, discount,offer):
        super().__init__(name, price, discount)
        self.offer = offer
        print("We are into the Seasonal Product Constructor")

    def get_price(self):
        price_after_discount = super().get_price()
        return price_after_discount - self.offer

p1 = SeasonalProduct("Laptop", 45000, 3000, 1000)
print(" Final price after discounts nad offers is ", p1.get_price())
