# print the board
print("Welcome players, player X can choose a spot!")
board = [" ", " ", " ", " ",
         " ", " ", " ", " ",
         " ", " ", " ", " ",
         " ", " ", " ", " ",]
current_player = "X"
winner = None
game_running = True


def print_board(board):
    print("\n      |      |      |      ")
    print(f"   {board[0]}  |   {board[1]}  |   {board[2]}  |   {board[3]}")
    print("______|______|______|______")
    print("      |      |      |      ")
    print(f"   {board[4]}  |   {board[5]}  |   {board[6]}  |   {board[7]}")
    print("______|______|______|______")
    print("      |      |      |      ")
    print(f"   {board[8]}  |   {board[9]}  |   {board[10]}  |   {board[11]}")
    print("______|______|______|______")
    print("      |      |      |      ")
    print(f"   {board[12]}  |   {board[13]}  |   {board[14]}  |   {board[15]}")
    print("      |      |      |      ")


# take player input

def player_input(board):
    global current_player
    while True:  # Keep asking until valid input
        inp = int(input(f"Player {current_player}, enter a number 1-16: "))
        if inp >= 1 and inp <= 16:
            if board[inp - 1] == " ":
                board[inp - 1] = current_player
                return True  # Valid move made
            else:
                print("This spot is already taken! Try again.")
        else:
            print("Please enter a number between 1 and 16.")


def check_horizontal(board):
    global winner
    if (board[0] == board[1] == board[2] and board[1] != " ") or (board[1] == board[2] == board[3] and board[1] != " "):
        winner = board[1]
        return True
    elif (board[4] == board[5] == board[6] and board[5] != " ") or (board[5] == board[6] == board[7] and board[5] != " "):
        winner = board[5]
        return True
    elif (board[8] == board[9] == board[10] and board[9] != " ") or (board[9] == board[10] == board[11] and board[9] != " "):
        winner = board[9]
        return True
    elif (board[12] == board[13] == board[14] and  board[13] != " ") or (board[13] == board[14] == board[15] and  board[13] != " "):
        winner = board[13]
        return True


def check_vertical(board):
    global winner
    if (board[0] == board[4] == board[8] and board[4] != " ") or (board[4] == board[8] == board[12] and board[4] != " "):
        winner = board[4]
        return True
    elif (board[1] == board[5] == board[9] and board[5] != " ") or (board[5] == board[9] == board[13] and board[5] != " "):
        winner = board[5]
        return True
    elif (board[2] == board[6] == board[10] and board[6] != " ") or (board[6] == board[10] == board[14] and board[6] != " "):
        winner = board[6]
        return True
    elif (board[3] == board[7] == board[11] and board[7] != " ") or (board[7] == board[11] == board[15] and board[7] != " "):
        winner = board[7]
        return True



def check_diagonal(board):
    global winner
    if (board[0] == board[5] == board[10] and board[5] != " ") or (board[5] == board[10] == board[15] and board[5] != " "):
        winner = board[5]
        return True
    elif (board[4] == board[6] == board[9] and board[6] != " ") or (board[6] == board[9] == board[12] and board[6] != " "):
        winner = board[6]
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
    player_input(board)
    check_win()
    check_tie()
    switch_player()