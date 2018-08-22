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
        for col in range(self._endy-config.speed,self._endy):
            if ( board._bufferboard[row, col ] == b"l"):
                    self._y+=5
                    self._endy += 5
                    animate(self,board)
                    return True

       
    
    if ( ch == 'a'):
        for row in range(self._x,self._endx):
            for col in range(self._y,self._y + config.speed):
                if ( board._bufferboard[row, col ] != ""):
                    return False

    if ( ch == 'd'):
        for row in range(self._x,self._endx):
            for col in range(self._endy-config.speed,self._endy):
                if ( board._bufferboard[row, col ] != ""):
                    return False

    if ( ch == 'w'):
        for col in range(self._y,self._endy):
            for row in range(self._x,self._x+config.speed):
                if ( board._bufferboard[row, col ] != ""):
                    return False


    if ( ch == 's'):
        for col in range(self._y,self._endy):
            for row in range(self._endx-config.speed,self._endx):
                if ( board._bufferboard[row, col ] != ""):
                    self.timeSinceLastJump = 10
                    return False
   
    if ( ch == 'j'):
        for col in range(self._y,self._endy):
            for row in range(self._x,self._x+config.jump):
                if ( board._bufferboard[row, col ] != ""):
                    return False


      
    return True
    
    
def animate(self,board):
    
    self._y=board.endlevel_y
    self._endy=board.endlevel_endy
    board.render(self._y)
    config.level +=1 
    
    

