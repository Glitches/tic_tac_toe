#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tic Tac Toe Game!!

board_store = {'s1':' ','s2':' ','s3':' ','s4':' ','s5':' ','s6':' ','s7':' ','s8':' ','s9':' '}

def board_drawer(board_store):
    '''
    Draws the board

    Input: board_store
    Output: print out the updated board
    '''
    board = '  '+board_store['s1']+' | '+board_store['s2']+' | '+board_store['s3']+' ''\n-------------\n'
    board2 = ' '+board_store['s4']+' | '+board_store['s5']+' | '+board_store['s6']+' \n-------------\n'
    board3 = ' '+board_store['s7']+' | '+board_store['s8']+' | '+board_store['s9']+' \n'
    print(board, board2, board3)

def play():
    max_blanks = 9
    counter = 0
    while counter <= max_blanks:
        if counter%2 == 0:
            ics = raw_input('Where to place your X? ')
            board_store[str(ics)] = X
            print(board, board2, board3)
        else:
            circle = raw_input('Where to place your O? ')
            board_store[str(circle)] = O
            print(board, board2, board3)





board_drawer(board_store)
