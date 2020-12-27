import random
from handman_wordlist import word_list
from hangman_art import logo, stages
import os

print(logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 7

print(f'Pssst, the solution is {chosen_word}.')

game_over = False
display = ["_"]*word_length

while not game_over:
    guess = input("Guess a letter. ").lower()
    os.system("clear")

    if guess in display:
        print(f"You already guessed {guess}.")
        continue

    for i in range(word_length):
        if chosen_word[i] == guess:
            display[i] = guess

    if guess not in chosen_word:
        print(f"The letter {guess} is not in the word. You will lose a life.")
        lives -= 1
        if lives == 0:
            print("\nHang'd the hangman. You LOOSE!")
            game_over = True

        print(stages[lives])

    print(" ".join(display))

    if '_' not in display:
        print("You've WON!")
        game_over = True
