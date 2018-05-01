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

# Study list searching behavior #######################################

reset(); print a in s; show()    # Linear search, left-to-right.  When there is no match, it takes len(s) comparisons
reset(); print b in s; show()    # There is an early-out for matches.
reset(); print c in s; show()    # Identity implies equality, saving one test for an exact match.

print 'Expected sort() cost:', n * log(n, 2)
reset(); s.sort(); show()        # Sorts of random data are O(n log g) but most data is partially ordered and the Timsort uses that fact to reduce the number of comparisons
reset(); bisect(s, a); show()    # Bisect has a constant speed of O(log n) regardless of whether the target is found or not
reset(); bisect(s, b); show()   
reset(); bisect(s, c); show()    # Bisect gets no benefit from an identity match

# Study set searching behavior   #######################################

print '=' * 50

s = map(Int, [10, 20, 30, 50, 20, 5, 10, 15, 20])
a = Int(111)
b = Int(20)
c = s[3]
n = len(s)

other_intdata = [20, 30, 40, 300, 400, 500, 300, 400]
otherdata = map(Int, other_intdata) + s[-4:]
odata = set(otherdata)

reset(); t = set(s); show()   # Cost is len(s) hashes and 1 comparison for each non-identical duplicate
reset(); print a in t; show() # Cost of unsuccessful lookup is 1 hash and zero compares
reset(); print b in t; show() # Cost of successful non-identity lookup is 1 hash and one compares
reset(); print c in t; show() # Cost of successful identity lookup is 1 hash and 0 compares

print 'Using sets is MUCH cheaper than building them'
reset(); dict.fromkeys(t); show() # Conversion to a dict costs 0 hashes and 0 compares
reset(); t & odata; show()    # Set-to-set operations cost 0 hashes and 1 comparison for each non-identical overlap
reset(); t | odata; show()
reset(); t - odata; show()
reset(); odata - t; show()

################################################################
print 'Fun for April fools'
import random

class FunInt(int):
    def __hash__(int):
        return random.randrange(2)

a = FunInt(50)
s = {a}

#################################################################

print 'We just learned that if a hash is random, the object may become unfindable'
print 'There is a hash homomorphism:'
print 'If x == y, then hash(x) should equal to the hash(y)'

class Str(str):
    'Make case-insensitive compares'

    def __eq__(self, other):
        return self.lower() == other.lower()

    def __ne__(self, other):
        return self.lower() != other.lower()

    def __hash__(self):
        return hash(self.lower())

names = map(Str, 'Raymond rachel MATTHEW raymond RACHEL Matthew'.split())
print set(names)
    
