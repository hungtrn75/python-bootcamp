import os
import random

# Global variables
theBoard = [' ']*10  # a list of empty spaces
available = [str(num) for num in range(0, 10)]  # a list comprehension
players = [0, 'X', 'O']   # note that players[1] == 'X' and players[-1] == 'O'


def display_board(a, b):
    print(f'Available   TIC-TAC-TOE\n  moves\n\n  {a[7]}|{a[8]}|{a[9]}        {b[7]}|{b[8]}|{b[9]}\n  -----        -----\n  {a[4]}|{a[5]}|{a[6]}        {b[4]}|{b[5]}|{b[6]}\n  -----        -----\n  {a[1]}|{a[2]}|{a[3]}        {b[1]}|{b[2]}|{b[3]}\n')


# display_board(available, theBoard)
def place_marker(available, board, marker, position):
    available[position] = ' '
    board[position] = marker

# check win


def win_check(board, marker):
    mark = [marker]*3
    return (board[7:10] == mark or
            board[1:4] == mark or
            board[4:7] == mark or
            board[1::3] == mark or
            board[2::3] == mark or
            board[3::3] == mark or
            board[1::4] == mark or
            board[3::2] == mark.append(marker)
            )


# print(win_check(theBoard, 'X'))

def random_player():
    return random.choice((-1, 1))


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    return ' ' not in board[1:]


def player_choice(board, player):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        try:
            position = int(
                input('Player %s, choose your next position: (1-9) ' % (player)))
        except:
            print("I'm sorry, please try again.")
    return position


def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


while True:
    os.system('cls')
    print('Welcome to Tic Tac Toe')

    toggle = random_player()
    player = players[toggle]
    print('For this round, Player %s will go first!' % (player))

    game_on = True
    input('Hit Enter to continue')
    while game_on:
        display_board(available, theBoard)
        position = player_choice(theBoard, player)
        place_marker(available, theBoard, player, position)

        if win_check(theBoard, player):
            display_board(available, theBoard)
            print('Congratulations! Player '+player+' wins!')
            game_on = False
        else:
            if full_board_check(theBoard):
                display_board(available, theBoard)
                print('The game is a draw!')
                break
            else:
                toggle *= -1
                player = players[toggle]
                os.system('cls')

    # reset the board and available moves list
    theBoard = [' '] * 10
    available = [str(num) for num in range(0, 10)]

    if not replay():
        break
