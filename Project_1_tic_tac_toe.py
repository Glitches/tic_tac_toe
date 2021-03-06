#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Tic Tac Toe Game!!

board_store = {'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}
board_numbered = {'1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9'}
welcome_message = '''

Welcome to my Tic Tac Toe Game!!
You already know the rules!
This app switches itself to player 1 and 2: you have just to type box number,
as you can see in the following scheme!
Have fun!'''

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
    for counter in range(0,max_blanks):
        if counter%2 == 0:
            empty_x()
            win()
        else:
            empty_o()
            win()
    print('No victory!!!')
    return



def empty_x():
    '''Checks if the box is empty and avoid overwrite

    Input a box number from the player'''
    ics = input('Where to place your X? ')
    ics = str(ics)
    while board_store[ics] != ' ':
        ics = input('Where to place your X? ')
        ics = str(ics)
    board_store[ics] = 'X'
    board_drawer(board_store)
    # print(board_store) # debug print

def empty_o():
    '''Checks if the box is empty and avoid overwrite

    Input a box number from the player'''
    circle = input('Where to place your O? ')
    circle = str(circle)
    while board_store[circle] != ' ':
        circle = input('Where to place your O? ')
        circle = str(circle)
    board_store[circle] = 'O'
    board_drawer(board_store)
    # print(board_store) # debug print




def win():
    '''Checks if we have 3 X or O and declares a winner or continue to play'''
    if  board_store['1'] == board_store['2'] == board_store['3'] == 'O' or  board_store['1'] == board_store['2'] == board_store['3'] == 'X':
        print(board_store['1'] + ' wins!!!')
        exit()
    elif board_store['4'] == board_store['5'] == board_store['6'] == 'O' or  board_store['4'] == board_store['5'] == board_store['6'] == 'X':
        print(board_store['4'] + ' wins!!!')
        exit()
    elif board_store['7'] == board_store['8'] == board_store['9'] == 'O' or  board_store['7'] == board_store['8'] == board_store['9'] == 'X':
        print(board_store['7'] + ' wins!!!')
        exit()
    elif board_store['1'] == board_store['4'] == board_store['7'] == 'O' or  board_store['1'] == board_store['4'] == board_store['7'] == 'X':
        print(board_store['1'] + ' wins!!!')
        exit()
    elif board_store['2'] == board_store['5'] == board_store['8'] == 'O' or  board_store['2'] == board_store['5'] == board_store['8'] == 'X':
        print(board_store['2'] + ' wins!!!')
        exit()
    elif board_store['3'] == board_store['6'] == board_store['9'] == 'O' or  board_store['3'] == board_store['6'] == board_store['9'] == 'X':
        print(board_store['3'] + ' wins!!!')
        exit()
    elif board_store['3'] == board_store['5'] == board_store['7'] == 'O' or  board_store['3'] == board_store['5'] == board_store['7'] == 'X':
        print(board_store['3'] + ' wins!!!')
        exit()
    elif board_store['1'] == board_store['5'] == board_store['9'] == 'O' or  board_store['1'] == board_store['5'] == board_store['9'] == 'X':
        print(board_store['1'] + ' wins!!!')
        exit()
    return

'''Welcom Message'''
print(welcome_message)
'''Draws the empty board'''
board_drawer(board_numbered)
'''Starts the game'''
play()
