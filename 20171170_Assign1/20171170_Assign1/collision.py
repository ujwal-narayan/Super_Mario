""" Contains collision logic """
import time
import config


def move_maadi(self, board, charac):

    if (self.x_pos or self.endx) < -20:
        return 0

    if (self.y_pos or self.endy) < 0:
        return 0

#    if board == b.level1:
    for row in range(self.x_pos, self.endx):
        for col in range(self.endy-1, self.endy):
            if (board.bufferboard[row, col] == b"l"):
                self.y_pos += 5
                self.endy += 5
                animate(self, board)
                return 1

    if charac == 'a':
        for row in range(self.x_pos, self.endx):
            for col in range(self.y_pos, self.y_pos + 1):
                if self.killed_by_enms:
                    if (board.bufferboard[row, col] == b"M" or board.bufferboard[row, col] == b'0'):
                        if board.bufferboard[row, col] == b"M":
                            board.player.score += 10
                        else:
                            board.player.score += 30
                        for i in board.enms:
                            if (self.y_pos >= i.y_pos and self.endy >= i.y_pos) or \
                            (self.endy <= i.endy and self.y_pos <= i.endy):
                                rtrn = reset(self, board, 'a')
                                if rtrn == 1:
                                    return 2
                                else:
                                    return 1
                    if board.bufferboard[row, col] == b"G":
                        for i in board.enms:
                            if (self.y_pos >= i.y_pos and self.endy >= i.y_pos) or \
                            (self.endy <= i.endy and self.y_pos <= i.endy):
                                board.bufferboard[i.x_pos:i.endx, i.y_pos:i.endy] = ""
                                board.enms.remove(i)
                                self.powerup1 = True
                                board.player.score += 50
                                return 1

                else:
                    if board.bufferboard[row, col] == b"@" or \
                    board.bufferboard[row, col] == b"|" or \
                    board.bufferboard[row, col] == b"/" or \
                    board.bufferboard[row, col] == b"\\":
                        if self.powerup1:
                            board.player.powerup1 = True
                            for i in board.enms:
                                if i.y_pos == self.y_pos and i.endy == self.endy:
                                    board.bufferboard[i.x_pos:i.endx, i.y_pos+1:i.endy+1] = ""
                                    board.enms.remove(i)
                                board.player.powerup1 = False
                            return 3
                        rtrn = reset(board.player, board, 'a')
                        if rtrn == 1:
                            return 2
                        else:
                            return 1
                if board.bufferboard[row, col] != "":
                    return 0

    if charac == 'd':
        for row in range(self.x_pos, self.endx):
            for col in range(self.endy-1, self.endy):
                if self.killed_by_enms:
                    if board.bufferboard[row, col] == b"M" or \
                    board.bufferboard[row, col] == b'0':
                        if board.bufferboard[row, col] == b"M":
                            board.player.score += 10
                        else:
                            board.player.score += 30
                        for i in board.enms:
                            if (self.y_pos <= i.y_pos and self.endy >= i.y_pos) or \
                            (self.endy >= i.endy and self.y_pos <= i.endy):
                                rtrn = reset(self, board, 'd')
                                if rtrn == 1:
                                    return 2
                                else:
                                    return 1
                    if board.bufferboard[row, col] == b"G":
                        for i in board.enms:
                            if (self.y_pos <= i.y_pos and self.endy >= i.y_pos) or \
                            (self.endy >= i.endy and self.y_pos <= i.endy):
                                board.bufferboard[i.x_pos:i.endx, i.y_pos:i.endy] = ""
                                board.enms.remove(i)
                                self.powerup1 = True
                                board.player.score += 50
                                return 1
                else:
                    if board.bufferboard[row, col] == b"@" or \
                    board.bufferboard[row, col] == b"|" or \
                    board.bufferboard[row, col] == b"/" or \
                    board.bufferboard[row, col] == b"\\":
                        if self.powerup1:
                            board.player.powerup1 = True
                            for i in board.enms:
                                if i.y_pos == self.y_pos and i.endy == self.endy:
                                    board.bufferboard[i.x_pos:i.endx, i.y_pos-1:i.endy-1] = ""
                                    board.enms.remove(i)
                                board.player.powerup1 = False
                            return 3
                        rtrn = reset(board.player, board, 'd')
                        if rtrn == 1:
                            return 2
                        else:
                            return 1
                if (board.bufferboard[row, col] != ""):
                    return 0

    if charac == 'w':
        for col in range(self.y_pos, self.endy):
            for row in range(self.x_pos, self.x_pos+1):
                if board.bufferboard[row, col] != "":
                    return 0

    if charac == 's':
        if self.endx > -2:
            if self.killed_by_enms:
                self.powerup1 = False
                reset(self, board, charac)
            else:
                board.bufferboard[self.x_pos:self.endx, self.y_pos:self.endy] = ""
                for i in board.enms:
                    if i.endx > -3:
                        board.enms.remove(i)

        for col in range(self.y_pos, self.endy):
            for row in range(self.endx-1, self.endx):
                if self.killed_by_enms:
                    if board.bufferboard[row, col] == b"M" or board.bufferboard[row, col] == b'0':
                        if board.bufferboard[row, col] == b"M":
                            board.player.score += 10
                        else:
                            board.player.score += 30
                        for i in board.enms:
                            if (self.y_pos <= i.y_pos and self.endy >= i.y_pos) or \
                            (self.endy >= i.endy and self.y_pos <= i.endy):
                                board.bufferboard[i.x_pos:i.endx, i.y_pos:i.endy] = ""
                                board.enms.remove(i)
                                move_maadi(self, board, charac)
                                move_maadi(self, board, charac)
                                move_maadi(self, board, charac)
                                move_maadi(self, board, charac)
                                board.render(self.y_pos-25)
                                return 1
                    if board.bufferboard[row, col] == b"G":
                        for i in board.enms:
                            if (self.y_pos <= i.y_pos and self.endy >= i.y_pos) or \
                            (self.endy >= i.endy and self.y_pos <= i.endy):
                                board.bufferboard[i.x_pos:i.endx, i.y_pos:i.endy] = ""
                                board.enms.remove(i)
                                self.powerup1 = True
                                board.player.score += 50
                                return 1

                if board.bufferboard[row, col] != "" and board.bufferboard[row, col] != b"c":
                    self.time_since_last_jump = 10
                    self.jumpCounter = 0

                    return 0

    if charac == 'j':
        for col in range(self.y_pos, self.endy):
            for row in range(self.x_pos, self.x_pos+1):
                if self.killed_by_enms:
                    if (board.bufferboard[row, col] == b"G"):
                        for i in board.enms:
                            if (self.y_pos <= i.y_pos and self.endy >= i.y_pos) or \
                            (self.endy >= i.endy and self.y_pos <= i.endy):
                                board.bufferboard[i.x_pos:i.endx, i.y_pos:i.endy] = ""
                                board.enms.remove(i)
                                self.powerup1 = True
                                return 1
                if (board.bufferboard[row, col] != "" and board.bufferboard[row, col] != b"c"):

                    return 0

    for row in range(self.x_pos, self.endx):
        for col in range(self.y_pos, self.endy):
            if board.bufferboard[row, col] == b"c":
                board.player.score += 5
    return 1


