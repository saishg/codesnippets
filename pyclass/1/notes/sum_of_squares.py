# History of Python as an ice-cream shop

n = 1000000

# 1990 -- Plain old Python -- Vanilla
squares = []
for i in range(n):
    square = i ** 2
    squares.append(square)
print sum(squares)

# 2000 -- List comprehensions -- Chocolate
print sum([i**2 for i in range(n)])

# 2002 -- Generators -- Peanut Butter
def squares(n):
    for i in xrange(n):
        square = i ** 2
        yield square
print sum(squares(n))

# 2003 -- Generator Expressions -- Reeses or KitKat
print sum(i**2 for i in xrange(n))
