### Dice Simulator ###
# concepts to keep in mind
#   - random
#   - integers
#   - print
#   - while loops

import random
import time
seed_me_captain = time.time()
random.seed(seed_me_captain)


print('Welcome to Dice Sim!')

def dice_menu():
    print(5*"*", "Select a die",5*"*")
    print(" 1. d4")
    print(" 2. d6")
    print(" 3. d8")
    print(" 4. d10")
    print(" 5. d12")
    print(" 6. d20")
    print(" 7. d100")
    print(" 8. dX")
    print(" 9. Exit")
    print(24 * "-")
    return
    
loop = True
while loop:
    dice_menu()
    choice = int(input("Selection:  "))

    if choice == 1:
        numb = int(input("How many?  "))
        while numb > 0:
            roll = random.randint(1,4)
            print(roll)
            numb = numb - 1
        
    elif choice == 2:
        numb = int(input("How many?  "))
        while numb > 0:
            roll = random.randint(1,6)
            print(roll)
            numb = numb - 1
        
    elif choice == 3:
        numb = int(input("How many?  "))
        while numb > 0:
            roll = random.randint(1,8)
            print(roll)
            numb = numb - 1
            
    elif choice == 4:
        numb = int(input("How many?  "))
        while numb > 0:
            roll = random.randint(1,10)
            print(roll)
            numb = numb - 1
        
    elif choice == 5:
        numb = int(input("How many?  "))
        while numb > 0:
            roll = random.randint(1,12)
            print(roll)
            numb = numb - 1
        
    elif choice == 6:
        numb = int(input("How many?  "))
        while numb > 0:
            roll = random.randint(1,20)
            print(roll)
            numb = numb - 1
        
    elif choice == 7:
        numb = int(input("How many?  "))
        while numb > 0:
            roll = random.randint(1,100)
            print(roll)
            numb = numb - 1
        
    elif choice == 8:
        x = int(input("dX: X =  "))
        numb = int(input("How many?  "))
        while numb > 0:
            roll = random.randint(1,x)
            print(roll)
            numb = numb - 1

    elif choice == 9:
        break
    
    else:
        numb = print("Oops! Make sure you enter a vaild number [1-9]! \nTry again!")
        



