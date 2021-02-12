from utils.constants import SCORES_FILE_PATH

CREATE_PLAYER_PROMPT = 'Enter your name: '
BOARD_SIZE_PROMPT = 'Choose a board size:\n    1: 8x8\n    2: 16x16\n'
CHOOSE_CELL_PROMPT = 'Enter coordinates for cell to open [xy]: '
CHOOSE_ACTION_PROMPT = 'To open cell enter "o". To mark mine enter "m": '

SIZE_ERROR_MSG = 'Invalid size choice. Try again.'
CELL_ERROR_MSG = 'Invalid cell. Try again.'
ACTION_ERROR_MSG = 'Invalid action. Try again.'


def print_welcome():
    print('Welcome to Minesweeper Console Edition!')
    print()


def print_goodbye(player):
    print(f'Goodbye {player.name}!')


def show_board(matrix):
    print('   ' + ' '.join(map(str, [i+1 for i in range(len(matrix))])))
    for row_i in range(len(matrix)):
        print(str(row_i+1) + ' |' + '|'.join(map(str, matrix[row_i])) + '| ' + str(row_i+1))
    print('   ' + ' '.join(map(str, [i+1 for i in range(len(matrix))])))


def print_total_results(player):
    print()
    print(f'You have {player.wins} wins and {player.losses} losses.')
    print()


def print_loss(player, x, y):
    print()
    print(f'{player.name} hit a mine at cell ({x + 1},{y + 1})!')
    print('GAME OVER...')
    print_total_results(player)


def print_win(player, best_time):
    print()
    print(f'{player.name.upper()} YOU WON!!!')
    print(f'Your time is: {player.time:.2f} seconds.')
    if player.time == player.best_time:
        print(f'You have new best time: {best_time:.2f} seconds!')
    else:
        print(f'Your best time is {best_time:.2f} seconds.')
    print_total_results(player)


def print_result_to_file(player):
    with open(SCORES_FILE_PATH, 'a') as file:
        result = f'{player.name},{player.wins}:{player.losses},{player.best_time:.2f}'
        file.write(result + '\n')
