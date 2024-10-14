# Imports the random statement.
import random
mode = str(input("What level do you want? Ex.(Hard, Easy, Meduim) "))
num_answer = 0 
guesses = 0
# Checks if the mode is hard or someting else.
if mode == "Hard" or mode == "hard":
    num_answer = random.randint(1, 100)
    guess = int(input("Guess the number from 1-100 "))
    guesses += 1
elif mode == "Meduim" or mode == "meduim":
    num_answer = random.randint(1, 50)
    guess = int(input("Guess the number from 1-50 "))
    guesses += 1
elif mode == "Easy" or mode == "easy":
    num_answer = random.randint(1, 30)
    guess = int(input("Guss the number from 1-30 "))
    guesses += 1
else:
    mode = str(input("What level do you want? ex(Hard, Easy, Meduim)"))




while not num_answer == guess:
    if num_answer == guess:
        print("You got it!")
    elif num_answer > guess:
        print(f"It is more than {guess}")
        guesses += 1
    elif num_answer < guess:
        print(f"It is less than {guess}")
        guesses += 1
    guess = int(input("Guss the number again "))
print(f"You got it! It was {num_answer}")
print(f"You got the answer in {guesses} guesses")
