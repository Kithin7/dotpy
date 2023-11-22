import random
# import time
import numpy as np

import tkinter as tk
from PIL import Image


# Variables for each card: [number, fill, color, shape]
# number: 1, 2, 3
# fill: hollow, solid, striped
# color: red, green, purple
# shape: diamond, oval, squiggle
# number of cards = 3^4 = 81 cards
# each row = 1 card
# each col = 1 property (3 types each)

# shuffle deck function
def ShuffleTheDeck():
    for i in range(0, random.randint(1000, 2000)):
        np.random.shuffle(Deck)
    print("Shuffling the deck...")
    pass


# In[3]:


# deck setup
Deck = np.array([['', '', '', '']])
cardnumber = 0
for Number in range(0, 3):
    if Number == 0: SetNumber = '1'
    if Number == 1: SetNumber = '2'
    if Number == 2: SetNumber = '3'

    for Fill in range(0, 3):
        if Fill == 0: SetFill = 'hollow'
        if Fill == 1: SetFill = 'solid'
        if Fill == 2: SetFill = 'striped'

        for Color in range(0, 3):
            if Color == 0: SetColor = 'green'
            if Color == 1: SetColor = 'red'
            if Color == 2: SetColor = 'purple'

            for Shape in range(0, 3):
                if Shape == 0: SetShape = 'oval'
                if Shape == 1: SetShape = 'diamond'
                if Shape == 2: SetShape = 'squiggle'

                cardnumber = cardnumber + 1
                Deck = np.append(Deck, [[SetNumber, SetFill, SetColor, SetShape]], 0)

Deck = np.delete(Deck, [0], 0)
print('Creating the deck...')
ShuffleTheDeck()
tablesize = 12  # number of cards flipped up


# Table - shows the top x cards of the deck
def Table(x):
    for i in range(0, x):
        print(Deck[i])
    pass


ShuffleTheDeck()
Table(tablesize)

# def inplay(x) #should this be a func?
# 'in play' area
inplay = ['', '', '', '']
for i in range(0, tablesize):
    inplay = np.append(inplay, Deck[i], 0)
y = tablesize + 1
inplay = np.reshape(inplay, (y, 4))
inplay = np.delete(inplay, [0], 0)
# return inplay


def findset(a, b, tablesize):
    # findset finds the 3rd card to complete the SET from 2 given cards, in play of x cards
    # returns 1 if there is a set or 0 if not
    card1 = inplay[a]
    card2 = inplay[b]
    card3 = ['', '', '', '']

    Number = ['1', '2', '3']
    Fill = ['hollow', 'solid', 'striped']
    Color = ['red', 'green', 'purple']
    Shape = ['diamond', 'oval', 'squiggle']

    # check number
    if card1[0] == card2[0]:  # same
        card3[0] = card1[0]
    else:  # dif
        if card1[0] == Number[0]:
            Number = np.delete(Number, [0], 0)
        elif card1[0] == Number[1]:
            Number = np.delete(Number, [1], 0)
        else:
            Number = np.delete(Number, [2], 0)
        if card2[0] == Number[0]:
            Number = np.delete(Number, [0], 0)
        else:
            Number = np.delete(Number, [1], 0)
        card3[0] = Number[0]

        # check fill
    if card1[1] == card2[1]:
        card3[1] = card1[1]
    else:
        if card1[1] == Fill[0]:
            Fill = np.delete(Fill, [0], 0)
        elif card1[1] == Fill[1]:
            Fill = np.delete(Fill, [1], 0)
        else:
            Fill = np.delete(Fill, [2], 0)
        if card2[1] == Fill[0]:
            Fill = np.delete(Fill, [0], 0)
        else:
            Fill = np.delete(Fill, [1], 0)
        card3[1] = Fill[0]

    # check color
    if card1[2] == card2[2]:
        card3[2] = card1[2]
    else:
        if card1[2] == Color[0]:
            Color = np.delete(Color, [0], 0)
        elif card1[2] == Color[1]:
            Color = np.delete(Color, [1], 0)
        else:
            Color = np.delete(Color, [2], 0)
        if card2[2] == Color[0]:
            Color = np.delete(Color, [0], 0)
        else:
            Color = np.delete(Color, [1], 0)
        card3[2] = Color[0]

    # check shape
    if card1[3] == card2[3]:
        card3[3] = card1[3]
    else:
        if card1[3] == Shape[0]:
            Shape = np.delete(Shape, [0], 0)
        elif card1[3] == Shape[1]:
            Shape = np.delete(Shape, [1], 0)
        else:
            Shape = np.delete(Shape, [2], 0)
        if card2[3] == Shape[0]:
            Shape = np.delete(Shape, [0], 0)
        else:
            Shape = np.delete(Shape, [1], 0)
        card3[3] = Shape[0]

    # print(card1)
    # print(card2)
    # print(card3)

    # check if CARD3 is in 'inplay'
    for i in range(0, tablesize):  # number & fill & color & shape
        if (card3[0] == inplay[i][0]) and (card3[1] == inplay[i][1]) and (card3[2] == inplay[i][2]) and (
                card3[3] == inplay[i][3]):
            # print('There is a SET in play for the selected cards')
            setfound = 1
        else:
            # print('There is Not a SET in play for the selected cards')
            setfound = 0

    return setfound



