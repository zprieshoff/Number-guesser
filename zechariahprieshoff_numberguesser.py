#Zechariah Prieshoff
#Number Guesser
#May 19, 2024
#Program chooses a random number and the user must guess the number in under 10 tries

import random

answer = random.randint(1, 50)
maxTries = 10

print("Welcome to the number guesser!\n==============================")

tries = 1
while tries <= maxTries:
    userGuess = input(f"You're on attempt {tries}, enter your guess!\n")
        
    if not userGuess.isdigit():
        print("Hey that's not a valid guess, numbers only!")
        print(f"You have {maxTries - tries} attempts left.")
        tries += 1
        continue
    userGuess = int(userGuess)
    
    if userGuess < answer:
        print("That's too low, try again!")
    elif userGuess > answer:
        print("That's too high, try again!")
    else:
        if tries == 1:
            print("Whoa first try!! Are you cheating?")
        else:
            print(f"You win!! \nYou got it in {tries} attempts!")
        break
    
    tries += 1
    
if tries > maxTries:
    print("You lost!! You were so close I bet.")
    print(f"The number was {answer}!")