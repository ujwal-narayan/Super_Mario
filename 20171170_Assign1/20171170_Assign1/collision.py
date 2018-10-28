import config
import board as b
import time


def move_maadi(self, board, ch):

    if (self.x or self.endx) < -20:
        return 0

    if (self.y or self.endy) < 0:
        return 0

#    if board == b.level1:
    for row in range(self.x, self.endx):
        for col in range(self.endy-1, self.endy):
            if (board._bufferboard[row, col] == b"l"):
                self.y += 5
                self.endy += 5
                animate(self, board)
                return 1

    if (ch == 'a'):
        for row in range(self.x, self.endx):
            for col in range(self.y, self.y + 1):
                if (self.killed_by_enms):
                    if (board._bufferboard[row, col] == b"M" or board._bufferboard[row, col] == b'0'):
                        if board._bufferboard[row, col] == b"M":
                            board.player.score += 10
                        else:
                            board.player.score += 30
                        for i in board.enms:
                            if ((self.y >= i.y and self.endy >= i.y) or (self.endy <= i.endy and self.y <= i.endy)):
                                rtrn = reset(self, board, 'a')
                                if rtrn == 1:
                                    return 2
                                else:
                                    return 1
                    if (board._bufferboard[row, col] == b"G"):
                        for i in board.enms:
                            if ((self.y >= i.y and self.endy >= i.y) or (self.endy <= i.endy and self.y <= i.endy)):
                                board._bufferboard[i.x:i.endx,
                                                   i.y:i.endy] = ""
                                board.enms.remove(i)
                                self.powerup1 = True
                                board.player.score += 50
                                return 1

                else:
                    if (board._bufferboard[row, col] == b"@" or board._bufferboard[row, col] == b"|" or board._bufferboard[row, col] == b"/" or board._bufferboard[row, col] == b"\\"):
                        if self.powerup1:
                            board.player.powerup1 = True
                            for i in board.enms:
                                if i.y == self.y and i.endy == self.endy:
                                    board._bufferboard[i.x:i.endx,
                                                       i.y+1:i.endy+1] = ""
                                    board.enms.remove(i)
                                board.player.powerup1 = False
                            return 3
                        rtrn = reset(board.player, board, 'a')
                        if rtrn == 1:
                            return 2
                        else:
                            return 1
                if (board._bufferboard[row, col] != ""):
                    return 0

    if (ch == 'd'):
        for row in range(self.x, self.endx):
            for col in range(self.endy-1, self.endy):
                if (self.killed_by_enms):
                    if (board._bufferboard[row, col] == b"M" or board._bufferboard[row, col] == b'0'):
                        if board._bufferboard[row, col] == b"M":
                            board.player.score += 10
                        else:
                            board.player.score += 30
                        for i in board.enms:
                            if ((self.y <= i.y and self.endy >= i.y) or (self.endy >= i.endy and self.y <= i.endy)):
                                rtrn = reset(self, board, 'd')
                                if rtrn == 1:
                                    return 2
                                else:
                                    return 1
                    if (board._bufferboard[row, col] == b"G"):
                        for i in board.enms:
                            if ((self.y <= i.y and self.endy >= i.y) or (self.endy >= i.endy and self.y <= i.endy)):
                                board._bufferboard[i.x:i.endx,
                                                   i.y:i.endy] = ""
                                board.enms.remove(i)
                                self.powerup1 = True
                                board.player.score += 50
                                return 1
                else:
                    if (board._bufferboard[row, col] == b"@" or board._bufferboard[row, col] == b"|" or board._bufferboard[row, col] == b"/" or board._bufferboard[row, col] == b"\\"):
                        if self.powerup1:
                            board.player.powerup1 = True
                            for i in board.enms:
                                if i.y == self.y and i.endy == self.endy:
                                    board._bufferboard[i.x:i.endx,
                                                       i.y-1:i.endy-1] = ""
                                    board.enms.remove(i)
                                board.player.powerup1 = False
                            return 3
                        rtrn = reset(board.player, board, 'd')
                        if rtrn == 1:
                            return 2
                        else:
                            return 1
                if (board._bufferboard[row, col] != ""):
                    return 0

    if (ch == 'w'):
        for col in range(self.y, self.endy):
            for row in range(self.x, self.x+1):
                if (board._bufferboard[row, col] != ""):
                    return 0

    if (ch == 's'):
        if self.endx > -2:
            if(self.killed_by_enms):
                self.powerup1 = False
                reset(self, board, ch)
            else:
                board._bufferboard[self.x:self.endx, self.y:self.endy] = ""
                for i in board.enms:
                    if i.endx > -3:
                        board.enms.remove(i)

        for col in range(self.y, self.endy):
            for row in range(self.endx-1, self.endx):
                if (self.killed_by_enms):
                    if (board._bufferboard[row, col] == b"M" or board._bufferboard[row, col] == b'0'):
                        if board._bufferboard[row, col] == b"M":
                            board.player.score += 10
                        else:
                            board.player.score += 30
                        for i in board.enms:
                            if ((self.y <= i.y and self.endy >= i.y) or (self.endy >= i.endy and self.y <= i.endy)):
                                board._bufferboard[i.x:i.endx,
                                                   i.y:i.endy] = ""
                                board.enms.remove(i)
                                move_maadi(self, board, ch)
                                move_maadi(self, board, ch)
                                move_maadi(self, board, ch)
                                move_maadi(self, board, ch)
                                board.render(self.y-25)
                                return 1
                    if (board._bufferboard[row, col] == b"G"):
                        for i in board.enms:
                            if ((self.y <= i.y and self.endy >= i.y) or (self.endy >= i.endy and self.y <= i.endy)):
                                board._bufferboard[i.x:i.endx,
                                                   i.y:i.endy] = ""
                                board.enms.remove(i)
                                self.powerup1 = True
                                board.player.score += 50
                                return 1

                if (board._bufferboard[row, col] != "" and board._bufferboard[row, col] != b"c"):
                    self.timeSinceLastJump = 10
                    self.jump_counter = 0

                    return 0

    if (ch == 'j'):
        for col in range(self.y, self.endy):
            for row in range(self.x, self.x+1):
                if (self.killed_by_enms):
                    if (board._bufferboard[row, col] == b"G"):
                        for i in board.enms:
                            if ((self.y <= i.y and self.endy >= i.y) or (self.endy >= i.endy and self.y <= i.endy)):
                                board._bufferboard[i.x:i.endx,
                                                   i.y:i.endy] = ""
                                board.enms.remove(i)
                                self.powerup1 = True
                                return 1
                if (board._bufferboard[row, col] != "" and board._bufferboard[row, col] != b"c"):

                    return 0

    for row in range(self.x, self.endx):
        for col in range(self.y, self.endy):
            if board._bufferboard[row, col] == b"c":
                board.player.score += 5
    return 1


