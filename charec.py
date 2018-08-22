""" List of All characters and their capabilities """
import numpy as np
from collision import move_maadi
import config
import board
class characters :
        """ Common for all characters """
        def __init__(self , x, y ,ex , ey):
            """ Figure out the x and Y shit later """
            self._x = x
            self._y = y 
            self.speed = 0 
            self.damage = 0 
            self.dies = True
            self.lives = 0
            self._endx = ex
            self._endy = ey 
        
        def get_coods(self):
            return (self._x,self._y,self._endx,self._endy)
        



class Mario(characters) :
    """ issa me , Mario """
    def __init__(self , x , ex ,y, ey , board,  lives = 1 ):
        super(Mario, self ).__init__(x,y,ex,ey)
        self.lives = lives 
        self.score = 0 
        self.speed = config.speed
        self.jump = config.jump 
        self.timeSinceLastJump = 100
        self.jumpCounter = 0
        self.damage = 10
        self.struct = config._mario
        board._bufferboard[self._x:self._endx,self._y:self._endy] = self.struct

  
       
    
    def moveDown(self,board,direction):
        ox = self._x
        oendx = self._endx
        oy = self._y
        oendy = self._endy
        self._x += self.speed
        self._endx += self.speed
        if  move_maadi(self,board,direction) == True :
            board._bufferboard[ox:oendx,oy:oendy] = ""
            board._bufferboard[self._x:self._endx,self._y:self._endy] = self.struct
        else :
            self._x = ox
            self._endx = oendx
            self._y = oy
            self._endy = oendy
            
      
    def moveUp(self,board,direction):
        ox = self._x
        oendx = self._endx
        oy = self._y
        oendy = self._endy
        self._x -= self.speed
        self._endx -= self.speed
        if  move_maadi(self,board,direction) == True :
            board._bufferboard[ox:oendx,oy:oendy] = ""
            board._bufferboard[self._x:self._endx,self._y:self._endy] = self.struct
        else :
            self._x = ox
            self._endx = oendx
            self._y = oy
            self._endy = oendy
        
    def moveLeft(self,board,direction):
        ox = self._x
        oendx = self._endx
        oy = self._y
        oendy = self._endy
        self._y -= self.speed
        self._endy -= self.speed
        if  move_maadi(self,board,direction) == True :
            board._bufferboard[ox:oendx,oy:oendy] = ""
            board._bufferboard[self._x:self._endx,self._y:self._endy] = self.struct
        else :
            self._x = ox
            self._endx = oendx
            self._y = oy
            self._endy = oendy


    def moveRight(self,board,direction):
        ox = self._x
        oendx = self._endx
        oy = self._y
        oendy = self._endy
        self._y += self.speed
        self._endy += self.speed

        if  move_maadi(self,board,direction) == True :
            board._bufferboard[ox:oendx,oy:oendy] = ""
            board._bufferboard[self._x:self._endx,self._y:self._endy] = self.struct
        else :
            self._x = ox
            self._endx = oendx
            self._y = oy
            self._endy = oendy
    
    def jumpUp(self,board,direction):
        ox = self._x
        oendx = self._endx
        oy = self._y
        oendy = self._endy
        self._x -= self.jump
        self._endx -= self.jump
        jumpPossible = True
    
        if self.timeSinceLastJump >  10  :
            self.jumpCounter = 0
        else:
            if(self.jumpCounter > 1):
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
    

     
    def move(self,ch , board ):
       # if ch == 'w' :
        #    self.moveUp(board,ch)
        if ch == 's':
            self.moveDown(board,ch)
        elif ch == 'a':
            self.moveLeft(board,ch)
        elif ch == 'd':
            self.moveRight(board,ch)
        elif ch == ' ':
            self.jumpUp(board,'j')
       
    
    
        
        



        
        
        

        

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

'''
class Mushroom(characters):
    
    def ___init___(self , x, ex , y, ey , board ):
        super(Mushroom , self ).__init__(x,y,ex,ey)
        self.lives = 1 
        self.damage = 50 
        self.speed = 5
        self.struct = config._mushroom
        board._bufferboard[self._x:self._endx,self._y:self._endy] = self.struct
'''
class Mushroom(characters) :
    """ Low level easy peasy enimies """
    def __init__(self , x , ex ,y, ey , board,lives = 1):
        super(Mushroom, self ).__init__(x,y,ex,ey)
        self.lives = lives
        self.speed = config.mushroom_speed
        self.struct = config._mushroom
        board._bufferboard[self._x:self._endx,self._y:self._endy] = self.struct        



