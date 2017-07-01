import sys

def proceed(matrix, R, C, r, c, direction):
    if direction == 'right':
        return r, c+1
    elif direction == 'left':
        return r, c-1
    elif direction == 'down':
        return r+1, c
    elif direction == 'up':
        return r-1, c

def checkdirection(matrix, R, C, r, c, direction):
    r, c = proceed(matrix, R, C, r, c, direction)
    if 0 <= r < R and 0 <= c < C and matrix[r][c] is not None:
        return direction
    else:
        if direction == 'right':
            return 'down'
        elif direction == 'left':
            return 'up'
        elif direction == 'down':
            return 'left'
        elif direction == 'up':
            return 'right'

def spiral_advance(matrix, R, C, r=0, c=0, direction='right'):
    while True:
        if matrix[r][c] is None:
            break
        print matrix[r][c],
        matrix[r][c] = None
        direction = checkdirection(matrix, R, C, r, c, direction)
        r, c = proceed(matrix, R, C, r, c, direction)


def parseFile(filename):
    f = open(filename, 'r')
    for l in f:
        R, C, num_list = l.strip().split(';')
        R, C = int(R), int(C)
        num_list = num_list.split()

        matrix = [[None] * C for i in xrange(R)]

        i = 0
        for r in xrange(R):
            for c in xrange(C):
                matrix[r][c] = num_list[i]
                i += 1
        spiral_advance(matrix, R, C)


parseFile(sys.argv[1])

