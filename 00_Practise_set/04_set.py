"""
•Defining Functions in Python 
•Function Arguments & Return Values 
•Lambda Functions in Python 
• Recursion in Python
•Modules and Pip – Using External Libraries 
•Variable Scope and Docstrings 
"""
# Answer to question 1 of practise set 4
def greet():
    print("Hello, Python Learner!")

greet() # Output: Hello, Python Learner!

# Answer to question 2 of practise set 4
def square(num):
    return num ** 2
print(square(5)) # Output: 25

# Answer to question 3 of practise set 4
def full_name(first_name, last_name):
    return f"{first_name} {last_name}"

print(full_name("John", "Doe")) # Output: John Doe

# Answer to question 4 of practise set 4
def calculate_area(length, width =10):
    return length * width

print(calculate_area(5)) # Output: 50
print(calculate_area(5, 20)) # Output: 100

# Answer to question 5 of practise set 4
add = lambda x, y: x + y
print(add(3, 5)) # Output: 8 

# Answer to question 6 of practise set 4
list1 = [1, 2, 3, 4, 5]

squared_list = list(map(lambda x: x ** 2, list1))
print(squared_list) # Output: [1, 4, 9, 16

# Answer to question 7 of practise set 4
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5)) # Output: 120

# Answer to question 8 of practise set 4
def sum_of_digits(num):
    if num == 0:
        return 0
    else:
        return (num % 10) + sum_of_digits(num // 10)

print(sum_of_digits(123)) # Output: 6

# Answer to question 9 of practise set 4
import math
print(math.sqrt(144)) # Output: 12.0

# Answer to question 10 of practise set 4
print(math.sin(math.radians(90))) # Output: 1.0

# Answer to question 11 of practise set 4
import requests
response = requests.get("https://api.github.com")
print(response.status_code) # Output: 200


# Answer to question 12 of practise set 4
def increment():
    a = 0
    a += 1
    return a

print(increment()) # Output: 1
print(increment()) # Output: 1

# Answer to question 13 of practise set 4
def multiply(a,b):
    """This function multiplies two numbers."""
    return a * b

print(multiply(4, 5)) # Output: 20
print(multiply.__doc__) # Output: This function multiplies two numbers.


# Answer to question 14 of practise set 4
def fibonacci(n):
    """Returns the nth Fibonacci number."""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(10)) # Output: 55 

def display_fibonacci_sequence(n):
    """Displays the Fibonacci sequence up to the nth number."""
    sequence = [fibonacci(i) for i in range(n)]
    print(sequence)

display_fibonacci_sequence(10) # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Answer to question 15 of practise set 4
def safe_divide(a, b):
    """Returns the result of a divided by b, or an error message if b is zero."""
    if b == 0:
        return "Error: Division by zero is not allowed."
    else:
        return a / b

print(safe_divide(10, 2)) # Output: 5.0
print(safe_divide(10, 0)) # Output: Error: Division by zero is not allowed.

# Answer to question 16 of practise set 4
import my_utils
print(my_utils.is_even(4)) # Output: True
print(my_utils.is_even(5)) # Output: False
