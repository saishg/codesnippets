import sys

triangle = []

def readfile(filename):
    global triagle
    f = open(filename, 'r')
    while True:
        l = f.readline()
        if l:
            triangle.append(map(int, l.split()))
        else:
            break

def traverse(row = 0, element = 0):
    if row >= len(triangle):
        return 0

    value = triangle[row][element]
    return value + max(traverse(row + 1, element),
                       traverse(row + 1, element + 1))


readfile(sys.argv[1])
print traverse()




