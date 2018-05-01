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

class Soldier(object):

    def __init__(self, rank, lastname):
        self.rank = rank
        self.lastname = lastname

    def shoot(self):
        print '{0.rank} {0.lastname} is shooting'.format(self)

    def __repr__(self):
        return '<<Instance of %r>>' % self.__class__.__name__

print Soldier
s = Soldier('Captain', 'America')
t = Soldier('Cadet', 'Battle')
u = Soldier('General', 'Nuisance')


############################################
# Repr
############################################

class CuteReprMeta(type):
    def __repr__(cls):
        return '<<Class %r>>' % cls.__name__

class CuteRepr:

    __metaclass__ = CuteReprMeta

class Soldier2(CuteRepr):

    def __init__(self, rank, lastname):
        self.rank = rank
        self.lastname = lastname

    def shoot(self):
        print '{0.rank} {0.lastname} is shooting'.format(self)

    def __repr__(self):
        return '<<Instance of %r>>' % self.__class__.__name__

class LostSoldier(Soldier2):

    def shoot(self):
        print '{0.rank} {0.lastname} where is my weapon'.format(self)

print Soldier2
s = Soldier2('Captain', 'America')
t = Soldier2('Cadet', 'Battle')
u = Soldier2('General', 'Nuisance')
v = LostSoldier('Private', 'Data')

############################################
# Instance Tracking
############################################

army = []

class InstanceTrackingMeta(type):

    def __call__(cls, *args):
        inst = type.__call__(cls, *args)
        army.append(inst)
        return inst

class Soldier3:

    __metaclass__ = InstanceTrackingMeta

    def __init__(self, rank, lastname):
        self.rank = rank
        self.lastname = lastname

    def shoot(self):
        print '{0.rank} {0.lastname} is shooting'.format(self)

    def __repr__(self):
        return '<<Instance of %r>>' % self.__class__.__name__

class LostSoldier3(Soldier3):

    def shoot(self):
        print '{0.rank} {0.lastname} where is my weapon'.format(self)

print Soldier3
s = Soldier3('Captain', 'America')
t = Soldier3('Cadet', 'Battle')
u = Soldier3('General', 'Nuisance')
v = LostSoldier3('Private', 'Data')
print army

############################################
# Dynamic attribute lookup
############################################

import time

class DynamicLookupMeta(type):
    def __getattribute__(cls, attr):
        if attr == 'now':
            return time.ctime()
        return type.__getattribute__(cls, attr)

class Soldier4:
    __metaclass__ = DynamicLookupMeta

    x = 10

    def __init__(self, rank, lastname):
        self.rank = rank
        self.lastname = lastname

    def shoot(self):
        print '{0.rank} {0.lastname} is shooting'.format(self)

    def __repr__(self):
        return '<<Instance of %r>>' % self.__class__.__name__

s = Soldier4('Captain', 'America')
t = Soldier4('Cadet', 'Battle')
print s.rank              # Instance level
print Soldier4.x          # Class level
print Soldier4.now        # Dynamic

############################################
# Singleton
############################################

singletons = {}

class SingletonMeta(type):

    def __call__(cls, *args):
        uid = (cls.__name__, args)
        if uid in singletons:
            return singletons[uid]

        inst = type.__call__(cls, *args)
        singletons[uid] = inst
        return inst

class Soldier5:

    __metaclass__ = SingletonMeta

    def __init__(self, rank, lastname):
        self.rank = rank
        self.lastname = lastname

    def shoot(self):
        print '{0.rank} {0.lastname} is shooting'.format(self)

    def __repr__(self):
        return '<<Instance of %r>>' % self.__class__.__name__

class SuperSoldier(Soldier5):

    def shoot(self):
        print 'Shooting in all diretions at once, not hitting friends'

s = SuperSoldier('Captain', 'America')
t = Soldier5('Cadet', 'Battle')
u = Soldier5('General', 'Nuisance')
v = SuperSoldier('Captain', 'America')
print "Is there only one", s.rank, s.lastname, "?", s is v

############################################
# Add Extra Attribute
############################################

class TimeStampMeta(type):

    def __new__(mcls, name, bases, mapping):
        mapping['creation_time'] = time.ctime()
        return type.__new__(mcls, name, bases, mapping)


class Soldier6:
    __metaclass__ = TimeStampMeta

    x = 10

    def __init__(self, rank, lastname):
        self.rank = rank
        self.lastname = lastname

    def shoot(self):
        print '{0.rank} {0.lastname} is shooting'.format(self)

    def __repr__(self):
        return '<<Instance of %r>>' % self.__class__.__name__

print "Soldier6 was created at", Soldier6.creation_time
