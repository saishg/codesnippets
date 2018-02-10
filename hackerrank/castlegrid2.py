ROWS = 0
COLS = 0
GRID = []
GRID_STR = []
QUEUE = []
START = (0, 0)
FINISH = (0, 0)


class Cell:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.blocked = False
        self.distance = 0
        self.visited = False

        if value != '.':
            self.blocked = True

    def update(self, distance):
        if self.blocked:
            return False
        elif not self.visited:
            self.visited = True
            self.distance = distance
            QUEUE.append(self)
            return True

    def is_finish(self):
        return (self.row, self.col) == FINISH

    def get_neighbors(self):
        row, col = self.row, self.col
        while True:
            row += 1
            if not get_cell(row, col).update(self.distance + 1):
                break

        row, col = self.row, self.col
        while True:
            row -= 1
            if not get_cell(row, col).update(self.distance + 1):
                break

        row, col = self.row, self.col
        while True:
            col -= 1
            if not get_cell(row, col).update(self.distance + 1):
                break

        row, col = self.row, self.col
        while True:
            col += 1
            if not get_cell(row, col).update(self.distance + 1):
                break


    def __repr__(self):
        if self.blocked:
            return "-"
        else:
            return "{}".format(self.distance)

def get_cell(row, col):
    if 0 <= row < ROWS and 0 <= col < COLS:
        return GRID[row][col]
    else:
        return Cell(-1, -1, ' ')


def print_grid():
    print "-------------------"
    for row in GRID:
        print row

def traverse():
    while QUEUE:
       cell = QUEUE.pop(0) 
       if cell.is_finish():
           return cell.distance
       cell.get_neighbors()


def read_input():
    global ROWS, COLS, GRID_STR, GRID, START, FINISH
    N = int(raw_input())
    ROWS = N
    COLS = N

    for row in range(ROWS):
        GRID_STR.append(raw_input())

    coords = map(int, raw_input().split())
    START = coords[0], coords[1]
    FINISH = coords[2], coords[3]

    for row in range(ROWS):
        for col in range(ROWS):
            if col == 0:
                GRID.append([])
            GRID[row].append(Cell(row, col, GRID_STR[row][col]))



if __name__ == '__main__':
    read_input()
#    print_grid()
    QUEUE.append(GRID[START[0]][START[1]])
    print traverse()
#    print_grid()
