#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tic Tac Toe Game!!

board_store = {'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}

def board_drawer(board_store):
    '''
    Draws the board

    Input: board_store
    Output: print out the updated board
    '''
    row1 = '  '+board_store['1']+' | '+board_store['2']+' | '+board_store['3']
    row2 = '  '+board_store['4']+' | '+board_store['5']+' | '+board_store['6']
    row3 = '  '+board_store['7']+' | '+board_store['8']+' | '+board_store['9']+'\n'
    divider = '\n------------- \n'
    print('\n')
    print(row1)
    print(divider)
    print(row2)
    print(divider)
    print(row3)

def play():
    '''Asks input from both players alternatively'''
    max_blanks = 9
    for counter in range(1,max_blanks):
        if counter%2 == 0:
            ics = input('Where to place your X? ')
            ics = str(ics)
            board_store[ics] = 'X'
            board_drawer(board_store)
            print(board_store)
        else:
            circle = input('Where to place your O? ')
            circle = str(circle)
            board_store[circle] = 'O'
            board_drawer(board_store)

def empty():
    '''Checks if the box is empty and avoid overwrite'''

def win():
    '''Checks if we have 3 X or O and declares a winner or continue to play'''
    if  board_store['1'] == board_store['2'] == board_store['3'] == 'O' or  board_store['1'] == board_store['2'] == board_store['3'] == 'X':
        print(board['1'] + 'wins!!!')
        exit()
    elif board_store['4'] == board_store['5'] == board_store['6'] == 'O' or  board_store['4'] == board_store['5'] == board_store['6'] == 'X':
        print(board['4'] + 'wins!!!')
        exit()
    elif board_store['7'] == board_store['8'] == board_store['9'] == 'O' or  board_store['7'] == board_store['8'] == board_store['9'] == 'X':
        print(board['7'] + 'wins!!!')
        exit()
    elif board_store['1'] == board_store['4'] == board_store['7'] == 'O' or  board_store['1'] == board_store['4'] == board_store['7'] == 'X':
        print(board_store['1'] + 'wins!!!')
        exit()
    elif board_store['2'] == board_store['5'] == board_store['8'] == 'O' or  board_store['2'] == board_store['5'] == board_store['8'] == 'X':
        print(board['2'] + 'wins!!!')
        exit()
    elif board_store['3'] == board_store['6'] == board_store['9'] == 'O' or  board_store['3'] == board_store['6'] == board_store['9'] == 'X':
        print(board['3'] + 'wins!!!')
        exit()
    elif board_store['3'] == board_store['5'] == board_store['7'] == 'O' or  board_store['3'] == board_store['5'] == board_store['7'] == 'X':
        print(board['3'] + 'wins!!!')
        exit()
    elif board_store['1'] == board_store['5'] == board_store['9x'] == 'O' or  board_store['1'] == board_store['5'] == board_store['9'] == 'X':
        print(board['1'] + 'wins!!!')
        exit()
    return


board_drawer(board_store)
play()
