

import numpy as np 
from os import system
import config
from colorama import init,Fore,Back,Style
import sys
from charec import Mushroom , Turtles , DarthVader

init(autoreset=True)
class Board:
    """ Its the board and scene gen classs """

    def __init__(self, m, n):
        """ preferred size = (FILL IT LATER) """
        assert isinstance(m, int) == True
        assert isinstance(n, int) == True
        self.height = m
        self.width = n
        self.dimen = (n, m)
        self._bufferboard = np.chararray((m, n))
        self._bufferboard[:, :] = "" #config.sky 
        self.framecounter = 0
        self.init_points = []
        self.endlevel_y = 0
        self.endlevel_endy = 0
        

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
     

        #assigning mario 
        #put it in config and import later 
        
        

        #self._bufferboard[-6:-3,:3]= _mario

    def printer(self,screenview_height_start , screenview_height_end,screenview_width_start , screenview_width_end):
        for row in range(screenview_height_start,screenview_height_end):
            for col in range(screenview_width_start,screenview_width_end):
                print(getcc(self._bufferboard[row,col]),end="")
            print("")

    def render(self,y):
        # display board at every frame
        sys.stdout.flush()
        try:
            system('clear')
        except BaseException:
            system('cls')
        # sys.stdout.write("\n")
        
        for row in range(20):
            for col in range(y,y+100 ):
                try:
                    sys.stdout.write(getcc(self._bufferboard[row,col]))
                except BaseException:
                    sys.stdout.write(self._bufferboard[row, col].decode())
            sys.stdout.write("\n")
        
           
#helper functions switch to another file later 
#put it in config and import later  


def getcc (ch):
    if ch == "" :
        return (Back.BLUE + " " )
    elif ch == b'-':
        return (Back.BLUE + u"\u25AC" )
    elif ch == b'+':
        return "#"
    elif ch == b'M':
        return Back.BLUE + "M"
    elif ch == b'\\':
        return  Back.BLUE + "\\"
    elif ch == b'/':
        return  Back.BLUE + "/"
    elif ch == b'@':
        return Back.BLUE + "@"
    elif ch == b'|':
        return Back.BLUE + "|"
    elif ch ==b"g":
        return Fore.GREEN +     '\u2588' 
    elif ch ==b"s":
        return Fore.BLUE + '\u2588'  
    elif ch == b"_":
        return Fore.LIGHTGREEN_EX +Back.BLUE +  u"\u25AC" 
    elif ch == b"b":
        return Fore.BLACK+Back.LIGHTRED_EX+ u"\u2591"
    elif ch == b"p":
        return Back.BLUE+ Fore.GREEN+ u"\u2503"
    elif ch == b"M":
        return "M"
    elif ch == b"0":
        return "0"
    elif ch == b"l":
        return Back.BLUE + "|"
    elif ch == b'W':
        return Fore.BLACK+Back.LIGHTRED_EX+ u"\u2591"
    elif ch == b"C":
        return Back.MAGENTA + Fore.BLACK +u"\u2591"
    elif ch == b"B":
        return Fore.BLACK + u"\u2591"


   

_mario1= "\
             \n \
─▄████▄▄░  \n \
▄▀█▀▐└─┐░░ \n \
█▄▐▌▄█▄┘██ \n  \
└▄▄▄▄▄┘███\n \
██▒█▒███▀  \n\
"


def pipeprinter():
    for row in range(4):
        for col in range(6):
            print(getcc(config._pipes[row,col]),end="")
        print("")

def brickwallsprinter():
    for row in range(3):
        for col in range(50):
              print(getcc(config._brickwalls[row,col]),end="")
        print("")


def mushroomprinter():
    for row in range(2):
        for col in range(4):
             print(getcc(config._mushroom[row,col]),end="")
        print("")

            
def turtleprinter():
    for row in range(3):
        for col in range(3):
            print(getcc(config._turtle[row,col]),end="")
        print("")
            
levels=[]
levels.append("debug")
level1= Board(20,500)
level1.endlevel_y = 342
level1.endlevel_endy = 345 
levels.append(level1)
mush_1 = Mushroom(-5,-3,28,32,level1)
mush_2 = Mushroom(-5,-3,105,109,level1)
mush_3 = Mushroom(-5,-3,170,174,level1)
mush_4 = Mushroom(-5,-3,176,180,level1)
mush_5 = Mushroom(-5,-3,220,224,level1)
mush_6 = Mushroom(-5,-3,265,269,level1)
mush_7 = Mushroom(-5,-3,273,277,level1 )
enms_1= [mush_1,mush_2,mush_3,mush_4,mush_5,mush_6,mush_7]

#defining level 1 
#level1._bufferboard[-5:-3,28:32 ]=e1
level1._bufferboard[-9:-7,34:38] = config._brickwalls
level1._bufferboard[-9:-7,43:47] = config._brickwalls
level1._bufferboard[-9:-7,47:51] = config._brickwalls
level1._bufferboard[-9:-7,51:55] = config._brickwalls
level1._bufferboard[-7:-3,66:74] = config._pipes
level1._bufferboard[-9:-3,90:98] = config._bigpipes
#level1._bufferboard[-5:-3,105:109 ]=config._mushroom
level1._bufferboard[-9:-7,106:110] = config._brickwalls
level1._bufferboard[-9:-7,110:114] = config._brickwalls
level1._bufferboard[-9:-7,114:118] = config._brickwalls
level1._bufferboard[-9:-3,150:158] = config._bigpipes
#level1._bufferboard[-5:-3,170:174 ]=config._mushroom
#level1._bufferboard[-5:-3,176:180 ]=config._mushroom
level1._bufferboard[-9:-3,200:210] = config._goingdownpipe
#level1._bufferboard[-5:-3,220:224 ]=config._mushroom
level1._bufferboard[-7:-3,238:246] = config._pipes
level1._bufferboard[-9:-7,260:264] = config._brickwalls
level1._bufferboard[-9:-7,264:268] = config._brickwalls
level1._bufferboard[-9:-7,268:272] = config._brickwalls
level1._bufferboard[-9:-7,272:276] = config._brickwalls
level1._bufferboard[-9:-7,284:288] = config._brickwalls
level1._bufferboard[-9:-7,280:284] = config._brickwalls
#level1._bufferboard[-5:-3,265:269 ]=config._mushroom
#level1._bufferboard[-5:-3,273:277 ]=config._mushroom
level1._bufferboard[-13:-3,300:314] = config._zigzagwall
level1._bufferboard[-13:-3,328:330] = config._flagpost
level1._bufferboard[-11:-3,338:348] = config._castle


level2 = Board(20,500)

