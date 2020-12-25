import random

# test_seed = int(input("Create a seed number: "))
# random.seed(test_seed)

names = input("Enter names seperated by a comma. ").split(", ")
# rand_int = random.randint(0, len(names) - 1)

# print(f"{names[rand_int]} is going to buy the meal today!")

print(f"{random.choice(names)} is going to buy the meal today!")