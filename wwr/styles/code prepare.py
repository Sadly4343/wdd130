word = "apple"
guess = input("Guess a 5 letter word?")

for letter in word:
    if letter.lower() == guess.lower():
        print(letter.upper(), end="")
    elif letter.lower() in guess.lower():
        print(letter.lower(), end="")
    else:
        print("_")
print()