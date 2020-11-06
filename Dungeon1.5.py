print("Welcome to Kithin's Dungeon of Doom!")
Char=input("Enter name here: ")
if Char=="Doug":
    PW=input("Password: ")
    if PW=="NY4N":
            print("You win! Here's how to get through. *Two ways*")
            print("2, Sneak, left, right, right, right, nicely greet old man, Yes, 42.")
            print("1,")
if Char!="Doug":
    print("Okay, %s, would you like to go left, 1, or right, 2?" % Char)
    choice=input("Choice: ")
    if choice=="1":
        print("So, you turn left. You run into a puddle of water that graually becomese deeper as you walk further into it.")
        a=input("Do you 'swim' or use the 'boat': ")
        if a=="swim":
            print("You start to swim off of the shore. After awhile of swimming you think you see something underwater.")
            b=input("Do you continue to 'swim' or do you 'dive'?: ")
            if b=="swim":
                print("You swim across the small pond and make it to the other side.")
                print("Once apown shore, you proceed into a goblin merchant's tent.")
                c=input("The merchant offers you a sword for 500 gold, do you accept? yes or no: ")
                if c=="yes":
                    print("The goblin merchant is pleased to sell you a high quallity sword for a low price.")
                    SW=input("He tells you to nams your sword. You decide on the name: ")
                    print("After naming your sword %s, the goblin moves one of his shelves and reveals a secret path." % SW)
                    print("You continue down the path and run into a room that has a skilled lv.10 Master Warrior Bear.")
                    print("The Warrior Bear notices your sword %s, and offers a duel to the death. You accept the offer." % SW)
                    print("You succeed in winning the duel to the death against the Warrior Bear.")
                    print("The dieing Bear's last words were, \"%s, when nothing goes right, go left.\"" % Char)
                    D=input("While confused at what the Warroir Bear said, you notice the two doors. Do you go through the left or right?: ")
                    if D=="right":
                        print("You walk through the right door and continue down a long hallway.")
                        print("When you reach the end of the hallway, you see light coming from the left, but the right is pitch black.")
                        E=input("Do you walks 'left' toward the light, or 'right' toward the pitch black?: ")
                        if E=="right":
                            print("You walk cowerdly into the pitch black part of the dungeon and run into a wall witch scares you enough to pee your pants.")
                            print("You notice, after changing clothing, that the wall has a ladder hanging on it. You climb the ladder and proceed to a room.")
                            print("Inside of the room is an very old man.")
                            GR=input("You greet the old timer by saying\": \"")
                            print("The old man just laughs. You stand there feeling akward.")
                            print("You notice that you are standing on woodenplanks, the old man tells you that under the planks is a pit of spikes.")
                            print("Not taking chances, you ask the old man what he wants. He replies he wants you answer a riddle.")
                            RID=input("Do you want to play the old man's game? yes or no: ")
                            if RID=="yes":
                                print("Thinking that you're pretty good at riddles, you accept his challenge, not having much of a choice anyway.")
                                print("The old man asks you, \"What is the only number that you have incountered throughout this dungeon.?\"")
                                F=input("Not remebering any numbers though the whole dungeon, you answer: ")
                                if F=="42":
                                    print("Congrats you young wipper-snapper!")
                                    print("You probably guessed to get to here, but good job!")
                                    print("Thanks for playing. made by Kithin. Coded in Python.")
                                if F=="10":
                                    print("Close, but no cigar! HAHAHHAHAHAHHAH!")
                                    print("FAILURE")
                                    print("The old man pushes the button beside him and you fall to your death.")
                                    print("Hint: Remember everthing that has been said to you?")
                                if F!="42":
                                    print("FAILURE")
                                    print("The old man pushes the button beside him and you fall to your death.")
                            if RID=="no":
                                print("FAILURE")
                                print("The old man pushes the button beside him and you fall to your death.")
                        if E=="left":
                            print("You walk toward the light and enter the room. Inside of the room is undisputed world champion grandmaster Emanuel Lasker")
                            print("Emanuel Lasker offers to play a match of chess, but who ever loses goes to the shadow realm forever.")
                            print("Remembering how you won the USCF (United States Chess Federation) league 2 years ago, you accept Mr.Lasker's offer.")
                            print("FAILURE")
                            print("After four long hours of chess, you lost and sent to the shadow realm forever.")
                    if D=="left":
                        print("You walk through the left door see a sign that says \"42\".")
                        print("FAILURE")
                        print("After reading the confusing sign, you imiditly fall through the ground into a spikey pit and die.")
                if c=="no":
                    print("FAILURE")
                    print("The goblin merchant is offended and kills you.")
            if b=="dive":
                print("While you are under water, see a shiny peral. Do you pick it up?")
                cc=input("yes or no: ")
                if cc =="no":
                    print("You decide that the peral is probably a trap and turn away.")
                    dd=input("Do you want to surface? yes or no?: ")
                    if dd=="no":
                        print("The boat from before just sailed by with pirates onboard.")
                        print("So you swim stealthily to shore like a Navy S.E.A.L.")
                        print("Once apown shore, you proceed into a goblin merchant's tent.")
                c=input("The merchant offers you a sword for 500 gold, do you accept? yes or no: ")
                if c=="yes":
                    print("The goblin merchant is pleased to sell you a high quallity sword for a low price.")
                    SW=input("He tells you to nams your sword. You decide on the name: ")
                    print("After naming your sword %s, the goblin moves one of his shelves and reveals a secret path." % SW)
                    print("You continue down the path and run into a room that has a skilled lv.10 Master Warrior Bear.")
                    print("The Warrior Bear notices your sword %s, and offers a duel to the death. You accept the offer." % SW)
                    print("You succeed in winning the duel to the death against the Warrior Bear.")
                    print("The dieing Bear's last words were, \"%s, when nothing goes right, go left.\"" % Char)
                    D=input("While confused at what the Warroir Bear said, you notice the two doors. Do you go through the left or right?: ")
                    if D=="right":
                        print("You walk through the right door and continue down a long hallway.")
                        print("When you reach the end of the hallway, you see light coming from the left, but the right is pitch black.")
                        E=input("Do you walks 'left' toward the light, or 'right' toward the pitch black?: ")
                        if E=="right":
                            print("You walk cowerdly into the pitch black part of the dungeon and run into a wall witch scares you enough to pee your pants.")
                            print("You notice, after changing clothing, that the wall has a ladder hanging on it. You climb the ladder and proceed to a room.")
                            print("Inside of the room is an very old man.")
                            GR=input("You greet the old timer by saying\": \"")
                            print("The old man just laughs. You stand there feeling akward.")
                            print("You notice that you are standing on woodenplanks, the old man tells you that under the planks is a pit of spikes.")
                            print("Not taking chances, you ask the old man what he wants. He replies he wants you answer a riddle.")
                            RID=input("Do you want to play the old man's game? yes or no: ")
                            if RID=="yes":
                                print("Thinking that you're pretty good at riddles, you accept his challenge, not having much of a choice anyway.")
                                print("The old man asks you, \"What is the only number that you have incountered throughout this dungeon.?\"")
                                F=input("Not remebering any numbers though the whole dungeon, you answer: ")
                                if F=="42":
                                    print("Congrats you young wipper-snapper!")
                                    print("You probably guessed to get to here, but good job!")
                                    print("Thanks for playing. made by Kithin. Coded in Python.")
                                if F=="10":
                                    print("Close, but no cigar! HAHAHHAHAHAHHAH!")
                                    print("FAILURE")
                                    print("The old man pushes the button beside him and you fall to your death.")
                                    print("Hint: Remember everthing that has been said to you?")
                                if F!="42":
                                    print("FAILURE")
                                    print("The old man pushes the button beside him and you fall to your death.")
                            if RID=="no":
                                print("FAILURE")
                                print("The old man pushes the button beside him and you fall to your death.")
                        if E=="left":
                            print("You walk toward the light and enter the room. Inside of the room is undisputed world champion grandmaster Emanuel Lasker")
                            print("Emanuel Lasker offers to play a match of chess, but who ever loses goes to the shadow realm forever.")
                            print("Remembering how you won the USCF (United States Chess Federation) league 2 years ago, you accept Mr.Lasker's offer.")
                            print("FAILURE")
                            print("After four long hours of chess, you lost and sent to the shadow realm forever.")
                    if D=="left":
                        print("You walk through the left door see a sign that says \"42\".")
                        print("FAILURE")
                        print("After reading the confusing sign, you imiditly fall through the ground into a spikey pit and die.")
                if c=="no":
                    print("FAILURE")
                    print("The goblin merchant is offended and kills you.")
                    if dd=="yes":
                        print("FAILURE")
                        print("You were shot by pirates! ARG!!")
                if cc =="yes":
                    print("FAILURE")
                    print("Stromfin (a giant pike fish) eats you in one glup.")
        if a=="boat":
            print("FAILURE")
            print("You were attack by pirates and was made to walk the plank. ARG!!")
    if choice=="2":
        print("So, you turn right. You see an sleeping orge.")
        A=input("What do you do, 'battle' the orge to show your strength or 'sneak' pass him: ")
        if A=="sneak":
            print("You snuck pass the ogre.")
            B=input("Do you continue straight or turn left?: ")
            if B=="straight":
                print("You open the metal door to continue through the hallway, seems to be hot.")
                print("FAILURE")
                print("You were incirated by lava.")
            if B=="left":
                print("You turn left into a blank room. There are two passages.")
                C=input("Do you go right or left?: ")
                if C=="right":
                    print("The passage takes you to a poorly lit room that has a large rock that is pierced with a sword.")
                    SW=input("You pull the sword from the rock and name it: ")
                    print("After naming your sword %s, you find that the room has no halls, so you return to the previous room." % SW)
                    print("You go through the left passage. The passage ends in a room. This room has a skilled lv.10 Master Warrior Bear.")
                    print("The Warrior Bear notices your sword %s, and offers a duel to the death. You accept the offer." % SW)
                    print("You succeed in winning the duel to the death against the Warrior Bear.")
                    print("The dieing Bear's last words were, \"%s, when nothing goes right, go left.\"" % Char)
                    D=input("While confused at what the Warroir Bear said, you notice the two doors. Do you go through the left or right?: ")
                    if D=="right":
                        print("You walk through the right door and continue down a long hallway.")
                        print("When you reach the end of the hallway, you see light coming from the left, but the right is pitch black.")
                        E=input("Do you walks 'left' toward the light, or 'right' toward the pitch black?: ")
                        if E=="right":
                            print("You walk cowerdly into the pitch black part of the dungeon and run into a wall witch scares you enough to pee your pants.")
                            print("You notice, after changing clothing, that the wall has a ladder hanging on it. You climb the ladder and proceed to a room.")
                            print("Inside of the room is an very old man.")
                            GR=input("You greet the old timer by saying\": \"")
                            print("The old man just laughs. You stand there feeling akward.")
                            print("You notice that you are standing on woodenplanks, the old man tells you that under the planks is a pit of spikes.")
                            print("Not taking chances, you ask the old man what he wants. He replies he wants you answer a riddle.")
                            RID=input("Do you want to play the old man's game? Yes or No: ")
                            if RID=="yes":
                                print("Thinking that you're pretty good at riddles, you accept his challenge, not having much of a choice anyway.")
                                print("The old man asks you, \"What is the only number that you have incountered throughout this dungeon.?\"")
                                F=input("Not remebering any numbers though the whole dungeon, you answer: ")
                                if F=="42":
                                    print("Congrats you young wipper-snapper!")
                                    print("You probably guessed to get to here, but good job!")
                                    print("Thanks for playing. made by Kithin. Coded in Python.")
                                if F=="10":
                                    print("Close, but no cigar! HAHAHHAHAHAHHAH!")
                                    print("FAILURE")
                                    print("The old man pushes the button beside him and you fall to your death.")
                                    print("Hint: Remember everthing that has been said to you?")
                                if F!="42":
                                    print("FAILURE")
                                    print("The old man pushes the button beside him and you fall to your death.")
                            if RID=="no":
                                print("FAILURE")
                                print("The old man pushes the button beside him and you fall to your death.")
                        if E=="left":
                            print("You walk toward the light and enter the room. Inside of the room is undisputed world champion grandmaster Emanuel Lasker")
                            print("Emanuel Lasker offers to play a match of chess, but who ever loses goes to the shadow realm forever.")
                            print("Remembering how you won the USCF (United States Chess Federation) league 2 years ago, you accept Mr.Lasker's offer.")
                            print("FAILURE")
                            print("After four long hours of chess, you lost and sent to the shadow realm forever.")
                    if D=="left":
                        print("You walk through the left door see a sign that says \"42\".")
                        print("FAILURE")
                        print("After reading the confusing sign, you imiditly fall through the ground into a spikey pit and die.")
                if C=="left":
                    print("You go through the left passage.")
                    print("The passage ends in a room. This room contains a skilled lv.10 Master Warrior Bear.")
                    print("FAILURE")
                    print("The Warroir Bear hands you a sword and honorably fights you. He succeeds in winning the duel to the death.")
        if A=="battle":
            print("FAILURE")
            print("You were ripped in half by the mightly ogre's strenght.")
