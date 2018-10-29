   
""" Test to see if the mario dies if he falls in the pits  """

import pytest
import board as b
from charec import Mario,Pits
import config

def move(mario,board):
    mario.move('s', board)

def test_answer():
    bboard = b.Board(20, 500, -6, -3, 342, 345, [] , [] , [])
    pit = Pits(-4, -1, 30, 34, bboard)
    board = b.Board(20, 500, -6, -3, 342, 345, [] , [pit] , [])
    mario = Mario(-4, -1, 30, 33, board)
    try:
        move(mario,board)
    except SystemExit :
        assert config.ALIVE is False
    