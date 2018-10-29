""" Mario move Right  """

import pytest
import board as b
from charec import Mario
import config

def right_movement(mario,board):
   
    val = mario.move_right(board)
    return val
def test_answer():
    board = b.Board(20, 500, -6, -3, 342, 345, [] , [] , [])
    mario = Mario(-6, -3, 10, 13, board)
    board.player=mario
    val = right_movement(mario,board)
    print(mario.x_pos,mario.y_pos,mario.endx,mario.endy)
    assert val is True