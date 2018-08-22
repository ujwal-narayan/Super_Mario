import input 
import os 
import sys 
import time

import board as b 
from charec import Mario
import config


board = b.level1
mario = Mario(-6,-3,0,3,board)
config.level=1



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

quit_val = 1
while a=='r':
    if config.level == 2 :
        break
    p_input = (input.get_input())

    if p_input == 'q':
        quit_val = 0
        break

    # cur_round = datetime.datetime.now()
    
    """ if (cur_round - prev_round) >= datetime.timedelta(seconds=1):
        # bd.update_frame()
        # prev_round = cur_round"""

    mario.move(p_input , board)
    board.render((mario._y - 25))
    #board.printer(0,20,0,190)
    print(mario.get_coods())

    time.sleep(0.02)
    if(mario._endx < -3 ):
        mario.move('s',board)
    mario.timeSinceLastJump += 1
    print(mario.timeSinceLastJump)
   
   

if config.level == 2:
    print("MOVING TO LEVEL 2 ")
    time.sleep(1)
    board = b.level2
    mario = Mario(-6,-3,320,323,board)  

    while a=='r':
    
        p_input = (input.get_input())

        if p_input == 'q':
            quit_val = 0
            break

    

        mario.move(p_input , board)
        board.render((mario._y - 25))
        #board.printer(0,20,0,190)
        print(mario.get_coods())

        time.sleep(0.02)
        if(mario._endx < -3 ):
            mario.move('s',board)
        mario.timeSinceLastJump += 1
        print(mario.timeSinceLastJump)
    
        
    
os.system('clear')
if quit_val == 0:
    print("Quitting ")
    exit()


    

'''
 os.system('clear')
print("Restart?")
a=input._getch()
os.system('reset')
'''