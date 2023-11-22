from random import shuffle as shuffle
import pygame as pg
import os.path
import pprint


class Button:
    """Button obj for clicking on and stuff. Returns a Surface obj."""
    def __init__(self, x, y, image_path, scale):
        self.x = x
        self.y = y
        self.image = pg.image.load(image_path)
        self.image = pg.transform.scale_by(self.image, scale)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.enable = True
        self.view = True

    def draw(self):
        command = False
        # get mouse pos
        pos = pg.mouse.get_pos()

        # check mouse over and clicked condit.
        if self.rect.collidepoint(pos):
            if not self.clicked and (pg.mouse.get_pressed()[0] == 1) and (not command):
                self.clicked = True
                command = True
            elif not self.clicked and (pg.mouse.get_pressed()[0] == 1) and command:
                self.clicked = True
                command = False
        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # blit on screen
        if self.view and self.enable:
            screen.blit(self.image, (self.rect.x, self.rect.y))

        # worky or no worky
        if self.enable:
            return command
        else:
            return False


class Card(pg.sprite.Sprite):
    """Card obj to hold all info about the card."""
    def __init__(self, number, fill, color, shape):
        pg.sprite.Sprite.__init__(self)    # parent class constructor

        # card info
        self.number = number
        self.fill = fill
        self.color = color
        self.shape = shape
        self.image = ""


def makedeck():
    """Returns a pygame.sprite.Group class.
    The deck is 81 cards, each card is a pygame.sprite.Sprite"""

    number = ['3', '2', '1']
    fill = ['Hollow', 'Solid', 'Striped']
    color = ['Green', 'Red', 'Purple']
    shape = ['Oval', 'Diamond', 'Squiggle']
    deck_ = pg.sprite.Group()

    for num in number:
        for fil in fill:
            for col in color:
                for sha in shape:
                    # assign values
                    card_ = Card(num, fil, col, sha)
                    # assign image
                    card_.image = pg.image.load('_assets\\' + num + fil + col + sha + '.png')
                    card_.image = pg.transform.scale_by(card_.image, scale)  # scale 4x size (
                    card_.add(deck_)
    return deck_


def findsets(table):
    """Input a list of card classes, Return a list of all the sets on the table.
    Pro Tip: len() on the return of this function to count the number of sets on the table."""
    sets_ = []
    k = 0
    # look at 2 cards, calculate 3rd
    for i in range(0, len(table)):
        for j in range(1, len(table)):
            # lists to help determine 3rd card
            # refresh the list on loop cycle
            number = ['3', '2', '1']
            fill = ['Hollow', 'Solid', 'Striped']
            color = ['Green', 'Red', 'Purple']
            shape = ['Oval', 'Diamond', 'Squiggle']
            dummy_card = ['', '', '', '']

            # start comparisons
                # could look at the table for a 3rd card with the same number and no card is there,
                # then skip and go to the next pair of cards.
                # but that seems a little complicated and idk how much time that will actually save...
            if i < j:  # skip comparing everything twice :)
                # number
                if table[i].number == table[j].number:
                    dummy_card[0] = table[i].number
                else:
                    number.remove(table[i].number)
                    number.remove(table[j].number)
                    dummy_card[0] = number[0]

                # fill
                if table[i].fill == table[j].fill:
                    dummy_card[1] = table[i].fill
                else:
                    fill.remove(table[i].fill)
                    fill.remove(table[j].fill)
                    dummy_card[1] = fill[0]

                # color
                if table[i].color == table[j].color:
                    dummy_card[2] = table[i].color
                else:
                    color.remove(table[i].color)
                    color.remove(table[j].color)
                    dummy_card[2] = color[0]

                # shape
                if table[i].shape == table[j].shape:
                    dummy_card[3] = table[i].shape
                else:
                    shape.remove(table[i].shape)
                    shape.remove(table[j].shape)
                    dummy_card[3] = shape[0]

                # check if dummy card is on the table
                for m in range(2, len(table)):
                    if m != i and m != j:  # skip the 2 picked cards
                        if table[m].number == dummy_card[0]:
                            if table[m].fill == dummy_card[1]:
                                if table[m].color == dummy_card[2]:
                                    if table[m].shape == dummy_card[3]:
                                        sets_.append([[table[i].number, table[i].fill, table[i].color, table[i].shape],
                                                      [table[j].number, table[j].fill, table[j].color, table[j].shape],
                                                      [table[m].number, table[m].fill, table[m].color, table[m].shape]
                                                      ])
    return sets_


