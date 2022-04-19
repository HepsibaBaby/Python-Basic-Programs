'''class employ1:
    def func1(self):
        print("This is first employee")
class employ2(employ1):
    def func2(self):
        print("This is second employee")
ob = employ2()
ob.func1()
ob.func2()'''

'''import math


class Shape:

    def circumference(self):
        return 0.0
    def area(self):
        return 0.0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi*(self.radius**2)
    def circumference(self):
        return 2 * math.pi*self.radius

class Rectangle(Shape):
    def __init__(self, w,h):
        self.width = w
        self.height = h
    def area(self):
        return self.width * self.height

    def circumference(self):
        return 2 * (self.width + self.height)


R = (float(input("Enter the radius of the circle")))
obj1 = Circle(R)
print("The area of circle is: ", obj1.area())
print("The circumference of circle is: ", obj1.circumference())

W=(float(input("Enter the width of the rectangle")))
H=(float(input("Enter the height of the rectangle")))
obj2 = Rectangle(W,H)
print("The area of rectangle is: ", obj2.area())
print("The circumference of rectangle is: ", obj2.circumference())


#Method Overriding

class father:
    def car(self):
        print("I have a car")
class child(father):
    def bike(self):
        print("I have a bike")

    def car(self):
        print("I have my own car")

obj = child()
obj.bike()
obj.car()


#Method Overloading
class calc:
    def add(self,a):
        print("number is:", a)

    def add(self, a,b):
        n=a+b
        print("addition of two number is:",n)

    def add(self, a, b, c):
    n = a+b+c
    print("addition of three number is:", n)

c=calc()
c.add(1,2,3)'''

