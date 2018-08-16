

import numpy as np 

class Board:
    """ Its the board and scene gen classs """

    def __init__(self, m, n, level):
        """ preferred size = (FILL IT LATER) """
        assert isinstance(m, int) == True
        assert isinstance(n, int) == True
        self.height = m
        self.width = n
        self.dimen = (n, m)
        self._bufferboard = np.chararray((m, n))
        self._bufferboard[:, :] = "" #config._empty
        self.framecounter = 0
        self.init_points = []
        self.level = level

        self.init_board()

        # This stores a list of all the enemies and coins
        """self._storage = {
            config._types[config._e1]: [],
            config._types[config._e2]: [],
            config._types[config._e3]: [],
            config._types[config._coins]: [],
            config._types[config._powerup]: []

        }
            """
        # Stores the player.Try multiplayer uing threading if there's time
        self.players = []

    def init_board(self, reset=False):
        """ Intialize the board and set it up """
        if reset:
            self.framecounter = 0

        # assigning the ground
        self._bufferboard[-3:, :] = "-"#config._ground
        # assigning the sky
        
        self._bufferboard[:3, :] = "-" #config._sky
    def printer(self):
        for row in range(self.height):
            for col in range(self.width):
                print(getcc(self._bufferboard[row,col]),end="")
            print("")
           
#helper functions switch to another file later 

def getcc (ch):
    if ch == "" :
        return " "
    if ch == b'-':
        return "-"

b=Board(30,190,0)
b.printer()