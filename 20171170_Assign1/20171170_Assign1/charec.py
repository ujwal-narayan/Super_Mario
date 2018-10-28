""" List of All Characters and their capabilities """
from collision import move_maadi
import config


class Characters:
    """ Common for all Characters """

    def __init__(self, x, ex, y, ey, board):
        """ Initial States """

        self.x = x
        self.y = y
        self.speed = 0
        self.damage = 0
        self.dies = True
        self.lives = 0
        self.endx = ex
        self.endy = ey
        self.struct = ""
        self.killed_by_enms = False
        self.powerup1 = False
        if config.reset is False:
            self.current_x = x
            self.current_y = y
            self.cendx = ex
            self.cendy = ey
        del board

    def get_coods(self):
        """ get the co-ordinates """
        return (self.x, self.y, self.endx, self.endy)

    def move_down(self, board, direction='s'):
        """ Function to implement downward movement"""
        orignal_x = self.x
        oendx = self.endx
        orignal_y = self.y
        oendy = self.endy
        self.x += 1
        self.endx += 1
        return_value_move = move_maadi(self, board, direction)
        if return_value_move == 1:
            board.bufferboard[orignal_x:oendx, orignal_y:oendy] = ""
            board.bufferboard[self.x:self.endx, self.y:self.endy] = self.struct
            return True
        elif return_value_move == 0:
            self.x = orignal_x
            self.endx = oendx
            self.y = orignal_y
            self.endy = oendy
            return False

    def move_up(self, board, direction='w'):
        """ Function to move up """
        orignal_x = self.x
        oendx = self.endx
        orignal_y = self.y
        oendy = self.endy
        self.x -= 1
        self.endx -= 1
        return_value_move = move_maadi(self, board, direction)
        if return_value_move == 1:
            board.bufferboard[orignal_x:oendx, orignal_y:oendy] = ""
            board.bufferboard[self.x:self.endx, self.y:self.endy] = self.struct
            return True
        elif return_value_move == 0:
            self.x = orignal_x
            self.endx = oendx
            self.y = orignal_y
            self.endy = oendy
            return False

    def move_left(self, board, direction='a'):
        """ Function to move left """
        orignal_x = self.x
        oendx = self.endx
        orignal_y = self.y
        oendy = self.endy
        self.y -= 1
        self.endy -= 1
        return_value_move = move_maadi(self, board, direction)
        if return_value_move == 1:
            board.bufferboard[orignal_x:oendx, orignal_y:oendy] = ""
            board.bufferboard[self.x:self.endx, self.y:self.endy] = self.struct
            return True
        elif return_value_move == 0:
            self.x = orignal_x
            self.endx = oendx
            self.y = orignal_y
            self.endy = oendy
            return False

    def move_right(self, board, direction='d'):
        """ Function to move right """
        orignal_x = self.x
        oendx = self.endx
        orignal_y = self.y
        oendy = self.endy
        self.y += 1
        self.endy += 1
        return_value_move = move_maadi(self, board, direction)
        if return_value_move == 1:
            board.bufferboard[orignal_x:oendx, orignal_y:oendy] = ""
            board.bufferboard[self.x:self.endx, self.y:self.endy] = self.struct
            return True
        elif return_value_move == 0:
            self.x = orignal_x
            self.endx = oendx
            self.y = orignal_y
            self.endy = oendy
            return False

    def speed_imp(self, board, charecter):
        """ Function to implement multiple speeds """
        ret = False
        if charecter == 's':
            for _ in range(self.speed):
                speed_var = self.move_down(board, charecter)
                if speed_var:
                    ret = True
        if charecter == 'd':
            for _ in range(self.speed):
                speed_var = self.move_right(board, charecter)
                if speed_var:
                    ret = True
        if charecter == 'a':
            for _ in range(self.speed):
                speed_var = self.move_left(board, charecter)
                if speed_var:
                    ret = True
        return ret


