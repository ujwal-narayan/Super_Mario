""" Test to see if I get right coordinates  """

import pytest
import board as b
from charec import Mario
import config

def coordinates(mario,board):
   
    val = mario.get_coods()
    return val
def test_answer():
    board = b.Board(20, 500, -6, -3, 342, 345, [] , [] , [])
    mario = Mario(-6, -3, 10, 13, board)
    board.player=mario
    val = coordinates(mario,board)
    assert val == (mario.x_pos, mario.y_pos, mario.endx, mario.endy)