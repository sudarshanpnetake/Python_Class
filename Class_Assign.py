
class Product:
    
    #constrcutor below
    def __init__(self,Name,Price,Brand,Warranty,Count):
        self.Name = Name
        self.Price = Price
        self.Brand = Brand
        self.Warranty = Warranty
        self.Count = Count
        

    def display(self):
        # print Details
        print("Name:", self.Name)
        print("Price:", self.Price)
        print("Brand:", self.Brand)
        print("Count:", self.Count)

    def calc_price(self, count):
        total_price = self.Price * count
        print("Total Price:", total_price)
        
    
# Child Class
class Electronics(Product):

    def __init__(self, Name, Price, Brand, Warranty, Count):
       
        # calling parent constructor
        super().__init__(Name, Price, Brand, Warranty,Count)
        self.type = "Electronics"
        self.count = Count

    def displayAlldetails(self):
        # print all 
        print("Type:", self.type)
        print("Name:", self.Name)
        print("Price:", self.Price)
        print("Brand:", self.Brand)
        print("Warranty:", self.Warranty)
        print("Count:", self.Count)
        
# Object Creation
PROD = Electronics("Laptop", 50000, "Dell", "5Y", 10)

print("Display")
PROD.display()

print("All Details")
PROD.displayAlldetails()

print("Total Price")
PROD.calc_price(PROD.count)