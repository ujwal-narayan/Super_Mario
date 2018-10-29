""" Mario Fall  """

import pytest
import board as b
from charec import Mario
import config

def down(mario,board):
   
    val = mario.move_down(board)
    return val
def test_answer():
    board = b.Board(20, 500, -6, -3, 342, 345, [] , [] , [])
    mario = Mario(-6, -3, 10, 13, board)
    board.player=mario
    val = down(mario,board)
    print(mario.x_pos,mario.y_pos,mario.endx,mario.endy)
    assert val is False