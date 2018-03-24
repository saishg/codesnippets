# https://www.careercup.com/question?id=6224114359468032


############## IMPLEMENTATION 1 ################

BOARD = [
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', 'B', 'B', ' ', ' '],
    [' ', 'B', 'W', 'W', 'B', ' '],
    [' ', 'B', 'W', 'B', ' ', ' '],
    [' ', ' ', 'B', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' '],
]

def get_color(row, col):
    if 0 <= row < len(BOARD) and 0 <= col < len(BOARD[0]):
        if BOARD[row][col] in ('W', 'B'):
            return BOARD[row][col]

    return ' '

def get_neighbors(row, col):
    return (get_color(row - 1, col),
            get_color(row + 1, col),
            get_color(row, col + 1),
            get_color(row, col - 1))

def check_surrounded():
    for row in range(len(BOARD)):
        for col in range(len(BOARD[0])):
            if get_color(row, col) == 'W':
                if ' ' in get_neighbors(row, col):
                    return False
    return True

############## IMPLEMENTATION 2 ################

def check_surrounded2():
    POSITIONS = {}
    WHITE_POSITIONS = []

    for row in range(len(BOARD)):
        for col in range(len(BOARD[0])):
            if BOARD[row][col] == 'B':
                POSITIONS[(row, col)] = 'B'
            elif BOARD[row][col] == 'W':
                POSITIONS[(row, col)] = 'W'
                WHITE_POSITIONS.append((row, col))

    for row, col in WHITE_POSITIONS:
        if (row - 1, col) not in POSITIONS or \
           (row + 1, col) not in POSITIONS or \
           (row, col + 1) not in POSITIONS or \
           (row, col - 1) not in POSITIONS:
            return False

    return True


if __name__ == '__main__':
    print check_surrounded()
    print check_surrounded2()

