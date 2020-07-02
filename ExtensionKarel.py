from karel.stanfordkarel import *

"""
File: ExtensionKarel.py
-----------------------
This file is for optional extension programs. 
"""

"""
Karel in any size maze world, pick up the coins (beepers) and put it down in a pink corner, functioning as a scoreboard.
Models of this worlds are ExtensionKarel , ExtensionKarel1 , ExtensionKarel2 , ExtensionKarel3 and ExtensionKarel4 .

Pre-conditions: She starts in a corner of a world, facing anywhere. She is inside a maze with all spaces of 1x1 and a magenta square
                in a corner of the world, this isn't the corner in where Karel starts. That maze has beepers scattered in it.
Post-conditions: She is in a gray corner next to the corner that was initially pink and that is, at the end, green.
                This corner is a scoreboard.
"""

def main():
    # She moves twice trough the maze, in two different ways
    two_rounds()
    # She puts all the beepers in the final corner and moves to make it visible
    score()

"""
Pre-conditions: She starts in a corner of a world, facing anywhere. She is inside a maze and a magenta square
                in a corner of the world. All the beepers are still.
Post-conditions: She is a green corner, that was initially magenta. There aren't any beepers, except in that corner
"""
def two_rounds():
    # She moves if the corner is blank, because that means that is not the final corner
    while corner_color_is(BLANK):
        # pick a beeper if there is in the first corner
        pick_coin()
        # She tries all sides and moves to the one that it's clear, picking the beepers
        round()
        # When reach the final corner, mark in magenta, puts all beepers in bag
        if corner_color_is(MAGENTA):
            while beepers_in_bag():
                put_beeper()
                # Change the color of the corner, to break the loop
                paint_corner(GREEN)
            # makes a second way to pick the uncollected beepers
            round()

"""
Pre-conditions: She is in the green corner. There aren't any beepers, except in that corner
Post-conditions: She is the next square, paint at the end in gray, of that corner.
                  She had put all the beepers of the world in the green corner.
"""
def score():
    # When reach the final corner, that is mark in green, puts all beepers in bag
    if corner_color_is(GREEN):
        while beepers_in_bag():
            put_beeper()
        # She moves to the corner that is clear, making final score visible
        if front_is_clear():
            move()
        else:
            if right_is_clear():
                turn_right()
                move()
            else:
                turn_around()
                move()
                # She paints the corner gray, and breaks the loop
                paint_corner(GRAY)

# She moves through the maze, and picks the beepers if any
def round():
    # check the left side, if it's clear she moves
    if left_is_clear():
        turn_left()
        move()
        pick_coin()
    else: # if the left is blocked, she tries front. If it's clear she moves
        if front_is_clear():
            move()
            pick_coin()
        else: # if the left is blocked, she tries right. If it's clear she moves
            if right_is_clear():
                turn_right()
                move()
                pick_coin()
            else: # if the left is blocked, she tries back. If it's clear she moves
                turn_around()
                move()
                pick_coin()

# pick a beeper if it's present
def pick_coin():
    if beepers_present():
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
