from pickle import TRUE

from pyparsing import empty


player_moves = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def set_board():
    """set up the board"""
    empty_board = """
___________________
|     |     |     |
|  1  |  2  |  3  |
|     |     |     |
|-----------------|
|     |     |     |
|  4  |  5  |  6  |
|     |     |     |
|-----------------|
|     |     |     |
|  7  |  8  |  9  |
|     |     |     |
|-----------------|
"""

    for cell in range(1,10):
        if player_moves[cell] == 'O' or player_moves[cell] == 'X':
            empty_board = empty_board.replace(str(cell), player_moves[cell])
        else:
            empty_board = empty_board.replace(str(cell), ' ')
    print(empty_board)
# set_board()


def choose_x_or_o():
    """choosing a marker"""
    player1 = input("Choose X or O: ")
    while True:
        if player1.upper() == "X":
            player2 = "O"
            return player1.upper(), player2
        elif player1.upper() == "O":
            player2 = "X"
            return player1.upper(), player2
        else: 
            player1 = input("Choose X or O: ")

def make_move(position, marker) -> list:
    """place a marker"""
    player_moves[position] = marker
    

def where_move(player):
    """choose where to place a marker"""
    position = int(input("Select the cell to make a move: "))
    while not check_for_empty(player_moves, position):
        position = input("This cell already has a marker. Choose another: ")
    make_move(position, marker=player)


def check_for_empty(player_moves: list, position):
    """check if the chosen spot is empty. Return true if empty"""
    return player_moves[position] == ' '

def is_full(player_moves: list):
    """check if the board is full"""
    for cell in player_moves:
        counter = 0
        if cell != ' ':
            counter += 1
        if counter == 9:
            return True
        else:
            return False

def is_winner():
    """check if player won"""
    if player_moves [1] == player_moves[2] == player_moves[3]:
        return True
    if player_moves [4] == player_moves[5] == player_moves[6]:
        return True
    if player_moves [7] == player_moves[8] == player_moves[9]:
        return True
    if player_moves [1] == player_moves[4] == player_moves[7]:
        return True
    if player_moves [2] == player_moves[5] == player_moves[8]:
        return True
    if player_moves [3] == player_moves[6] == player_moves[9]:
        return True
    if player_moves [1] == player_moves[5] == player_moves[9]:
        return True
    if player_moves [3] == player_moves[5] == player_moves[7]:
        return True

    return False


# def replay():
#     """restart the game"""

# set_board()
# player_x, player_o = choose_x_or_o()


# # print(player_x)
# # print(player_o)

# where_move(player_x)

# print(player_moves)
# set_board()