class Powerup1(Characters):
    """" Comrade Mario , unleash the beasts of revolution . Bring forth da GUNS """

    def __init__(self, x, ex, y, ey, board):
        super(Powerup1, self).__init__(x, ex, y, ey, board)
        self.speed = config.powerup_speed
        self.struct = config.powerup1
        self.mover = 'd'
        self.powerup1 = True
        board.bufferboard[self.current_x:self.cendx, self.current_y:self.cendy] = self.struct

    def move(self, board):
        """ Function to move """
        if self.y == 0:
            pass
        if self.speed_imp(board, 's'):
            pass
        else:
            if self.mover == 'a':
                if self.speed_imp(board, 'a'):
                    pass
                else:
                    self.mover = 'd'
            elif self.mover == 'd':
                if self.speed_imp(board, 'd'):
                    pass
                else:
                    self.mover = 'a'


class Mario(Characters):
    """ issa me , Mario """

    def __init__(self, x, ex, y, ey, board, lives=3):
        super(Mario, self).__init__(x, ex, y, ey, board)
        self.lives = lives
        self.score = 0
        self.speed = config.speed
        self.jump = config.jump
        self.time_since_last_jump = 100
        self.jump_counter = 0
        self.damage = 10
        self.killed_by_enms = True
        self.powerup1 = False
        self.struct = config.mario
        board.bufferboard[self.current_x:self.cendx, self.current_y:self.cendy] = self.struct

    def jump_up(self, board, direction):
        """ Function to jump """
        orignal_x = self.x
        oendx = self.endx
        orignal_y = self.y
        oendy = self.endy
        self.x -= 1
        self.endx -= 1
        jump_possible = True

        if self.time_since_last_jump > 10:
            self.jump_counter = 0
        else:
            if self.jump_counter > 2 * self.jump:
                jump_possible = False
        return_value_move = move_maadi(self, board, direction)
        if return_value_move == 1 and jump_possible:
            board.bufferboard[orignal_x:oendx, orignal_y:oendy] = ""
            board.bufferboard[self.x:self.endx, self.y:self.endy] = self.struct
            self.time_since_last_jump = 0
            self.jump_counter += 1
            return True
        elif return_value_move == 0 or not jump_possible:
            self.x = orignal_x
            self.endx = oendx
            self.y = orignal_y
            self.endy = oendy
            return False

    def jump_ups(self, board, charecter):
        """ Function to implement multiple jumps """
        for _ in range(self.jump):
            self.jump_up(board, charecter)

    def move(self, charecter, board):
        """ Function to implement move """
        if charecter == 'w' or charecter == 'W':
            self.jump_ups(board, 'j')
        if charecter == 's' or charecter == 'S':
            self.speed_imp(board, 's')
            # self.move_down(board,charecter)
        elif charecter == 'a' or charecter == 'A':
            self.speed_imp(board, 'a')
            # self.move_left(board,charecter)
        elif charecter == 'd' or charecter == 'D':
            self.speed_imp(board, 'd')
            # self.move_right(board,charecter)
        elif charecter == ' ':
            self.jump_ups(board, 'j')


class Mushroom(Characters):
    """ Low level easy peasy enimies """

    def __init__(self, x, ex, y, ey, board, lives=1):
        super(Mushroom, self).__init__(x, ex, y, ey, board)
        self.lives = lives
        self.speed = config.mushroom_speed
        self.struct = config.mushroom
        board.bufferboard[self.current_x:self.cendx, self.current_y:self.cendy] = self.struct
        self.mover = 'a'

    def move(self, board):
        """ Function to implement move """
        if self.mover == 'a':
            if self.speed_imp(board, 'a'):
                pass
            else:
                self.mover = 'd'
        elif self.mover == 'd':
            if self.speed_imp(board, 'd'):
                pass
            else:
                self.mover = 'a'


class Turtles(Characters):
    """Medium level annoying beasts """

    def __init__(self, x, ex, y, ey, board, lives=1):
        super(Turtles, self).__init__(x, ex, y, ey, board)
        self.lives = lives
        self.damage = 50
        self.speed = config.mushroom_speed
        self.struct = config.turtle
        board.bufferboard[self.current_x:self.cendx, self.current_y:self.cendy] = self.struct

    def move(self, board):
        """ FUnction to implement move """
        if self.y > board.player.y:
            self.speed_imp(board, 'a')
        else:
            self.speed_imp(board, 'd')


