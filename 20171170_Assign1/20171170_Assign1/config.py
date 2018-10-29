'''

contains all the symbols, constants
directions, etc

'''
import numpy as np

# ch repr of objects
GROUND = u"\u2588"

SKY = u"\u2588"

BRICKS = u"\u2588"

MARIO = np.chararray((3, 3))
MARIO[:, :] = ""
MARIO[0, 1] = "@"
MARIO[1, 0] = "/"
MARIO[1, 1] = "|"
MARIO[1, 2] = "\\"
MARIO[2, 0] = MARIO[1, 0]
MARIO[2, 2] = MARIO[1, 2]


E1 = "E"
E2 = "M"
E3 = "D"
EMPTY = " "

# TYPES of objects
TYPES = {

    EMPTY: "Unassigned",

    GROUND: "Ground",

    SKY: "Sky",


    #   MARIO : "Mario",

    # E1 : "Mushrooms",

    #E2 : "Turtles",

    #E3 : "DarthVader"
}
# SCORES
SCORES = {
    BRICKS: 20,
    E1: 100
}






# PIPES
PIPES = np.chararray((4, 8))
PIPES[:, :] = ""
PIPES[1:, 1] = 'p'
PIPES[1:, 6] = 'p'
PIPES[0, :] = '_'


BIGPIPES = np.chararray((6, 8))
BIGPIPES[:, :] = ""
BIGPIPES[0, :] = '_'
BIGPIPES[1:, 1] = 'p'
BIGPIPES[1:, -2] = 'p'

GOINGDOWNPIPE = np.chararray((6, 10))
GOINGDOWNPIPE[:, :] = ""
GOINGDOWNPIPE[0, :] = '_'
GOINGDOWNPIPE[1:, 1] = 'p'
GOINGDOWNPIPE[1:, -2] = 'p'


# BRICKWALLS

BRICKWALLS = np.chararray((2, 4))
BRICKWALLS[:, :] = "b"

# the zigzaggy wall
ZIGZAGWALL = np.chararray((10, 14))
ZIGZAGWALL[:, :] = ""
ZIGZAGWALL[:, -1] = 'W'
ZIGZAGWALL[-3:, 3:] = 'W'
ZIGZAGWALL[-5:, -8:] = 'W'
ZIGZAGWALL[-7:, -5:] = 'W'
ZIGZAGWALL[-9:, -3:] = 'W'
ZIGZAGWALL[-1:, :] = 'W'

# flag post
FLAGPOST = np.chararray((10, 2))
FLAGPOST[:, :] = "l"
# add a flag or a triangle on top
#FLAGPOST[:,:]

# CASTLE
CASTLE = np.chararray((8, 10))
CASTLE[:, :] = ""
CASTLE[-4:, :] = "C"
CASTLE[2:4, 2:8] = "C"
CASTLE[-2:, 4:7] = "B"
CASTLE[-3, 4:7] = "B"
CASTLE[2:4, 3] = "B"
CASTLE[2:4, 6] = "B"
CASTLE[0, 4:6] = "C"
CASTLE[1, 3:7] = "C"

# pits
PITS = np.chararray((3, 4))
PITS[:, :] = "0"
# Powerups

POWERUP1 = np.chararray((2, 3))
POWERUP1[:, :] = "G"
POWERUP1[-1, -1] = " "
POWERUP1[-1, 0] = " "

# enemy1

MUSHROOM = np.chararray((2, 4))
MUSHROOM[:, :] = "M"
MUSHROOM[1, 0] = " "
MUSHROOM[-1, -1] = " "

# enemy2

TURTLE = np.chararray((2, 4))
TURTLE[:, :] = "0"
TURTLE[1, 0] = " "
TURTLE[-1, -1] = " "

# enemy3

# darthvader = np.chararray((3, 3))
# darthvader[:, :] = ""
# darthvader[0, 1] = "O"
# darthvader[1, 0] = "["
# darthvader[2, 0] = "<"
# darthvader[2, 1:] = "I"
# darthvader[2, 2] = ">"
# darthvader[2, 1] = "]"


# coins
COINS = np.chararray((1, 1))
COINS[:, :] = "c"


'''constants '''
SPEED = 1
JUMP = 5
MUSHROOM_SPEED = 3
LEVEL = 1
POWERUP_SPEED = 5
RESET = False
X_POS = 0
ALIVE = True
