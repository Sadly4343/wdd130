def check_word():
  hidden_word = "snail"
  attempt = 6
  while attempt > 0:
    guess = str(input("Guess the word: "))
    if guess == hidden_word:
      print("You guessed the words correctly! WIN 🕺🕺🕺 ")
      break
    else:
      attempt = attempt - 1
      print(f"you have {attempt} attempt(s) ,, \n ")
      for char, word in zip(hidden_word, guess):
            if word in hidden_word and word in char:
                print(word + " ✔ ")

            elif word in hidden_word:
                print(word + " ➕ ")
            else:
                print(" ❌ ")
      if attempt == 0:
        print(" Game over !!!! ")

check_word()