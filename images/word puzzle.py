def check_word():
    secret_word = "apple"
    attempt = 8
    num1 = 9
    while attempt > 0:
        guess = str(input("Guess the word: "))
        if guess == secret_word:
            print(f"You guessed the word correct! in {guesses}")
            break
        elif len(guess) != len(secret_word):
            print("Choose the correct amount of letters")
            continue
        else:
            attempt = attempt - 1
            print(f"You have {attempt} attempt left")
            for char, word in zip(secret_word, guess):
                if word in secret_word and word in char:
                    print(word.upper(), end="")
                elif word in secret_word:
                    print(word.lower(), end="")
                else:
                    print("_", end="")
            if attempt == 0:
                print("Game Over")
            guesses = num1 - attempt
check_word()