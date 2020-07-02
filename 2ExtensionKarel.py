from karel.stanfordkarel import *

"""
File: 2ExtensionKarel.py
-----------------------
This file is for optional extension programs. 
"""

"""
Karel moves through holes in columns that are one corner separate, that makes a hall. She pick up the coins (beepers) and put it down
at the finish line, that function as a scoreboard.
The finish line is mark in orange with beepers, that Karel also picks.
The coins are just at the holes. Holes are 1*1.

Models of this worlds are 2ExtensionKarel and 2ExtensionKarel1.
The world must have a orange finish line. The beepers should be right in the gaps
"""

def main():
    enter_hall()
    cross_hall()
    finish_line()

"""
Pre-conditions: Karel is in (1,1), faces east
Post-conditions: Karel is in the first gap, faces east and had picked the beepers if there was some in her way.
"""
def enter_hall():
    go_to_wall()
    go_up()
    go_through_right()

# She moves trough the holes in the wall until the finish line, because that corners are not blank
def cross_hall():
    while corner_color_is(BLANK):
        slide_up()
        slide_down()

# This is when Karel reach the orange line. karel faces north
def finish_line():
    if corner_color_is(ORANGE):
        pick_all_beepers()
        put_all_beepers()
        # She move out of the scoreboard
        turn_around()
        move()

# It moves forward until the first wall, she faces east. If there are beepers, she picks them
def go_to_wall():
    while front_is_clear():
        advance()

# It moves to north while right is blocked. If there are beepers, she picks them
def go_up():
    turn_left()
    pick_coin()
    while right_is_blocked():
        advance()

# She moves through a hole in a wall if it's in her right, and enter a new gap. If there are beepers, she picks them
def go_through_right():
    turn_right()
    move()
    pick_coin()

# She moves through a hole in a wall if it's in her left, and enter a new gap. If there are beepers, she picks them
def go_through_left():
    turn_left()
    move()
    pick_coin()

# Karel is in a gap, facing east. If left is clear, she turn an move searching a hole in his right side.
def slide_up():
    if left_is_clear():
        turn_left()
    while right_is_blocked() and front_is_clear():
        advance()
    if right_is_clear():    # If there is a hole in her right, she go through it.
        go_through_right()
    else:                   # If there is't any, she turn around to slide down
        turn_around()

# Karel had move up and had no find any hole. So se had turn around and now is facing south.
# Now, she is always going ato find a hole.
def slide_down():
    while left_is_blocked() and front_is_clear():
        advance()
    if left_is_clear():     # When is a hole in her left, she go through it.
        go_through_left()


"""     
Karel picks all beepers in the finish line
Pre-conditions: Karel faces north in any part of the finish line
Post-conditions: Karel face south in the first street of the finish line
"""
def pick_all_beepers():
    while front_is_clear():  # She moves up to pick up al the finals beepers. She faces north
        advance()
    turn_around()            # She turns to face south
    while front_is_clear():  # She moves down to pick up al the finals beepers. She faces south
        advance()

def put_all_beepers():
    while beepers_in_bag():  # When she has pick up all the beepers, she puts it all in the first avenue, ( faces same direction)
        put_beeper()


# Karel advances the next corner and if there is a beeper in it she picks it up.
def advance():
    move()
    pick_coin()

# pick a beeper is it's present
def pick_coin():
    while beepers_present():
        pick_beeper()

# Karel turns 90º to left
def turn_around():
    for i in range(2):
        turn_left()

# Karel turns 180º to left
def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
