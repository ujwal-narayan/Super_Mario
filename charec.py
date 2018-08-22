""" List of All characters and their capabilities """
import numpy as np
from collision import move_maadi
import config
import board
import time
class characters :
    """ Common for all characters """
    def __init__(self , x, y ,ex , ey,board):
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
    
    def get_coods(self):
        return (self._x,self._y,self._endx,self._endy)
    
    def moveDown(self,board,direction='s'):
        ox = self._x
        oendx = self._endx
        oy = self._y
        oendy = self._endy
        self._x += 1
        self._endx += 1
        if  move_maadi(self,board,direction) == True :
            board._bufferboard[ox:oendx,oy:oendy] = ""
            board._bufferboard[self._x:self._endx,self._y:self._endy] = self.struct
            return True
        else :
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
        if  move_maadi(self,board,direction) == True :
            board._bufferboard[ox:oendx,oy:oendy] = ""
            board._bufferboard[self._x:self._endx,self._y:self._endy] = self.struct
            return True
        else :
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
        if  move_maadi(self,board,direction) == True :
            board._bufferboard[ox:oendx,oy:oendy] = ""
            board._bufferboard[self._x:self._endx,self._y:self._endy] = self.struct
            return True
        else :
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

        if  move_maadi(self,board,direction) == True :
            board._bufferboard[ox:oendx,oy:oendy] = ""
            board._bufferboard[self._x:self._endx,self._y:self._endy] = self.struct
            return True 
        else :
            self._x = ox
            self._endx = oendx
            self._y = oy
            self._endy = oendy
            return False

    
    def speed_imp(self,board,ch):
        if ch == 's':
            for i in range(self.speed):
                self.moveDown(board,ch)
        if ch == 'd':
            for i in range(self.speed):
                self.moveRight(board,ch)
        if ch == 'a':
            for i in range(self.speed):
                self.moveLeft(board,ch)
        




class Mario(characters) :
    """ issa me , Mario """
    def __init__(self , x , ex ,y, ey , board,  lives = 1 ):
        super(Mario, self ).__init__(x,y,ex,ey,board)
        self.lives = lives 
        self.score = 0 
        self.speed = config.speed
        self.jump = config.jump 
        self.timeSinceLastJump = 100
        self.jumpCounter = 0
        self.damage = 10
        self.struct = config._mario
        board._bufferboard[self._x:self._endx,self._y:self._endy] = self.struct


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
        
        if  move_maadi(self,board,direction) and (jumpPossible) :
            board._bufferboard[ox:oendx,oy:oendy] = ""
            board._bufferboard[self._x:self._endx,self._y:self._endy] = self.struct
            self.timeSinceLastJump = 0
            self.jumpCounter += 1
        else :
            self._x = ox
            self._endx = oendx
            self._y = oy
            self._endy = oendy
    
    def jumpUps(self,board,ch):
        for i in range(self.jump):
            self.jumpUp(board,ch)

     
    def move(self,ch , board ):
       # if ch == 'w' :
        #    self.moveUp(board,ch)
        if ch == 's':
            self.speed_imp(board,ch)
            #self.moveDown(board,ch)
        elif ch == 'a':
            self.speed_imp(board,ch)
            #self.moveLeft(board,ch)
        elif ch == 'd':
            self.speed_imp(board,ch)
            #self.moveRight(board,ch)
        elif ch == ' ':
            self.jumpUps(board,'j')
       
class Mushroom(characters) :
    """ Low level easy peasy enimies """
    def __init__(self , x , ex ,y, ey , board,lives = 1):
        super(Mushroom, self ).__init__(x,y,ex,ey,board)
        self.lives = lives
        self.speed = config.mushroom_speed
        self.struct = config._mushroom
        board._bufferboard[self._x:self._endx,self._y:self._endy] = self.struct 
        self.mover = 'a'  


    def move(self,board):
        if self.mover == 'a':
            if(self.moveLeft(board)):
                pass
            else:
                self.mover = 'd'
        elif self.mover == 'd':
            if(self.moveRight(board)):
                pass
            else:
                self.mover = 'a'
        
                
       


class Turtles(characters):
    """Medium level annoying beasts """
    def __init__(self, x, y,ex,ey) :
        super(Turtles,self).__init__(x,y,ex,ey)
        self.lives = 1
        self.damage =50
        self.speed = 10

class DarthVader(characters):
    """I AM THE SENATE < the big bad boss himself """
    def __init__(self, x, y,ex,ey,lives = 2):
        super(DarthVader , self).__init__(x,y,ex,ey)
        self.damage = 10
        self.lives = 2 
        self.speed = 10     




