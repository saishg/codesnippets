'Goal:  Learn to use __format__ to create customized string formatting codes'

class IPAddr(object):

    def __init__(self, *octets):
        self.octets = octets

    def __repr__(self):               # Accessed with repr(o) or format(o, '!r')
        return '{0.__class__.__name__}{0.octets!r}'.format(self)

    def __str__(self):                # str(o) called by "print o" or format(o, '!s')
        return 'stir it up'

    def __format__(self, code):
        if code == '':                # format(o) or '{0}'.format(o) 
            return '.'.join(map(str, self.octets))
        elif code == 'x':             # format(o, 'x') or '{0:x}'.format(o)
            return ':'.join([format(octet, '02x') for octet in self.octets])
        raise ValueError('Unknown format code: %r' % code)

if __name__ == '__main__':
    import datetime
    
    a = IPAddr(171, 0, 1, 15)
    print a
    print repr(a)
    print format(a)
    print format(a, 'x')
    print 'The object {0!r} is usually shown as {0} but sometimes as {0:x}'.format(a)
    print 'but some folks just like to {0!s}.'.format(a)
    print 'Today is {0:%A} in century {0:%C}'.format(datetime.datetime.now())
    print 'The answer is {0:,d} today'.format(1234567890)

