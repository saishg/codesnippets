'Reinvent OOP from scratch so you can see the advantages and learn how EVERYTHING works'

class Thing:
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
f1 = Furn('brown', 40)

for thing in [c1, c2, f1]:
    thing.show()



