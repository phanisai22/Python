import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

face = random.randint(0, 1)
if face:
    print("Head")
else:
    print("Tail")
