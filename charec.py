""" List of All characters and their capabilities """
import numpy as np
from collision import move_maadi
import config
import board
import time
class characters :
    """ Common for all characters """
    def __init__(self , x,ex ,y, ey,board):
        """ Figure out the x and Y shit later """

        self._x = x
        self._y = y 
        self.speed = 0 
        self.damage = 0 
        self.dies = True
        self.lives = 0
        self._endx = ex
        self._endy = ey 
        self.struct = ""
        self.killedByEnms = False
        self.powerup1 = False
        if config.reset == False :
            self._cx=x
            self._cy=y
            self._cendx = ex
            self._cendy = ey
    
    def get_coods(self):
        return (self._x,self._y,self._endx,self._endy)
    
    def moveDown(self,board,direction='s'):
        ox = self._x
        oendx = self._endx
        oy = self._y
        oendy = self._endy
        self._x += 1
        self._endx += 1
        rt = move_maadi(self,board,direction)
        if  rt  == 1 :
            board._bufferboard[ox:oendx,oy:oendy] = ""
            board._bufferboard[self._x:self._endx,self._y:self._endy] = self.struct
            return True
        elif rt == 0 :
            self._x = ox
            self._endx = oendx
            self._y = oy
            self._endy = oendy
            return False
    
    def moveUp(self,board,direction='w'):
        ox = self._x
        oendx = self._endx
        oy = self._y
        oendy = self._endy
        self._x -= 1
        self._endx -= 1
        rt = move_maadi(self,board,direction)
        if  rt  == 1 :
            board._bufferboard[ox:oendx,oy:oendy] = ""
            board._bufferboard[self._x:self._endx,self._y:self._endy] = self.struct
            return True
        elif rt == 0 :
            self._x = ox
            self._endx = oendx
            self._y = oy
            self._endy = oendy
            return False
        
    def moveLeft(self,board,direction='a'):
        ox = self._x
        oendx = self._endx
        oy = self._y
        oendy = self._endy
        self._y -= 1
        self._endy -= 1
        rt = move_maadi(self,board,direction)
        if  rt  == 1 :
            board._bufferboard[ox:oendx,oy:oendy] = ""
            board._bufferboard[self._x:self._endx,self._y:self._endy] = self.struct
            return True
        elif rt == 0 :
            self._x = ox
            self._endx = oendx
            self._y = oy
            self._endy = oendy
            return False


    def moveRight(self,board,direction='d'):
        ox = self._x
        oendx = self._endx
        oy = self._y
        oendy = self._endy
        self._y += 1
        self._endy += 1
        rt = move_maadi(self,board,direction)
        if  rt  == 1 :
            board._bufferboard[ox:oendx,oy:oendy] = ""
            board._bufferboard[self._x:self._endx,self._y:self._endy] = self.struct
            return True
        elif rt == 0 :
            self._x = ox
            self._endx = oendx
            self._y = oy
            self._endy = oendy
            return False    

    
    def speed_imp(self,board,ch):
        ret = False
        if ch == 's':
            for i in range(self.speed):
                a = self.moveDown(board,ch)
                if a :
                    ret = True
        if ch == 'd':
            for i in range(self.speed):
                a = self.moveRight(board,ch)
                if a :
                    ret = True
        if ch == 'a':
            for i in range(self.speed):
                a = self.moveLeft(board,ch)
                if a :
                    ret = True
        return ret
        

class Powerup1(characters):
    """" Comrade Mario , unleash the beasts of revolution . Bring forth da GUNS """
    def __init__(self,x,ex,y,ey,board):
        super(Powerup1,self).__init__(x,ex,y,ey,board)
        self.speed = config.powerup_speed
        self.struct = config._powerup1
        self.mover = 'd'
        board._bufferboard[self._cx:self._cendx,self._cy:self._cendy] = self.struct
        

    def move(self,board):
        if self._y == 0 :
            pass
        if self.speed_imp(board,'s')  :
            pass
        else:
            if self.mover == 'a':
                if(self.speed_imp(board,'a')):
                    pass
                else:
                    self.mover = 'd'
            elif self.mover == 'd':
                if(self.speed_imp(board,'d')):
                    pass
                else:
                    self.mover = 'a'


