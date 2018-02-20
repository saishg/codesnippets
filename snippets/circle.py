import math

COUNT = 42
ARRAY = [None] * COUNT


def init_2darray():
    for i in range(COUNT):
        ARRAY[i] = [' '] * COUNT

def print_2darray():
    for row in reversed(ARRAY):
        print ' '.join(row)

def plot(x, y):
    if x < COUNT/2 and y < COUNT/2:
        ARRAY[y + COUNT/2][x + COUNT/2] = 'X'

def plot_line(x1, y1):
    m = float(y1) / float(x1)
    for x in range(x1):
        y = int(m * x)
        plot(x, y)

    for y in range(y1):
        x = int(y/m)
        plot(x, y)

def plot_8(x, y):
    plot(x, y)
    plot(x, -y)
    plot(-x, y)
    plot(-x, -y)

    plot(y, x)
    plot(-y, x)
    plot(y, -x)
    plot(-y, -x)

def plot_circle2(R):
    R_2 = R * R
    for x in range(0, R+1):
        y = int(round(math.sqrt(R_2 - x**2)))
        plot_8(x, y)
        if x > y:
            break


def plot_circle(R):
    R_2 = R * R
    y = R
    for x in range(0, R+1):
        if x*x + y*y > R_2:
            y -= 1
        plot_8(x, y)
        if x > y:
            break
        

if __name__ == '__main__':
    init_2darray()
#    plot_line(5, 10)
    plot_circle(20)
#    plot_circle2(10)
    print_2darray()

