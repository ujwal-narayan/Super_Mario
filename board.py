

import numpy as np 
from os import system
import config
from colorama import init,Fore,Back,Style
import sys
from charec import Mushroom , Turtles , DarthVader,Pipes,Flagpost,BigPipes,Bricks,Castle,SldingPipes,ZigZagWall,Powerup1 , Pits , Coins
import time
init(autoreset=True)
class Board:
    """ Its the board and scene gen classs """

    def __init__(self, m, n,ex=0,eex=0,ey=0,eey=0,enemy = [] , obsta = [] ,coins = [], player = 0 ,mx=-6,mex=-3,my=0,mey=3  ):
        """ preferred size = (FILL IT LATER) """
        assert isinstance(m, int) == True
        assert isinstance(n, int) == True
        print("WAAKING UP")

        self.height = m
        self.width = n
        self.dimen = (n, m)
        self._bufferboard = np.chararray((m, n))
        self._bufferboard[:, :] = "" #config.sky 
        self.framecounter = 0
        self.init_points = []
        self.endlevel_y = ey
        self.endlevel_endy = eey
        self.endlevel_x= ex
        self.endlevel_endx=eex
        self.enms = enemy + []
        self.obs = obsta + []
        self.coins = coins
        self.mariospawn_x = mx
        self.mariospawn_endx = mex 
        self.mariospawn_y = my
        self.mariospawn_endy =mey
        self.player = player
        self.resen = enemy
        self.resob = obsta
        for i in self.enms :
            i.__init__(i._cx,i._cendx,i._cy,i._cendy,self)
        for i in self.obs:
            i.__init__(i._x,i._endx,i._y,i._endy,self)
        for i in self.coins:
            i.__init__(i._x,i._y,self)

        

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
        if config.level == 2 :
            self._bufferboard[-3:,76:83] =""
            self._bufferboard[-3:,137:142] = ""
     

        #assigning mario 
        #put it in config and import later 
        
        

        #self._bufferboard[-6:-3,:3]= _mario



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
                    sys.stdout.write(getcc(self,self._bufferboard[row,col]))
                except BaseException:
                    sys.stdout.write(self._bufferboard[row, col].decode())
            sys.stdout.write("\n")
        
           
#helper functions switch to another file later 
#put it in config and import later  


def getcc (self,ch):
    if config.level == 2:
        if ch == "" :
            return (Back.LIGHTWHITE_EX + " " ) 
        elif ch == b'-':
            return (Back.LIGHTWHITE_EX + u"\u25AC" )
        elif ch == b'+':
            return "#"
        elif ch == b'M':
            return Back.LIGHTWHITE_EX + "M" 
        elif ch == b'\\':
            if self.player.powerup1:
                return Fore.RED +  Back.LIGHTWHITE_EX + "\\" 
            return  Back.LIGHTWHITE_EX + "\\"
        elif ch == b'/':
            if self.player.powerup1:
                return Fore.RED +  Back.LIGHTWHITE_EX + "/"
            return  Back.LIGHTWHITE_EX + "/" 
        elif ch == b'@':
            if self.player.powerup1:
                return Fore.RED +  Back.LIGHTWHITE_EX + "@"
            return Back.LIGHTWHITE_EX + "@" 
        elif ch == b'|':
            if self.player.powerup1:
                return Fore.RED +  Back.LIGHTWHITE_EX + "|"
            return Back.LIGHTWHITE_EX + "|" 
        elif ch ==b"g":
            return Fore.GREEN +     '\u2588' 
        elif ch ==b"s":
            return Fore.LIGHTWHITE_EX + '\u2588'  
        elif ch == b"_":
            return Fore.LIGHTGREEN_EX +Back.LIGHTWHITE_EX +  u"\u25AC" 
        elif ch == b"b":
            return Fore.BLACK+Back.LIGHTRED_EX+ u"\u2591"
        elif ch == b"p":
            return Back.LIGHTWHITE_EX+ Fore.GREEN+ u"\u2503"
        elif ch == b"M":
            return "M"
        elif ch == b"l":
            return Back.LIGHTWHITE_EX  + "|" 
        elif ch == b'W':
            return Fore.BLACK+Back.LIGHTRED_EX+ u"\u2591"
        elif ch == b"C":
            return Back.MAGENTA  +u"\u2591"
        elif ch == b"B":
            return Fore.BLACK + u"\u2591"
        elif ch == b"G":
            return Fore.CYAN + Back.LIGHTWHITE_EX+ 'O'
        elif ch == b"0":
            return Back.LIGHTWHITE_EX + '0' 
        elif ch == b"c":
            return Back.LIGHTWHITE_EX + Fore.YELLOW +  	 	u"\U0001F4B0"
            
    else :
        if ch == "" :
            return (Back.BLUE + " " )
        elif ch == b'-':
            return (Back.BLUE + u"\u25AC" )
        elif ch == b'+':
            return "#"
        elif ch == b'M':
            return Back.BLUE + "M"
        elif ch == b'\\':
            if self.player.powerup1:
                return Fore.RED +  Back.BLUE + "\\"
            return  Back.BLUE + "\\"
        elif ch == b'/':
            if self.player.powerup1:
                return Fore.RED +  Back.BLUE + "/"
            return  Back.BLUE + "/"
        elif ch == b'@':
            if self.player.powerup1:
                return Fore.RED +  Back.BLUE + "@"
            return Back.BLUE + "@"
        elif ch == b'|':
            if self.player.powerup1:
                return Fore.RED +  Back.BLUE + "|"
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
        elif ch == b"l":
            return Back.BLUE + "|"
        elif ch == b'W':
            return Fore.BLACK+Back.LIGHTRED_EX+ u"\u2591"
        elif ch == b"C":
            return Back.MAGENTA  +u"\u2591"
        elif ch == b"B":
            return Fore.BLACK + u"\u2591"
        elif ch == b"G":
            return Fore.CYAN + Back.BLUE+ 'O'
        elif ch == b"0":
            return Back.BLUE + '0'
        elif ch == b"c":
            return Back.BLUE + Fore.YELLOW +  	 	u"\U0001F4B0"
            
        



   

