import input
import os
import sys
import time

import board as b
from charec import Mario
import config


board = b.Board(20, 500, -6, -3, 342, 345, b.ENMS_1, b.OBS1, b.COINSARR)
mario = Mario(-6, -3, 0, 3, board)
config.level = 2
board.player = mario


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
a = 'r'

quit_val = 1
timer = time.time()
timer1 = time.time()
lev1_start = time.time()

while a == 'r':
    if config.level == 2:
        mario.score += round(config.x_pos)
        break
    p_input = (input.get_input())
    config.x_pos = 200 - (time.time()-lev1_start)
    if config.x_pos <= 0:
        print("TIME IS UP")
        print("Score :", end="")
        print(mario.score)
        exit()
    if p_input == 'q':
        quit_val = 0
        break

    # cur_round = datetime.datetime.now()

    """ if (cur_round - prev_round) >= datetime.timedelta(seconds=1):
        # bd.update_frame()
        # prev_round = cur_round"""

    mario.move(p_input, board)
    board.render((mario.y_pos - 25))
    # board.printer(0,20,0,190)
    print(mario.get_coods())
    print("Score :", end="")
    print(mario.score)
    print("Lives left :", end="")
    print(mario.lives)
    print("Time left ", end="")
    print(round(config.x_pos))

    if time.time() > timer1:
        if(mario.endx < -3):
            mario.move('s', board)
        mario.time_since_last_jump += 1

        timer1 = time.time()
    if time.time() > timer + 1:

        for i in board.enms:
            i.move(board)
        timer = time.time()


if config.level == 2:

    print("MOVING TO LEVEL 2 ")
    time.sleep(1)
    board = b.Board(20, 500, -6, -3, 342, 345,
                    b.ENMS_2, b.OBS2, b.COINSARR, mario)

    mario.selfx = -6
    mario.selfendx = -3
    mario.selfy = 0
    mario.selfendy = 3
    lv2_START = time.time()

    while a == 'r':

        p_input = (input.get_input())

        if p_input == 'q':
            quit_val = 0
            break

        config.x_pos = 200 - (time.time()-lv2_START)
        if config.x_pos <= 0:
            print("TIMES UP")
            print("Score :", end="")
            print(mario.score)
            exit()

        mario.move(p_input, board)
        board.render((mario.y_pos - 25))
        # board.printer(0,20,0,190)
        print(mario.get_coods())
        print("Score :", end="")
        print(mario.score)
        print("Lives left :", end="")
        print(mario.lives)
        print("Time left ", end="")
        print(round(config.x_pos))

        time.sleep(00.02)
        if time.time() > timer1:
            if(mario.endx < 0):
                mario.move('s', board)
            mario.time_since_last_jump += 1

            timer1 = time.time()
        if time.time() > timer + 1:

            for i in board.enms:
                i.move(board)
            timer = time.time()

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
