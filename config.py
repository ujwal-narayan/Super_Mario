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
_mario  = np.chararray((3,3))
_mario [:,:]= ""
_mario[0,1]="@"
_mario[1,0]="/"
_mario[1,1]="|"
_mario[1,2]="\\"
_mario[2,0]=_mario[1,0]
_mario[2,2]=_mario[1,2]


_e1 = "E"
_e2 = "M"
_e3 = "D"
_expl = "e"
_bomb = "O"
_empty = " "

# types of objects
types = {

    _empty : "Unassigned",

    _ground : "Ground",

    _sky : "Sky",
    
    
    #   _mario : "Mario",

   # _e1 : "Mushrooms",

    #_e2 : "Turtles",

    #_e3 : "DarthVader"
}
# scores
scores = {
    _bricks : 20,
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

print(_mario)
'''
ground_coods_x=None
ground_coods_ex=None
ground_coods_y=None
ground_coods_ey=None


#pipes 
_pipes = np.chararray((4,8))
_pipes [:,:] = ""
_pipes[1:,1] = 'p'
_pipes[1:,6] = 'p'
_pipes[0,:]='_'


_bigpipes = np.chararray((6,8))
_bigpipes [:,:] = ""
_bigpipes[0,:]='_'
_bigpipes[1:,1] = 'p'
_bigpipes[1:,-2] = 'p'

_goingdownpipe = np.chararray((6,10))
_goingdownpipe [:,:] = ""
_goingdownpipe[0,:]='_'
_goingdownpipe[1:,1] = 'p'
_goingdownpipe[1:,-2] = 'p'




#brickwalls 

_brickwalls = np.chararray((2,4))
_brickwalls[:,:] = "b"

#the zigzaggy wall 
_zigzagwall = np.chararray((10,14))
_zigzagwall[:,:]=""
_zigzagwall[:,-1]='W'
_zigzagwall[-3:,3:]='W'
_zigzagwall[-5:,-8:]='W'
_zigzagwall[-7:,-5:]='W'
_zigzagwall[-9:,-3:]='W'
_zigzagwall[-1:,:]='W'

#flag post 
_flagpost = np.chararray((10,2))
_flagpost [:,:] = "l"
#add a flag or a triangle on top 
#_flagpost[:,:]

#castle 
_castle = np.chararray((8,10))
_castle[:,:]= ""
_castle[-4:,:]="C"
_castle[2:4,2:8]="C"
_castle[-2:,4:7]="B"
_castle[-3,4:7]="B"
_castle[2:4,3]="B"
_castle[2:4,6]="B"
_castle[0,4:6]="C"
_castle[1,3:7]="C"


#enemy1

_mushroom = np.chararray((2,4))
_mushroom[:,:] = "M"
_mushroom[1,0] = " "
_mushroom[-1,-1] = " "

#enemy2

_turtle = np.chararray((3,3))
_turtle[:,:]=""
_turtle[0,1]= _turtle[1,0] = _turtle[1,-1] = '0'
_turtle[-1,0] = _turtle[-1,-1] = 'l'

#enemy3



'''constants '''
speed = 1
jump = 5
mushroom_speed = 3
level = 1