_mario1= "\
             \n \
─▄████▄▄░  \n \
▄▀█▀▐└─┐░░ \n \
█▄▐▌▄█▄┘██ \n  \
└▄▄▄▄▄┘███\n \
██▒█▒███▀  \n\
"


            
levels=[]
levels.append("debug")

level0= Board(20,500,-6,-3,342,345)

mush_1 = Mushroom(-5,-3,28,32,level0)
mush_2 = Mushroom(-5,-3,105,109,level0)
mush_3 = Mushroom(-5,-3,170,174,level0)
mush_4 = Mushroom(-5,-3,176,180,level0)
mush_5 = Mushroom(-5,-3,220,224,level0)
mush_6 = Mushroom(-5,-3,265,269,level0)
mush_7 = Mushroom(-5,-3,273,277,level0 )
guns_1 = Powerup1(-11,-9,43,46,level0)
enms_1= [mush_1,mush_2,mush_3,mush_4,mush_5,mush_6,mush_7,guns_1]

obs_1 = Bricks(-9,-7,34,38,level0)
obs_2 = Bricks(-9,-7,43,47,level0)
obs_3 = Bricks(-9,-7,47,51,level0)
obs_4 = Bricks(-9,-7,51,55,level0)
obs_5 = Pipes(-7,-3,66,74,level0)
obs_6 = BigPipes(-9,-3,90,98,level0)
obs_7 = Bricks(-9,-7,106,110,level0)
obs_8 = Bricks(-9,-7,110,114,level0)
obs_9 = Bricks(-9,-7,114,118,level0)
obs_10 = BigPipes(-9,-3,150,158,level0)
obs_18 = SldingPipes(-9,-3,200,210,level0)
obs_19 = Pipes(-7,-3,238,246,level0)
obs_11 = Bricks(-9,-7,260,264,level0)
obs_12 = Bricks(-9,-7,264,268,level0)
obs_13 = Bricks(-9,-7,268,272,level0)
obs_14 = Bricks(-9,-7,272,276,level0)
obs_15 = ZigZagWall(-13,-3,300,314,level0)
obs_16 = Flagpost(-13,-3,328,330,level0)
obs_17 = Castle (-11,-3,338,348,level0)
obs1 = [obs_1,obs_2,obs_3,obs_4,obs_5,obs_6,obs_7,obs_8,obs_9,obs_10,obs_11,obs_12,obs_13,obs_14,obs_15,obs_16,obs_17,obs_18,obs_19]


enms_2 = enms_1 + []
obs2 = obs1 + []

'''
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
'''

t1 = Turtles(-5,-3,33,37,level0)
t2 = Turtles(-5,-3,137,141,level0)

enms_2.append(t1)
enms_2.append(t2)
enms_2.remove(mush_1)
enms_2.remove(mush_2)

obs_1 = Bricks(-9,-7,34,38,level0)
obs_2 = Bricks(-9,-7,43,47,level0)
obs_3 = Bricks(-9,-7,47,51,level0)
obs_4 = Bricks(-9,-7,51,55,level0)
obs_4 = Bricks(-9,-7,55,59,level0)
obs_5 = Pipes(-7,-3,66,74,level0)
obs_6 = BigPipes(-9,-3,90,98,level0)
obs_7 = Bricks(-9,-7,106,110,level0)
obs_8 = Bricks(-9,-7,110,114,level0)
obs_9 = Bricks(-9,-7,114,118,level0)
obs_20 = Pits(-4,-1,30,34,level0)


c1 =Coins(-7,1,level0)
c2 = Coins(-7,4,level0)
c3 = Coins(-7,6,level0)
c4 = Coins(-15,72,level0)
c5 = Coins(-14,73,level0)
c6 = Coins(-13,74,level0)
c7 = Coins(-13,106,level0)
c8 = Coins(-13,107,level0)
c9 = Coins(-13,108,level0)
c10 = Coins(-13,109,level0)
c11 = Coins(-13,110,level0)
c12 = Coins(-13,111,level0)
c13 = Coins(-13,112,level0)
c14 = Coins(-13,113,level0)
c15 = Coins(-13,114,level0)
c16 = Coins(-13,115,level0)
c17 = Coins(-13,116,level0)
c18 = Coins(-13,117,level0)
c19 = Coins(-13,118,level0)
c20 = Coins(-13,119,level0)
c21 = Coins(-8,170,level0)
c22 = Coins(-8,171,level0)
c23 = Coins(-8,172,level0)
c24 = Coins(-8,173,level0)
c25 = Coins(-8,174,level0)
c26 = Coins(-8,175,level0)
c27 = Coins(-8,176,level0)
c28 = Coins(-8,177,level0)
c29 = Coins(-8,178,level0)
coins = [c1,c2,c3 ,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15,c16,c17,c18,c19,c20,c21,c22,c23,c24,c25,c26,c27,c28,c29]
