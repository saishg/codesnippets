'A simple demonstration of Python'

n = 20

squares = [i**2 for i in xrange(n)]

print 'The sum of squares is %d' % sum(squares)

def cube(x):
    return x ** 3

print map(cube, range(n))

if __name__ == '__main__':
    print 'Happy!'
