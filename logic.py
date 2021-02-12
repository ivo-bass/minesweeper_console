import time

from utils.constants import EMPTY_CELL, MINE_CELL, EXPLOSION, VALID_ACTIONS, OPEN, MARK, MARKED_CELL, CLOSED_CELL
from utils.prints import CHOOSE_CELL_PROMPT, CELL_ERROR_MSG, show_board, CHOOSE_ACTION_PROMPT, ACTION_ERROR_MSG, \
    print_loss, print_win

DELTAS = [
    (0, -1),  # left
    (-1, -1),  # up left
    (-1, 0),  # up
    (-1, -1),  # up right
    (0, 1),  # right
    (1, 1),  # down right
    (1, 0),  # down
    (1, -1),  # down left
]


def is_valid_input(choice):
    return len(choice) == 2 and all([s.isdigit() for s in choice])


def is_valid_cell(board, x, y):
    return 0 <= x < len(board) and 0 <= y < len(board)


def choose_cell(board):
    while True:
        choice = input(CHOOSE_CELL_PROMPT)
        if is_valid_input(choice):
            x, y = [int(d) - 1 for d in choice]
            if is_valid_cell(board, x, y):
                return x, y
        print(CELL_ERROR_MSG)


def is_valid_action(action):
    return action in VALID_ACTIONS


def choose_action():
    while True:
        action = input(CHOOSE_ACTION_PROMPT).lower()
        if is_valid_action(action):
            return action
        print(ACTION_ERROR_MSG)


def is_valid_value(x, max_x):
    return 0 <= x < max_x


def reveal_all_empty_cells(play_board, reference_board, x, y):
    reveal_cell(play_board, reference_board, x, y)
    if not reference_board[x][y] == EMPTY_CELL:
        return
    for delta in DELTAS:
        delta_row, delta_col = delta
        next_row = x + delta_row
        next_col = y + delta_col
        if not is_valid_value(next_row, len(reference_board)) or not is_valid_value(next_col, len(reference_board)):
            continue
        if not play_board[next_row][next_col] == EMPTY_CELL:
            reveal_all_empty_cells(play_board, reference_board, next_row, next_col)


def reveal_board(play_board, reference_board, x, y):
    for row in range(len(play_board)):
        for col in range(len(play_board)):
            if play_board[row][col] == CLOSED_CELL:
                play_board[row][col] = reference_board[row][col]
    play_board[x][y] = EXPLOSION


def reveal_cell(play_board, reference_board, x, y):
    play_board[x][y] = reference_board[x][y]


def activate_cell(play_board, reference_board, x, y):
    reference_cell = reference_board[x][y]
    if reference_cell == EMPTY_CELL:
        reveal_all_empty_cells(play_board, reference_board, x, y)
        return False
    elif reference_cell == MINE_CELL:
        reveal_board(play_board, reference_board, x, y)
        return True
    else:
        reveal_cell(play_board, reference_board, x, y)
        return False


def mark_mine(play_board, x, y):
    play_board[x][y] = MARKED_CELL


def the_game_is_over(player, x, y):
    player.losses += 1
    print_loss(player, x, y)


def you_win(player, start_time):
    player.time = time.time() - start_time
    player.wins += 1
    best_time = player.give_best_time()
    print_win(player, best_time)


def is_win(play_board):
    for row in play_board:
        for cell in row:
            if cell == CLOSED_CELL:
                return False
    return True


def play(player, play_board, reference_board):
    start_time = time.time()
    game_over = False
    while True:
        x, y = choose_cell(play_board)
        action = choose_action()
        if action == OPEN:
            game_over = activate_cell(play_board, reference_board, x, y)
        elif action == MARK:
            mark_mine(play_board, x, y)
        show_board(play_board)
        if game_over:
            the_game_is_over(player, x, y)
            break
        if is_win(play_board):
            you_win(player, start_time)
            break
