

class Foo(object):
    def getter(self):
        print "getter"
        return None

    def setter(self, value):
        print "setter", value

    var = property(getter, setter)