def animate(self, board):

    self.y = board.endlevely
    self.endy = board.endlevelendy
    self.x = board.endlevelx
    self.endx = board.endlevelendx
    board.render(self.y)
    config.level += 1
    time.sleep(1)
    self.x = -6
    self.endx = -3
    self.y = 0
    self.endy = 3
    if config.level == 3:
        print()
        print("GAME OVER < YOU WON > ")
        print("Score:", end=" ")
        print(self.score)
        exit()


def reset(self, board, ch):
    if self.powerup1:
        self.powerup1 = False
        if (ch == 'a'):
            for row in range(self.x, self.endx):
                for col in range(self.y, self.y + 1):
                    if (board._bufferboard[row, col] == b"M" or board._bufferboard[row, col] == b'0'):
                        if board._bufferboard[row, col] == b"M":
                            board.player.score += 10
                        else:
                            board.player.score += 30
                        for i in board.enms:
                            if ((self.y >= i.y and self.endy >= i.y) or (self.endy <= i.endy and self.y <= i.endy)):
                                board._bufferboard[i.x:i.endx,
                                                   i.y:i.endy] = ""
                                board.enms.remove(i)
                                return 2
        if (ch == 'd'):
            for row in range(self.x, self.endx):
                for col in range(self.endy-1, self.endy):
                    if (board._bufferboard[row, col] == b"M" or board._bufferboard[row, col] == b'0'):
                        if board._bufferboard[row, col] == b"M":
                            board.player.score += 10
                        else:
                            board.player.score += 30
                        for i in board.enms:
                            if ((self.y <= i.y and self.endy >= i.y) or (self.endy >= i.endy and self.y <= i.endy)):
                                board._bufferboard[i.x:i.endx,
                                                   i.y:i.endy] = ""
                                board.enms.remove(i)
                                return 2

    self.lives -= 1
    if self.lives == -1:
        print("DEAD")
        exit()
    print("RESPAWNING")
    time.sleep(1)
    self.y = board.mariospawny
    self.endy = board.mariospawnendy
    self.x = board.mariospawnx
    self.endx = board.mariospawnendx

    board.__init__(board.height, board.width, board.endlevelx, board.endlevelendx,
                   board.endlevely, board.endlevelendy, board.resen, board.resob, board.coins, board.player)
    board._bufferboard[self.x:self.endx, self.y:self.endy] = self.struct
    board.render(self.y-25)
    config.reset = True
    return 1
