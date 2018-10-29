   
""" Test to see if the mario dies if he falls in the pits  """

import pytest
import board as b
from charec import Mario,Pipes
import config

def move(mario,board):
    return mario.move_right(board)

def test_answer():
    bboard = b.Board(20, 500, -6, -3, 342, 345, [] , [] , [])
    pipe = Pipes(-7, -3, 66, 74, bboard)
    board = b.Board(20, 500, -6, -3, 342, 345, [] , [pipe] , [])
    mario = Mario(-6, -3, 63, 66, board)
    val = move(mario,board)
    val = move(mario,board)
    assert val is False

    
    