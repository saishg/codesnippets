"""
https://www.hackerrank.com/challenges/crossword-puzzle

INPUT:
+-++++++++
+-++++++++
+-++++++++
+-----++++
+-+++-++++
+-+++-++++
+++++-++++
++------++
+++++-++++
+++++-++++
LONDON;DELHI;ICELAND;ANKARA

"""

GRID = []

WORDS = []

BLANKS = []

class Blank:
    def __init__(self, start, end, length, vertical):
        self.start = start
        self.end = end
        self.filled_end = start
        self.length = length
        self.vertical = vertical
        BLANKS.append(self)

    def fill(self, value):
        if len(value) != self.length:
            self.filled_end = self.start
            return False

        if self.vertical:
            start_row, col = self.start
            end_row, col = self.end
            i = 0
            for row in range(start_row, end_row):
                if GRID[row][col] not in ('-', value[i]):
                    self.filled_end = (row, col)
                    return False
                GRID[row] = GRID[row][:col] + value[i] + GRID[row][col+1:]
                i += 1
        else:
            row, start_col = self.start
            row, end_col = self.end
            i = 0
            for col in range(start_col, end_col):
                if GRID[row][col] not in ('-', value[i]):
                    self.filled_end = (row, col)
                    return False
                GRID[row] = GRID[row][:col] + value[i] + GRID[row][col+1:]
                i += 1

        self.filled_end = self.end
        return True

    def unfill(self):
        if self.vertical:
            start_row, col = self.start
            end_row, col = self.filled_end
            for row in range(start_row, end_row):
                GRID[row] = GRID[row][:col] + '-' + GRID[row][col+1:]
        else:
            row, start_col = self.start
            row, end_col = self.filled_end
            for col in range(start_col, end_col):
                GRID[row] = GRID[row][:col] + '-' + GRID[row][col+1:]

    def __repr__(self):
        return "{}->{}".format(self.start, self.end)

def within_bounds(row, col):
    return 0 <= row < len(GRID) and 0 <= col < len(GRID[0])

def get_value(row, col):
    if within_bounds(row, col):
        return GRID[row][col]
    else:
        return '+'

def is_vert_start(row, col):
    if not within_bounds(row - 1, col) or GRID[row - 1][col] != '-':
        return True
    else:
        return False

def is_horz_start(row, col):
    if not within_bounds(row, col - 1) or GRID[row][col - 1] != '-':
        return True
    else:
        return False


def check_vert(row, col):
    start = (row, col)
    length = 0
    while get_value(row, col) == '-':
        row += 1
        length += 1

    if length > 1:
        end = (row, col)
        Blank(start, end, length, vertical=True)

def check_horz(row, col):
    start = (row, col)
    length = 0
    while get_value(row, col) == '-':
        col += 1
        length += 1

    if length > 1:
        end = (row, col)
        Blank(start, end, length, vertical=False)

def parse_grid():
    for row in range(len(GRID)):
        for col in range(len(GRID[0])):
            if GRID[row][col] == '-':
                if is_vert_start(row, col):
                    check_vert(row, col)
                if is_horz_start(row, col):
                    check_horz(row, col)

def print_grid():
    for line in GRID:
        print line
    print

USED = None

def recurse(blank_index=0):
    if len(BLANKS) == blank_index:
        print_grid()
        return True

    for word_index in range(len(WORDS)):
        if not USED[word_index]:
            if BLANKS[blank_index].fill(WORDS[word_index]):
                USED[word_index] = True
                if recurse(blank_index + 1):
                    return True
                USED[word_index] = False
            BLANKS[blank_index].unfill()
    return False

def read_input():
    global USED
    for i in range(10):
        GRID.append(raw_input())
    WORDS.extend(raw_input().split(';'))
    USED = [False] * len(WORDS)


if __name__ == "__main__":
    read_input()
    parse_grid()
    recurse()
