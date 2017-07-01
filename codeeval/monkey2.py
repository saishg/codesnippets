
LIMIT = 300
SUM_LIMIT = 19

coordinates = {}

def sumofdigits(x, y):
    return reduce(lambda x,y: int(x)+int(y), str(abs(x)) + str(abs(y)))


def traverse(x, y, depth):
    if (x, y) in coordinates:
        return

    if sumofdigits(x, y) >= SUM_LIMIT:
        return

    print x, y, "=", sumofdigits(x, y), "(%d)" % depth
    coordinates[(x, y)] = True
    traverse(x + 1, y, depth + 1)
    traverse(x - 1, y, depth + 1)
    traverse(x, y + 1, depth + 1)
    traverse(x, y - 1, depth + 1)


traverse(0, 0, 0)




