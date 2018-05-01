''' A metaclass is sometimes called a "class of classes".
    We built one called ClassObj(name, bases, namespace).

    Two are already provided:
       classobj(name, bases, namespace) --> old-style classes
       type(name, bases, namespace) --> new-style classses

    Build custom metaclasses by subclassing "type" and overriding
    or extending its default behaviors:

       type.__new__               Makes a new class (you can change the result type here)
       type.__init__              Initializing the class (the metaclass is already fixed)
       type.__getattribute__      Implement class lookups
       type.__setter__            Stores values in the class dict
       type.__call__              Creates instances of the class
       type.__repr__              Controls the appearance
       type.__dir__               Controls dir()


    The most common way to make metaclasses is to subclass "type"
    and replace behaviors you don't like.

    The overall relationship between instances, classes and metaclasses looks like this:

                 Metaclass                                  __call__
                 ^
                / behavior controlled by
               /                                            Soldier(a)
             Class --> attributes unique to each instance   __call__           <-- type
             ^
            / behavior controlled by
           /
Instance  o--> attributes unique to each instance            s(a)              <-- object

'''

def __init__(self, rank, lastname):
    self.rank = rank
    self.lastname = lastname

def shoot(self):
    print '{0.rank} {0.lastname} is shooting'.format(self)

def __repr__(self):
    return '<<Instance of %r>>' % self.__class__.__name__

namespace = dict(__init__=__init__, shoot=shoot, __repr__=__repr__)

del __init__, shoot, __repr__

Soldier = type('Soldier', (object,), namespace)

print Soldier
s = Soldier('Captain', 'America')
t = Soldier('Cadet', 'Battle')
u = Soldier('General', 'Nuisance')
v = type.__call__(Soldier, 'Major', 'Pita')

for soldier in [s, t, u, v]:
    soldier.shoot()

print Soldier.__module__
