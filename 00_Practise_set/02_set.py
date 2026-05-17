# Answer to question 1 of practise set 2
num = int(input("Enter a number: "))
if num<0:
    print("The number is negative.")
elif num>0:
    print("The number is positive.")
else:
    print("The number is zero.")

# Answer to question 2 of practise set 2
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Answer to question 3 of practise set 2
num1 = int(input("Enter the first number: "))
if num1 % 2 == 0:
    print(f"{num1} is an even number.")
else:
    print(f"{num1} is an odd number.")

# Answer to question 4 of practise set 2
day_number = int(input("Enter a number (1-7) representing the day of the week: "))

match day_number:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid input. Please enter a number between 1 and 7.")

# Answer to question 5 of practise set 2
number1 = int(input("Enter a number1: "))
number2 = int(input("Enter a number2: "))
operation = input("Enter the operation (+, -, *, /): ")
match operation:
    case "+":
        result = number1 + number2
        print(f"The result of {number1} + {number2} is {result}")
    case "-":
        result = number1 - number2
        print(f"The result of {number1} - {number2} is {result}")
    case "*":
        result = number1 * number2
        print(f"The result of {number1} * {number2} is {result}")
    case "/":
        if number2 != 0:
            result = number1 / number2
            print(f"The result of {number1} / {number2} is {result}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operation. Please enter one of the following: +, -, *, /")

# Answer to question 6 of practise set 2
for i in range(1, 11):
    print(i)

# Answer to question 7 of practise set 2
number = int(input("Enter a number: "))
print(f"The multiplication table of {number} is:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# Answer to question 8 of practise set 2
sum = 0
for i in range(1, 101):
    sum += i
print(f"The sum of numbers from 1 to 100 is: {sum}")

# Answer to question 9 of practise set 2
for i in range(1, 5):
    for j in range(1, i + 1):
        print("*",end="")
    print()  # Move to the next line after each row of stars

# Answer to question 10 of practise set 2
i=1
while i<=10:
    print(i)
    i+=1

password = "python123"
while True:
    user_input = input("Enter the password: ")
    if user_input == password:
        print("Access granted.")
        break
    else:
        print("Incorrect password. Try again.")

# Answer to question 11 of practise set 2        
user_num = int(input("Enter a number: "))
rev_num = 0
while user_num > 0:
    digit = user_num % 10
    rev_num = rev_num * 10 + digit
    user_num //= 10
print(f"The reverse of the number is: {rev_num}")

# Answer to question 12 of practise set 2
for i in range(1, 11):
    if i ==7:
        break
    print(i)

# Answer to question 13 of practise set 2
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# Answer to question 14 of practise set 2
for i in range(1, 5):
    if i == 3:
        pass
    print(i)