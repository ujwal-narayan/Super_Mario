""" Takes care of the input to the game """
UP, DOWN, LEFT, RIGHT, BOMB, QUIT = range(6)
DIR = [UP, DOWN, LEFT, RIGHT]
INVALID = -1

ALLOWEDINPUTS = {
    UP: ['w', '\x1b[A'],
    DOWN: ['s', '\x1b[B'],
    LEFT: ['a', '\x1b[D'],
    RIGHT: ['d', '\x1b[C'],
    QUIT: ['q']
}


def get_key(key):
    """ Check if it's a valid input or not"""
    for input_character_result in ALLOWEDINPUTS:
        if key in ALLOWEDINPUTS[input_character_result]:
            return input_character_result
    return INVALID


class _Getch:
    """ Gets a single character from standard input.  Does not echo to the screen."""
    def __init__(self):
        # try:
            # placeholer_silfimplwin = _GetchWindows()
            # isplaceholder = 0
        # except ImportError:
        placeholer_silfimplunix = _GetchUnix()
        # isplaceholder = 1
        # if isplaceholder == 1:
        self.impl = placeholer_silfimplunix
        # elif isplaceholder == 0:
            # self.impl = placeholer_silfimplwin
    def __call__(self):
        return self.impl()

class _GetchUnix:
    def __init__(self):
        import tty
        import sys

    def __call__(self):
        import sys
        import tty
        import termios
        fedvar = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fedvar)
        try:
            tty.setraw(sys.stdin.fileno())
            character = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fedvar, termios.TCSADRAIN, old_settings)
        return character


# class _GetchWindows:

#     def __init__(self):
#         import msvcrt

#     def __call__(self):
#         import msvcrt
#         return msvcrt.getch()


GETCH = _Getch()


class AlarmException(Exception):
    """ To stop the alarms """
    pass


def alarmhandler(signum, frame):
    """ Function to detect alarms """
    del signum
    del frame
    raise AlarmException


def get_input(timeout=1):
    """ Function to get the user input """
    import signal
    signal.signal(signal.SIGALRM, alarmhandler)
    signal.alarm(timeout)
    try:
        text = GETCH()
        signal.alarm(0)
        return text
    except AlarmException:
        pass
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''
