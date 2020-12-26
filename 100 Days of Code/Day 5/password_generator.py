import random

lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the py_password_generator!")
n_letters = int(input("How many letters would you like in your password?\n"))
choice_upper = input(
    "Letters mixed with both upper case and lower case? Y/N \n").lower()
upper_case = True if choice_upper == 'y' else False
n_symbols = int(input("How many symbols would you like?\n"))
n_numbers = int(input("How many numbers would you like? \n"))

g_password = []
for i in range(n_letters):
    ch = ''
    if upper_case:
        ch = random.choice(lower_letters+upper_letters)
    else:
        ch = random.choice(lower_letters)
    g_password.append(ch)

for i in range(n_symbols):
    g_password.append(random.choice(symbols))

for i in range(n_numbers):
    g_password.append(random.choice(numbers))

random.shuffle(g_password)
print("Here is your password: " + ''.join(g_password))
