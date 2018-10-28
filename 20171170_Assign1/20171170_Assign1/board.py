""" The board """
from os import system
import sys
import numpy as np
import config
from colorama import init, Fore, Back
from charec import Mushroom, Turtles, Pipes, \
Flagpost, BigPipes, Bricks, Castle, SldingPipes, ZigZagWall, Powerup1, Pits, Coins
init(autoreset=True)


class Board:
    """ Its the board and scene gen classs """

    def __init__(self, m, n, ex=0, eex=0, ey=0, eey=0, enemy=[], obsta=[], coins=[],\
     player=0, mx=-6, mex=-3, my=0, mey=3):
        """ preferred size = (FILL IT LATER) """
        assert isinstance(m, int) is True
        assert isinstance(n, int) is True
        print("WAAKING UP")

        self.height = m
        self.width = n
        self.dimen = (n, m)
        self.bufferboard = np.chararray((m, n))
        self.bufferboard[:, :] = ""  # config.sky
        self.framecounter = 0
        self.init_points = []
        self.endlevely = ey
        self.endlevelendy = eey
        self.endlevelx = ex
        self.endlevelendx = eex
        self.enms = enemy + []
        self.obs = obsta + []
        self.coins = coins
        self.mariospawnx = mx
        self.mariospawnendx = mex
        self.mariospawny = my
        self.mariospawnendy = mey
        self.player = player
        self.resen = enemy
        self.resob = obsta
        for i in self.enms:
            i.__init__(i.current_x, i.cendx, i.current_y, i.cendy, self)
        for i in self.obs:
            i.__init__(i.x_pos, i.endx, i.y_pos, i.endy, self)
        for i in self.coins:
            i.__init__(i.x_pos, i.y_pos, self)

        self.init_board()

        self.players = []

    def init_board(self, reset=False):
        """ Intialize the board and set it up """
        if reset:
            self.framecounter = 0

        # assigning the ground
        self.bufferboard[-3:, :] = "g"  # config.GROUND
        if config.LEVEL == 2:
            self.bufferboard[-3:, 76:83] = ""
            self.bufferboard[-3:, 137:142] = ""

        # assigning MARIO
        # put it in config and import later

        #self.bufferboard[-6:-3,:3]= MARIO

    def render(self, y_coordinate):
        """ display board at every frame """
        sys.stdout.flush()
        try:
            system('clear')
        except BaseException:
            system('cls')
        # sys.stdout.write("\n")

        for row in range(20):
            for col in range(y_coordinate, y_coordinate+100):
                try:
                    sys.stdout.write(getcc(self, self.bufferboard[row, col]))
                except BaseException:
                    sys.stdout.write(self.bufferboard[row, col].decode())
            sys.stdout.write("\n")


# helper functions switch to another file later
# put it in config and import later


def getcc(self, charecter):
    """ Prints the right character """
    if config.LEVEL == 2:
        if charecter == "":
            return Back.LIGHTWHITE_EX + " "
        elif charecter == b'-':
            return Back.LIGHTWHITE_EX + u"\u25AC"
        elif charecter == b'+':
            return "#"
        elif charecter == b'M':
            return Back.LIGHTWHITE_EX + "M"
        elif charecter == b'\\':
            if self.player.powerup1:
                return Fore.RED + Back.LIGHTWHITE_EX + "\\"
            return Back.LIGHTWHITE_EX + "\\"
        elif charecter == b'/':
            if self.player.powerup1:
                return Fore.RED + Back.LIGHTWHITE_EX + "/"
            return Back.LIGHTWHITE_EX + "/"
        elif charecter == b'@':
            if self.player.powerup1:
                return Fore.RED + Back.LIGHTWHITE_EX + "@"
            return Back.LIGHTWHITE_EX + "@"
        elif charecter == b'|':
            if self.player.powerup1:
                return Fore.RED + Back.LIGHTWHITE_EX + "|"
            return Back.LIGHTWHITE_EX + "|"
        elif charecter == b"g":
            return Fore.GREEN + '\u2588'
        elif charecter == b"s":
            return Fore.LIGHTWHITE_EX + '\u2588'
        elif charecter == b"_":
            return Fore.LIGHTGREEN_EX + Back.LIGHTWHITE_EX + u"\u25AC"
        elif charecter == b"b":
            return Fore.BLACK+Back.LIGHTRED_EX + u"\u2591"
        elif charecter == b"p":
            return Back.LIGHTWHITE_EX + Fore.GREEN + u"\u2503"
        elif charecter == b"M":
            return "M"
        elif charecter == b"l":
            return Back.LIGHTWHITE_EX + "|"
        elif charecter == b'W':
            return Fore.BLACK+Back.LIGHTRED_EX + u"\u2591"
        elif charecter == b"C":
            return Back.MAGENTA + u"\u2591"
        elif charecter == b"B":
            return Fore.BLACK + u"\u2591"
        elif charecter == b"G":
            return Fore.CYAN + Back.LIGHTWHITE_EX + 'O'
        elif charecter == b"0":
            return Back.LIGHTWHITE_EX + '0'
        elif charecter == b"c":
            return Back.LIGHTWHITE_EX + Fore.YELLOW + u"\U0001F4B0"

    else:
        if charecter == "":
            return Back.BLUE + " "
        elif charecter == b'-':
            return Back.BLUE + u"\u25AC"
        elif charecter == b'+':
            return "#"
        elif charecter == b'M':
            return Back.BLUE + "M"
        elif charecter == b'\\':
            if self.player.powerup1:
                return Fore.RED + Back.BLUE + "\\"
            return Back.BLUE + "\\"
        elif charecter == b'/':
            if self.player.powerup1:
                return Fore.RED + Back.BLUE + "/"
            return Back.BLUE + "/"
        elif charecter == b'@':
            if self.player.powerup1:
                return Fore.RED + Back.BLUE + "@"
            return Back.BLUE + "@"
        elif charecter == b'|':
            if self.player.powerup1:
                return Fore.RED + Back.BLUE + "|"
            return Back.BLUE + "|"
        elif charecter == b"g":
            return Fore.GREEN + '\u2588'
        elif charecter == b"s":
            return Fore.BLUE + '\u2588'
        elif charecter == b"_":
            return Fore.LIGHTGREEN_EX + Back.BLUE + u"\u25AC"
        elif charecter == b"b":
            return Fore.BLACK+Back.LIGHTRED_EX + u"\u2591"
        elif charecter == b"p":
            return Back.BLUE + Fore.GREEN + u"\u2503"
        elif charecter == b"M":
            return "M"
        elif charecter == b"l":
            return Back.BLUE + "|"
        elif charecter == b'W':
            return Fore.BLACK+Back.LIGHTRED_EX + u"\u2591"
        elif charecter == b"C":
            return Back.MAGENTA + u"\u2591"
        elif charecter == b"B":
            return Fore.BLACK + u"\u2591"
        elif charecter == b"G":
            return Fore.CYAN + Back.BLUE + 'O'
        elif charecter == b"0":
            return Back.BLUE + '0'
        elif charecter == b"c":
            return Back.BLUE + Fore.YELLOW + u"\U0001F4B0"


