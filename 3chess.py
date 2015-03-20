# 3chess
# by Maciej Sobolewski

import pygame
import sys
import random
import pickle
import glyph
from pygame.locals import *


pygame.init()


# Colours definitions:
white = (255,255,255)
black = (0,0,0)
grey = (89,99,99)


# Globals definitions:
fps = 25
res_x = 960
res_y = 960
debug_mode = True
lang = 'english'
square = {} # Definitions of the board's squares.
alphabet_codes = {1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H', 9:'I', 10:'J', 11:'K', 12:'L'}
chosen = False  # False, when there is no chessman chosen.
turn = ''   # States whose turn it is.
out = ''    # Console output for moves.
history = ['', '', '', '', '', '', '', '', '', '']  # History of moves.
chessmen_list = []  # Chessmen list.


# Functions definitions:
def defineLanguages():
    """Defines language dictionaries."""

    global ld, turn
    global turn

    ld = {
        'english': {'white':'white', 'crimson':'crimson', 'green':'green', 'pawn':'pawn', 'knight':'knight', 'bishop':'bishop', 'rook':'rook', 'queen':'queen', 'king':'king', 'to':'to', 'killed':'captures', 'on':'on', 'its':"It's", 'turn':'turn', 'start':'Start.'}
    }

    turn = ld[lang]['white'] # Set first turn.

def findSquaresCoordOld():
    """THAT WAS AN EXPERIMENTAL FUNCTION THAT DEGRADED PERFORMANCE. Defines square codes. Finds and assigns squares coordinates."""

    for l, i in ((c,d) for c in range(1, 13) for d in range(1, 13)): # Iterate through all possible squares (A1, A2, ..., L12 etc.).
        square[alphabet_codes[l] + str(i)] = [str((l*10, i*10, 0, 255)),None,alphabet_codes[l] + str(i)] # First place in this list is for a colour, second is reserved for position, third one is just a name.

    x = 0
    y = 0
    
    while x < res_y:
        while y < res_y:
            colour = str(board_colour.get_at((x,y))) # Check colour of selected coordinates.
            for l, i in ((c,d) for c in range(1, 13) for d in range(1, 13)): # Iterate through all possible squares (A1, A2, ..., L12 etc.).
                square_item = square[alphabet_codes[l] + str(i)] # Just a shortcut.
                if colour == square_item[0] and square_item[1] == None: # Only continue if the selected colour is the same as square (eg. A1) colour and if our item is still not assigned.
                    square_item[1] = (x, y) # Assign coordinates to a square.
                    print alphabet_codes[l] + str(i)
                    # You can add "skips" here, for faster searching (ex. x and y += 10).
            y += 3
        y = 0
        x += 3

def findSquaresCoord():
    """Defines square codes. Finds and assigns squares coordinates."""

    for l, i in ((c,d) for c in range(1, 13) for d in range(1, 13)): # Iterate through all the possible squares (A1, A2, ..., L12 etc.).
        square[alphabet_codes[l] + str(i)] = [str((l*10, i*10, 0, 255)),None,alphabet_codes[l] + str(i)] # First place in this list is for a colour, second is reserved for a position, third one is just a name.

    square['L9'][1] = (round(res_y/2.021052632, 0), round(res_y/4.923076923, 0))
    square['K9'][1] = (round(res_y/2.004175365, 0), round(res_y/3.720930233, 0))
    square['J9'][1] = (round(res_y/1.983471074, 0), round(res_y/3.037974684, 0))
    square['I9'][1] = (round(res_y/1.951219512, 0), round(res_y/2.546419098, 0))
    square['E9'][1] = (round(res_y/1.832061069, 0), round(res_y/2.258823529, 0))
    square['F9'][1] = (round(res_y/1.681260946, 0), round(res_y/2.082429501, 0))
    square['G9'][1] = (round(res_y/1.55088853, 0), round(res_y/1.939393939, 0))
    square['H9'][1] = (round(res_y/1.432835821, 0), round(res_y/1.811320755, 0))

    square['L10'][1] = (round(res_y/1.825095057, 0), round(res_y/5.78313253, 0))
    square['K10'][1] = (round(res_y/1.7777777785, 0), round(res_y/4.304932735, 0))
    square['J10'][1] = (round(res_y/1.742286751, 0), round(res_y/3.428571429, 0))
    square['I10'][1] = (round(res_y/1.699115044, 0), round(res_y/2.865671642, 0))
    square['E10'][1] = (round(res_y/1.621621622, 0), round(res_y/2.5, 0))
    square['F10'][1] = (round(res_y/1.511811024, 0), round(res_y/2.269503546, 0))
    square['G10'][1] = (round(res_y/1.418020679, 0), round(res_y/2.073434125, 0))
    square['H10'][1] = (round(res_y/1.33148405, 0), round(res_y/1.92, 0))

    square['L11'][1] = (round(res_y/1.660899654, 0), round(res_y/7.058823529, 0))
    square['K11'][1] = (round(res_y/1.608040201, 0), round(res_y/5.052631579, 0))
    square['J11'][1] = (round(res_y/1.555915721, 0), round(res_y/3.966942149, 0))
    square['I11'][1] = (round(res_y/1.507064364, 0), round(res_y/3.265306122, 0))
    square['E11'][1] = (round(res_y/1.43928036, 0), round(res_y/2.815249267, 0))
    square['F11'][1] = (round(res_y/1.369472183, 0), round(res_y/2.493506494, 0))
    square['G11'][1] = (round(res_y/1.300813008, 0), round(res_y/2.242990654, 0))
    square['H11'][1] = (round(res_y/1.243523316, 0), round(res_y/2.038216561, 0))

    square['L12'][1] = (round(res_y/1.526232114, 0), round(res_y/9.056603774, 0))
    square['K12'][1] = (round(res_y/1.461187215, 0), round(res_y/6.193548387, 0))
    square['J12'][1] = (round(res_y/1.40556369, 0), round(res_y/4.682926829, 0))
    square['I12'][1] = (round(res_y/1.352112676, 0), round(res_y/3.80952381, 0))
    square['E12'][1] = (round(res_y/1.302578019, 0), round(res_y/3.2, 0))
    square['F12'][1] = (round(res_y/1.251629726, 0), round(res_y/2.766570605, 0))
    square['G12'][1] = (round(res_y/1.206030151, 0), round(res_y/2.430379747, 0))
    square['H12'][1] = (round(res_y/1.165048544, 0), round(res_y/2.176870748, 0))

    square['A1'][1] = (round(res_y/3.720930233, 0), round(res_y/1.271523179, 0))
    square['B1'][1] = (round(res_y/3.076923077, 0), round(res_y/1.271523179, 0))
    square['C1'][1] = (round(res_y/2.601626016, 0), round(res_y/1.271523179, 0))
    square['D1'][1] = (round(res_y/2.269503546, 0), round(res_y/1.271523179, 0))
    square['E1'][1] = (round(res_y/2.004175365, 0), round(res_y/1.271523179, 0))
    square['F1'][1] = (round(res_y/1.804511278, 0), round(res_y/1.271523179, 0))
    square['G1'][1] = (round(res_y/1.629881154, 0), round(res_y/1.271523179, 0))
    square['H1'][1] = (round(res_y/1.488372093, 0), round(res_y/1.271523179, 0))
    
    square['A2'][1] = (round(res_y/3.720930233, 0), round(res_y/1.381294964, 0))
    square['B2'][1] = (round(res_y/3.076923077, 0), round(res_y/1.407624633, 0))
    square['C2'][1] = (round(res_y/2.601626016, 0), round(res_y/1.432835821, 0))
    square['D2'][1] = (round(res_y/2.269503546, 0), round(res_y/1.454545455, 0))
    square['E2'][1] = (round(res_y/2.004175365, 0), round(res_y/1.454545455, 0))
    square['F2'][1] = (round(res_y/1.804511278, 0), round(res_y/1.432835821, 0))
    square['G2'][1] = (round(res_y/1.629881154, 0), round(res_y/1.407624633, 0))
    square['H2'][1] = (round(res_y/1.488372093, 0), round(res_y/1.381294964, 0))
    
    square['A3'][1] = (round(res_y/3.720930233, 0), round(res_y/1.509433962, 0))
    square['B3'][1] = (round(res_y/3.076923077, 0), round(res_y/1.555915721, 0))
    square['C3'][1] = (round(res_y/2.601626016, 0), round(res_y/1.613445378, 0))
    square['D3'][1] = (round(res_y/2.269503546, 0), round(res_y/1.672473868, 0))
    square['E3'][1] = (round(res_y/2.004175365, 0), round(res_y/1.672473868, 0))
    square['F3'][1] = (round(res_y/1.804511278, 0), round(res_y/1.613445378, 0))
    square['G3'][1] = (round(res_y/1.629881154, 0), round(res_y/1.555915721, 0))
    square['H3'][1] = (round(res_y/1.488372093, 0), round(res_y/1.509433962, 0))

    square['A4'][1] = (round(res_y/3.720930233, 0), round(res_y/1.660899654, 0))
    square['B4'][1] = (round(res_y/3.076923077, 0), round(res_y/1.74863388, 0))
    square['C4'][1] = (round(res_y/2.609626016, 0), round(res_y/1.846153846, 0))
    square['D4'][1] = (round(res_y/2.269503546, 0), round(res_y/1.947261663, 0))
    square['E4'][1] = (round(res_y/2.004175365, 0), round(res_y/1.947261663, 0))
    square['F4'][1] = (round(res_y/1.804511278, 0), round(res_y/1.846153846, 0))
    square['G4'][1] = (round(res_y/1.629881154, 0), round(res_y/1.74863388, 0))
    square['H4'][1] = (round(res_y/1.488372093, 0), round(res_y/1.666899654, 0))

    square['A8'][1] = (round(res_y/12.307692308, 0), round(res_y/2.162162162, 0))
    square['B8'][1] = (round(res_y/8.80733945, 0), round(res_y/2.430379747, 0))
    square['C8'][1] = (round(res_y/6.90647482, 0), round(res_y/2.750716332, 0))
    square['D8'][1] = (round(res_y/5.714285714, 0), round(res_y/3.189368771, 0))
    square['I8'][1] = (round(res_y/4.897959184, 0), round(res_y/3.764705882, 0))
    square['J8'][1] = (round(res_y/4.304932735, 0), round(res_y/4.660194175, 0))
    square['K8'][1] = (round(res_y/3.870967742, 0), round(res_y/6.114649682, 0))
    square['L8'][1] = (round(res_y/3.516483516, 0), round(res_y/8.971962617, 0))

    square['A7'][1] = (round(res_y/7.441860465, 0), round(res_y/2.033898305, 0))
    square['B7'][1] = (round(res_y/5.78313253, 0), round(res_y/2.237762238, 0))
    square['C7'][1] = (round(res_y/4.729064039, 0), round(res_y/2.493506494, 0))
    square['D7'][1] = (round(res_y/4.033613445, 0), round(res_y/2.807017544, 0))
    square['I7'][1] = (round(res_y/3.622641509, 0), round(res_y/3.254237288, 0))
    square['J7'][1] = (round(res_y/3.356643357, 0), round(res_y/3.93442623, 0))
    square['K7'][1] = (round(res_y/3.147540984, 0), round(res_y/5.052631579, 0))
    square['L7'][1] = (round(res_y/2.972136223, 0), round(res_y/7.00729927, 0))

    square['A6'][1] = (round(res_y/5.333333333, 0), round(res_y/1.908548708, 0))
    square['B6'][1] = (round(res_y/4.285714286, 0), round(res_y/2.082429501, 0))
    square['C6'][1] = (round(res_y/3.595505618, 0), round(res_y/2.269503546, 0))
    square['D6'][1] = (round(res_y/3.127035831, 0), round(res_y/2.506527415, 0))
    square['I6'][1] = (round(res_y/2.840236686, 0), round(res_y/2.857142857, 0))
    square['J6'][1] = (round(res_y/2.735042735, 0), round(res_y/3.428571429, 0))
    square['K6'][1] = (round(res_y/2.651933702, 0), round(res_y/4.304932735, 0))
    square['L6'][1] = (round(res_y/7.441860465, 0), round(res_y/2.033898305, 0))

    square['A5'][1] = (round(res_y/4.120171674, 0), round(res_y/1.807909605, 0))
    square['B5'][1] = (round(res_y/3.404255319, 0), round(res_y/1.935483871, 0))
    square['C5'][1] = (round(res_y/2.909090909, 0), round(res_y/2.086956522, 0))
    square['D5'][1] = (round(res_y/2.53968254, 0), round(res_y/2.258823529, 0))
    square['I5'][1] = (round(res_y/2.37037037, 0), round(res_y/2.573726542, 0))
    square['J5'][1] = (round(res_y/2.31884058, 0), round(res_y/3.037974684, 0))
    square['K5'][1] = (round(res_y/2.285714286, 0), round(res_y/3.75, 0))
    square['L5'][1] = (round(res_y/2.269503546, 0), round(res_y/4.923076923, 0))

def saveSquare(name = 'res_conf/' + str(res_x) + 'x'+ str(res_y) + '.res'):
    """Saves square to file. Default name is an actual resolution."""

    pickle.dump(square, open(name, 'wb'))

def loadSquare(name = 'res_conf/' + str(res_x) + 'x' + str(res_y) + '.res'):
    """Loads the square dictionary from a file"""

    global square

    square = pickle.load(open(name, 'rb'))

def testResolutionConfig():
    """Checks if config for actual resolution was set. If not, generates it."""

    try: 
        test = open('res_conf/' + str(res_x) + 'x' + str(res_y) + '.res', 'r')
        test.close()
        loadSquare()
        print 'Res config file loaded.'
    except:
        findSquaresCoord()
        saveSquare()
        print 'Res config file generated.'

def createChessmen():
    """Creates chessmen."""

    pawng1 = Chessman(ld[lang]['green'], ld[lang]['pawn'], 'img/chessmen/pawng.png', 'L11')
    pawng2 = Chessman(ld[lang]['green'], ld[lang]['pawn'], 'img/chessmen/pawng.png', 'K11')
    pawng3 = Chessman(ld[lang]['green'], ld[lang]['pawn'], 'img/chessmen/pawng.png', 'J11')
    pawng4 = Chessman(ld[lang]['green'], ld[lang]['pawn'], 'img/chessmen/pawng.png', 'I11')
    pawng5 = Chessman(ld[lang]['green'], ld[lang]['pawn'], 'img/chessmen/pawng.png', 'E11')
    pawng6 = Chessman(ld[lang]['green'], ld[lang]['pawn'], 'img/chessmen/pawng.png', 'F11')
    pawng7 = Chessman(ld[lang]['green'], ld[lang]['pawn'], 'img/chessmen/pawng.png', 'G11')
    pawng8 = Chessman(ld[lang]['green'], ld[lang]['pawn'], 'img/chessmen/pawng.png', 'H11')
    rookg1 = Chessman(ld[lang]['green'], ld[lang]['rook'], 'img/chessmen/rookg.png', 'L12')
    rookg2 = Chessman(ld[lang]['green'], ld[lang]['rook'], 'img/chessmen/rookg.png', 'H12')
    knightg1 = Chessman(ld[lang]['green'], ld[lang]['knight'], 'img/chessmen/knightg.png', 'K12')
    knightg2 = Chessman(ld[lang]['green'], ld[lang]['knight'], 'img/chessmen/knightg.png', 'G12')
    bishopg1 = Chessman(ld[lang]['green'], ld[lang]['bishop'], 'img/chessmen/bishopg.png', 'F12')
    bishopg2 = Chessman(ld[lang]['green'], ld[lang]['bishop'], 'img/chessmen/bishopg.png', 'J12')
    queeng = Chessman(ld[lang]['green'], ld[lang]['queen'], 'img/chessmen/queeng.png', 'E12')
    kingg = Chessman(ld[lang]['green'], ld[lang]['king'], 'img/chessmen/kingg.png', 'I12')

    pawnw1 = Chessman(ld[lang]['white'], ld[lang]['pawn'], 'img/chessmen/pawnw.png', 'A2')
    pawnw2 = Chessman(ld[lang]['white'], ld[lang]['pawn'], 'img/chessmen/pawnw.png', 'B2')
    pawnw3 = Chessman(ld[lang]['white'], ld[lang]['pawn'], 'img/chessmen/pawnw.png', 'C2')
    pawnw4 = Chessman(ld[lang]['white'], ld[lang]['pawn'], 'img/chessmen/pawnw.png', 'D2')
    pawnw5 = Chessman(ld[lang]['white'], ld[lang]['pawn'], 'img/chessmen/pawnw.png', 'E2')
    pawnw6 = Chessman(ld[lang]['white'], ld[lang]['pawn'], 'img/chessmen/pawnw.png', 'F2')
    pawnw7 = Chessman(ld[lang]['white'], ld[lang]['pawn'], 'img/chessmen/pawnw.png', 'G2')
    pawnw8 = Chessman(ld[lang]['white'], ld[lang]['pawn'], 'img/chessmen/pawnw.png', 'H2')
    rookw1 = Chessman(ld[lang]['white'], ld[lang]['rook'], 'img/chessmen/rookw.png', 'A1')
    rookw2 = Chessman(ld[lang]['white'], ld[lang]['rook'], 'img/chessmen/rookw.png', 'H1')
    knightw1 = Chessman(ld[lang]['white'], ld[lang]['knight'], 'img/chessmen/knightw.png', 'B1')
    knightw2 = Chessman(ld[lang]['white'], ld[lang]['knight'], 'img/chessmen/knightw.png', 'G1')
    bishopw1 = Chessman(ld[lang]['white'], ld[lang]['bishop'], 'img/chessmen/bishopw.png', 'C1')
    bishopw2 = Chessman(ld[lang]['white'], ld[lang]['bishop'], 'img/chessmen/bishopw.png', 'F1')
    queenw = Chessman(ld[lang]['white'], ld[lang]['queen'], 'img/chessmen/queenw.png', 'D1')
    kingw = Chessman(ld[lang]['white'], ld[lang]['king'], 'img/chessmen/kingw.png', 'E1')

    pawnr1 = Chessman(ld[lang]['crimson'], ld[lang]['pawn'], 'img/chessmen/pawnr.png', 'A7')
    pawnr2 = Chessman(ld[lang]['crimson'], ld[lang]['pawn'], 'img/chessmen/pawnr.png', 'B7')
    pawnr3 = Chessman(ld[lang]['crimson'], ld[lang]['pawn'], 'img/chessmen/pawnr.png', 'C7')
    pawnr4 = Chessman(ld[lang]['crimson'], ld[lang]['pawn'], 'img/chessmen/pawnr.png', 'D7')
    pawnr5 = Chessman(ld[lang]['crimson'], ld[lang]['pawn'], 'img/chessmen/pawnr.png', 'I7')
    pawnr6 = Chessman(ld[lang]['crimson'], ld[lang]['pawn'], 'img/chessmen/pawnr.png', 'J7')
    pawnr7 = Chessman(ld[lang]['crimson'], ld[lang]['pawn'], 'img/chessmen/pawnr.png', 'K7')
    pawnr8 = Chessman(ld[lang]['crimson'], ld[lang]['pawn'], 'img/chessmen/pawnr.png', 'L7')
    rookr1 = Chessman(ld[lang]['crimson'], ld[lang]['rook'], 'img/chessmen/rookr.png', 'A8')
    rookr2 = Chessman(ld[lang]['crimson'], ld[lang]['rook'], 'img/chessmen/rookr.png', 'L8')
    knightr1 = Chessman(ld[lang]['crimson'], ld[lang]['knight'], 'img/chessmen/knightr.png', 'B8')
    knightr2 = Chessman(ld[lang]['crimson'], ld[lang]['knight'], 'img/chessmen/knightr.png', 'K8')
    bishopr1 = Chessman(ld[lang]['crimson'], ld[lang]['bishop'], 'img/chessmen/bishopr.png', 'J8')
    bishopr2 = Chessman(ld[lang]['crimson'], ld[lang]['bishop'], 'img/chessmen/bishopr.png', 'C8')
    queenr = Chessman(ld[lang]['crimson'], ld[lang]['queen'], 'img/chessmen/queenr.png', 'I8')
    kingr = Chessman(ld[lang]['crimson'], ld[lang]['king'], 'img/chessmen/kingr.png', 'D8')

def redrawChessmen():
    """Redraws all chessmen on the board."""

    for chessman in chessmen_list:
        if chessman.state != 'killed':  
            playerDisplay.blit(chessman.image, chessman.pos)

def mouseClick(square, symbol):
    """Defines action for a mouse click."""

    if chosen != True:  # Action, when there is now chessman chosen.
        for chessman in chessmen_list:
            if square == chessman.pos:
                chessman.choose()
                return

    if chosen == True: # Action, when there is a chosen chessman.
        for chessman in chessmen_list:
            if square == chessman.pos:
                if chessman.state == 'chosen':  # Action, when the player clicks on the chosen chessman again.
                    return
                elif chessman.state == 'idle':  # Action, when the player clicks on the actually occupied square.
                    if chessman.colour == turn: # If the chessman is friendly, choose it.
                        chessman.choose()
                    else:                       # If the chessman is an enemy, kill it.
                        chessman.kill(symbol)
                        moveChessman(square, symbol, True)
                    return
        moveChessman(square, symbol, False)

def moveChessman(square, symbol, kill):
    """Prepares chessman to move to the desired square. Cycles to the next turn."""

    global chosen, out

    for chessman in chessmen_list:
        if chessman.state == 'chosen':
            chessman.move(square, symbol)
            chessman.state = 'idle'
            chosen = False
            if kill == False:
                out += '%s %s.\n' % (ld[lang]['to'], symbol)
            else:
                out += '%s %s.\n' % (ld[lang]['on'], symbol)
            #console.printConsole(out)
            print out
            chessman.changeImage(chessman.graphic) # Change image to default.
            nextTurn()
            return

def nextTurn():
    """Switches to the next turn"""

    global turn

    if turn == ld[lang]['white']:
       turn = ld[lang]['crimson']
    elif turn == ld[lang]['crimson']:
       turn = ld[lang]['green']
    elif turn == ld[lang]['green']:
       turn = ld[lang]['white']
    print '%s %s %s.' % (ld[lang]['its'], turn, ld[lang]['turn'])


# Classes definitions:
class Chessman(object):
    """Chessman information."""

    def __init__(self, colour, figure, image, position):

        global chessmen_list

        self.colour = colour
        self.type = figure
        self.pos = square[position][1]
        self.square = square[position][2]
        self.state = 'idle'
        self.graphic = image
        self.changeImage(self.graphic)
        chessmen_list.append(self)


    def choose(self):
        """Makes chessman chosen."""

        global chosen, out

        for chessman in chessmen_list: # Make other chessmen idle.
            if chessman.state != 'killed':
                chessman.state = 'idle'
                chessman.changeImage(chessman.graphic)

        if self.colour == turn:   # Check, if the chosen one is own by the actual player.
            out = '%s %s %s ' % (str.capitalize(self.colour), self.type, self.square)
            self.state = 'chosen'
            chosen = True
            self.changeImage('img/chessmen/chosen_' + self.type + '.png')
        return

    def move(self, position, symbol):
        """Moves chessman - changes it's position, blits, and redraw."""

        self.pos = position
        self.square = symbol
        playerDisplay.blit(board, (0,0))
        redrawChessmen()

    def kill(self, symbol):
        """Kills chessman - moves it to (0,0)."""

        global out

        self.move((0,0), '0')
        redrawChessmen()
        self.state = 'killed'
        out += '%s %s %s ' % (ld[lang]['killed'], self.colour, self.type)

    def changeImage(self, image):
        """Changes chessman image file."""

        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (res_y/20, res_y/20)) 

