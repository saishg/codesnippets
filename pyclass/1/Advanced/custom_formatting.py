

class IPAddr(object):

    def __init__(self, *octets):
        self.octets = octets

    def __repr__(self):
        return '{0.__class__.__name__}{0.octets!r}'.format(self)

    def __str__(self):
        return 'stir it up'

    def __format__(self, code):
        if code == '':
            return '.'.join(map(str, self.octets))
        elif code == 'x':
            return '.'.join(format(octet, '02x') for octet in self.octets)
        return ValueError('Unknown format code: %r' % code)


a = IPAddr(171, 0, 1, 15)
print a
print repr(a)
print format(a)
print format(a, 'x')

print 'The object {0!r} is usually shown as {0} but sometimes as {0:x}'.format(a)
print 'but prints as {0!s}'.format(a)