class Mario(characters) :
    """ issa me , Mario """
    def __init__(self , x , ex ,y, ey , board,  lives = 3 ):
        super(Mario, self ).__init__(x,ex,y,ey,board)
        self.lives = lives 
        self.score = 0 
        self.speed = config.speed
        self.jump = config.jump 
        self.timeSinceLastJump = 100
        self.jumpCounter = 0
        self.damage = 10
        self.killedByEnms = True
        self.powerup1 = False
        self.struct = config._mario
        board._bufferboard[self._cx:self._cendx,self._cy:self._cendy] = self.struct


    def jumpUp(self,board,direction):
        ox = self._x
        oendx = self._endx
        oy = self._y
        oendy = self._endy
        self._x -= 1
        self._endx -= 1
        jumpPossible = True
    
        if self.timeSinceLastJump >  10  :
            self.jumpCounter = 0
        else:
            if(self.jumpCounter > 2* self.jump):
                jumpPossible = False
        rt = move_maadi(self,board,direction)
        if  rt  == 1 and jumpPossible:
            board._bufferboard[ox:oendx,oy:oendy] = ""
            board._bufferboard[self._x:self._endx,self._y:self._endy] = self.struct
            self.timeSinceLastJump = 0
            self.jumpCounter += 1
            return True
        elif rt == 0 or not jumpPossible:
            self._x = ox
            self._endx = oendx
            self._y = oy
            self._endy = oendy
            return False

    
    def jumpUps(self,board,ch):
        for i in range(self.jump):
            self.jumpUp(board,ch)

     
    def move(self,ch , board ):
        if ch == 'w' or ch == 'W':
           self.jumpUps(board,'j')
        if ch == 's' or ch == 'S':
            self.speed_imp(board,'s')
            #self.moveDown(board,ch)
        elif ch == 'a' or ch == 'A':
            self.speed_imp(board,'a')
            #self.moveLeft(board,ch)
        elif ch == 'd' or ch == 'D':
            self.speed_imp(board,'d')
            #self.moveRight(board,ch)
        elif ch == ' ':
            self.jumpUps(board,'j')
       
class Mushroom(characters) :
    """ Low level easy peasy enimies """
    def __init__(self , x , ex ,y, ey , board,lives = 1):
        super(Mushroom, self ).__init__(x,ex,y,ey,board)
        self.lives = lives
        self.speed = config.mushroom_speed
        self.struct = config._mushroom
        board._bufferboard[self._cx:self._cendx,self._cy:self._cendy] = self.struct 
        self.mover = 'a'  


    def move(self,board):
        if self.mover == 'a':
            if(self.speed_imp(board,'a')):
                pass
            else:
                self.mover = 'd'
        elif self.mover == 'd':
            if(self.speed_imp(board,'d')):
                pass
            else:
                self.mover = 'a'
        
                
       


class Turtles(characters):
    """Medium level annoying beasts """
    def __init__(self, x, ex,y,ey) :
        super(Turtles,self).__init__(x,y,ex,ey)
        self.lives = 1
        self.damage =50
        self.speed = 10

class DarthVader(characters):
    """I AM THE SENATE < the big bad boss himself """
    def __init__(self, x, ex,y,ey,lives = 2):
        super(DarthVader , self).__init__(x,y,ex,ey)
        self.damage = 10
        self.lives = 2 
        self.speed = 10   




class Obstacles:
    ''' Class for obstacles and other '''
    def __init__(self,x,ex,y,ey,board):
        self._x= x
        self._endx=ex
        self._y=y
        self._endy=ey
        self.struct=""
        self.breakable = False

class Pipes(Obstacles):
    '''class for various pipes , default is this one '''
    def __init__(self, x, ex, y, ey,board):
        super(Pipes,self).__init__(x,ex,y,ey,board)
        self.struct = config._pipes
        board._bufferboard[self._x:self._endx,
                           self._y:self._endy] = self.struct

class BigPipes(Obstacles):
    ''' Bigger Pipes '''
    def __init__(self,x,ex,y,ey,board):
        super(BigPipes,self).__init__(x,ex,y,ey,board)
        self.struct=config._bigpipes
        board._bufferboard[self._x:self._endx,
                           self._y:self._endy] = self.struct


class SldingPipes(Obstacles):
    ''' The kinda pipes you'll use to slide down '''
    def __init__(self,x,ex,y,ey,board):
        super(SldingPipes,self).__init__(x,ex,y,ey,board)
        self.struct = config._goingdownpipe
        board._bufferboard[self._x:self._endx,
                           self._y:self._endy] = self.struct

class Bricks(Obstacles):
    ''' Bricks are domesticated Rocks , Let 'em free '''
    def __init__(self,x,ex,y,ey,board):
        super(Bricks,self).__init__(x,ex,y,ey,board)
        self.struct = config._brickwalls
        board._bufferboard[self._x:self._endx,
                           self._y:self._endy] = self.struct

class Flagpost(Obstacles):
    ''''Jai Hind xD'''
    def __init__(self,x,ex,y,ey,board):
        super(Flagpost,self).__init__(x,ex,y,ey,board)
        self.struct=config._flagpost
        board._bufferboard[self._x:self._endx,
                           self._y:self._endy] = self.struct

class ZigZagWall(Obstacles):
    ''' Le Obstacle at le end'''
    def __init__(self,x,ex,y,ey,board):
        super(ZigZagWall,self).__init__(x,ex,y,ey,board)
        self.struct=config._zigzagwall
        board._bufferboard[self._x:self._endx,
                           self._y:self._endy] = self.struct

class Castle(Obstacles):
    '''Castle at the end of a hill . Hogwarts <3 '''
    def __init__(self,x,ex,y,ey,board):
        super(Castle,self).__init__(x,ex,y,ey,board)
        self.struct=config._castle
        board._bufferboard[self._x:self._endx,
                           self._y:self._endy] = self.struct