class Console(object):
    """Console for printing moves."""

    def __init__(self):
        console_font = pygame.font.SysFont("monospace", 15)
        self.console1 = console_font.render(history[-1], 1, white)
        self.console2 = console_font.render(history[-2], 1, white)
        self.console3 = console_font.render(history[-3], 1, white)
        self.console4 = console_font.render(history[-4], 1, white)
        self.console5 = console_font.render(history[-5], 1, white)
        self.console6 = console_font.render(history[-6], 1, white)
        self.console7 = console_font.render(history[-7], 1, white)
        self.console8 = console_font.render(history[-8], 1, white)
        self.console9 = console_font.render(history[-9], 1, white)
        self.console10 = console_font.render(history[-10], 1, white)

    def printConsole(self, text):
        """ Prints text."""

        global history

        history.append(text)

        playerDisplay.blit(self.console1 , (965, 605))
        playerDisplay.blit(self.console2 , (965, 615))
        playerDisplay.blit(self.console3 , (965, 625))
        playerDisplay.blit(self.console4 , (965, 635))
        playerDisplay.blit(self.console5 , (965, 645))
        playerDisplay.blit(self.console6 , (965, 655))
        playerDisplay.blit(self.console7 , (965, 665))
        playerDisplay.blit(self.console8 , (965, 675))
        playerDisplay.blit(self.console9 , (965, 685))
        playerDisplay.blit(self.console10 , (965, 695))


