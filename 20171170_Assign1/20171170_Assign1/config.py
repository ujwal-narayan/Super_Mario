'''

contains all the symbols, constants
directions, etc

'''
import numpy as np

# ch repr of objects
_ground = u"\u2588"

_sky = u"\u2588"

_bricks = u"\u2588"
'''
_
mari = np.chararray((7,137))
mari[:,:] = "+"
#6*13 size mario
'''
mario = np.chararray((3, 3))
mario[:, :] = ""
mario[0, 1] = "@"
mario[1, 0] = "/"
mario[1, 1] = "|"
mario[1, 2] = "\\"
mario[2, 0] = mario[1, 0]
mario[2, 2] = mario[1, 2]


_e1 = "E"
_e2 = "M"
_e3 = "D"
_expl = "e"
_bomb = "O"
_empty = " "

# types of objects
types = {

    _empty: "Unassigned",

    _ground: "Ground",

    _sky: "Sky",


    #   mario : "Mario",

    # _e1 : "Mushrooms",

    #_e2 : "Turtles",

    #_e3 : "DarthVader"
}
# scores
scores = {
    _bricks: 20,
    _e1: 100
}
# number of properties per level (0 is debug)
enemies = []

lives = [10, 3, 5, 7]

timelimit = [100, 90, 90, 80]
timers = [
    [5],
    [5],
    [5, 7],
    [4, 6, 9]
]


'''
def getcc(ch):

    try:
        if ch == _empty:
            return ch
        elif ch == _bomb_man:
            color = 'Blue'
        elif ch == _enemy:
            color = 'Red'
        elif ch == _bricks:
            color = 'Brown'
        elif ch == _expl:
            color = 'Yellow'
        elif ch in [str(x) for x in range(10)]:
            color = 'White'
        elif ch == '[' or ch == ']':
            color = 'Purple'
        else:
            color = 'None'
        return colors[color] + ch + ENDC
    except KeyError:
        return ch


def printcc(st, color):
    try:
        return colors[color] + st + END
    except KeyError:
        return st

print(mario)
'''
ground_coodsx = None
ground_coods_ex = None
ground_coodsy = None
ground_coods_ey = None


# pipes
pipes = np.chararray((4, 8))
pipes[:, :] = ""
pipes[1:, 1] = 'p'
pipes[1:, 6] = 'p'
pipes[0, :] = '_'


bigpipes = np.chararray((6, 8))
bigpipes[:, :] = ""
bigpipes[0, :] = '_'
bigpipes[1:, 1] = 'p'
bigpipes[1:, -2] = 'p'

goingdownpipe = np.chararray((6, 10))
goingdownpipe[:, :] = ""
goingdownpipe[0, :] = '_'
goingdownpipe[1:, 1] = 'p'
goingdownpipe[1:, -2] = 'p'


# brickwalls

brickwalls = np.chararray((2, 4))
brickwalls[:, :] = "b"

# the zigzaggy wall
zigzagwall = np.chararray((10, 14))
zigzagwall[:, :] = ""
zigzagwall[:, -1] = 'W'
zigzagwall[-3:, 3:] = 'W'
zigzagwall[-5:, -8:] = 'W'
zigzagwall[-7:, -5:] = 'W'
zigzagwall[-9:, -3:] = 'W'
zigzagwall[-1:, :] = 'W'

# flag post
flagpost = np.chararray((10, 2))
flagpost[:, :] = "l"
# add a flag or a triangle on top
#flagpost[:,:]

# castle
castle = np.chararray((8, 10))
castle[:, :] = ""
castle[-4:, :] = "C"
castle[2:4, 2:8] = "C"
castle[-2:, 4:7] = "B"
castle[-3, 4:7] = "B"
castle[2:4, 3] = "B"
castle[2:4, 6] = "B"
castle[0, 4:6] = "C"
castle[1, 3:7] = "C"

# pits
pits = np.chararray((3, 4))
pits[:, :] = "0"
# Powerups

powerup1 = np.chararray((2, 3))
powerup1[:, :] = "G"
powerup1[-1, -1] = " "
powerup1[-1, 0] = " "

# enemy1

mushroom = np.chararray((2, 4))
mushroom[:, :] = "M"
mushroom[1, 0] = " "
mushroom[-1, -1] = " "

# enemy2

turtle = np.chararray((2, 4))
turtle[:, :] = "0"
turtle[1, 0] = " "
turtle[-1, -1] = " "

# enemy3

darthvader = np.chararray((3, 3))
darthvader[:, :] = ""
darthvader[0, 1] = "O"
darthvader[1, 0] = "["
darthvader[2, 0] = "<"
darthvader[2, 1:] = "I"
darthvader[2, 2] = ">"
darthvader[2, 1] = "]"


# coins
coins = np.chararray((1, 1))
coins[:, :] = "c"


'''constants '''
speed = 1
jump = 5
mushroom_speed = 3
level = 1
powerup_speed = 5
reset = False
x_pos = 0
