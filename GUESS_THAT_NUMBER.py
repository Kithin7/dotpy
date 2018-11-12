# concepts to keep in mind:
#   - random number functions   - while loops       - if/else 
#   - variables                 - print             - I/O
#   - integers

import random
import time

yes = ["y", 'yes', 'yee', 'ye', 'yah', 'yeah', 'sure']
no = ["n", "no", "nah", "noda", "no way", "nope"]

Acount = 1
Bcount = 0
direction = "up"
playing = True

print("WELCOME TO GUESS THE NUMBER!!")
time.sleep(2)
while Bcount <= random.randint(6,12):
    if direction == "up":
        if Acount <= 10:
            print(Acount * "*")
            time.sleep(.025)
            Acount = Acount + 1
        else:
            direction = "down"
            Bcount = Bcount + 1
            
    elif direction == "down":
        if Acount > 1:
            Acount = Acount - 1
            print(Acount * "*")
            time.sleep(.025)
        else:
            direction = "up"
            Bcount = Bcount + 1
    else:
        input("Oops! Something went wrong...")
else:
    answer = random.randint(0,100)
    tries = 0
    Round = 1

    print("HERE WE GO! \nThe rules are simple: \nGuess a positive integer (0-100) \nand you will be told if you are too HIGH or too LOW!")
    while playing == True:
        tries = tries + 1
        guess = int(input("\nWhat is your guess?  "))
        
        if guess == answer & tries == 1:
            print("\nWOW! You guessed it right on the money!!")
            again = input("Would you like to play again?  ")
            answer = random.randint(0,100)
            if again in no:
                playing = False
                input("Good playing with you!")
            else:
                tries = 0
                Round = Round + 1
                print("\nROUND",Round,"GO!")
                
        elif guess == answer:
            print("WOW! You guessed the answer in",tries,"tries!")
            again = input("Would you like to play again?  ")
            answer = random.randint(0,100)
            if again in no:
                playing = False
                input("Good playing with you!")
            else:
                tries = 0
                Round = Round + 1
                print("\nROUND",Round,"GO!")
            
        elif guess > answer:
            print("Your guess is...")
            time.sleep(.50)
            print("...")
            time.sleep(.50)
            print("...")
            time.sleep(.50)
            print("too HIGH!")
            
        elif guess < answer:
            print("Your guess is...")
            time.sleep(.50)
            print("...")
            time.sleep(.50)
            print("...")
            time.sleep(.50)
            print("too LOW!")
            
        else:
            input("Oops! Something went wrong...")
        
