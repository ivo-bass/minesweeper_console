import csv

from random import randint

from utils.constants import VALID_SIZE_CHOICES, EMPTY_CELL, SIZES, MINE_CELL, COUNT_OF_MINES, NEIGHBOUR_CELLS_DISTANCE, \
    CLOSED_CELL, POSITIVE_ANSWERS
from utils.prints import SIZE_ERROR_MSG, CREATE_PLAYER_PROMPT, BOARD_SIZE_PROMPT


class Player:
    def __init__(self, name):
        self.name = name
        self.time = 0
        self.wins = 0
        self.losses = 0
        self.best_time = 0

    def give_best_time(self):
        if self.best_time < self.time:
            self.best_time = self.time
        return self.best_time


def create_player_instance():
    return Player(input(CREATE_PLAYER_PROMPT))


def is_valid_choice_for_size(string):
    return string in VALID_SIZE_CHOICES


def choose_board_size():
    while True:
        choice_for_size = input(BOARD_SIZE_PROMPT)
        if is_valid_choice_for_size(choice_for_size):
            if choice_for_size == '1':
                return SIZES[choice_for_size]
            else:
                print('This size feature is not available yet.')
        print(SIZE_ERROR_MSG)


def create_new_empty_board(size):
    return [[CLOSED_CELL for _ in range(size)] for _ in range(size)]


def add_mines_to_board(board):
    size = len(board)
    for _ in range(COUNT_OF_MINES):
        board[randint(0, size-1)][randint(0, size-1)] = MINE_CELL


def is_in_range(index, size):
    return 0 <= index < size


def check_for_mine(board, row, col):
    cell_to_observe = board[row][col]
    if cell_to_observe == MINE_CELL:
        return 1
    return 0


def count_neighbours_mines(board, row_index, col_index):
    count_mines = 0
    board_size = len(board)
    for neighbour_distance in NEIGHBOUR_CELLS_DISTANCE:
        row_distance, col_distance = neighbour_distance
        observed_row = row_index + row_distance
        observed_col = col_index + col_distance
        if is_in_range(observed_row, board_size) and is_in_range(observed_col, board_size):
            count_mines += check_for_mine(board, observed_row, observed_col)
    return count_mines


def draw_numbers_on_board(board, row_i, col_i):
    number = count_neighbours_mines(board, row_i, col_i)
    if number:
        board[row_i][col_i] = number
    else:
        board[row_i][col_i] = EMPTY_CELL


def add_numbers_to_board(board):
    for row_i in range(len(board)):
        for col_i in range(len(board)):
            current_cell = board[row_i][col_i]
            if current_cell == CLOSED_CELL:
                draw_numbers_on_board(board, row_i, col_i)


def create_boards():
    size = choose_board_size()
    play_board = create_new_empty_board(size)
    reference_board = create_new_empty_board(size)
    add_mines_to_board(reference_board)
    add_numbers_to_board(reference_board)
    return play_board, reference_board


def ask_for_a_game():
    prompt = input('Do you want to play another game? [y/n]: ').lower()
    if prompt in POSITIVE_ANSWERS:
        return True
