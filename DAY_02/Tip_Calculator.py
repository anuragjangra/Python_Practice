# This is a simple program that generates a band name based on the user's input.
print("Welcome to the Tip Calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("How much you like to to give?10 ,12 or 15? "))
num_of_people = int(input("How many people to spilt the bill? "))
individual_bill = float((bill+(tip*bill)/100)/num_of_people)
print(f"Each person should pay: ${round(individual_bill,2)}")