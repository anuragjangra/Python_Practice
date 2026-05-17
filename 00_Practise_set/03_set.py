# Answer to question 1 of practise set 3
# name ="Anurag Jangra"
# print(name[0]) # Output: A
# print(name[12]) # Output: a
# print(len(name)) # Output: 13

# # Answer to question 2 of practise set 3
# str1 = "Hello"
# str2 = "World"
# str3 = str1 + " " + str2
# print(str3) # Output: Hello World

# Answer to question 3 of practise set 3
# text = "Python Programming"
# print(text[0:6]) # Output: Python
# print(text[-6:18]) # Output: amming
# print(text[0:18:2]) # Output: Pto rgamn
# print(text[-1:-19:-1]) # Output: gnimmargorP nohtyP

# Answer to question 4 of practise set 3
str1 = " i love python programming "
print(str1.strip()) # Output: i love python programming
print(str1.title()) # Output:  I Love Python Programming
print(str1.count("o")) # Output: 3

str2 = "123abc"
print(str2.isalnum()) # Output: True

# Answer to question 5 of practise set 3
name = "John"
age = 25

template = "My name is {} and I am {} years old."
print(template.format(name, age))
print(f"My name is {name} and I am {age} years old.") # Output: My name is John and I am 25 years old.

# Answer to question 6 of practise set 3
sentence = "Coding in Python is fun"
sentence.replace("fun", "awesome")
print(sentence) # Output: Coding in Python is fun

# Answer to question 7 of practise set 3
print(sentence.find("Python")) # Output: 11

# Answer to question 8 of practise set 3
print(sentence.upper()) # Output: CODING IN PYTHON IS FUN

# Answer to question 9 of practise set 3
usr_str = str(input("Enter a string: "))
vowel_count = usr_str.count("a") + usr_str.count("e") + usr_str.count("i") + usr_str.count("o") + usr_str.count("u")
print(f"The number of vowels in the string is: {vowel_count}")

# Answer to question 10 of practise set 3
usr_str1 = str(input("Enter the string: "))
if usr_str1 == usr_str1[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")