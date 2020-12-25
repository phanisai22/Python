import random

hands = [
    """
      _______
  ---'   ____)
        (_____)
        (_____)
        (____)
  ---.__(___)
""",

    '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
    '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]

choice = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

print("You choose: ")
print(hands[choice])

c_choice = random.randint(0, 2)
win_combinations = [[2, 1], [0, 2], [1, 0]]

print("Computer choose: ")
print(hands[c_choice])

if choice == c_choice:
    print("Draw.")
elif [choice, c_choice] in win_combinations:
    print("You Win.")
else:
    print("You Lose.")
