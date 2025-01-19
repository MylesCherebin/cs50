"""
Tic Tac Toe Player
"""

import math

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
    empty_spaces = 0
    for row in board:
        for col in range(len(row)):
            if row[col] == EMPTY:
                empty_spaces += 1
    
    if empty_spaces % 2 == 1:
        return X
    return O
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return actions
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Raise exception if the space is already taken
    if not action or (action[0] < 0 or action[0] > 2) or (action[1] < 0 or action[1] > 2):
        raise Exception
    i, j = action
    if board[i][j] != EMPTY:
        raise Exception
    
    copy = [[], [], []]
    for row in range(3):
        for col in range(3):
            copy[row].append(board[row][col])

    copy[i][j] = player(board)
    return copy

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows
    for row in board:
        if row[0] and row[0] == row[1] and row[0] == row[2]:
            return row[0]
    
    # Check columns
    for j in range(3):
        if board[0][j] and board[0][j] == board[1][j] and board[0][j] == board[2][j]:
            return board[0][j]
    
    # Check diagonals
    if board[0][0] and board[0][0] == board[2][2] and board[0][0] == board[1][1]:
        return board[0][0]
    
    if board[0][2] and board[0][2] == board[2][0] and board[0][2] == board[1][1]:
        return board[0][2]

    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Check if this board is a winner
    if winner(board):
        return True
    
    # Check if all cells are filled
    empty_spaces = 0
    for row in board:
        for col in range(len(row)):
            if row[col] == EMPTY:
                empty_spaces += 1
    
    if not empty_spaces:
        return True
    
    return False
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    won = winner(board)
    if won == X:
        return 1
    elif won == O:
        return -1
    
    return 0
    raise NotImplementedError


def max_value(board):
    v = -2
    if terminal(board):
        return utility(board)
    moves = actions(board)

    for action in moves:
        next_state = result(board, action)
        v = max(v, min_value(next_state))
    return v


def min_value(board):
    v = 2 
    if terminal(board):
        return utility(board)
    
    moves = actions(board)
    
    for action in moves:
        next_state = result(board, action)
        v = min(v, max_value(next_state))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board): 
        return None
    
    turn = player(board)
    moves = actions(board)
    act = moves.pop()
    optimal_move = act
    moves.add(act)

    if turn == X:
        options = []
        for action in moves:
            score = min_value(result(board, action))
            options.append((score, action))
        optimal_move = sorted(options)[-1][1]
    else:
        options = []
        for action in moves:
            score = max_value(result(board, action))
            options.append((score, action))
        print(options[0])
        optimal_move = sorted(options)[0][1]  
    return optimal_move
    raise NotImplementedError
