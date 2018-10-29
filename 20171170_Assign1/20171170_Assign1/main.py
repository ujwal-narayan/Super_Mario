""" Main Executable """
import os
import time

import board as b
from charec import Mario
import config
import input as myinput


BOARD = b.Board(20, 500, -6, -3, 342, 345, b.ENMS_1, b.OBS1, b.COINSARR)
MARIO = Mario(-6, -3, 0, 3, BOARD)
config.LEVEL = 2
BOARD.player = MARIO



RESET_CONTRL = 'r'

QUIT_VAL = 1
TIMER = time.time()
TIMER1 = time.time()
LEV1_START = time.time()

while RESET_CONTRL == 'r':
    if config.LEVEL == 2:
        MARIO.score += round(config.X_POS)
        break
    P_INPUT = (myinput.get_input())
    config.X_POS = 200 - (time.time()-LEV1_START)
    if config.X_POS <= 0:
        print("TIME IS UP")
        print("Score :", end="")
        print(MARIO.score)
        exit()
    if P_INPUT == 'q':
        QUIT_VAL = 0
        break

    # cur_round = datetime.datetime.now()

    # """ if (cur_round - prev_round) >= datetime.timedelta(seconds=1):
    #     # bd.update_frame()
    #     # prev_round = cur_round"""

    MARIO.move(P_INPUT, BOARD)
    BOARD.render((MARIO.y_pos - 25))
    # BOARD.printer(0,20,0,190)
    print(MARIO.get_coods())
    print("Score :", end="")
    print(MARIO.score)
    print("Lives left :", end="")
    print(MARIO.lives)
    print("Time left ", end="")
    print(round(config.X_POS))

    if time.time() > TIMER1:
        if MARIO.endx < -3:
            MARIO.move('s', BOARD)
        MARIO.time_since_last_jump += 1

        TIMER1 = time.time()
    if time.time() > TIMER + 1:

        for i in BOARD.enms:
            i.move(BOARD)
        TIMER = time.time()


if config.LEVEL == 2:

    print("MOVING TO LEVEL 2 ")
    time.sleep(1)
    BOARD = b.Board(20, 500, -6, -3, 342, 345,
                    b.ENMS_2, b.OBS2, b.COINSARR, MARIO)

    MARIO.selfx = -6
    MARIO.selfendx = -3
    MARIO.selfy = 0
    MARIO.selfendy = 3
    LV2_START = time.time()

    while RESET_CONTRL == 'r':

        P_INPUT = (myinput.get_input())

        if P_INPUT == 'q':
            QUIT_VAL = 0
            break

        config.X_POS = 200 - (time.time()-LV2_START)
        if config.X_POS <= 0:
            print("TIMES UP")
            print("Score :", end="")
            print(MARIO.score)
            exit()

        MARIO.move(P_INPUT, BOARD)
        BOARD.render((MARIO.y_pos - 25))
        # BOARD.printer(0,20,0,190)
        print(MARIO.get_coods())
        print("Score :", end="")
        print(MARIO.score)
        print("Lives left :", end="")
        print(MARIO.lives)
        print("Time left ", end="")
        print(round(config.X_POS))

        time.sleep(00.02)
        if time.time() > TIMER1:
            if MARIO.endx < 0:
                MARIO.move('s', BOARD)
            MARIO.time_since_last_jump += 1

            TIMER1 = time.time()
        if time.time() > TIMER + 1:

            for i in BOARD.enms:
                i.move(BOARD)
            TIMER = time.time()

    os.system('clear')
    if QUIT_VAL == 0:
        print("Quitting ")
        exit()



