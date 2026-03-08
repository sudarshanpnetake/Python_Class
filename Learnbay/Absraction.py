from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def disp(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

    def disp(self):
        print('The circle is printing')


class Reactangle(Shape):

    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l  * self.b

    def disp(self):
        print('The rectangle is printing')


c = Circle(5)
print(c.area())
print(c.disp())

r = Reactangle(4, 5)
print(r.area())

print(r.disp())