# Main function:
def runGame():
    """ Start game. """

    while True:
        
        # Event definitions:
        for event in pygame.event.get():

            # Quit event:
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


        # Checking mouse click by colour and coordinates:
        mpos = pygame.mouse.get_pos()
        for i in square:
            # try:
            if pygame.mouse.get_pressed()[0] == True and str(board_colour.get_at(mpos)) == square[i][0]:
                mouseClick(square[i][1], square[i][2])
            # except:
            #     print 'Mouse is not on the board.'


        # Debug mode:
        if debug_mode == True:
            if pygame.mouse.get_pressed()[1] == True:
                print pygame.mouse.get_pos()


        # Display board stuff:
        playerDisplay.blit(board, (0,0))
        #pygame.draw.rect(playerDisplay, black, (960, 600, 330, 300))
        #pygame.draw.rect(playerDisplay, white, (985, 25, 275, 50), 2)

        # Testing:
        redrawChessmen()
        pygame.display.update()
        fpsTime.tick(fps)


# Start game:
while True: 
    global playerDisplay
    global fpsTime

    fpsTime = pygame.time.Clock() # Set fps.
    playerDisplay = pygame.display.set_mode((res_x,res_y)) 
    debugDisplay = pygame.display.set_mode((res_x,res_y))
    playerDisplay.fill(grey)
    pygame.display.set_caption('3chess') # Set caption.


    # Load and scale images:
    board = pygame.image.load('img/board.png')
    board_colour = pygame.image.load('img/board_colour.png')
    board = pygame.transform.scale(board, (res_y, res_y)) # Scale board image file.
    board_colour = pygame.transform.scale(board_colour, (res_y, res_y)) # Scale colour board image file.
    console = Console() # Create console.


    # Run basic starting functions:
    defineLanguages()
    testResolutionConfig()
    createChessmen()

    runGame()