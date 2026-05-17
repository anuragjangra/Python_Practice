"""
- Introduction to Lists
- List Methods
- Tuples and Operations on Tuples
- Sets and Set Methods
- Dictionaries and Dictionary Methods
"""
# Answer to question 1 of practise set 5
fruits = ["apple", "banana", "cherry"]
print(fruits[0]) # Output: apple

# Answer to question 2 of practise set 5
fruits[1] = "orange"
print(fruits) # Output: ['apple', 'orange', 'cherry']

# Answer to question 3 of practise set 5
print(len(fruits)) # Output: 3

# Answer to question 4 of practise set 5
list1 = [i for i in range(1, 11)]
print(list1[0:3]) # Output: [1, 2, 3]
print(list1[7:10]) # Output: [8, 9, 10]

# Answer to question 5 of practise set 5
numbers = [5, 2, 9, 1, 7]
numbers.sort()
print(numbers) # Output: [1, 2, 5, 7, 9]

# Answer to question 6 of practise set 5
numbers.append(10)
print(numbers) # Output: [1, 2, 5, 7, 9, 10]

# Answer to question 7 of practise set 5
numbers.remove(2)
print(numbers) # Output: [1, 5, 7, 9, 10]

# Answer to question 8 of practise set 5
names = ["Alice", "Bob", "Charlie"]
names.insert(1, "David")
print(names) # Output: ['Alice', 'David', 'Bob', 'Charlie']

# Answer to question 9 of practise set 5
coordinates = (10, 20)
print(coordinates) # Output: (10, 20)

# Answer to question 10 of practise set 5
# coordinates[0]=50 # This will raise a TypeError since tuples are immutable

# Answer to question 11 of practise set 5
list2 = list(coordinates)
list2[0]=50
coordinates = tuple(list2)
print(coordinates) # Output: (50, 20)

# Answer to question 12 of practise set 5
my_set = {1, 2, 3,  3, 4}
print(my_set) # Output: {1, 2, 3, 4}

my_set.add(5)
my_set.remove(2)
print(4 in my_set) # Output: True

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2)) # Output: {1, 2, 3, 4, 5}
print(set1.intersection(set2)) # Output: {3}
print(set1.difference(set2)) # Output: {1, 2}

# Answer to question 13 of practise set 5
student = {"name": "John","age": 20,"grade": "A"}
print(student["name"]) # Output: John
student["grade"] = "A+"
student["city"] = "Delhi"
print(student) # Output: {'name': 'John', 'age': 20, 'grade': 'A+', 'city': 'Delhi'}

# Answer to question 14 of practise set 5
friends = {"Alice": 123, "Bob": 456, "Charlie": 789}
print(friends.keys()) # Output: dict_keys(['Alice', 'Bob', 'Charlie'])
print(friends.values()) # Output: dict_values([123, 456, 789])
print(friends.items()) # Output: dict_items([('Alice', 123), ('Bob

# Answer to question 15 of practise set 5
# list_of_numbers = []
# for i in range(1, 5):
#     a = int(input(f"Enter number {i}: "))
#     list_of_numbers.append(a)
# print(f"The list of numbers is: {list_of_numbers}")

# set3 = set(list_of_numbers)
# print(f"The set of numbers is: {set3}")

# Answer to question 16 of practise set 5
dict_of_products = {"Laptop": 1000, "Phone": 500, "Tablet": 300}
highest_price = max(dict_of_products.values())
print(f"The highest price is: {highest_price}") # Output: The highest price is: 1000

# Answer to question 17 of practise set 5
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
merged_dict = {**dict1, **dict2}
print(merged_dict) # Output: {'a': 1, 'b': 4, 'c': 5, 'd': 6}
