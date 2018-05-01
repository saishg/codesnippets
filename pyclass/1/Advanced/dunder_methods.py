'''
    Square brackets:
           d[k]      -> d.__getitem__(k) -> v                # Override __getitem__ to customize lookup
                             \-->  d.__missing__(k)          # Override __missing__ to customize handling of failed lookups
                              \--> KeyError
           d[k] = v  -> d.__setitem__(k, v)
           del d[k]  -> d.__delitem__(k)
                              \--> KeyError
                    
'''


class CIDict(dict):

    def __getitem__(self, key):
        key = key.lower()
        return dict.__getitem__(self, key)

    def __missing__(self, key): # called by __getitem__ if its missing a key
        raise KeyError('Missing key, could be any case variant of {0!r}'.format(key))

    def __setitem__(self, key, value):
        key = key.lower()
        dict.__setitem__(self, key, value)

    def __delitem__(self, key):
        key = key.lower()
        dict.__delitem__(self, key)

class ZeroDict(dict):

    def __missing__(self, key):
        return 0

class CIDot(object):

    def __getattribute__(self, attr):
        attr = attr.lower()
        return object.__getattribute__(self, attr)

    def __getattr__(self, attr):
        raise AttributeError('Missing attribute')

    def __setattr__(self, attr, value):
        attr = attr.lower()
        object.__setattr__(self, attr, value)

    def __delattr__(self, attr):
        attr = attr.lower()
        return object.__delattr__(self, attr)

    def foo(self):
        print "inside foo, even if you called Foo or FOO"

class Everything(object):

    def __new__(cls, *args):
        print 'Create a new {0!r} with {1!r}'.format(cls, args)
        inst = object.__new__(cls, *args)
        print 'Made an instance at 0x{0:08x}'.format(id(inst))
        return inst

    def __init__(self, y):
        print 'Initializing from:', vars(self)
        self.y = y
        print 'to instance variables:', vars(self)

    def __call__(self, z):
        print 'Called with', z
        return z ** 2

    def __repr__(self):
        return '%s(%r)' %  (self.__class__.__name__, self.y)

if 0:
    f = Everything(44)
    f(5)


if 1:
    e = CIDot()
    e.RAYMOND = 'red'
    print vars(e)
    print e.Raymond
    e.FOO()

if 0:
    d = ZeroDict(horses=6, cats=4, dogs=2)
    print d['dogs']
    print d['dragons']
    d['dragons'] += 1
    print d['dragons']

if 0:
    c = CIDict()
    c['RAYMOND'] = 'red'
    print c
    print c['Raymond']
    del c['RAYmond']
    print c
    print c['ROGER']
