#Hangman_game
import random
from Hangman_art import logo,stages
from Hangman_words import word_list
# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
lives = 6

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)
game_over = False

choosen_word = random.choice(word_list)

place_holder = ""
length = len(choosen_word)
for i in range(length):
    place_holder+="_"
print(f"Word to guess: "+ place_holder)

correct_letters = []
while not game_over:
    # TODO-6: - Update the code below to tell the user how many lives they have left.
    print(f"**************************** {lives}/6 lives remaining left ***********************************")
    guess = input("Guess the letter: ").lower()
    display = ""
    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in correct_letters:
        print(f"You have already guessed {guess} letter")
    else:
        for letter in choosen_word:
            if guess == letter:
                display+=guess
                correct_letters.append(guess)
            elif letter in correct_letters:
                display+=letter
            else:
                display+="_"

        print("Word to guess: "+ display)
    # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        #  e.g. You guessed d, that's not in the word. You lose a life.
        if guess not in choosen_word:
            lives-=1
            print(f"You guessed {guess}, that's not in the word. You lose a life.")    
            if lives == 0:
                game_over = True
                print(f"***********************IT WAS {choosen_word}!YOU LOSE**********************")

    # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
    if "_" not in display:
        print(f"***********************You Win*****************************")
        game_over = True
    # TODO-2: - Update the code below to use the stages List from the file hangman_art.py
    print(stages[lives])