# mario1 = "\
#              \n \
# ─▄████▄▄░  \n \
# ▄▀█▀▐└─┐░░ \n \
# █▄▐▌▄█▄┘██ \n  \
# └▄▄▄▄▄┘███\n \
# ██▒█▒███▀  \n\
# "


LEVELS = []
LEVELS.append("debug")

LEVEL0 = Board(20, 500, -6, -3, 342, 345)

MUSH_1 = Mushroom(-5, -3, 28, 32, LEVEL0)
MUSH_2 = Mushroom(-5, -3, 105, 109, LEVEL0)
MUSH_3 = Mushroom(-5, -3, 170, 174, LEVEL0)
MUSH_4 = Mushroom(-5, -3, 176, 180, LEVEL0)
MUSH_5 = Mushroom(-5, -3, 220, 224, LEVEL0)
MUSH_6 = Mushroom(-5, -3, 265, 269, LEVEL0)
MUSH_7 = Mushroom(-5, -3, 273, 277, LEVEL0)
GUNS_1 = Powerup1(-11, -9, 43, 46, LEVEL0)
ENMS_1 = [MUSH_1, MUSH_2, MUSH_3, MUSH_4, MUSH_5, MUSH_6, MUSH_7, GUNS_1]

OBS_1 = Bricks(-9, -7, 34, 38, LEVEL0)
OBS_2 = Bricks(-9, -7, 43, 47, LEVEL0)
OBS_3 = Bricks(-9, -7, 47, 51, LEVEL0)
OBS_4 = Bricks(-9, -7, 51, 55, LEVEL0)
OBS_5 = Pipes(-7, -3, 66, 74, LEVEL0)
OBS_6 = BigPipes(-9, -3, 90, 98, LEVEL0)
OBS_7 = Bricks(-9, -7, 106, 110, LEVEL0)
OBS_8 = Bricks(-9, -7, 110, 114, LEVEL0)
OBS_9 = Bricks(-9, -7, 114, 118, LEVEL0)
OBS_10 = BigPipes(-9, -3, 150, 158, LEVEL0)
OBS_18 = SldingPipes(-9, -3, 200, 210, LEVEL0)
OBS_19 = Pipes(-7, -3, 238, 246, LEVEL0)
OBS_11 = Bricks(-9, -7, 260, 264, LEVEL0)
OBS_12 = Bricks(-9, -7, 264, 268, LEVEL0)
OBS_13 = Bricks(-9, -7, 268, 272, LEVEL0)
OBS_14 = Bricks(-9, -7, 272, 276, LEVEL0)
OBS_15 = ZigZagWall(-13, -3, 300, 314, LEVEL0)
OBS_16 = Flagpost(-13, -3, 328, 330, LEVEL0)
OBS_17 = Castle(-11, -3, 338, 348, LEVEL0)
OBS1 = [OBS_1, OBS_2, OBS_3, OBS_4, OBS_5, OBS_6, OBS_7, OBS_8, OBS_9, OBS_10,
        OBS_11, OBS_12, OBS_13, OBS_14, OBS_15, OBS_16, OBS_17, OBS_18, OBS_19]


