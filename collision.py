import config 
import board as b 
import time

def move_maadi(self,board,ch):
    
    
    
    if (self._x or self._endx ) < -20 : 
        return 0
   
    if (self._y or self._endy ) < 0 :
        return 0
    
#    if board == b.level1:
    for row in range(self._x,self._endx):
        for col in range(self._endy-1,self._endy):
            if ( board._bufferboard[row, col ] == b"l"):
                    self._y+=5
                    self._endy += 5
                    animate(self,board)
                    return 1

       
    
    if ( ch == 'a'):
        for row in range(self._x,self._endx):
            for col in range(self._y,self._y + 1):
                if (self.killedByEnms):
                    if ( board._bufferboard[row,col] == b"M"):
                        for i in board.enms:
                            if ((self._y <= i._y and self._endy >= i._y) or ( self._endy >= i._endy and self._y <= i._endy)):
                                    rtrn = reset(self,board,'a')
                                    if rtrn == 1:
                                        return 2
                                    else :
                                        return 1
                    if (board._bufferboard[row,col] == b"G"):
                        for i in board.enms:
                            if ((self._y <= i._y and self._endy >= i._y) or ( self._endy >= i._endy and self._y <= i._endy)):
                                board._bufferboard[i._x:i._endx , i._y:i._endy] = ""
                                board.enms.remove(i) 
                                self.powerup1 = True
                                return 1

                    
                
                else :
                    if ( board._bufferboard[row,col] == b"@" or board._bufferboard[row,col] == b"|" or board._bufferboard[row,col] == b"/" or board._bufferboard[row,col] == b"\\"):
                        rtrn = reset(board.player,board,'a')
                        if rtrn == 1:
                            return 2
                        else :
                            return 1
                if ( board._bufferboard[row, col ] != ""):
                    return 0

    if ( ch == 'd'):
        for row in range(self._x,self._endx):
            for col in range(self._endy-1,self._endy):
                if (self.killedByEnms):
                    if ( board._bufferboard[row,col] == b"M"):
                        for i in board.enms:
                            if ((self._y <= i._y and self._endy >= i._y) or ( self._endy >= i._endy and self._y <= i._endy)):
                                    rtrn = reset(self,board,'d')
                                    if rtrn == 1:
                                        return 2
                                    else :
                                        return 1
                    if (board._bufferboard[row,col] == b"G"):
                        for i in board.enms:
                            if ((self._y <= i._y and self._endy >= i._y) or ( self._endy >= i._endy and self._y <= i._endy)):
                                board._bufferboard[i._x:i._endx , i._y:i._endy] = ""
                                board.enms.remove(i) 
                                self.powerup1 = True
                                return 1                
                else :
                    if ( board._bufferboard[row,col] == b"@" or board._bufferboard[row,col] == b"|" or board._bufferboard[row,col] == b"/" or board._bufferboard[row,col] == b"\\"):
                        rtrn = reset(board.player,board,'d')
                        if rtrn == 1:
                            return 2
                        else :
                            return 1
                if ( board._bufferboard[row, col ] != ""):
                    return 0

    if ( ch == 'w'):
        for col in range(self._y,self._endy):
            for row in range(self._x,self._x+1):
                if ( board._bufferboard[row, col ] != ""):
                    return 0


    if ( ch == 's'):
        for col in range(self._y,self._endy):
            for row in range(self._endx-1,self._endx):
                if (self.killedByEnms):
                    if ( board._bufferboard[row,col] == b"M"):
                        for i in board.enms:
                            if ((self._y <= i._y and self._endy >= i._y) or ( self._endy >= i._endy and self._y <= i._endy)) :
                                board._bufferboard[i._x:i._endx , i._y:i._endy] = ""
                                board.enms.remove(i)  
                                move_maadi(self,board,ch)
                                move_maadi(self,board,ch)
                                move_maadi(self,board,ch)
                                move_maadi(self,board,ch)
                                board.render(self._y-25 )
                                return 1 
                    if (board._bufferboard[row,col] == b"G"):
                        for i in board.enms:
                            if ((self._y <= i._y and self._endy >= i._y) or ( self._endy >= i._endy and self._y <= i._endy)):
                                board._bufferboard[i._x:i._endx , i._y:i._endy] = ""
                                board.enms.remove(i) 
                                self.powerup1 = True
                                return 1 



                

                if ( board._bufferboard[row, col ] != ""):
                    self.timeSinceLastJump = 10
                    return 0
   
    if ( ch == 'j'):
        for col in range(self._y,self._endy):
            for row in range(self._x,self._x+1):
                if (self.killedByEnms):
                    if (board._bufferboard[row,col] == b"G"):
                        for i in board.enms:
                            if ((self._y <= i._y and self._endy >= i._y) or ( self._endy >= i._endy and self._y <= i._endy)):
                                board._bufferboard[i._x:i._endx , i._y:i._endy] = ""
                                board.enms.remove(i) 
                                self.powerup1 = True
                                return 1  
                if ( board._bufferboard[row, col ] != ""):
                    return 0


      
    return 1
    
    
def animate(self,board):
    
    self._y=board.endlevel_y
    self._endy=board.endlevel_endy
    self._x = board.endlevel_x
    self._endx=board.endlevel_endx
    board.render(self._y)
    config.level +=1 
    

def reset(self,board,ch):
    if self.powerup1 :
        self.powerup1 = False
        if ( ch == 'a'):
            for row in range(self._x,self._endx):
                for col in range(self._y,self._y + 1):
                        if (board._bufferboard[row,col] == b"M"):
                            for i in board.enms:
                                if ((self._y <= i._y and self._endy >= i._y) or ( self._endy >= i._endy and self._y <= i._endy)):
                                    board._bufferboard[i._x:i._endx , i._y:i._endy] = ""
                                    board.enms.remove(i) 
                                    return 2
        if ( ch == 'd'):
            for row in range(self._x,self._endx):
                for col in range(self._endy-1,self._endy):
                        if (board._bufferboard[row,col] == b"M"):
                            for i in board.enms:
                                if ((self._y <= i._y and self._endy >= i._y) or ( self._endy >= i._endy and self._y <= i._endy)):
                                    board._bufferboard[i._x:i._endx , i._y:i._endy] = ""
                                    board.enms.remove(i) 
                                    return 2  
        



    self.lives -= 1
    if self.lives == -1 :
        print("DEAD")
        exit()
    print("RESPAWNING")
    time.sleep(1)
    self._y=board.mariospawn_y
    self._endy=board.mariospawn_endy
    self._x = board.mariospawn_x
    self._endx=board.mariospawn_endx
    
    board.__init__(board.height,board.width,board.endlevel_x,board.endlevel_endx,board.endlevel_y,board.endlevel_endy,board.resen,board.resob,board.player)
    board._bufferboard[self._x:self._endx,self._y:self._endy]= self.struct
    board.render(self._y-25)
    config.reset = True
    return 1
    

    



