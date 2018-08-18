

import numpy as np 
import os
import config
from colorama import init,Fore

init(autoreset=True)
class Board:
    """ Its the board and scene gen classs """

    def __init__(self, m, n, level):
        """ preferred size = (FILL IT LATER) """
        assert isinstance(m, int) == True
        assert isinstance(n, int) == True
        self.height = m
        self.width = n
        self.dimen = (n, m)
        self._bufferboard = np.chararray((m, n))
        self._bufferboard[:, :] = "" #config._empty
        self.framecounter = 0
        self.init_points = []
        self.level = level

        self.init_board()

        # This stores a list of all the enemies and coins
        """self._storage = {
            config._types[config._e1]: [],
            config._types[config._e2]: [],
            config._types[config._e3]: [],
            config._types[config._coins]: [],
            config._types[config._powerup]: []

        }
            """
        # Stores the player.Try multiplayer uing threading if there's time
        self.players = []

    def init_board(self, reset=False):
        """ Intialize the board and set it up """
        if reset:
          self.framecounter = 0
        # assigning the ground
        self._bufferboard[-3:,:] = "g"#config._ground
        # assigning the sky       
        self._bufferboard[:10, :] = "s" #config._sky
        #assigning mario 
        #put it in config and import later 
        
        _mario  = np.chararray((3,3))
        _mario [:,:]= " "
        _mario[0,1]="@"
        _mario[1,0]="/"
        _mario[1,1]="|"
        _mario[1,2]="\\"
        _mario[2,0]=_mario[1,0]
        _mario[2,2]=_mario[1,2]

        self._bufferboard[-6:-3,:3]= _mario

    def printer(self,screenview_height_start , screenview_height_end,screenview_width_start , screenview_width_end):
        for row in range(screenview_height_start,screenview_height_end):
            for col in range(screenview_width_start,screenview_width_end):
                print(getcc(self._bufferboard[row,col]),end="")
            print("")
           
#helper functions switch to another file later 
#put it in config and import later  

def getcc (ch):
    if ch == "" :
        return " "
    if ch == b'-':
        return "-"
    if ch == b'+':
        return "#"
    if ch == b'M':
        return "M"
    if ch == b'\\':
        return "\\"
    if ch == b'/':
        return "/"
    if ch == b'@':
        return "@"
    if ch == b'|':
        return "|"
    if ch ==b"g":
        return Fore.GREEN + "-"
    if ch ==b"s":
        return Fore.BLUE + " "
    

_mario1= "\
             \n \
─▄████▄▄░  \n \
▄▀█▀▐└─┐░░ \n \
█▄▐▌▄█▄┘██ \n  \
└▄▄▄▄▄┘███\n \
██▒█▒███▀  \n\
"

b=Board(20,390,0)
b.printer(0,20,0,190)
