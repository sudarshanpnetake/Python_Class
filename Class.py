class Bike:
    name = ""
    gear = 0

    #create objects 

b1= Bike()
b1.name = 'Mountain Bike'
b1.gear = 3

print (f"Name : {b1.name} has gear {b1.gear}")


# 2nd Exaple

class Room:

    length = 0.0
    bredth = 0.0
    # area calculation

    def calculate_area(self):

        c = self.length * self.bredth
        print ("Area of Room is", c)

    # Craete 1st Object
Study_Room = Room()
Study_Room.length = 40.0
Study_Room.bredth = 60.0
Study_Room.calculate_area()

  # Craete 2nd Object
Bed_Room = Room()
Bed_Room.length = 15.0
Bed_Room.bredth = 30.0
Bed_Room.calculate_area()

####Using Constructor

# 2nd Exaple

class Room:

  
    # area calculation

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):

        c = self.length * self.bredth
        print ("Area of Room is", c)

    # Craete 1st Object
Study_Room = Room(40.0,60.0)
#Study_Room.length = 40.0
#Study_Room.bredth = 60.0
Study_Room.calculate_area("Study Room")

  # Craete 2nd Object
Bed_Room = Room(15.0,30.0)
#Bed_Room.length = 15.0
#Bed_Room.bredth = 30.0
Bed_Room.calculate_area("Bed Room")





