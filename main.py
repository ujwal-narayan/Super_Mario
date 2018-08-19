from input import Get , input_to
import os 
import sys 
from board import Board
from charec import Mario


board = Board(20,390,0)
mario = Mario(-6,-3,0,3,board)
getch = Get()
board.printer(0,20,0,190)

while True :
    input = input_to(getch)
    os.system('clear')
    #print here 
    board.printer(0,20,0,190)
    if input is not None :
        mario.move(input , board)

    if input == 'q' :
        os.system('clear')
        sys.exit()
