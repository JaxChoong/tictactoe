"""
Tic Tac Toe Player
"""

import math
import copy
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == terminal(board):
        return None
    if board == initial_state():
        return X
    else:
        x_count = 0
        o_count = 0
        for row in board:
            for cell in row:
                if cell == X:
                    x_count += 1
                elif cell == O:
                    o_count += 1
        # If the number of Xs is equal to the number of Os, it's X's turn
        return X if x_count == o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    if board == terminal(board):
        return None
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                possible_actions.add((i, j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0][0]] != EMPTY:
        raise Exception("Invalid action")
    # make a copy of the board ( so original one not modified)
    new_board = copy.deepcopy(board)
    # decide which player's turn it is, then place their move on the board
    new_board[action[0][0]][action[0][1]] = player(board)
    return new_board
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return row[0]
    # check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[0][i]
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
