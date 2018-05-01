'''Reinvent OOP from scratch so you can see the advantages and learn how EVERYTHING works

Object:  unique data plus a link to shared functions and data

        c.__dict__           <= collection of unique data
        c.__class__          <= link to shared information

Class:   named collection of shared functions and data
         that possibly reuse functions in other classes

        C.__name__
        C.__dict__
        C.__bases__

'''

class Thing:

    x = 8

    def __init__(self, color, size):
        self.color = color
        self.size = size    

class Car(Thing):

    x = 10

    def show(self):
        print 'The beautiful %s car is %s long' % (self.color, self.size)

class Furn(Thing):

    x = 12

    def show(self):
        print 'The fabulous %s furniture is %s long' % (self.color, self.size)

c1 = Car('red', 20)
c2 = Car('blue', 30)
c3 = Car('orange', 35)
f1 = Furn('brown', 40)

things = [c1, c2, f1, c3]
for thing in things:
    thing.show()




