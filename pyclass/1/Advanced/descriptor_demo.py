

class Desc(object):
    def __get__(self, obj, objtype):
        print 'Invocation!'
        print 'Returning x + 10'
        return obj.x + 10


class A(object):
    def __init__(self, x):
        self.x = x

    plus_ten = Desc()

a = A(5)
print "a.x", a.x
print "a.plus_ten", a.plus_ten
print "Doesn't work --> A.__dict__['plus_ten']", A.__dict__['plus_ten']
try:
    print "A.plus_ten", A.plus_ten
except AttributeError:
    print "Doesn't work --> A.plus_ten --> AttributeError"


class B(object):
    def __init__(self, x):
        self.x = x
        self.plus_ten = Desc()

b = B(5)
print "Doesn't work --> b.x", b.x
print "Doesn't work --> b.plus_ten", b.plus_ten
