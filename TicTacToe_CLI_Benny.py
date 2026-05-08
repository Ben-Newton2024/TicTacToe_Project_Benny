# Tic tac toe project

# needs
# Working tic-tac-toe logic to play the game
# two player game
# cli


def board_creation():
    """ Create the board for the game to be played into """
    board = [[(str(x) + "," + str(y)) for x in range(3)] for y in range(3)]
    return board


def user_turn_inputs():
    """ CLI user inputs into the game, takes two user inputs as coords """
    x = int(input("please enter an X coord: "))
    y = int(input("please enter an Y coord: "))
    coords = (x, y)
    return coords


def check_winner(board):
    """ check for winners on vertical, horizontal and diagonal axis """
    for letter_check in [" X ", " O "]:
        for i in range(3):
            # Horizontal check
            if board[i][0] == letter_check and board[i][1] == letter_check and board[i][2] == letter_check:
                print(letter_check, " is the winner")
                return True
            # Vertical check
            elif board[0][i] == letter_check and board[1][i] == letter_check and board[2][i] == letter_check:
                print(letter_check, " is the winner")
                return True
            # Diagonal check
            elif board[0][0] == letter_check and board[1][1] == letter_check and board[2][2] == letter_check:
                print(letter_check, " is the winner")
                return True
            if board[0][2] == letter_check and board[1][1] == letter_check and board[2][0] == letter_check:
                print(letter_check, " is the winner")
                return True
    return False


def check_player_move(board, coord):
    """ Check if the players move is valid """
    if board[coord[1]][coord[0]] == " O ":
        return "fail_O"
    elif board[coord[1]][coord[0]] == " X ":
        return "fail_X"
    else:
        return "success"


def game_turn(board, player_id, coord):
    """ takes a turn on the users game """

    if player_id == " O ":
        player_id = " X "
    else:
        player_id = " O "
    # set the players move to the grid
    board[coord[1]][coord[0]] = player_id
    rtn = (board, player_id)
    return rtn


def main_cli():
    """ Main for the game loop and calling of game logic functions """
    # create the board
    board = board_creation()
    for i in range(3):
        print(board[i])
    # boolean flag for knowing whose turn it is
    player_id = " O "

    # loop for the game
    while not check_winner(board):
        # user input
        # check for valid move
        # if yes play game move
        # if not require input again
        co_ords = user_turn_inputs()
        move_check = check_player_move(board, co_ords)
        if move_check == "success":
            rtn = game_turn(board, player_id, co_ords)
            board = rtn[0]
            player_id = rtn[1]
            for i in range(3):
                print(board[i])
        elif move_check == "fail_O":
            print("move not possible, there is a O there")
        elif move_check == "fail_X":
            print("move not possible, there is a X there")
        else:
            print("Error")

main_cli()