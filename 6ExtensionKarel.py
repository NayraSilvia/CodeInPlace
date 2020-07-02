from karel.stanfordkarel import *
from random import *
"""
File: 6ExtensionKarel.py
-----------------------
This file is for optional extension programs. 
"""

"""
Karel moves in the world searching black corners. When she finds one, she paints a watermelon
She paints randomly black corners at the beginning. Those must be separated by at least 16 corners in width and 9 in height.
She finally paints all watermelons.
Karel's initial position is (1,1) and faces east.

Models world for this are 6ExtensionKarel and 6ExtensionKarel1. 6ExtensionKarel2 has already black corners, that makes 
overlapping watermelon pattern.
"""


def main():
    put_all_beepers()
    initial_position()
    while left_is_clear():
        # Pre: Karel is facing East, start of row
        paint_row()
        next_row()
        # Post: Karel is facing East, start of next row
    paint_row()

def put_all_beepers():
    while front_is_clear():
        # She go up, random times
        random_up()
        if front_is_clear():
            # She moves horizontally, random times
            random_horizontally()


# Pre: faces north, first avenue
# Post: Karel returns to her initial position(1,1) and faces east
def initial_position():
    turn_around()
    move_to_wall()
    turn_left()

# Karel move up to take at least the 9 corners of height
def random_up():
    # Start random generation
    seed()
    z = randint(9, 11)
    turn_left()
    for i in range(z):
        if front_is_clear():
            move()
    if front_is_clear():          # just if she can move 9 times up she paints a new line
        turn_right()



def random_horizontally():
    seed()
    w = randint(0, 2)
    j = randint(0, 4)
    first_corner()
    # She moves at least 16 times to paint the next corner
    while front_is_clear():
        for i in range(16):
            if front_is_clear():
                move()
            else:               # If that doesn't possible, the loop breaks
                break
        # Just if it can move at least 16 corner she continue and add the additional random corners
        if front_is_clear():
            for i in range(j):
                if front_is_clear():
                    move()
                    if random():          # When is true, she go up w times
                        turn_left()
                        if front_is_clear():
                            for i in range(w):
                                if front_is_clear():
                                    move()
                        turn_right()       # and return to  faces east to continue with the row
            paint_corner(BLACK)
        else:
            remove_last_corner()
    next_row()

# If front is blocked, means that she is in the edge, so she can move 16 time. For that, she remove the last painted corner
# Post: edge, facing east
def remove_last_corner():
    turn_around()
    while corner_color_is(BLANK):
        move()
    paint_corner(BLANK)
    turn_around()
    move_to_wall()


# She moves horizontally p times to paint the first corner
def first_corner():
    seed()
    p = randint(0, 16)
    for i in range(p):
        move()
    paint_corner(BLACK)

# pre: karel is at the start of a row
# post: karel is at the end of a row with a paint if there was a beeper
def paint_row():
    while front_is_clear():
        if corner_color_is(BLANK):
            move()
        else:
            paint_watermelon()
            go_up()

# paint the watermelon by rows, start up and go down
def paint_watermelon():
    if front_is_clear():
        row_1()
        next_down_row()
        row_2()
        next_down_row()
        row_3()
        next_down_row()
        row_4()
        next_down_row()
        row_5()
        next_down_row()
        row_6()
        next_down_row()
        row_7()
        next_down_row()
        row_8()
        next_down_row()
        row_9()
    else:                    # She is in a black corner an the front is blocked
        paint_corner(BLANK)  # She remove that corner, It isn't possible to paint

# when she finish painting she go up to the first street of the painting.
def go_up():
    turn_left()
    for i in range(8):
        move()
    turn_right()
    if front_is_clear():
        move()

# When finish a row. She moves to the row below
def next_down_row():
    turn_around()
    for i in range(14):
        move()
    turn_left()
    move()
    turn_left()

# In each row she paints the corner with the color necessary

def row_1():
    for i in range(3):
        black()
    for i in range(4):
        move()
    for i in range(7):
        black()

def row_2():
    simple_first_border()
    red()
    black()
    for i in range(3):
        move()
    paint_corner(BLACK)
    for i in range(4):
        red()
    simple_second_border()

def row_3():
    simple_first_border()
    for i in range(2):
        red()
    for i in range(2):
        black()
    for i in range(2):
        red()
    black()
    for i in range(2):
        red()
    simple_second_border()

def row_4():
    simple_first_border()
    black()
    for i in range(7):
        red()
    black()
    simple_second_border()

def row_5():
    double_first_border()
    for i in range(4):
        red()
    black()
    for i in range(2):
        red()
    double_second_border()

def row_6():
    move()
    double_first_border()
    red()
    black()
    for i in range(3):
        red()
    double_second_border()
    move()

def row_7():
    for i in range(2):
        move()
    double_first_border()
    for i in range(3):
        yellow()
    double_second_border()
    move()
    move()

def row_8():
    for i in range(2):
        move()
    black()
    for i in range(7):
        green()
    black()
    for i in range(3):
        move()

def row_9():
    for i in range(3):
        move()
    for i in range(7):
         black()
    for i in range(4):
        move()

# Karel paints first border of the paint and that is simple
def simple_first_border():
    paint_corner(BLACK)
    green()
    yellow()

# Karel paints last border of the paint and that is simple
def simple_second_border():
    yellow()
    green()
    black()

# Karel paints first border of the paint and that hs double green
def double_first_border():
    paint_corner(BLACK)
    for i in range(2):
        green()
    yellow()

# Karel paints last border of the paint and that hs double green
def double_second_border():
    yellow()
    for i in range(2):
        green()
    black()

# She move to the next corner and paint it with the color

def black():
    move()
    paint_corner(BLACK)

def green():
    move()
    paint_corner(GREEN)

def red():
    move()
    paint_corner(RED)

def yellow():
    move()
    paint_corner(YELLOW)


# pre: karel is at the end of a clean row
# post: karel is at the start of the next messy row
def next_row():
    while front_is_clear():
        move()
    turn_around()
    move_to_wall()
    turn_right()
    if front_is_clear():
        move()
    turn_right()


# Karel moves until a wall
def move_to_wall():
    while front_is_clear():
        move()

# Karel turns 180º to left
def turn_around():
    turn_left()
    turn_left()

# Karel turns 90º to right
def turn_right():
    turn_left()
    turn_left()
    turn_left()


if __name__ == "__main__":
    run_karel_program()