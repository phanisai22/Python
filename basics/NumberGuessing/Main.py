import random

highestNumber = 10
answer = random.randint(1, highestNumber)
start = 1
end = highestNumber
userGuess = -1
while userGuess != answer:
    userGuess = int(input("Guess the number from {} to {} : ".format(start, end)))
    if (userGuess < start and userGuess != 0) or userGuess > end:
        # when the user enters the invalid number i.e out of our provided
        # bound then the game is terminated .
        print("Invalid move. Game over !")
        break
    elif userGuess < answer and userGuess > 0:
        print("please guess higher ")
        start = userGuess
    elif userGuess > answer and userGuess <= highestNumber:
        print("please guess lower ")
        end = userGuess
    elif userGuess == 0:
        print("Game exited")
        break

else:
    print("You won the game !")

print('The random number generated was {}'.format(answer))
