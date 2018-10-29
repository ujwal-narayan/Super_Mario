""" Test to see if the speed function works  """

import pytest
import board as b
from charec import Mario
import config

def move(mario,board):
    mario.move('d', board)
def test_answer():
    board = b.Board(20, 500, -6, -3, 342, 345, [] , [] , [])
    mario = Mario(-6, -3, 10, 13, board)
    board.player=mario
    move(mario,board)
    assert mario.y_pos == 11