if __name__ == "__main__":
    pg.init()
    pg.font.init()

    # colors
    ltgray1 = (169, 183, 198)
    gray1 = (128, 128, 128)
    gray2 = (60, 63, 65)
    dkgray1 = (49, 51, 53)
    dkgray2 = (43, 43, 43)

    pixel_font = pg.font.SysFont('Celtic Time', 32)

    # constants for drawing
    scale = 4  # changing this might break a lot of stuff, BTW
    card_x = 36 * scale  # 144
    card_y = 17 * scale  # 68
    pad = 2.5 * scale  # 10 was working well

    # game run stuff
    resolution = (1100, 800)
    fps = 60
    screen = pg.display.set_mode(resolution)
    clock = pg.time.Clock()
    pg.display.set_caption('pySET!')
    icon = pg.image.load('_assets/pySET_icon.png')
    pg.display.set_icon(icon)

    # pre-load textures
    # main menu state
    splash = pg.image.load('_assets/pySET_splash.png')
    splash = pg.transform.scale_by(splash, scale)
    solo_btn = Button(14*pad, 200+232+pad, '_assets/solo_btn.png', scale)
    multi_btn = Button(resolution[0]-14*pad-400, 200+232+pad, '_assets/multi_btn.png', scale)
    exit_btn = Button((resolution[0]-400)/2, 200+232+2*pad+160, '_assets/exit_btn.png', scale)
    opt_btn = Button(resolution[0]-78-pad, pad, '_assets/opt_btn.png', scale/2)

    # solo/multi state
    select_img = '_assets/select_frame.png'
    select_btns = []
    x, y = card_x-8, 2*card_y-8
    for r in range(0, 6):  # only setting up 18 select buttons
        for c in range(0, 3):
            select_btns.append(Button(x, y, select_img, scale))
            select_btns[len(select_btns)-1].enable = False
            select_btns[len(select_btns)-1].view = False
            # increment
            x += card_x+8 + pad-8

        x = card_x-8
        y += card_y + pad
    set_call_btn = Button(4*card_x+4*pad+2*pad, 2*card_y-pad, '_assets/set_call_btn.png', scale/2)
    set_check_btn = Button(4 * card_x + 4 * pad + 2 * pad, 2 * card_y - pad, '_assets/set_check_btn.png', scale / 2)

    # options state -- read from a settings file
    # sound sliders (bgm, sfx)
    # video settings

    # make the deck
    deck_group = makedeck()
    deck = deck_group.sprites()  # list of card classes (the deck)
    for sd in range(0, 100):
        shuffle(deck)

    # set up the table
    size = 12  # initially 12 cards
    table_group = pg.sprite.Group()
    table = table_group.sprites()  # table cards as a list

    # set up discard
    discard_group = pg.sprite.Group()
    discard = discard_group.sprites()  # list of cards in the discard pile

    # game state variables
    run = True
    main_menu = True
    gamemode_solo = False
    solo_endscreen = False
    gamemode_multi = False
    deal = True
    selected_cards = []
    set_call = False
    selections_to_cards = []
    collected_sets = 0
    clean_up = False

    # main loop
    while run:
        # always fill the screen--helps clean up remaining artifacts
        screen.fill(gray2)

        # game states
        if main_menu:
            # splash
            screen.blit(splash, (235, 150, 636, 232))
            # 4 buttons
            if solo_btn.draw():  # solo game
                main_menu = False
                gamemode_solo = True
            if multi_btn.draw():  # add multiplayer in later
                main_menu = False
                gamemode_multi = True
            if exit_btn.draw():
                run = False
                pg.quit()
                quit()
            if opt_btn.draw():
                main_menu = False
                settings = True

        elif gamemode_solo:

            # mat for cards -- adjusts to size
            mat = pg.Surface((4 * pad + 3 * card_x, (size/3+1) * pad + (size/3) * card_y))
            mat.fill(gray1)
            screen.blit(mat, (card_x-pad, 2*card_y-pad, 4*pad+3*card_x, 5*pad+4*card_y))
            screen.blit(pg.font.Font.render(pixel_font, str(pg.mouse.get_pos()), 0, ltgray1),
                        (2, resolution[1]-28))

            # add size# of cards to table group
            try:
                for t in range(0, size):
                    deck[t].add(table_group)
                table = table_group.sprites()  # table cards as a list
            except IndexError:
                for t in range(0, len(deck)):
                    deck[t].add(table_group)
                table = table_group.sprites()  # table cards as a list
            else:
                for t in range(0, size):
                    deck[t].add(table_group)
                table = table_group.sprites()  # table cards as a list

            # check for sets in table group
            sets = findsets(table)
            num_sets = len(sets)
            num_sets_txt = pg.font.Font.render(pixel_font,
                                               'Sets on table: ' + str(num_sets),
                                               0,
                                               ltgray1)
            screen.blit(num_sets_txt, (6*pad+4*card_x, 3*card_y+pad, 0, 0))

            # place cards on screen
            t = 0
            x, y = card_x, 2*card_y
            for r in range(0, int(size/3)):
                for c in range(0, 3):
                    # draw cards
                    screen.blit(table[t].image, (x, y, card_x, card_y))

                    # enable selection buttons
                    select_btns[t].enable = True
                    if select_btns[t].draw():  # basically on click stuff
                        if set_call:
                            if not select_btns[t].view:
                                select_btns[t].view = True
                                selected_cards.append(select_btns[t])
                                if len(selected_cards) > 3:  # limit to 3 selected
                                    select_btns[select_btns.index(selected_cards[0])].view = False
                                    selected_cards.pop(0)
                            elif select_btns[t].view:  # deselect
                                select_btns[t].view = False
                                selected_cards.remove(select_btns[t])
                    # increment
                    x += card_x + pad
                    t += 1  # counter
                x = card_x
                y += card_y + pad

            # set_call_btn
            if set_call_btn.draw():  # SET called on click
                set_call = True  # enable selecting cards
                # start timer
                # select 3 cards
            # check set
            if set_call:
                if set_check_btn.draw() and len(selected_cards) == 3:  # click to confirm selected cards
                    # convert select_btn to card
                    selections_to_cards.append(table[select_btns.index(selected_cards[0])])
                    selections_to_cards.append(table[select_btns.index(selected_cards[1])])
                    selections_to_cards.append(table[select_btns.index(selected_cards[2])])
                    if len(findsets(selections_to_cards)) > 0:  # correct :)
                        collected_sets += 1
                        for i in range(0, 3):
                            # add to discard first, then remove from table and deck
                            table[select_btns.index(selected_cards[i])].add(discard_group)
                            deck[select_btns.index(selected_cards[i])].remove(deck_group)
                            deck.remove(deck[select_btns.index(selected_cards[i])])
                            table[select_btns.index(selected_cards[i])].remove(table_group)
                        # update lists
                        discard = discard_group.sprites()
                        table = table_group.sprites()
                        # don't update deck bc it was keeping the og order and reshuffling would mess up the table

                        # clean up / prep for next
                        clean_up = True

                    else:  # not a set :(
                        collected_sets -= 1
                        # clean up / prep for next
                        clean_up = True

                    # clean up / prep for next -- regardless of correct or not
                    if clean_up:
                        # remove all from convert list
                        selections_to_cards = []

                        # deselect cards
                        select_btns[select_btns.index(selected_cards[0])].view = False
                        select_btns[select_btns.index(selected_cards[1])].view = False
                        select_btns[select_btns.index(selected_cards[2])].view = False
                        selected_cards = []

                        # new table
                        # done! back to game
                        set_call = False
                        clean_up = False

            # end condition solo
            if len(deck) == 0 and num_sets == 0:
                solo_endscreen = True
                # high score = #sets/time = ##.# sets/minute

        # multiplayer
        elif gamemode_multi:
            # online and local?
            pass

        # game event handler
        for event in pg.event.get():
            # click detection
            if event.type == pg.MOUSEBUTTONDOWN:
                pass
            if event.type == pg.MOUSEBUTTONUP:
                click_pos = pg.mouse.get_pos()

            # quit
            if event.type == pg.QUIT:
                run = False
        pg.display.update()
        clock.tick(fps)

    pg.quit()
    quit()
