""" List of All characters and their capabilities """
import numpy as np
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
        self.speed = 1 
        self.damage = 10
        self.struct  = np.chararray((3,3))
        self.struct [:,:]= ""
        self.struct[0,1]="@"
        self.struct[1,0]="/"
        self.struct[1,1]="|"
        self.struct[1,2]="\\"
        self.struct[2,0]=self.struct[1,0]
        self.struct[2,2]=self.struct[1,2]
        board._bufferboard[self._x:self._endx,self._y:self._endy] = self.struct

  
       
    
    def moveDown(self,board):
        ox = self._x
        oendx = self._endx
        oy = self._y
        oendy = self._endy
        self._x += self.speed
        self._endx += self.speed
        board._bufferboard[ox:oendx,oy:oendy] = ""
        board._bufferboard[self._x:self._endx,self._y:self._endy] = self.struct
      
    def moveUp(self,board):
        ox = self._x
        oendx = self._endx
        oy = self._y
        oendy = self._endy
        self._x -= self.speed
        self._endx -= self.speed
        board._bufferboard[ox:oendx,oy:oendy] = ""
        board._bufferboard[self._x:self._endx,self._y:self._endy] = self.struct
        print("i try")
        
    def moveLeft(self,board):
        ox = self._x
        oendx = self._endx
        oy = self._y
        oendy = self._endy
        self._y -= self.speed
        self._endy -= self.speed
        board._bufferboard[ox:oendx,oy:oendy] = ""
        board._bufferboard[self._x:self._endx,self._y:self._endy] = self.struct
       
    def moveRight(self,board):
        ox = self._x
        oendx = self._endx
        oy = self._y
        oendy = self._endy
        self._y += self.speed
        self._endy += self.speed
        board._bufferboard[ox:oendx,oy:oendy] = ""
        board._bufferboard[self._x:self._endx,self._y:self._endy] = self.struct 
       
        
     
    def move(self,ch , board ):
        if ch == 'w' :
            self.moveUp(board)
        elif ch == 's':
            self.moveDown(board)
        elif ch == 'a':
            self.moveLeft(board)
        elif ch == 'd':
            self.moveRight(board)
       
    
    
        
        



        
        
        
class Mushroom(characters):
    """ Low level easy peasy enimies """
    def ___init___(self , x, y,ex,ey ):
        super(Mushroom , self ).__init__(x,y,ex,ey)
        self.lives = 1 
        self.damage = 50 
        self.speed = 5

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
        



