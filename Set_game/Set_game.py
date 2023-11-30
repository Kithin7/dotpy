from random import shuffle as shuffle
import pygame as pg
import time
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


class Slider:
    """horizontal slider. Returns a slider class obj."""
    def __init__(self, window, x:int, y:int, lower_val:float, upper_val:float, height:int, initial:float, bar_color:tuple, handle_color:tuple):
        self.window = window
        self.x = x
        self.y = y
        self.lower = lower_val
        self.upper = upper_val
        self.height = height
        self.initial = initial

        self.bar_color = bar_color
        self.handle_color = handle_color

        length = self.upper - self.lower
        self.handle_rect = pg.rect.Rect(self.x + self.initial, self.y, length * 0.15, self.y + self.height)


    def draw(self):
        length = self.upper - self.lower

        # draw the bar (range)
        bar = pg.surface.Surface((self.upper - self.lower, self.height))
        bar.fill(self.bar_color)
        self.window.blit(bar, (self.x, self.y,))

        # draw the handle (value)
        handle = pg.surface.Surface((self.handle_rect[2], self.height))
        handle.fill(self.handle_color)
        self.window.blit(handle, self.handle_rect)

    def move(self):
        # mouse pos
        pos = pg.mouse.get_pos()

        # mouse on handle
        if self.handle_rect.collidepoint(pos):
            print('on')

    def value(self):
        loc = handle.get_rect()


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
            if i < j:  # skip comparing everything twice
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
                    if m != i and m != j and m > j:  # skip the 2 picked cards
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
    white = (255, 255, 255)
    ltgray1 = (169, 183, 198)
    gray1 = (128, 128, 128)
    gray2 = (60, 63, 65)
    dkgray1 = (49, 51, 53)
    dkgray2 = (43, 43, 43)
    black = (0, 0, 0)
    green = (20, 167, 80)
    red = (234, 28, 45)
    purple = (97, 51, 148)
    blue = (27, 102, 232)
    yellow = (244, 180, 27)
    blue2 = (72, 136, 186)
    yellow2 = (255, 232, 115)

    # fonts
    pixel_font = pg.font.SysFont('Celtic Time', 32)
    pixel_font_big = pg.font.SysFont('Celtic Time', 120)

    # constants for drawing
    scale = 4  # changing this might break a lot of stuff, BTW
    card_x = 36 * scale  # 144
    card_y = 17 * scale  # 68
    pad = 2.5 * scale  # 10 was working well

    # game run stuff
    resolution = (1100, 800)  # 1100, 800
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
    size = 12
    # mat bg
    mat = pg.Surface((4 * pad + 3 * card_x, (size / 3 + 1) * pad + (size / 3) * card_y))
    mat.fill(gray1)
    # blank card for at end of deck
    blank_card = pg.Surface((card_x, card_y))
    blank_card.fill(gray1)
    # setting up the selection buttons
    select_img = '_assets/select_frame.png'
    select_btns = []  # list of the selection buttons
    x, y = card_x-8, 2*card_y-8
    for r in range(0, 6):  # only setting up 18 select buttons bc it's unlikely to need more
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
    # game time loc
    clock_loc = (2 * card_x - 3 * pad, card_y - pad)
    # end screen menu
    solo_end_menu1 = pg.surface.Surface((resolution[0], resolution[1]), pg.SRCALPHA)
    solo_end_menu1.fill((gray2[0], gray2[1], gray2[2], 200))
    solo_end_menu2 = pg.surface.Surface((resolution[0]*.6, resolution[1]*.6), pg.SRCALPHA)
    solo_end_menu2.fill((dkgray1[0], dkgray1[1], dkgray1[2], 240))
    back_to_main_btn = Button(300, 450, '_assets/main_btn.png', scale)

    # options state -- read from a settings file
        # sound sliders (bgm, sfx)
        # video settings
    bgm_slider = Slider(screen, int(resolution[0] * 0.3), int(resolution[1] * 0.4), 0, 100, 25, 50, gray1, green)
    sfx_slider = Slider(screen, int(resolution[0] * 0.3), int(resolution[1] * 0.45), 0, 100, 25, 50, gray1, red)
    call_time_slider = Slider(screen, int(resolution[0] * 0.3), int(resolution[1] * 0.50), 0, 100, 25, 50, gray1, purple)
    settings_to_main_btn = Button(int(resolution[0] * 0.3), int(resolution[1] * 0.55), '_assets/main_btn.png', scale)

    # game state variables
    run = True
    main_menu = True
    settings = False
    game_clock = 0
    show_num_sets = False
    gamemode_solo = False
    solo_endscreen = False
    gamemode_multi = False
    gamemode_multi_local = False
    gamemode_multi_online = False
    selected_cards = []
    set_call = False
    set_call_time_master = 10
    selections_to_cards = []
    collected_sets = 0
    clean_up = False
    end_bg = True
    # debug
    debug_short_deck = True
    debug_show_mouse_pos = False
    debug_printout = False

    # main loop
    while run:
        # game states
        # main menu
        if main_menu:
            # fill the screen
            screen.fill(gray2)
            # splash
            screen.blit(splash, (235, 150, 636, 232))
            # 4 buttons
            # settings button
            if opt_btn.draw():
                settings = True
                main_menu = False
                time.sleep(.1)

            # solo game
            if solo_btn.draw():
                # make the deck
                deck_group = makedeck()
                deck = deck_group.sprites()  # list of card classes (the deck)
                for sd in range(0, 30):
                    shuffle(deck)
                if debug_short_deck:
                    for i in range(0, 69):
                        deck.pop(0)

                # set up the table group
                size = 12  # initially 12 cards
                table_group = pg.sprite.Group()
                table = table_group.sprites()  # table cards as a list

                # set up discard group
                discard_group = pg.sprite.Group()
                discard = discard_group.sprites()  # list of cards in the discard pile

                # game state vars
                run = True
                main_menu = False
                game_clock = 0
                gamemode_solo = True
                solo_endscreen = False
                gamemode_multi = False
                selected_cards = []
                set_call = False
                selections_to_cards = []
                collected_sets = 0
                clean_up = False
                end_bg = True

                time.sleep(.1)

            # add multiplayer in later
            if multi_btn.draw():
                main_menu = False
                game_clock = 0
                gamemode_solo = False
                solo_endscreen = False
                gamemode_multi = True
                selected_cards = []
                set_call = False
                selections_to_cards = []
                collected_sets = 0
                clean_up = False
                end_bg = True
                time.sleep(.1)

            # exit button
            if exit_btn.draw():
                run = False
                pg.quit()
                quit()

        # settings menu
        elif settings:
            # fill the screen
            screen.fill(gray2)
            # sliders
            bgm_slider.draw()
            sfx_slider.draw()
            call_time_slider.draw()
            # back to menu
            if settings_to_main_btn.draw():
                main_menu = True
                settings = False
                time.sleep(.1)

        # solo play
        elif gamemode_solo:

            # end screen
            if solo_endscreen:
                if end_bg:  # run once
                    # nice bg
                    screen.blit(solo_end_menu1, (0, 0, 0, 0))
                    screen.blit(solo_end_menu2, (resolution[0]*.2, resolution[1]*.2, 0, 0))
                    # load highscore from file
                    first_line = 'date & time, points, seconds, points/minute (highscore)'
                    try:
                        with open('highscores_solo.txt', 'r') as hs:
                            highscore = hs.readlines()[-1].split(',')[-1]
                    except:
                        hs = open('highscores_solo.txt', 'x')
                        hs.write(first_line)
                        hs.close()
                        highscore = 0
                    else:
                        highscore = 0
                        with open('highscores_solo.txt', 'r') as hs:
                            line = hs.readline()  # read first line and skip
                            while not line:  # loop to find highscore, although it should only be a highscore at the end...
                                line = hs.readline()
                                if 'debug' in line.split(',')[0]:
                                    pass
                                elif highscore < float(line.split(',')[-1].rstrip('\n')):
                                    highscore = float(line.split(',')[-1].rstrip('\n'))
                    end_bg = False

                else:  # actual end screen
                    screen.blit(pg.font.Font.render(pixel_font_big, 'FINISH!',
                                                    0, ltgray1), (300, 150))
                    screen.blit(pg.font.Font.render(pixel_font,
                                                    'Score = ' + str(collected_sets) + ' pts',
                                                    0, ltgray1), (300, 250))
                    screen.blit(pg.font.Font.render(pixel_font,
                                                    'Time = ' + str(game_clock_min) + ' minutes ' +
                                                    str(game_clock_sec) + ' seconds',
                                                    0, ltgray1), (300, 275))
                    screen.blit(pg.font.Font.render(pixel_font,
                                                    'Score / Time = ' + str(
                                                        round(collected_sets / game_clock * 60, 3)) + ' pts/min',
                                                    0, ltgray1), (300, 300))
                    screen.blit(pg.font.Font.render(pixel_font,
                                                    'Highscore = ' + str(highscore) + ' pts/min',
                                                    0, ltgray1), (300, 350))
                    if round(collected_sets / game_clock * 60, 3) > round(float(highscore), 3):
                        screen.blit(pg.font.Font.render(pixel_font,
                                                        'New Highscore! ' +
                                                        str(round(collected_sets / game_clock * 60, 3)) + ' pts/min',
                                                        0, ltgray1), (300, 375))
                        screen.blit(pg.font.Font.render(pixel_font,
                                                        "            *** Click 'Menu' to save your score! ***",
                                                        0, ltgray1), (300, 400))

                    if back_to_main_btn.draw():  # main btn
                        # new highscore, add to txt file
                        with open('highscores_solo.txt', 'a') as hs:
                            if not debug_short_deck:
                                scoreline = [str(time.strftime("%d %b %Y %H:%M:%S")),
                                             str(collected_sets) + ' points',
                                             str(round(game_clock, 3)) + ' seconds',
                                             str(round(collected_sets / game_clock * 60, 3))]
                                hs.write('\n'+','.join(scoreline))
                            else:
                                scoreline = [str('debug'),
                                             str(time.strftime("%d %b %Y %H:%M:%S")),
                                             str(collected_sets) + ' points',
                                             str(round(game_clock, 3)) + ' seconds',
                                             str(round(collected_sets / game_clock * 60, 3))]
                                hs.write('\n' + ','.join(scoreline))

                        solo_endscreen = False
                        gamemode_solo = False
                        main_menu = True
                        time.sleep(.1)

            # run the game
            else:
                # fill the screen
                screen.fill(gray2)

                # mouse pos
                if debug_show_mouse_pos:
                    screen.blit(pg.font.Font.render(pixel_font, str(pg.mouse.get_pos()), 0, ltgray1),
                                (2, resolution[1] - 28))

                # timer
                game_clock += float(clock.get_time()) / 1000
                game_clock_min = round(game_clock / 60)
                game_clock_sec = round(game_clock % 60)
                if game_clock_sec < 10 and game_clock_min < 10:
                    screen.blit(pg.font.Font.render(pixel_font, 'Game Time:  0' +
                                                    str(game_clock_min) + ':0' + str(game_clock_sec), 0, ltgray1),
                                clock_loc)
                elif game_clock_sec < 10 and not game_clock_min < 10:
                    screen.blit(pg.font.Font.render(pixel_font, 'Game Time:  ' +
                                                    str(game_clock_min) + ':0' + str(game_clock_sec), 0, ltgray1),
                                clock_loc)
                elif not game_clock_sec < 10 and game_clock_min < 10:
                    screen.blit(pg.font.Font.render(pixel_font, 'Game Time:  0' +
                                                    str(game_clock_min) + ':' + str(game_clock_sec), 0, ltgray1),
                                clock_loc)
                else:
                    screen.blit(pg.font.Font.render(pixel_font, 'Game Time:  ' +
                                                    str(game_clock_min) + ':' + str(game_clock_sec), 0, ltgray1),
                                clock_loc)
                # points text
                screen.blit(pg.font.Font.render(pixel_font, ('Points:  ' + str(collected_sets)), 0, ltgray1),
                            (2 * card_x + 1.5 * pad, card_y + 2 * pad, 0, 0))

                # add size# of cards to table group
                try:
                    for t in range(0, size):
                        deck[t].add(table_group)
                    table = table_group.sprites()  # table cards as a list
                except IndexError:
                    for t in range(0, len(deck)):  # just add the remainder of the deck
                        deck[t].add(table_group)
                    table = table_group.sprites()
                else:
                    for t in range(0, size):
                        deck[t].add(table_group)
                    table = table_group.sprites()
                # mat for cards -- adjusts to size
                mat = pg.Surface((4 * pad + 3 * card_x, (size / 3 + 1) * pad + (size / 3) * card_y))
                mat.fill(gray1)
                screen.blit(mat, (card_x - pad, 2 * card_y - pad, 4 * pad + 3 * card_x, 5 * pad + 4 * card_y))

                # check for sets in table group
                sets = findsets(table)
                num_sets = len(sets)
                if num_sets == 0 and size <= 18 and len(table) >= 12:
                    size += 3
                elif len(table) <= 12 and num_sets == 0:  # end condition solo
                    solo_endscreen = True

                # num sets label
                if show_num_sets:
                    num_sets_txt = pg.font.Font.render(pixel_font, 'Sets on table: ' + str(num_sets), 0, ltgray1)
                    screen.blit(num_sets_txt, (6*pad+4*card_x, 3*card_y+pad, 0, 0))

                # place cards on screen
                t = 0
                x, y = card_x, 2*card_y
                for r in range(0, int(size/3)):
                    for c in range(0, 3):
                        # draw cards
                        try:
                            screen.blit(table[t].image, (x, y, card_x, card_y))
                        except IndexError:  # this is to handle when the deck is running out of cards
                            screen.blit(blank_card, (x, y, card_x, card_y))

                        # enable selection buttons
                        select_btns[t].enable = True
                        if select_btns[t].draw():  # basically on click stuff
                            if set_call:  # only view if set called button clicked
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
                if set_call_btn.draw() and not set_call:  # SET called on click & lock out clicking again
                    set_call = True  # enable selecting cards
                    set_call_time = set_call_time_master  # idk like 10 sec?
                    # start timer
                    # select 3 cards

                # SET called, so now...
                if set_call:
                    # set_call timer
                    set_call_time -= float(clock.get_time())/1000
                    screen.blit(pg.font.Font.render(pixel_font, str(round(set_call_time, 1)), 0, ltgray1),
                                (4*card_x+4*pad+2*pad, card_y+2*pad))

                    # time up!
                    if set_call_time <= 0:
                        # lose a point
                        collected_sets -= 1
                        # reset the clock
                        set_call_time = set_call_time_master
                        # trigger clean up
                        clean_up = True

                    # select 3 and check
                    if set_check_btn.draw() and len(selected_cards) == 3:  # click to confirm selected cards
                        # convert select_btn to card
                        selections_to_cards.append(table[select_btns.index(selected_cards[0])])
                        selections_to_cards.append(table[select_btns.index(selected_cards[1])])
                        selections_to_cards.append(table[select_btns.index(selected_cards[2])])
                        if debug_printout:
                            print(num_sets)
                            pprint.pprint(sets)
                            print(len(table))
                            pprint.pprint(table)
                            print(len(deck))

                        if len(findsets(selections_to_cards)) > 0:  # correct :)
                            collected_sets += 1
                            # add to discard & remove from table and deck
                            for card in selections_to_cards:
                                discard_group.add(card)
                                table_group.empty()
                                deck_group.remove(card)
                                deck.remove(card)

                            # update lists
                            discard = discard_group.sprites()
                            table = table_group.sprites()
                            # don't update deck bc it was keeping the og order and reshuffling would mess up the table

                            # reset size
                            size = 12

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
                        for i in range(0, len(selected_cards)):
                            select_btns[select_btns.index(selected_cards[i])].view = False
                        selected_cards = []

                        # done! back to game
                        set_call = False
                        clean_up = False

        # multiplayer
        elif gamemode_multi:
            # fill the screen
            screen.fill(gray2)
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

        # update stuff like the display and the clock
        pg.display.update()
        clock.tick(fps)

    pg.quit()
    quit()
