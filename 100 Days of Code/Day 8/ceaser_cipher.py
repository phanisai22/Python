from art import logo


def caesar(text, shift, direction):
    if direction == 'decode':
        shift *= -1

    end_text = ''
    for letter in text:
        if letter not in alphabet:
            end_text += letter
            continue
        value = alphabet.index(letter)
        end_text += alphabet[value + shift]

    return f'{direction}d code: {end_text}'


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
over = False

print(logo + '\n')

while not over:
    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 25
    print(caesar(text, shift, direction))
    choise = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if choise == 'no':
        print('Good Bye!')
        over = True
