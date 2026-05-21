import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = {"rock":rock,"paper":paper,"scissors":scissors}
user_choice = str(input("Select your choice (rock,paper, scissors): ")).lower()
print(f"User choose: {user_choice}")
print(choices[user_choice])
Computer_choice = random.choice(["rock","paper","scissors"])
print(f"Computer choose: {Computer_choice}")
print(choices[Computer_choice])

if(user_choice == "rock" and Computer_choice == "scissors"):
    print("User win")
elif(user_choice == "paper" and Computer_choice == "rock"):
    print("User win")
elif(user_choice == "scissors" and Computer_choice == "paper"):
    print("User win")
elif(user_choice == Computer_choice):
    print("Match Draws")
else:
    print("You Loose")
