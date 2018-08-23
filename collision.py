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
                    if ( board._bufferboard[row,col] == b"M" or board._bufferboard[row,col] == b'0'):
                        for i in board.enms:
                            if ((self._y >= i._y and self._endy >= i._y) or ( self._endy <= i._endy and self._y <= i._endy)):
                                    rtrn = reset(self,board,'a')
                                    if rtrn == 1:
                                        return 2
                                    else :
                                        return 1
                    if (board._bufferboard[row,col] == b"G"):
                        for i in board.enms:
                            if ((self._y >= i._y and self._endy >= i._y) or ( self._endy <= i._endy and self._y <= i._endy)):
                                board._bufferboard[i._x:i._endx , i._y:i._endy] = ""
                                board.enms.remove(i) 
                                self.powerup1 = True
                                return 1

                    
                
                else :
                    if ( board._bufferboard[row,col] == b"@" or board._bufferboard[row,col] == b"|" or board._bufferboard[row,col] == b"/" or board._bufferboard[row,col] == b"\\"):
                        if self.powerup1 :
                            board.player.powerup1 = True
                            for i in board.enms :
                                if i._y == self._y and i._endy == self._endy:
                                    board._bufferboard[i._x:i._endx , i._y+1:i._endy+1] = ""
                                    board.enms.remove(i)
                            return 3
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
                    if ( board._bufferboard[row,col] == b"M" or board._bufferboard[row,col] == b'0'):
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
                        if self.powerup1 :
                            board.player.powerup1 = True
                            for i in board.enms :
                                if i._y == self._y and i._endy == self._endy:
                                    board._bufferboard[i._x:i._endx , i._y-1:i._endy-1] = ""
                                    board.enms.remove(i)
                            return 3    
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
        if self._endx > -2 :
            if(self.killedByEnms):
                self.powerup1 = False
                reset(self,board,ch)
            else:
                board._bufferboard[self._x:self._endx,self._y:self._endy]= ""
                for i in board.enms:
                    if i._endx > -3 :
                        board.enms.remove(i)

        for col in range(self._y,self._endy):
            for row in range(self._endx-1,self._endx):
                if (self.killedByEnms):
                    if ( board._bufferboard[row,col] == b"M" or board._bufferboard[row,col] == b'0'):
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



                

                if ( board._bufferboard[row, col ] != "" and   board._bufferboard[row, col ] !=b"c"):
                    self.timeSinceLastJump = 10
                    self.jumpCounter = 0
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
                if ( board._bufferboard[row, col ] != "" and board._bufferboard[row, col ] != b"c"):
                    return 0


      
    return 1
    
    
def animate(self,board):
    
    self._y=board.endlevel_y
    self._endy=board.endlevel_endy
    self._x = board.endlevel_x
    self._endx=board.endlevel_endx
    board.render(self._y)
    config.level +=1 
    if config.level == 3 :
        print("GAME OVER < YOU WON > ")
        exit()
    

def reset(self,board,ch):
    if self.powerup1 :
        self.powerup1 = False
        if ( ch == 'a'):
            for row in range(self._x,self._endx):
                for col in range(self._y,self._y + 1):
                        if (board._bufferboard[row,col] == b"M" or board._bufferboard[row,col] == b'0'):
                            for i in board.enms:
                                if ((self._y >= i._y and self._endy >= i._y) or ( self._endy <= i._endy and self._y <= i._endy)):
                                    board._bufferboard[i._x:i._endx , i._y:i._endy] = ""
                                    board.enms.remove(i) 
                                    return 2
        if ( ch == 'd'):
            for row in range(self._x,self._endx):
                for col in range(self._endy-1,self._endy):
                        if (board._bufferboard[row,col] == b"M" or board._bufferboard[row,col] == b'0' ):
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
    
    board.__init__(board.height,board.width,board.endlevel_x,board.endlevel_endx,board.endlevel_y,board.endlevel_endy,board.resen,board.resob,board.coins,board.player)
    board._bufferboard[self._x:self._endx,self._y:self._endy]= self.struct
    board.render(self._y-25)
    config.reset = True
    return 1
    

    



