
''' Give a typical OOP example.
    Clarify how wide-open the implementation is.
    Show the most common magic methods (special methods).
'''

class Animal:
    'A generic class of critters'

    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    def __str__(self):
        return 'I am a %s named %s' % (self.__class__.__name__.lower(), self.name)

    def __repr__(self):
        return '%s(%r, %r)' % (self.__class__.__name__, self.name, self.color)


class Cat(Animal):
    'A simple feline class'

    def talk(self):
        print 'Meow! %s is purring at the door.' % self.name



class Dog(Animal):
    'A simple canine class'

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def talk(self):
        print 'Woof! %s is barking at the moon.' % self.name

    def __len__(self):
        return len(self.name)


    def __call__(self, action):
        if action == 'fetch':
            return '%s is fetching' % self.name
        else:
            return "%s can't do everythign you say" % self.name

c = Cat('Socks', 'white')
d = Dog('Fido', 'white')
e = Dog('Buddy', 'black')
f = Dog('Checkers', 'spotted')

animals = [d, e, f, Dog('Rex', 'brown'), d, c]
for animal in animals:
    animal.talk()
