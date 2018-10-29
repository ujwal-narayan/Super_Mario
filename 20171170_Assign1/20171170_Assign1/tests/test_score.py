   
""" Test to see if the mario dies if he falls in the pits  """

import pytest
import board as b
from charec import Mario,Coins
import config

def move(mario,board):
    mario.move('w', board)

def test_answer():
    bboard = b.Board(20, 500, -6, -3, 342, 345, [] , [] , [])
    coin = Coins(-7, 30, bboard)
    board = b.Board(20, 500, -6, -3, 342, 345, [] , [] , [coin])
    mario = Mario(-6, -3, 30, 33, board)
    board.player=mario
    intial_score = mario.score
    move(mario,board)
    assert mario.score == intial_score + 5
