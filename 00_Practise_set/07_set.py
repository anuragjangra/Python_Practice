"""
-Decorators in Python
-Getters and Setters
-Static & Class Methods
-Magic/Dunder Methods
-Exception Handling and Custom Errors
-map(), filter(), and reduce()
-Walrus Operator
-args and kwargs
"""

# Answer to question 1 of practise set 7 (Decorators in Python)
def logger(func):
    def wrapper():
        print("Function is being called")
        func()
    return wrapper

@logger
def say_hello():
    print("Hello!")

say_hello() # Output: Function is being called
            #         Hello! 

# Answer to question 2 of practise set 7
def timer(func):
    import time
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
    return wrapper

@timer
def sum():
    total = 0
    for i in range(1000000):
        total += i
    print(total)

sum() # Output: 499999500000 

# Answer to question 3 of practise set 7 (getters and setters)
class Employee:
    def __init__(self,salary):
        self._salary = salary

    @property    
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value

emp = Employee(50000)
print(emp.salary) # Output: 50000
emp.salary = 60000
print(emp.salary) # Output: 60000
# emp.salary = -10000 # Output: ValueError: Salary cannot be negative

# Answer to question 4 of practise set 7 (Static & Class Methods)
class MathUtils:
    @staticmethod   # Static method does not take 'self' or 'cls' as the first parameter
    def add(a,b):
        return a+b
    
    @classmethod
    def description(cls):  # Class method takes 'cls' as the first parameter
        print("This class contains utility methods for mathematical operations.")

print(MathUtils.add(5,10)) # Output: 15
MathUtils.description() # Output: This class contains utility methods for mathematical operations.


# Answer to question 5 of practise set 7 (Magic/Dunder Methods)
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):         # The __str__ method is a magic method that defines the string representation of an object. It is called when you use the str() function or print the object.
        return f"{self.title} by {self.author}"
    
    def __len__(self):         # The __len__ method is a magic method that defines the behavior of the len() function when called on an instance of the class. It should return the length of the object.
        return len(self.title)

book = Book("The Great Gatsby", "F. Scott Fitzgerald")   
print(book)  # Output: The Great Gatsby by F. Scott Fitzgerald
print(len(book))  # Output: 20

# Answer to question 6 of practise set 7 (Exception Handling and Custom Errors)
num= int(input("Enter a number: "))
try:
    result = 10 / num
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

def custom_error_example(value):
    if value < 0:
        raise ValueError("Negative value is not allowed.")
    return value

num1 = int(input("Enter the first number: "))
try:
    result = custom_error_example(num1)
    print(f"Updated Result: {result}")
except ValueError as e:
    print(f"Error: {e}")
finally:                       # The finally block is used to execute code that must run regardless of whether an exception was raised or not. It is typically used for cleanup actions, such as closing files or releasing resources.
    print("This block will always execute, regardless of exceptions.")

# Answer to question 7 of practise set 7 (map(), filter(), and reduce())
list1 = [1, 2, 3, 4, 5]
cubes = list(map(lambda x: x**3, list1))  # Output: [1, 8, 27, 64, 125]
print(cubes)

list2 = [10,11,12,13,14]
even_numbers = list(filter(lambda x: x % 2 == 0, list2))  # Output: [10, 12, 14]
print(even_numbers)

from functools import reduce
list3 = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, list3)  # Output: 24
print(product)

# Answer to question 8 of practise set 7 (Walrus Operator)
while (n := input("Enter a number (quit to exit): ")) != "quit":  # The walrus operator (:=) allows you to assign a value to a variable as part of an expression. In this case, it assigns the input value to 'n' and checks if it is not equal to "quit".
    print(f"You entered: {n}")


words = ["python","rocks","ai"]
lengths = [len(word) for word in words if (length := len(word)) > 4]  # The walrus operator is used here to assign the length of each word to the variable 'length' and check if it is greater than 4 before including it in the list of lengths.
print(lengths)  # Output: [6, 5, 2]

# Answer to question 9 of practise set 7 (args and kwargs)
def sum_all(*args):  # The *args syntax allows you to pass a variable number of non-keyword arguments to a function. Inside the function, 'args' is treated as a tuple containing all the passed arguments.
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3, 4, 5))  # Output: 15

def print_details(**kwargs):  # The **kwargs syntax allows you to pass a variable number of keyword arguments to a function. Inside the function, 'kwargs' is treated as a dictionary containing all the passed keyword arguments.
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Alice", age=25, city="Delhi")
# Output:
# name: Alice
# age: 25
# city: Delhi


# Answer to question 10 of practise set 7 (args and kwargs and decorators)
def log_args(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, Keyword Arguments: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_args
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")
greet("Alice")  # Output: Arguments: ('Alice',), Keyword Arguments: {}
                #         Hello, Alice!

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # The __add__ method is a magic method that defines the behavior of the addition operator (+) when applied to instances of the class. It should return a new instance of the class that represents the result of the addition.
        return Vector(self.x + other.x, self.y + other.y)
    
v1 = Vector(1, 2)
v2 = Vector(3, 4)   
v3 = v1 + v2         # Output: Vector(x=4, y=6)
print(f"v3: ({v3.x}, {v3.y})")  # Output: v3: (4, 6)

# Answer to question 11 of practise set 7 (Invalid user input and exception handling)
def get_integer():
    while True:
        try:
            num = int(input("Enter an integer: "))
            return num
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

number = get_integer()
print(f"You entered: {number}")