class DarthVader(Characters):
    """I AM THE SENATE .the big bad boss himself """

    def __init__(self, x, ex, y, ey, board, lives=3):
        super(DarthVader, self).__init__(x, ex, y, ey, board)
        self.damage = 10
        self.lives = lives
        self.speed = 10
        self.struct = config.darthvader
        board.bufferboard[self.current_x:self.cendx, self.current_y:self.cendy] = self.struct

    def move(self, board):
        """ Function to implement move """
        if board.player.endx < -3:
            self.y = board.player.y + 1
            self.endy = board.player.endy + 1
        else:
            if self.y > board.player.y:
                self.speed_imp(board, 'a')
            else:
                self.speed_imp(board, 'd')


class Obstacles:
    ''' Class for obstacles and other '''

    def __init__(self, x, ex, y, ey, board):
        self.x = x
        self.endx = ex
        self.y = y
        self.endy = ey
        self.struct = ""
        self.breakable = False


class Pipes(Obstacles):
    '''class for various pipes , default is this one '''

    def __init__(self, x, ex, y, ey, board):
        super(Pipes, self).__init__(x, ex, y, ey, board)
        self.struct = config.pipes
        board.bufferboard[self.x:self.endx, self.y:self.endy] = self.struct


class BigPipes(Obstacles):
    ''' Bigger Pipes '''

    def __init__(self, x, ex, y, ey, board):
        super(BigPipes, self).__init__(x, ex, y, ey, board)
        self.struct = config.bigpipes
        board.bufferboard[self.x:self.endx, self.y:self.endy] = self.struct


class SldingPipes(Obstacles):
    ''' The kinda pipes you'll use to slide down '''

    def __init__(self, x, ex, y, ey, board):
        super(SldingPipes, self).__init__(x, ex, y, ey, board)
        self.struct = config.goingdownpipe
        board.bufferboard[self.x:self.endx, self.y:self.endy] = self.struct


class Bricks(Obstacles):
    ''' Bricks are domesticated Rocks , Let 'em free '''

    def __init__(self, x, ex, y, ey, board):
        super(Bricks, self).__init__(x, ex, y, ey, board)
        self.struct = config.brickwalls
        board.bufferboard[self.x:self.endx, self.y:self.endy] = self.struct


class Flagpost(Obstacles):
    ''''Jai Hind xD'''

    def __init__(self, x, ex, y, ey, board):
        super(Flagpost, self).__init__(x, ex, y, ey, board)
        self.struct = config.flagpost
        board.bufferboard[self.x:self.endx, self.y:self.endy] = self.struct


class ZigZagWall(Obstacles):
    ''' Le Obstacle at le end'''

    def __init__(self, x, ex, y, ey, board):
        super(ZigZagWall, self).__init__(x, ex, y, ey, board)
        self.struct = config.zigzagwall
        board.bufferboard[self.x:self.endx, self.y:self.endy] = self.struct


class Castle(Obstacles):
    '''Castle at the end of a hill . Hogwarts <3 '''

    def __init__(self, x, ex, y, ey, board):
        super(Castle, self).__init__(x, ex, y, ey, board)
        self.struct = config.castle
        board.bufferboard[self.x:self.endx, self.y:self.endy] = self.struct


class Pits(Obstacles):
    ''' One way ticket to Tartarus  '''

    def __init__(self, x, ex, y, ey, board):
        super(Pits, self).__init__(x, ex, y, ey, board)
        self.struct = config.pits
        board.bufferboard[self.x:self.endx, self.y:self.endy] = self.struct


class Coins():
    """ MONEEEEE , gimme mone Jai jai money"""

    def __init__(self, x, y, board):
        self.x = x
        self.y = y
        self.struct = config.coins
        board.bufferboard[self.x:self.x+1, self.y:self.y+1] = self.struct
