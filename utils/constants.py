import os


OPEN = 'o'
MARK = 'm'
VALID_ACTIONS = (OPEN, MARK)
VALID_SIZE_CHOICES = ('1', '2')
SIZES = {'1': 8, '2': 16}
POSITIVE_ANSWERS = ('y', 'yes', 'ъ', 'ъес')

EMPTY_CELL = ' '
CLOSED_CELL = u'\u2592'
MINE_CELL = '*'
EXPLOSION = ' ' + u'\u0489'
MARKED_CELL = u'\u2691'
COUNT_OF_MINES = 12


NEIGHBOUR_CELLS_DISTANCE = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
)


BASE_PATH = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_PATH, 'db')
SCORES_FILE_PATH = os.path.join(DB_PATH, 'scores.txt')
