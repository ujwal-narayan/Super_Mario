import config 
import board as b 
import time

def move_maadi(self,board,ch):
    
    
    
    if (self._x or self._endx ) < -20 : 
        return False
   
    if (self._y or self._endy ) < 0 :
        return False
    
#    if board == b.level1:
    for row in range(self._x,self._endx):
        for col in range(self._endy-1,self._endy):
            if ( board._bufferboard[row, col ] == b"l"):
                    self._y+=5
                    self._endy += 5
                    animate(self,board)
                    return True

       
    
    if ( ch == 'a'):
        for row in range(self._x,self._endx):
            for col in range(self._y,self._y + 1):
                if ( board._bufferboard[row, col ] != ""):
                    return False

    if ( ch == 'd'):
        for row in range(self._x,self._endx):
            for col in range(self._endy-1,self._endy):
                if ( board._bufferboard[row, col ] != ""):
                    return False

    if ( ch == 'w'):
        for col in range(self._y,self._endy):
            for row in range(self._x,self._x+1):
                if ( board._bufferboard[row, col ] != ""):
                    return False


    if ( ch == 's'):
        for col in range(self._y,self._endy):
            for row in range(self._endx-1,self._endx):
                if ( board._bufferboard[row, col ] != ""):
                    self.timeSinceLastJump = 10
                    return False
   
    if ( ch == 'j'):
        for col in range(self._y,self._endy):
            for row in range(self._x,self._x+1):
                if ( board._bufferboard[row, col ] != ""):
                    return False


      
    return True
    
    
def animate(self,board):
    
    self._y=board.endlevel_y
    self._endy=board.endlevel_endy
    self._x = board.endlevel_x
    self._endx=board.endlevel_endx
    board.render(self._y)
    config.level +=1 
    
    

