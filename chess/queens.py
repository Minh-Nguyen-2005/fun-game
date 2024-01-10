# Author: Minh Nguyen
# Date: 10/06/2023
# Purpose: CS1 - Solution for A6 (Queens) assignment

from cs1lib import *
from random import randint

WIN_SIZE = 500
N = 4
first = True

# This function creates list of lists
# representation of an n*n chessboard and
# places a queen randomly in each row.

def place_random_queens(n):
    board_lol = []
    i = 0
    while i < n:
        # creates a list of length n where all elements are False
        inner_list = [False] * n

        # change a value at random index in inner_list to True
        rand_indx = randint(0, n - 1)
        inner_list[rand_indx] = True

        # add the inner_list to the board list of lists
        board_lol.append(inner_list)
        i = i + 1

    return board_lol


# The function that a list of lists representation of the board
# and draw the chessboard. It draws placed queens as red circles.

def draw_board(glol, n):
    # clear background
    set_clear_color(1, 1, 1)
    clear()

    if len(glol) != n:
        print("Wrong outer list length")
        return
    sqr_width = WIN_SIZE // n
    i = 0
    while i < n:
        if len(glol[i]) != n:
            print("Wrong inner list length")
            return
        j = 0
        while j < n:
            if (j + i) % 2 == 0:
                set_fill_color(1, 1, 1)
            else:
                set_fill_color(0.5, 0.5, 0.5)

            sqr_x = i * sqr_width
            sqr_y = j * sqr_width
            draw_rectangle(sqr_y, sqr_x, sqr_width, sqr_width)

            # Check if that cell has a queen and draw a
            # circle in red.
            if glol[i][j] == 1:
                set_fill_color(0.9, 0, 0)
                draw_circle(sqr_y + sqr_width // 2, sqr_x + sqr_width // 2, sqr_width // 10)

            j = j + 1
        i = i + 1


# This function takes a list of lists representing the N*N chessboard
# which is a list of lists of length N, where each inner list of length N represents a row in the chessboard,
# with N queens placed randomly on board and returns True if no two queens attach each other.
# Otherwise, it returns False.

def check_board(glol):
    row = 0
    while row < len(glol):
        col = 0
        while col < len(glol):
            if glol[row][col] == True:
                check = queens(row, col, glol)
                if check == False:
                    return False
            col = col + 1
        row = row + 1
    return True

def queens(r, c, glol): #
    i = 0
    while i < len(glol):
        j = 0
        while j < len(glol):
            if glol[i][j] == True:
                check = check_queens(r, c, i, j)
                if check == False:
                    return False
            j = j + 1
        i = i + 1
    return True

def check_queens(r1, c1, r2, c2): #check if two queens can attack each other.
    if (r1 == r2 or c1 == c2 or r1 - c1 == r2 - c2 or r1 + c1 == r2 + c2) and (r1 != r2 or c1 != c2):
        return False
    return True


# Main draw function

def my_draw():
    global first
    if first:
        # clear only once,this makes the correct board to stay on screen
        set_clear_color(1, 1, 1)
        clear()
        first = False

    board = place_random_queens(N)
    check = check_board(board)
    if check:
        draw_board(board, N)
    print(check)


start_graphics(my_draw, width=WIN_SIZE, height=WIN_SIZE)