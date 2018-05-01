'''
    Square brackets:
           d[k]      -> d.__getitem__(k) -> v                # Override __getitem__ to customize lookup
                             \-->  d.__missing__(k)          # Override __missing__ to customize handling of failed lookups
                              \--> KeyError
           d[k] = v  -> d.__setitem__(k, v)
           del d[k]  -> d.__delitem__(k)
                              \--> KeyError

    The dot:

            d.a      -> d.__getattribute__('a')           <- getattr(d, 'a')
                              \--> d.__getattr__(k)
                               \--> AttributeError
            d.a = v  -> d.__setattr__('a', v)             <- setattr(d, 'a', v)
            del d.a  -> d.__delattr__('a')                <- delattr(d, 'a')
                    
'''

class CIDict(dict):

    def __getitem__(self, key):                                 # d[k]
        key = key.lower()
        return dict.__getitem__(self, key)

    def __missing__(self, key):                                 # called by __getitem__ for a missing key
        raise KeyError('Missing key, could be any case variant of {0!r}'.format(key))
    
    def __setitem__(self, key, value):                          # d[k] = v
        key = key.lower()
        dict.__setitem__(self, key, value)

    def __delitem__(self, key):                                 # del d[k]
        key = key.lower()
        dict.__delitem__(self, key)

class CIDot(object):

    def foo(self, x):                                           # e.foo(15) or e.FOO(15)
        print 'Foo was called with', x

    def __getattribute__(self, attr):                           # e.a or getattr(e, 'a')
        attr = attr.lower()
        return object.__getattribute__(self, attr)

    def __getattr__(self, attr):                                # called by __getattribute__ when the attribute is missing
        raise AttributeError('Missing attribute, could be any case variant of {0!r}'.format(attr))
        
    def __setattr__(self, attr, value):                         # e.a = v or setattr(e, 'a', v)
        attr = attr.lower()
        object.__setattr__(self, attr, value)

    def __delattr__(self, attr):                                # del e.a or delattr(e, 'a')
        attr = attr.lower()
        return object.__delattr__(self, attr)

class Everything(object):

    def __new__(cls, *args):                                    # creates the instance
        print 'Create a new {0!r} with {1!r}'.format(cls, args)
        inst = object.__new__(cls)
        print 'Made an instance at 0x{0:08x}'.format(id(inst))
        return inst

    def __init__(self, y):                                      # initializes data in the instance dict
        print 'Initializing from:', vars(self)
        self.y = y
        print 'to:', vars(self)

    def __call__(self, z):                                      # f(15)
        print 'Called with', z
        return z ** 2

    def __repr__(self):                                         # print f
        return '%s(%r)' % (self.__class__.__name__, self.y)

class ZeroDict(dict):
    def __missing__(self, key):
        return 0

if 0:
    f = Everything(44)
    print f(15)
    print f


if 0:
    e = CIDot()
    e.RAYMOND = 'red'
    print vars(e)
    print e.Raymond
    del e.RAYmond
    print vars(e)
    e.foo(15)
    e.FOO(15)
    #print e.ROGER

if 0:
    c = CIDict()
    c['RAYMOND'] = 'red'
    print c
    print c['Raymond']
    del c['RAYmond']
    print c
    print c['ROGER']

if 0:
    d = ZeroDict(horses=6, cats=4, dogs=2)
    print d['dogs']
    print d['dragons']
    d['dragons'] += 1
    print d['dragons']