ENMS_2 = ENMS_1 + []
OBS2 = OBS1 + []

'''
#defining level 1
#level1.bufferboard[-5:-3,28:32 ]=e1
level1.bufferboard[-9:-7,34:38] = config.brickwalls
level1.bufferboard[-9:-7,43:47] = config.brickwalls
level1.bufferboard[-9:-7,47:51] = config.brickwalls
level1.bufferboard[-9:-7,51:55] = config.brickwalls
level1.bufferboard[-7:-3,66:74] = config.pipes
level1.bufferboard[-9:-3,90:98] = config.bigpipes
#level1.bufferboard[-5:-3,105:109 ]=config.mushroom
level1.bufferboard[-9:-7,106:110] = config.brickwalls
level1.bufferboard[-9:-7,110:114] = config.brickwalls
level1.bufferboard[-9:-7,114:118] = config.brickwalls
level1.bufferboard[-9:-3,150:158] = config.bigpipes
#level1.bufferboard[-5:-3,170:174 ]=config.mushroom
#level1.bufferboard[-5:-3,176:180 ]=config.mushroom
level1.bufferboard[-9:-3,200:210] = config.goingdownpipe
#level1.bufferboard[-5:-3,220:224 ]=config.mushroom
level1.bufferboard[-7:-3,238:246] = config.pipes
level1.bufferboard[-9:-7,260:264] = config.brickwalls
level1.bufferboard[-9:-7,264:268] = config.brickwalls
level1.bufferboard[-9:-7,268:272] = config.brickwalls
level1.bufferboard[-9:-7,272:276] = config.brickwalls
level1.bufferboard[-9:-7,284:288] = config.brickwalls
level1.bufferboard[-9:-7,280:284] = config.brickwalls
#level1.bufferboard[-5:-3,265:269 ]=config.mushroom
#level1.bufferboard[-5:-3,273:277 ]=config.mushroom
level1.bufferboard[-13:-3,300:314] = config.zigzagwall
level1.bufferboard[-13:-3,328:330] = config.flagpost
level1.bufferboard[-11:-3,338:348] = config.castle
'''

T1 = Turtles(-5, -3, 33, 37, LEVEL0)
T2 = Turtles(-5, -3, 137, 141, LEVEL0)

ENMS_2.append(T1)
ENMS_2.append(T2)
ENMS_2.remove(MUSH_1)
ENMS_2.remove(MUSH_2)

OBS_1 = Bricks(-9, -7, 34, 38, LEVEL0)
OBS_2 = Bricks(-9, -7, 43, 47, LEVEL0)
OBS_3 = Bricks(-9, -7, 47, 51, LEVEL0)
OBS_4 = Bricks(-9, -7, 51, 55, LEVEL0)
OBS_4 = Bricks(-9, -7, 55, 59, LEVEL0)
OBS_5 = Pipes(-7, -3, 66, 74, LEVEL0)
OBS_6 = BigPipes(-9, -3, 90, 98, LEVEL0)
OBS_7 = Bricks(-9, -7, 106, 110, LEVEL0)
OBS_8 = Bricks(-9, -7, 110, 114, LEVEL0)
OBS_9 = Bricks(-9, -7, 114, 118, LEVEL0)
OBS_20 = Pits(-4, -1, 30, 34, LEVEL0)


C1 = Coins(-7, 1, LEVEL0)
C2 = Coins(-7, 4, LEVEL0)
C3 = Coins(-7, 6, LEVEL0)
C4 = Coins(-15, 72, LEVEL0)
C5 = Coins(-14, 73, LEVEL0)
C6 = Coins(-13, 74, LEVEL0)
C7 = Coins(-13, 106, LEVEL0)
C8 = Coins(-13, 107, LEVEL0)
C9 = Coins(-13, 108, LEVEL0)
C10 = Coins(-13, 109, LEVEL0)
C11 = Coins(-13, 110, LEVEL0)
C12 = Coins(-13, 111, LEVEL0)
C13 = Coins(-13, 112, LEVEL0)
C14 = Coins(-13, 113, LEVEL0)
C15 = Coins(-13, 114, LEVEL0)
C16 = Coins(-13, 115, LEVEL0)
C17 = Coins(-13, 116, LEVEL0)
C18 = Coins(-13, 117, LEVEL0)
C19 = Coins(-13, 118, LEVEL0)
C20 = Coins(-13, 119, LEVEL0)
C21 = Coins(-8, 170, LEVEL0)
C22 = Coins(-8, 171, LEVEL0)
C23 = Coins(-8, 172, LEVEL0)
C24 = Coins(-8, 173, LEVEL0)
C25 = Coins(-8, 174, LEVEL0)
C26 = Coins(-8, 175, LEVEL0)
C27 = Coins(-8, 176, LEVEL0)
C28 = Coins(-8, 177, LEVEL0)
C29 = Coins(-8, 178, LEVEL0)
COINSARR = [C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13, C14,\
C15, C16, C17, C18, C19, C20, C21, C22, C23, C24, C25, C26, C27, C28, C29]
