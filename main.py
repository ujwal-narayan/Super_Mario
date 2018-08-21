import input 
import os 
import sys 
import time
from board import Board
from charec import Mario


board = Board(20,390,0)
mario = Mario(-6,-3,0,3,board)


'''
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
    time.sleep(0.2)
'''
a='r'


while a=='r':
    p_input = (input.get_input())

    if p_input == 'q':
        break

    # cur_round = datetime.datetime.now()
    
    """ if (cur_round - prev_round) >= datetime.timedelta(seconds=1):
        # bd.update_frame()
        # prev_round = cur_round"""

    mario.move(p_input , board)
    board.render()
    #board.printer(0,20,0,190)
    print(mario.get_coods())
    time.sleep(0.001)
   
    
    

'''
os.system('clear')
print("Restart?")
a=input._getch()
os.system('reset')
'''