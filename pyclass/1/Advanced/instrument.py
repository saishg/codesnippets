''' Goals:

* Learn to instrument Python for performance analysis and debugging
* Practice subclassing built-in types
* Review the dunder methods for comparisons (including partial ordering and total ordering)
    * Solidify the knowledge of how containers work
    * Practice using map() and filter()

'''
from math import log
from bisect import bisect

cmp_cnt = 0
hash_cnt = 0

def reset():
    global cmp_cnt, hash_cnt
    cmp_cnt = 0
    hash_cnt = 0

def show():
    print '{0} comparisons and {1} hashes'.format(cmp_cnt, hash_cnt)
    print '--------------------'

class Int(int):
    'Instrumented tracer version of ints'

    def __cmp__(self, other):
        global cmp_cnt
        cmp_cnt += 1
        print 'Comparing {0!r} to {1!r}'.format(self, other)
        return int.__cmp__(self, other)

    def __hash__(self):
        global hash_cnt
        hash_cnt += 1
        print 'Hashing {0!r}'.format(self)
        return int.__hash__(self)

s = map(Int, [10, 20, 30, 50, 20, 5, 10, 15, 20])
a = Int(111)
b = Int(20)
c = s[3]
n = len(s)

reset(); print a in s; show()
reset(); print b in s; show()
reset(); print c in s; show()

print 'Expected sort() cost:', n * log(n, 2)
reset(); s.sort(); show()
reset(); bisect(s, a); show()
reset(); bisect(s, b); show()
reset(); bisect(s, c); show()


# Set searching behavior
s = map(Int, [10, 20, 30, 50, 20, 5, 10, 15, 20])
a = Int(111)
b = Int(20)
c = s[3]
n = len(s)

other_intdata = [20, 30, 40, 300, 400, 500, 300, 400]
otherdata = map(Int, other_intdata) + s[-4:]
odata = set(otherdata)

reset(); t = set(s); show() 
reset(); a in t; show()
reset(); b in t; show()
reset(); c in t; show()

print 'Using sets is MUCH cheaper than building them'
reset(); dict.fromkeys(t); show()
reset(); t & odata; show()
reset(); t | odata; show()
reset(); t - odata; show()
reset(); odata - t; show()

print 'Fun for April fools'
import random

class FunInt(int):
    def __hash__(int):
        return random.randrange(2)

a = FunInt(50)
s = {a}



class Str(str):
    'Make case insensitive compares'

    def __eq__(self, other):
        return self.lower() == other.lower()

    def __ne__(self, other):
        return self.lower() != other.lower()

    def __hash__(self):
        return hash(self.lower())


names = map(Str, 'Raymond rachel MATTHEW raymond RACHEL Matthew'.split())