def animate(self, board):
    """ End of level animation """
    self.y_pos = board.endlevely
    self.endy = board.endlevelendy
    self.x_pos = board.endlevelx
    self.endx = board.endlevelendx
    board.render(self.y_pos)
    config.level += 1
    time.sleep(1)
    self.x_pos = -6
    self.endx = -3
    self.y_pos = 0
    self.endy = 3
    if config.level == 3:
        print()
        print("GAME OVER < YOU WON > ")
        print("Score:", end=" ")
        print(self.score)
        exit()


def reset(self, board, charac):
    """ Resets the board"""
    if self.powerup1:
        self.powerup1 = False
        if charac == 'a':
            for row in range(self.x_pos, self.endx):
                for col in range(self.y_pos, self.y_pos + 1):
                    if (board.bufferboard[row, col] == b"M" or board.bufferboard[row, col] == b'0'):
                        if board.bufferboard[row, col] == b"M":
                            board.player.score += 10
                        else:
                            board.player.score += 30
                        for i in board.enms:
                            if (self.y_pos >= i.y_pos and self.endy >= i.y_pos) or \
                            (self.endy <= i.endy and self.y_pos <= i.endy):
                                board.bufferboard[i.x_pos:i.endx, i.y_pos:i.endy] = ""
                                board.enms.remove(i)
                                return 2
        if charac == 'd':
            for row in range(self.x_pos, self.endx):
                for col in range(self.endy-1, self.endy):
                    if (board.bufferboard[row, col] == b"M" or board.bufferboard[row, col] == b'0'):
                        if board.bufferboard[row, col] == b"M":
                            board.player.score += 10
                        else:
                            board.player.score += 30
                        for i in board.enms:
                            if (self.y_pos <= i.y_pos and self.endy >= i.y_pos) or \
                            (self.endy >= i.endy and self.y_pos <= i.endy):
                                board.bufferboard[i.x_pos:i.endx, i.y_pos:i.endy] = ""
                                board.enms.remove(i)
                                return 2

    self.lives -= 1
    if self.lives == -1:
        print("DEAD")
        exit()
    print("RESPAWNING")
    time.sleep(1)
    self.y_pos = board.mariospawny
    self.endy = board.mariospawnendy
    self.x_pos = board.mariospawnx
    self.endx = board.mariospawnendx

    board.__init__(board.height, board.width, board.endlevelx, board.endlevelendx, \
    board.endlevely, board.endlevelendy, board.resen, board.resob, \
    board.coins, board.player)
    board.bufferboard[self.x_pos:self.endx, self.y_pos:self.endy] = self.struct
    board.render(self.y_pos-25)
    config.RESET = True
    return 1
