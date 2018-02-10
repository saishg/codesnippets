"""
https://www.hackerrank.com/challenges/castle-on-the-grid/problem

Sample Input:
3
.X.
.X.
...
0 0 0 2

Sample Output:
3
"""

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
            print "update {},{} to {}".format(self.row, self.col, distance)
            self.visited = True
            self.distance = distance
            QUEUE.append(self)
            return True
        else:
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
        print "---"


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
    print_grid()



"""
75
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
..........................................................................X
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X
X.......................................................................X.X
X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X
X.X...................................................................X.X.X
X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X
X.X.X...............................................................X.X.X.X
X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X
X.X.X.X...........................................................X.X.X.X.X
X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X
X.X.X.X.X.......................................................X.X.X.X.X.X
X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X
X.X.X.X.X.X...................................................X.X.X.X.X.X.X
X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X
X.X.X.X.X.X.X...............................................X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X...........................................X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.......................................X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X...................................X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X...............................X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X...........................X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.......................X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X...................X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X...............X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X...........X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XXXXXXXXX.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.......X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XXXXX.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X...X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XXX.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.....X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XXXXXXX.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.........X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XXXXXXXXXXX.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.............X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.X.................X.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.X.....................X.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.X.........................X.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.X.............................X.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.X.................................X.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.X.....................................X.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.X.........................................X.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.X.............................................X.X.X.X.X.X.X.X
X.X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X.X
X.X.X.X.X.X.X.................................................X.X.X.X.X.X.X
X.X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X.X
X.X.X.X.X.X.....................................................X.X.X.X.X.X
X.X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X.X
X.X.X.X.X.........................................................X.X.X.X.X
X.X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X.X
X.X.X.X.............................................................X.X.X.X
X.X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X.X
X.X.X.................................................................X.X.X
X.X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X.X
X.X.....................................................................X.X
X.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX.X
X.........................................................................X
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
1 0 37 37

Output:
73
"""


"""
70
.X..X.X..X..X.......XX..XX....X.X...X........X.....XX.X.X...X.X...X..X
...X.....XX.........XX......X.X.......X......X..XX.X..X..X.....X.X....
............X.......X........X..X.X......X.......X...X.X.....X.X...X..
.........X....XX.X.X.X......X..X......X.....X.........X..X.......XX...
.....X.......X.X.....XX.....X.XXX.........X.....X.X....XX......XX.....
..X....X..........................X...X.........XX.....X..............
......X.......X...XX.....X.X....X.......X.............X........X.X....
...X.X.XX.XX...X............XX...X.....X..X..X....X.........X.........
X.XX........X..........XX..X.X..X.XX.XXX..X........X..X.....XX......X.
......X..XXX.......X..XX.XX...........X.....XX..X..X.X......X.X...X...
X........X.X....X..X..................XX......X..X.......X.....X..X...
...X......X....XX.......X.....X...........X..X....X.....XXX...X...X.X.
......X..X....X.XXX.X.....X..X....XX.....X....X.....X...X...........X.
....X..X.X...XX..X.X.X..X.....X......X..X......X.X.X.X......X......X..
..X..............X...X.........X........X...........X..X.X......X....X
.X....X..X......X.........X.....XX....XX............XX..X...X...X.....
...........X....X.X...XX...X......X...............X....XX..........X..
.X..X..XX..X...X.....XX...XX...........X.....X..XXX.........XX..X....X
.XX........XX.XX..........XX............X.........X.XXXX.X.X.........X
.....X........X......X.............X.......X............X....X...X..X.
X..X.X..X...........XX..X.....X......X...XXX........XX...........X....
..X....X.XX.X.....X..X..X...........X......X..........X.....X.......X.
..........X.X...X.....X....XX.XX.......XX...X.............XXX..X..X..X
X.....X....XX...X.X...X.X.X..X.X..X....X..X..XXX...X...........X.X.X..
...XX.X....X...X.....XX...X.....X..XXX.......XX......X....XX......X.XX
X..X......X.....X......X.X...X............X.X..........X.X.X..X......X
..X....X..X.X....XX....X.XXX..X.XX.....X........X..X...X...X.X......X.
.......X...............XX..........X...X......XX...X.X........X.......
XXX....X.....X..X.....X.X.....XX..X.......X..X.....XX.......X..X.....X
.......X......X.......X..X.......X.........X...X.........X...X.....XXX
...X..X....X....X.X..XX......X.......X............X...................
.X.....X............X...............X.....X.X...X...X.XXX..X....X..XXX
..........X........X...........XX..........X..............X.....XX.X..
.X...............XX..X.X......................X..X...X......X.....X...
XX..X.X..XXXX..X..........XX..XX..X.............X................XX...
......X.XX..X...............X.X....X....X......X.....X..XX............
..X.X..X..X......X..X................X......X...X......X.XX...X..X....
.........X............X......X......XX.X..................X.....X.....
X..X....X...........X.....XX..X.......XXX.....XXX.......X....X.....X.X
XX..............XXX....X.X......XX..........X....X.....X......X.......
.......X.XX.......X......X..XXX.............X.......XX.....X.XX.......
..X.X.....XXX.X.......X.X.........X..X...X...X..X.....X.....XX.......X
..XX........XX....X..XX..X...XXX.................X..X...........X.....
...X........X..X.....X......X.X...XXX..X..XX.X..X...X........X.XXXX...
...X.X....X.....X.X.......X..............X...X.X.XX...X...XX.X.......X
......X...........X.......X.....XXXX...........X.X.XX......X...X......
....X......X......XXX..XX.X.......X.............X.......X.........X..X
..X..X..X......X.....X............XX....X..........X......X..X..X.X...
X.........X..X..XX........X.X.X......................X.X....X.....X...
.....X.X...X.X..X...X...XX...X...X............X..............X...X....
......................X....X...X....X.X..............XX.....X.........
.................X..X.....X.....XX......X.......X......X.........X.X..
...........X..X...X.....X..X.............X............X..X..XX.X......
X..........X.X..X..X..........X.XX.............X...X.XX........X......
..XX.XX.....X.....X..X.....X.....X...X...........X..X..X....X.........
..X.XX...X.X....X.X....X..X.X...X..X.........X..X.....................
............X...................X....X.X......X.XX..X...X....X..XX.XX.
...X..X.X....X..............X..X.....X.X.........X..........X.......X.
..X...........................X......X.X...X........X.................
.........X..X...............X...........X..X.X......X.................
..XX.............XX.X.........X....XX........X..X...X........X.....X..
.............X.X....X.X...X...X.....X...X.....X.....X..X......X......X
.....X....X.X.X...XXX...X.X.X.X...X...X.X.....X..X...........X.X.X...X
...XX.X...XX......X..........X.......XX..X.......X...X..X.X......X....
.......X.......X....................X..........XX.....XXXX..X.X.......
.....X...XX...X........X..X...X.X...X..........X...X.........X........
XXX..XX.....X...................X.....X.X.......X.X.X..X..............
....X.........X.....X.X...XX.....XX......X..........XX..X.XXX...X.X...
..X...............X.XX.......X....X......X......X.X.X.......X.......X.
..X.X.......XXX..X....X...X....X.....X.X......X..X......X.............
2 42 68 12

Output:
13





4
X...
...X
.X..
....
0 1 3 2

Output:
2
"""