def IsThereASet(tablesize):
    # checks play area for all possible sets
    # returns number of possible sets
    y = 0
    for i in range(0, tablesize):  # is this the right looping size?
        for j in range(1, tablesize):
            x = findset(i, j, tablesize)
            y = y + x
            numfound = str(y) + " SET(s) found!"
    return numfound


def WhatIsTheSet(a, b, tablesize):
    # shows (all) possible set(s)
    # returns a set
    card1 = inplay[a]
    card2 = inplay[b]
    card3 = ['', '', '', '']

    Number = ['1', '2', '3']
    Fill = ['hollow', 'solid', 'striped']
    Color = ['red', 'green', 'purple']
    Shape = ['diamond', 'oval', 'squiggle']

    # check number
    if card1[0] == card2[0]:  # same
        card3[0] = card1[0]
    else:  # dif
        if card1[0] == Number[0]:
            Number = np.delete(Number, [0], 0)
        elif card1[0] == Number[1]:
            Number = np.delete(Number, [1], 0)
        else:
            Number = np.delete(Number, [2], 0)
        if card2[0] == Number[0]:
            Number = np.delete(Number, [0], 0)
        else:
            Number = np.delete(Number, [1], 0)
        card3[0] = Number[0]

        # check fill
    if card1[1] == card2[1]:
        card3[1] = card1[1]
    else:
        if card1[1] == Fill[0]:
            Fill = np.delete(Fill, [0], 0)
        elif card1[1] == Fill[1]:
            Fill = np.delete(Fill, [1], 0)
        else:
            Fill = np.delete(Fill, [2], 0)
        if card2[1] == Fill[0]:
            Fill = np.delete(Fill, [0], 0)
        else:
            Fill = np.delete(Fill, [1], 0)
        card3[1] = Fill[0]

    # check color
    if card1[2] == card2[2]:
        card3[2] = card1[2]
    else:
        if card1[2] == Color[0]:
            Color = np.delete(Color, [0], 0)
        elif card1[2] == Color[1]:
            Color = np.delete(Color, [1], 0)
        else:
            Color = np.delete(Color, [2], 0)
        if card2[2] == Color[0]:
            Color = np.delete(Color, [0], 0)
        else:
            Color = np.delete(Color, [1], 0)
        card3[2] = Color[0]

    # check shape
    if card1[3] == card2[3]:
        card3[3] = card1[3]
    else:
        if card1[3] == Shape[0]:
            Shape = np.delete(Shape, [0], 0)
        elif card1[3] == Shape[1]:
            Shape = np.delete(Shape, [1], 0)
        else:
            Shape = np.delete(Shape, [2], 0)
        if card2[3] == Shape[0]:
            Shape = np.delete(Shape, [0], 0)
        else:
            Shape = np.delete(Shape, [1], 0)
        card3[3] = Shape[0]

    # print(card1)
    # print(card2)
    # print(card3)

    # check if CARD3 is in 'inplay'
    for i in range(0, tablesize):  # number & fill & color & shape
        if (card3[0] == inplay[i][0]) and (card3[1] == inplay[i][1]) and (card3[2] == inplay[i][2]) and (
                card3[3] == inplay[i][3]):
            # print('There is a SET in play for the selected cards')
            thesetis = [[card1], [card2], [card3]]
        else:
            # print('There is Not a SET in play for the selected cards')
            thesetis = []

    return thesetis


def ShowSets(tablesize):
    # checks play area for all possible sets
    # returns number of possible sets
    y = 0
    setsfound = ['', '', '', '']
    for i in range(0, tablesize):
        for j in range(0, tablesize):
            if i < j:  # filtering comparisons
                if WhatIsTheSet(i, j, tablesize) != []:  # second filter for no sets
                    y = y + 1
                    z = WhatIsTheSet(i, j, tablesize)
                    setsfound = np.append(setsfound, z, 0)

    setsfound = np.delete(setsfound, [0], 0)
    setsfound = np.reshape(setsfound, (len(setsfound), 1))
    print(y)
    return setsfound


print(inplay)
aaa = IsThereASet(tablesize)
print(aaa)
bbb = WhatIsTheSet(2, 3, tablesize)
print(bbb)
ccc = ShowSets(tablesize)
print(ccc)
ShuffleTheDeck()


window = tk.Tk()
for i in range(4):
    window.columnconfigure(i, weight=1)
    window.rowconfigure(i, weight=1)
    for j in range(3):
        frame = tk.Frame(
                        master=window,
                        relief=tk.FLAT,
                        borderwidth=1
                        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        button = tk.Button(master=frame, text=f"Row {i}\nColumn {j}")
        button.pack(padx=5, pady=5)
tk.mainloop()