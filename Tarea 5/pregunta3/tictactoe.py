"""
Tic Tac Toe Player
"""

import math
import copy

X = "-"
O = "|"
B = "+"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return {"board": [[EMPTY, EMPTY, EMPTY],
                      [EMPTY, EMPTY, EMPTY],
                      [EMPTY, EMPTY, EMPTY]], "last_action": {"pos": None, "player": None}}


def player(state):
    """
    Returns player who has the next turn on a board.
    """
    # Count the empty spaces on the board, i.e., available movements.
    last_player = state["last_action"]["player"]

    # If count is a multiple of two, it'll be O's turn. Otherwise, it is X's turn.
    if last_player == X:
        return O
    return X


def valid_action(state, current_action):
    """
    Check if current action is valid in the considered state.
    """
    board = state["board"]
    last_action = state["last_action"]
    return current_action != last_action["pos"] and board[current_action[0]][current_action[1]] is not B and board[current_action[0]][current_action[1]] != player(state)


def actions(state):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    board = state["board"]
    available_actions = set()
    # Add empty spaces to the set of available actions on the board (on that state).
    for i in range(len(board)):
        for j in range(len(board[i])):
            if valid_action(state, (i, j)):
                available_actions.add((i, j))
    return available_actions


def result(state, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board = state["board"]
    if not valid_action(state, (action[0], action[1])):
        raise "Not valid action"
    # Copy the original board (state) so the action is applied in the copy, creating a new state.
    result_board = copy.deepcopy(board)
    current_player = player(state)
    result_board[action[0]][action[1]] = current_player if result_board[action[0]][action[1]] is EMPTY else B
    return {"board": result_board, "last_action": {"pos": (action[0], action[1]), "player": current_player }}


def winner(state):
    """
    Returns the winner of the game, if there is one.
    """
    board = state["board"]
    last_player = state["last_action"]["player"]

    # Check if someone wins horizontally or vertically. Return winner.
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] == B:
            return last_player
        elif board[0][i] == board[1][i] == board[2][i] == B:
            return last_player
    # Check if someone wins diagonally. Return winner.
    if board[0][0] == board[1][1] == board[2][2] == B or board[0][2] == board[1][1] == board[2][0] == B:
        return last_player
    # There's no winner, return None.
    return None


def terminal(state):
    """
    Returns True if game is over, False otherwise.
    """
    # If someone wins, then that is a terminal state.
    if winner(state) is not None:
        return True
    # If there aren't actions left, it is a terminal state.
    return (len(actions(state)) == 0)


def utility(state):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Assign a number to the board according to the winner.
    win = winner(state)
    if win == X:
        return 1
    elif win == O:
        return -1
    return 0


def minimax(state):
    """
    Returns the optimal action for the current player on the board.
    """
    # X tries to maximize. O tries to minimize.
    if player(state) == X:
        maxv = max_value(state, -math.inf, math.inf)
        return maxv[1]
    else:
        minv = min_value(state, -math.inf, math.inf)
        return minv[1]


def max_value(state, alpha, beta):
    """
    Tries to maximize the value. Returns a tuple with the maximum value and the best action to achieve it.
    """
    if terminal(state):
        return (utility(state), None)
    v = -math.inf
    best_action = None
    for action in actions(state):
        v_max = min_value(result(state, action), alpha, beta)[0]
        if v < v_max:
            v = v_max
            best_action = action
        if v >= beta:
            return (v, best_action)
        if v > alpha:
            alpha = v
    return (v, best_action)


def min_value(state, alpha, beta):
    """
    Tries to minimize the value. Returns a tuple with the maximum value and the best action to achieve it.
    """
    if terminal(state):
        return (utility(state), None)
    v = math.inf
    best_action = None
    for action in actions(state):
        v_min = max_value(result(state, action), alpha, beta)[0]
        if v > v_min:
            v = v_min
            best_action = action
        if v <= alpha:
            return (v, best_action)
        if v < beta:
            beta = v
    return (v, best_action)
