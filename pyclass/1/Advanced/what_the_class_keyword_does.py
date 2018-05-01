# mcls(name, bases, mapping) -> cls

from pprint import pprint


def inspect(*args, **kwargs):
    print 'Inpsect called with:'
    pprint(args)
    pprint(kwargs)
    return 42

class Demo:
    'A simple demonstration of the class keyword'

    __metaclass__ = inspect

    x = 10

    def hello(self):
        print 'Howdy!'

print "Demo class is now", Demo

d = Demo()
