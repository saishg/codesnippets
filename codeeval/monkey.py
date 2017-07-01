
LIMIT = 300
SUM_LIMIT = 19

#coordinates = [[False] * LIMIT * 2] * LIMIT * 2
coordinates = [[0] * LIMIT * 2 for x in xrange(LIMIT * 2)] 

def sumofdigits(x, y):
    return reduce(lambda x,y: int(x)+int(y), str(abs(x)) + str(abs(y)))


def fix_coordinates():
    global coordinates

    for x in xrange(0, LIMIT * 2):
        for y in xrange(0, LIMIT * 2):
            if sumofdigits(x, y) >= SUM_LIMIT:
                coordinates[x][y] = False
            else:
                coordinates[x][y] = True

def count_coordinates():
    global coordinates
    count = 0

    for x in xrange(0, LIMIT * 2):
        for y in xrange(0, LIMIT * 2):
            count += 1

    print count

fix_coordinates()
count_coordinates()





