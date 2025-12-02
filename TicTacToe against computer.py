# choose between player against another player or against a computer

import random
print("Welcome")

#choose 1 or 2 player game

while True:
    mode_input = input("Type '1' for 2-player mode or '2' to play against the computer: ")

    if mode_input == "1":
        mode = "1"
        break
    elif mode_input == "2":
        mode = "2"
        break
    else:
        print("Invalid choice! Please enter '1' or '2' only.\n")

# print the board

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]
current_player = "X"
winner = None
game_running = True


def print_board(board):
    print("\n      |      |      ")
    print(f"   {board[0]}  |   {board[1]}  |   {board[2]}   ")
    print("______|______|______")
    print("      |      |      ")
    print(f"   {board[3]}  |   {board[4]}  |   {board[5]}   ")
    print("______|______|______")
    print("      |      |      ")
    print(f"   {board[6]}  |   {board[7]}  |   {board[8]}   ")
    print("      |      |      ")

# computer move function

def computer_move(board):
    print("\nComputer is choosing a spot...")

    empty_positions = []
    for i in range(len(board)):
        if board[i] == " ":
            empty_positions.append(i)

    choice = random.choice(empty_positions)

    board[choice] = "O"
    print(f"Computer chose position {choice + 1}.")


# take player input

def player_input(board):
    global current_player
    while True:  # Keep asking until valid input
        inp = int(input(f"Player {current_player}, enter a number 1-9: "))
        if inp >= 1 and inp <= 9:
            if board[inp - 1] == " ":
                board[inp - 1] = current_player
                return True  # Valid move made
            else:
                print("This spot is already taken! Try again.")
        else:
            print("Please enter a number between 1 and 9.")


def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != " ":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != " ":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != " ":
        winner = board[6]
        return True


def check_vertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != " ":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != " ":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != " ":
        winner = board[2]
        return True


def check_diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != " ":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != " ":
        winner = board[2]
        return True


def check_tie():
    global game_running
    if " " not in board:
        print_board(board)
        print("It is a tie")
        game_running = False


def check_win():
    global game_running
    if check_horizontal(board) or check_vertical(board) or check_diagonal(board):
        print_board(board)
        print(f"The winner is {winner}!")
        game_running = False


def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


while game_running:
    print_board(board)

    if mode == "2" and current_player == "O":
        computer_move(board)
    else:
        player_input(board)
    check_win()
    check_tie()

    switch_player()
