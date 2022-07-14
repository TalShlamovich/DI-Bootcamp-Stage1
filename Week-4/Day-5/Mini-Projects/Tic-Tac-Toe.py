from pickle import TRUE


player_moves = ['','','','','','','','','','']

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

# def make_move():
#     """place a marker"""

# def where_move():
#     """choose where to place a marker"""

# def is_full():
#     """check if the board is full"""

# def is_winner():
#     """check if player won"""

# def replay():
#     """restart the game"""