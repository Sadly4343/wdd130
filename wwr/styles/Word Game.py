word = "apple"

print('Guess a word?')
guess = input('What is your guess?')

for letter in word:
    if letter.lower() == guess.lower():
        print(letter.upper(), end="")
    else:
        print(letter.lower(), end="")
print()

for letter in word:
    if letter.lower() == guess.lower():
        print("_", end="")
    else:
        print(letter.lower(), end="")
print()
