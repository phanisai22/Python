import random
import sys

play = True

while play:
    print("\n\n\n==================Guess The Number==================\n\n\n")
    print("Hey friend!")
    start_number = int(input("Enter the starting range : "))
    end_number = int(input("Enter the ending range : "))

    guess_number = random.randint(start_number, end_number)

    if end_number - start_number < 3:
        print("Invalid range")
    else:
        print("I'm guessing a number ranging from " + str(start_number) + " to " + str(end_number))
        allowed_guesses = int((end_number - start_number) / 3)

        print("You will be allowed to guess only " + str(allowed_guesses) + " times.")

        for guesses_taken in range(0, allowed_guesses):
            guess = int(input("Enter your guess " + str(guesses_taken + 1) + " : "))
            if guess > guess_number:
                print("Your guess is too high")
            elif guess < guess_number:
                print("Your guess is too low")
            else:
                # Guessed the correct number.
                print("Good job friend! You guessed my number in " + str(guesses_taken + 1) + " Attempts")
                break

    print("Wanna guess again? y / n")
    if input().lower() == 'n':
        play = False
    else:
        print("Starting the new game.")
