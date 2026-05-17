"""
-Introduction to OOP
-Classes and Objects in Python
-Constructors in Python
-Instance and Class Attributes
-Inheritance and Polymorphism
-Method Overriding and Operator Overloading
"""
# Answer to question 1 of practise set 6 (Classes and Objects in Python)
class car:
    def drive(self):
        print("The car is moving")

my_car = car()
my_car.drive() # Output: The car is moving

# Answer to question 2 of practise set 6 (Constructors and Instance Attributes)
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

person1 = person("Alice", 30)
print(person1.name) # Output: Alice
print(person1.age) # Output: 30

# Answer to question 3 of practise set 6 (Simple Inheritance)
class Animal:
    def sound(self):
        print("Speaking now...")

class Dog(Animal):
    def sound(self):
        super().sound() # Call the parent class method
        print("Bark!")

my_dog = Dog()
my_dog.sound() # Output: Speaking now...
              #         Bark!

# Answer to question 4 of practise set 6 (Operator Overloading)
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):                    #operator overloading for addition        
        return Point(self.x + other.x, self.y + other.y)
    
point1 = Point(2, 3)
point2 = Point(4, 5)
result = point1 + point2
print(result.x) # Output: 6
print(result.y) # Output: 8
