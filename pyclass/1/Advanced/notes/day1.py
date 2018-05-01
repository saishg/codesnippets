Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 26 2016, 12:10:39) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 

>>> a = 'hello'
>>> type(a)
<type 'str'>
>>> id(a)
4362373712
>>> hex(id(a))
'0x104048a50'
>>> hex(id(str))
'0x100187540'
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
=============================== RESTART: Shell ===============================
>>> a = 'hello'
>>> type(a)
<type 'str'>
>>> import sys
>>> sys.getrefcount(a)
3
>>> 
>>> 
>>> 
>>> b = 'goodbye'
>>> sys.getrefcount(b)
2
>>> c = b                    # assignments never make copies
>>> sys.getrefcount(b)
3
>>> del b
>>> sys.getrefcount(c)
2
>>> del c
>>> 
>>> d = "C'ya'"
>>> s = []
>>> s.append(d)
>>> sys.getrefcount(d)
3
>>> s.append(d)
>>> sys.getrefcount(d)
4
>>> s
["C'ya'", "C'ya'"]
>>> # Strings are immutable
>>> t = s[:]
>>> # Slices make shallow copies
>>> s
["C'ya'", "C'ya'"]
>>> t
["C'ya'", "C'ya'"]
>>> map(hex, map(id, s))
['0x1049ea2d0', '0x1049ea2d0']
>>> map(hex, map(id, t))
['0x1049ea2d0', '0x1049ea2d0']
>>> sys.getrefcount(d)
6
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> d = [10, 20]
>>> map(hex, map(id, d))
['0x1004085e0', '0x1004084f0']
>>> hex(id(d))
'0x1063bfd40'
>>> s = [d, d]
>>> t = s[:]
>>> s
[[10, 20], [10, 20]]
>>> t
[[10, 20], [10, 20]]
>>> map(hex, map(id, s))
['0x1063bfd40', '0x1063bfd40']
>>> map(hex, map(id, t))
['0x1063bfd40', '0x1063bfd40']
>>> d.append(30)
>>> s
[[10, 20, 30], [10, 20, 30]]
>>> t
[[10, 20, 30], [10, 20, 30]]
>>> map(hex, map(id, s))
['0x1063bfd40', '0x1063bfd40']
>>> map(hex, map(id, t))
['0x1063bfd40', '0x1063bfd40']
>>> 
>>> 
>>> 
>>> import copy
>>> u = copy.deepcopy(s)
>>> s
[[10, 20, 30], [10, 20, 30]]
>>> u
[[10, 20, 30], [10, 20, 30]]
>>> map(hex, map(id, s))
['0x1063bfd40', '0x1063bfd40']
>>> map(hex, map(id, u))
['0x10029c8c0', '0x10029c8c0']
>>> d.append(40)
>>> s
[[10, 20, 30, 40], [10, 20, 30, 40]]
>>> t
[[10, 20, 30, 40], [10, 20, 30, 40]]
>>> u
[[10, 20, 30], [10, 20, 30]]
>>> 
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> # What parts of identity are guaranteed and what is am implementation, non-guarantteed
>>> # Guaranteed:
>>> # 1) "is" with singleton:  None
>>> # 2) assignments never make copies:   a = b           ->   a is b
>>> # 3) containers don't change ids:     s[2] = a        ->   s[2] is a
>>> 
>>> # Non-guaranteed optimizations:#
>>> # 1) small integers -5 to 256 are precomputed and reused
>>> # 2) in easy cases where we compute a string, the same string is re-used
>>> 
>>> a = 10
>>> b = 5 + 5
>>> a == b
True
>>> a is b
True
>>> a = 1000
>>> b = 500 + 500
>>> a == b
True
>>> a is b
False
>>> a = 'san jose'
>>> b =
SyntaxError: invalid syntax
>>> b = 'san jose'
>>> a is b
False
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj151/tmp.py ============
>>> a is b
True
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj151/tmp.py ============
>>> a is c
False
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj151/tmp.py ============
>>> a, b, c = f()
>>> a is c
False
>>> from dis import dis
>>> dis(f)
  2           0 LOAD_CONST               1 ('san jose')
              3 STORE_FAST               0 (a)

  3           6 LOAD_CONST               1 ('san jose')
              9 STORE_FAST               1 (b)

  4          12 LOAD_CONST               4 ('san jose')
             15 STORE_FAST               2 (c)

  5          18 LOAD_FAST                0 (a)
             21 LOAD_FAST                1 (b)
             24 LOAD_FAST                2 (c)
             27 BUILD_TUPLE              3
             30 RETURN_VALUE        
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj151/tmp.py ============
>>> a, b, c, d = f()
>>> a is b
True
>>> a is c
False
>>> a is d
False
>>> a is c or a == c
True
>>> # a == b -> False
>>> # re.match(pattern, s) -> True              re.UNICODE  re.LOCALe
>>> 
>>> # L o umlaut w i s
>>> # L umlaut-o w i s
>>> # re.IGNORECASE
>>> 
>>> 
>>> n = 10
>>> range(1)
[0]
>>> range(n)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> s = []
>>> i = 0
>>> while i < n:
	s.append(i)
	i += 1

	
>>> s
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
\
>>> 
>>> s = 'hello'
>>> len(s)
5
>>> list(s)
['h', 'e', 'l', 'l', 'o']
>>> [10, 20, 30]
[10, 20, 30]
>>> def f(x):
	return [x, 2*x, 3*x]

>>> from dis import dis
>>> dis(f)
  2           0 LOAD_FAST                0 (x)
              3 LOAD_CONST               1 (2)
              6 LOAD_FAST                0 (x)
              9 BINARY_MULTIPLY     
             10 LOAD_CONST               2 (3)
             13 LOAD_FAST                0 (x)
             16 BINARY_MULTIPLY     
             17 BUILD_LIST               3
             20 RETURN_VALUE        
>>> 
>>> 

>>> import sys
>>> sys.getsizeof([])
72
>>> s = []
>>> s.append(10)
>>> sys.getsizeof([])
72
>>> sys.getsizeof(s)
104
>>> 104 - 72
32
>>> 8 * 4
32
>>> s.append(20)
>>> sys.getsizeof(s)
104
>>> s.append(30)
>>> sys.getsizeof(s)
104
>>> s.append(40)
>>> sys.getsizeof(s)
104
>>> s.append(50)
>>> sys.getsizeof(s)
136
>>> 
>>> 
>>> dict.fromkeys('abcde')
{'a': None, 'c': None, 'b': None, 'e': None, 'd': None}
>>> dict.fromkeys('abcde', 0)
{'a': 0, 'c': 0, 'b': 0, 'e': 0, 'd': 0}
>>> dict.fromkeys(range(10), 0)
{0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
>>> 
>>> 
>>> sys.getsizeof(dict.fromkeys(range(0), 0))
280
>>> sys.getsizeof(dict.fromkeys(range(1), 0))
280
>>> sys.getsizeof(dict.fromkeys(range(5), 0))
280
>>> sys.getsizeof(dict.fromkeys(range(6), 0))
1048
>>> 8 * (3 * 8)
192
>>> 280 - 192
88
>>> 32 * (3 * 8) + 192
960
>>> 32 * (3 * 8) + 88
856
>>> 
>>> 
>>> 
>>> sys.getsizeof(dict.fromkeys(range(10), 0))
1048
>>> sys.getsizeof(dict.fromkeys(range(100), 0))
12568
>>> sys.getsizeof(dict.fromkeys(range(1000), 0))
49432
>>> sys.getsizeof(dict.fromkeys(range(10000), 0))
786712
>>> sys.getsizeof(dict.fromkeys(range(100000), 0))
6291736
>>> sys.getsizeof(dict.fromkeys(range(1000000), 0))
50331928
>>> 
>>> 
>>> dict(raymond='red')
{'raymond': 'red'}
>>> dict(raymond='red', rachel='blue')
{'rachel': 'blue', 'raymond': 'red'}
>>> hash('raymond')
2729357497184525765
>>> hash('rachel')
-9091735575445484789
>>> abs(hash('raymond'))
2729357497184525765
>>> abs(hash('rachel'))
9091735575445484789
>>> abs(hash('raymond')) % 8
5
>>> abs(hash('rachel')) % 8
5
>>> abs(hash('rachel') >> 5 ) % 8
0
>>> dict(raymond='red', rachel='blue', matthew='yellow')
{'matthew': 'yellow', 'rachel': 'blue', 'raymond': 'red'}
>>> 
>>> 
>>> # Break: 10 minute   instrument python  application
>>> 

>>> 
>>> 
>>> ord('A')
65
>>> ord(' ')
32
>>> map(ord, 'Raymond')
[82, 97, 121, 109, 111, 110, 100]
>>> [ord('R'), ord('a'), ord('y')]
[82, 97, 121]
>>> 
>>> 
>>> 'a'.isupper()
False
>>> 'A'.isupper()
True
>>> filter(str.isupper, 'Everybody Loves Raymond')
'ELR'
>>> # IDLE -- Eric Idle -- IDE
>>> # PyCharm  WingIDE   Komodo
>>> # Emacs Vi
>>> #   \----\---- ipython
>>> # TextMate  Eclipse(pydev)
>>> # Visual Studio (Intellisense) (PyDev)
>>> 
>>> 
>>> # __dunder__
>>> 
>>> dir(int)
['__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__', '__delattr__', '__div__', '__divmod__', '__doc__', '__float__', '__floordiv__', '__format__', '__getattribute__', '__getnewargs__', '__hash__', '__hex__', '__index__', '__init__', '__int__', '__invert__', '__long__', '__lshift__', '__mod__', '__mul__', '__neg__', '__new__', '__nonzero__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'imag', 'numerator', 'real']
>>> 3 + 6
9
>>> (3).__add__(6)
9
>>> len('hello')
5
>>> 'hello'.__len__()
5
>>> pow(2, 5)
32
>>> (2).__pow__(5)
32
>>> abs(-5)
5
>>> (-5).__abs__()
5
>>> z = 3 + 4j
>>> type(z)
<type 'complex'>
>>> 2000
2000
>>> 300 / 2000.
0.15
>>> # Coursera:  high school  teachers   artists    gamers  scientists  kids ...
>>> # classes, modules, basics ops, file
>>> # xmlrpc rest api  xml json yaml re parse  clol  sockets tcp/udp
>>> 
>>> 
>>> dir(complex)
['__abs__', '__add__', '__class__', '__coerce__', '__delattr__', '__div__', '__divmod__', '__doc__', '__eq__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__int__', '__le__', '__long__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__nonzero__', '__pos__', '__pow__', '__radd__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', 'conjugate', 'imag', 'real']
>>> abs(z)
5.0
>>> # Top level functions just call dunder methods
>>> 
>>> # Keywords just call dunder methods
>>> #    print         __str__
>>> #    >>>           __repr__
>>> #    for           __iter__          __getitem__(0) -> IndexError
>>> #    with          __enter__ __exit__
>>> 
>>> # Operators just call dunders methods
>>> #  a + b           __add__  --(NotImplemented)-->  b.__radd__(a)  --> TypeError
>>> #  a ** b          __pow__                           __rpow__
>>> #  a / b           __div__  (which for floats does floordivisio)
>>> 38 / 5
7
>>> #  a // b          __floordiv__  (which for floats does floordivision)
>>> 38 // 5
7
>>> # In Python 3
>>> from __future__ import division
>>> #  a / b           __truediv__
>>> 38 / 5
7.6
>>> #  a // b          __floordiv__  (which for floats does floordivision)
>>> 38 // 5
7
>>> 
>>> a = 38
>>> b = 17
>>> a > b
True
>>> dir(int)
['__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__', '__delattr__', '__div__', '__divmod__', '__doc__', '__float__', '__floordiv__', '__format__', '__getattribute__', '__getnewargs__', '__hash__', '__hex__', '__index__', '__init__', '__int__', '__invert__', '__long__', '__lshift__', '__mod__', '__mul__', '__neg__', '__new__', '__nonzero__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'imag', 'numerator', 'real']
>>> 
>>> # Int comparisons call __cmp__ which is a three-way compare:
>>> #      -1 for less than    0 for equal     1 for greater than
>>> a.__cmp__(b)
1
>>> b.__cmp__(a)
-1
>>> b.__cmp__(b)
0
>>> a > b
True
>>> a.__cmp__(b) == 1
True
>>> b > a
False
>>> b.__cmp__(a) == 1
False
>>> a = 'goodbye'
>>> b = 'hello'
>>> a < b
True
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> # Rich comparisions:  __lt__ __le__ __eq__ __ne__ __gt__ __ge__
>>> a < b
True
>>> a.__lt__(b)
True
>>> # Rich comparisions:  __lt__ __le__ __eq__ __ne__ __gt__ __ge__ -> True or False
>>> # Rich comparisions:  __lt__ __le__ __eq__ __ne__ __gt__ __ge__ -> Usally: True or False
>>> # You can get them to return other types
>>> import numpy as np
>>> a = np.array([10, 5, 20])
>>> b = np.array([7, 8, 9])
>>> a > b
array([ True, False,  True], dtype=bool)
>>> 
>>> dir(float)
['__abs__', '__add__', '__class__', '__coerce__', '__delattr__', '__div__', '__divmod__', '__doc__', '__eq__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getformat__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__int__', '__le__', '__long__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__nonzero__', '__pos__', '__pow__', '__radd__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__', '__setformat__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']
>>> 
>>> a = 30
>>> b = 20
>>> a >= b
True
>>> a.__cmp__(b)
1
>>> a.__cmp__(b) != -1
True
>>> 
>>> 
>>> # Total ordering:
>>> # * Transitivity:   a > b and b > c ==> a > c
>>> # * Exactly 1:      a > b or  a == b or a < b
>>> 
>>> # Partial ordering:
>>> # * Transitivity:   a > b and b > c ==> a > c
>>> # * 0 or more:      a > b or  a == b or a < b
>>> # * 0 or 1:         a > b or  a == b or a < b
>>> 
>>> 
>>> s = {10, 20, 30, 40}
>>> t = {30, 40, 50, 60}
>>> u = {10, 20, 30, 40, 50, 60}
>>> 
>>> s < u
True
>>> t < u
True
>>> s == u
False
>>> s > u
False
>>> 
>>> s = {10, 20, 30, 40}
>>> t = {30, 40, 50, 60}
>>> s <= t
False
>>> s == t
False
>>> s >= t
False
>>> # min   max   sorted            all depend on total orderig
>>> min([10, 5, 30])
5
>>> min([5, 10, 30])
5
>>> min(s, t)
set([40, 10, 20, 30])
>>> min(t, s)
set([40, 50, 60, 30])
>>> def mymin(x, y):
	if x < y:
		return x
	return y

>>> mymin(40, 50)
40
>>> mymin(50, 40)
40
>>> mymin(s, t)
set([40, 50, 60, 30])
>>> mymin(t, s)
set([40, 10, 20, 30])
>>> s < t
False
>>> t < s
False
>>> # Sets implement a partial ordering
>>> # min() max() sorted() depend on total orderings
>>> # Therefore sets confuse those tools
>>> 
>>> s = 'hello'
>>> hash(s)
840651671246116861
>>> s.__hash__()
840651671246116861
>>> t = 3.14
>>> hash(t)
3146129223
>>> t.__hash__()
3146129223
>>> 
>>> 
>>> 
>>> x = 10
>>> ++x
10
>>> x
10
>>> 
>>> - x
-10
>>> - - x
10
>>> --x
10
>>> ++x
10
>>> x++
SyntaxError: invalid syntax
>>> x++ - y

Traceback (most recent call last):
  File "<pyshell#353>", line 1, in <module>
    x++ - y
NameError: name 'y' is not defined
>>> y = 5
>>> x++ - y
5
>>> x
10
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj151/instrument.py =========
>>> a < b
Comparing 111 to  20
False
>>> b > a
Comparing 20 to  111
False
>>> cmp_cnt
2
>>> show()
2 comparisons
>>> reset()
>>> show()
0 comparisons
>>> type(s)

Traceback (most recent call last):
  File "<pyshell#363>", line 1, in <module>
    type(s)
NameError: name 's' is not defined
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj151/instrument.py =========
>>> type(s)
<type 'list'>
>>> type(s[0])
<class '__main__.Int'>
>>> map(type, s)
[<class '__main__.Int'>, <class '__main__.Int'>, <class '__main__.Int'>, <class '__main__.Int'>, <class '__main__.Int'>, <class '__main__.Int'>, <class '__main__.Int'>, <class '__main__.Int'>, <class '__main__.Int'>]
>>> len(set(map(type, s)))
1
>>> 
>>> a < b
Comparing 111 to 20
False
>>> show()
1 comparisons
>>> 
>>> x = 10; print x**2
100
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj151/instrument.py =========
Comparing 111 to 10
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
Comparing 111 to 20
Comparing 111 to 5
Comparing 111 to 10
Comparing 111 to 15
Comparing 111 to 20
False
9 comparisons
>>> n
9
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj151/instrument.py =========
Comparing 111 to 10
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
Comparing 111 to 20
Comparing 111 to 5
Comparing 111 to 10
Comparing 111 to 15
Comparing 111 to 20
False
9 comparisons
Comparing 20 to 10
Comparing 20 to 20
True
2 comparisons
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj151/instrument.py =========
Comparing 111 to 10
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
Comparing 111 to 20
Comparing 111 to 5
Comparing 111 to 10
Comparing 111 to 15
Comparing 111 to 20
False
9 comparisons
Comparing 20 to 10
Comparing 20 to 20
True
2 comparisons
Comparing 50 to 10
Comparing 50 to 20
Comparing 50 to 30
True
3 comparisons
>>> # Sorting is n log n
>>> n
9
>>> from math import *
>>> log(n, 2)
3.1699250014423126
>>> log(n, 2) * n
28.529325012980813
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj151/instrument.py =========
Comparing 111 to 10
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
Comparing 111 to 20
Comparing 111 to 5
Comparing 111 to 10
Comparing 111 to 15
Comparing 111 to 20
False
9 comparisons
Comparing 20 to 10
Comparing 20 to 20
True
2 comparisons
Comparing 50 to 10
Comparing 50 to 20
Comparing 50 to 30
True
3 comparisons
Expected sort() cost: 28.529325013
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj151/instrument.py =========
Comparing 111 to 10
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
Comparing 111 to 20
Comparing 111 to 5
Comparing 111 to 10
Comparing 111 to 15
Comparing 111 to 20
False
9 comparisons
Comparing 20 to 10
Comparing 20 to 20
True
2 comparisons
Comparing 50 to 10
Comparing 50 to 20
Comparing 50 to 30
True
3 comparisons
Expected sort() cost: 28.529325013
Comparing 20 to 10
Comparing 30 to 20
Comparing 50 to 30
Comparing 20 to 50
Comparing 20 to 30
Comparing 20 to 20
Comparing 5 to 20
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 10 to 20
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
18 comparisons
>>> # Random number generators   -->  Knuth8
>>> # Most random number generators do a crummy job
>>> # Ah, that means that truly random data is a rarity.  Why?  Because data is hard to scramble even when we are trying.
>>> 
>>> # The norm is that most data has some order already in it.
>>> # Most research on sorts focuses on random inputs.
>>> # Can we do better?
>>> # Yes, scan for existing ordering within the dataset and use it to reduce the number of comparison
>>> # Uncle Timmy -> Timsort
>>> s
[5, 10, 10, 15, 20, 20, 20, 30, 50]
>>> from bisect import bisect
>>> cuts = [60, 70, 80, 90]
>>> grades = 'FDCBA'
>>> 
>>> score = 75
>>> grades[bisect(cuts, score)]
'C'
>>> [grades[bisect(cuts, score)] for score in [37, 99, 82, 70, 75, 81, 100, 69, 72]]
['F', 'A', 'B', 'C', 'C', 'B', 'A', 'D', 'C']
>>> # Bisecting O(log n)              n = 128   steps = 7      2 ** 7 ==> 128
>>> # Hashing O(1)                    n = 128   steps = 1.5
>>> #   \-->   key -> value
>>> # Bisecting
>>> #   \-->   range -> value
>>> n
9
>>> log(n, 2)
3.1699250014423126
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj151/instrument.py =========
Comparing 111 to 10
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
Comparing 111 to 20
Comparing 111 to 5
Comparing 111 to 10
Comparing 111 to 15
Comparing 111 to 20
False
9 comparisons
Comparing 20 to 10
Comparing 20 to 20
True
2 comparisons
Comparing 50 to 10
Comparing 50 to 20
Comparing 50 to 30
True
3 comparisons
Expected sort() cost: 28.529325013
Comparing 20 to 10
Comparing 30 to 20
Comparing 50 to 30
Comparing 20 to 50
Comparing 20 to 30
Comparing 20 to 20
Comparing 5 to 20
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 10 to 20
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
18 comparisons

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj151/instrument.py", line 44, in <module>
    reset(); bisect(s, a); show()
NameError: name 'bisect' is not defined
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj151/instrument.py =========
Comparing 111 to 10
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
Comparing 111 to 20
Comparing 111 to 5
Comparing 111 to 10
Comparing 111 to 15
Comparing 111 to 20
False
9 comparisons
Comparing 20 to 10
Comparing 20 to 20
True
2 comparisons
Comparing 50 to 10
Comparing 50 to 20
Comparing 50 to 30
True
3 comparisons
Expected sort() cost: 28.529325013
Comparing 20 to 10
Comparing 30 to 20
Comparing 50 to 30
Comparing 20 to 50
Comparing 20 to 30
Comparing 20 to 20
Comparing 5 to 20
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 10 to 20
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
18 comparisons
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
3 comparisons
>>> s
[5, 10, 10, 15, 20, 20, 20, 30, 50]
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj151/instrument.py =========
Comparing 111 to 10
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
Comparing 111 to 20
Comparing 111 to 5
Comparing 111 to 10
Comparing 111 to 15
Comparing 111 to 20
False
9 comparisons
Comparing 20 to 10
Comparing 20 to 20
True
2 comparisons
Comparing 50 to 10
Comparing 50 to 20
Comparing 50 to 30
True
3 comparisons
Expected sort() cost: 28.529325013
Comparing 20 to 10
Comparing 30 to 20
Comparing 50 to 30
Comparing 20 to 50
Comparing 20 to 30
Comparing 20 to 20
Comparing 5 to 20
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 10 to 20
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
18 comparisons
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
3 comparisons
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
3 comparisons
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj151/instrument.py =========
Comparing 111 to 10
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
Comparing 111 to 20
Comparing 111 to 5
Comparing 111 to 10
Comparing 111 to 15
Comparing 111 to 20
False
9 comparisons
Comparing 20 to 10
Comparing 20 to 20
True
2 comparisons
Comparing 50 to 10
Comparing 50 to 20
Comparing 50 to 30
True
3 comparisons
Expected sort() cost: 28.529325013
Comparing 20 to 10
Comparing 30 to 20
Comparing 50 to 30
Comparing 20 to 50
Comparing 20 to 30
Comparing 20 to 20
Comparing 5 to 20
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 10 to 20
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
18 comparisons
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
3 comparisons
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
3 comparisons
Comparing 50 to 20
Comparing 50 to 30
Comparing 50 to 50
3 comparisons
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj151/instrument.py =========
Comparing 111 to 10
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
Comparing 111 to 20
Comparing 111 to 5
Comparing 111 to 10
Comparing 111 to 15
Comparing 111 to 20
False
9 comparisons
Comparing 20 to 10
Comparing 20 to 20
True
2 comparisons
Comparing 50 to 10
Comparing 50 to 20
Comparing 50 to 30
True
3 comparisons
Expected sort() cost: 28.529325013
Comparing 20 to 10
Comparing 30 to 20
Comparing 50 to 30
Comparing 20 to 50
Comparing 20 to 30
Comparing 20 to 20
Comparing 5 to 20
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 10 to 20
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
18 comparisons
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
3 comparisons
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
3 comparisons
Comparing 50 to 20
Comparing 50 to 30
Comparing 50 to 50
3 comparisons
>>> s
[5, 10, 10, 15, 20, 20, 20, 30, 50]
>>> 2 ** 3
8
>>> 4
4
>>> 
>>> # Searching a string is O(n) and it does a substring test
>>> 
>>> 'brown' in 'the quick brown fox'
True
>>> 'bro' in 'the quick brown fox'
True
>>> # Substring tests can give false positives if you a not careful
>>> 
>>> ping_result = '20 packets sent. 20 packets received. 0.0% loss rate'
>>> assert '0.0%' in ping_result
>>> ping_result = '20 packets sent. 10 packets received. 50.0% loss rate'
>>> assert '0.0%' in ping_result
>>> 
>>> # List membership tests do EXACT matches
>>> ping_result.split()
['20', 'packets', 'sent.', '10', 'packets', 'received.', '50.0%', 'loss', 'rate']
>>> assert '50.0%' in ping_result
>>> assert '0.0%' in ping_result
>>> assert '0.0%' in ping_result.split()

Traceback (most recent call last):
  File "<pyshell#423>", line 1, in <module>
    assert '0.0%' in ping_result.split()
AssertionError
>>> 
>>> 
>>> device_status = 'Dev status:  connected'
>>> assert 'connected' in device_status
>>> device_status = 'Dev status:  disconnected'
>>> assert 'connected' in device_status
>>> assert 'connected' in device_status.split()

Traceback (most recent call last):
  File "<pyshell#430>", line 1, in <module>
    assert 'connected' in device_status.split()
AssertionError
>>> assert 'disconnected' in device_status.split()
>>> 
>>> 
>>> s = 'hello'
>>> str(s)
'hello'
>>> repr(s)
"'hello'"
>>> print s
hello
>>> s
'hello'
>>> str(10)
'10'
>>> repr(10)
'10'
>>> 
>>> 
>>> 
>>> 
>>> x = 3 + 4
>>> print x
7
>>> x = 30 + 40
>>> print x
70
>>> y = '7' + '0'
>>> print y
70
>>> 
>>> x
70
>>> y
'70'
>>> x * 5
350
>>> y * 5
'7070707070'
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj151/instrument.py =========
Comparing 111 to 10
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
Comparing 111 to 20
Comparing 111 to 5
Comparing 111 to 10
Comparing 111 to 15
Comparing 111 to 20
False
9 comparisons and 0 hashes
Comparing 20 to 10
Comparing 20 to 20
True
2 comparisons and 0 hashes
Comparing 50 to 10
Comparing 50 to 20
Comparing 50 to 30
True
3 comparisons and 0 hashes
Expected sort() cost: 28.529325013
Comparing 20 to 10
Comparing 30 to 20
Comparing 50 to 30
Comparing 20 to 50
Comparing 20 to 30
Comparing 20 to 20
Comparing 5 to 20
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 10 to 20
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
18 comparisons and 0 hashes
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
3 comparisons and 0 hashes
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
3 comparisons and 0 hashes
Comparing 50 to 20
Comparing 50 to 30
Comparing 50 to 50
3 comparisons and 0 hashes
==================================================
Hashing 20
Hashing 30
Hashing 40
Hashing 300
Hashing 400
Hashing 500
Hashing 300
Comparing 300 to 300
Hashing 400
Comparing 400 to 400
Hashing 5
Hashing 10
Hashing 15
Hashing 20
Comparing 20 to 20
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj151/instrument.py =========
Comparing 111 to 10
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
Comparing 111 to 20
Comparing 111 to 5
Comparing 111 to 10
Comparing 111 to 15
Comparing 111 to 20
False
9 comparisons and 0 hashes
Comparing 20 to 10
Comparing 20 to 20
True
2 comparisons and 0 hashes
Comparing 50 to 10
Comparing 50 to 20
Comparing 50 to 30
True
3 comparisons and 0 hashes
Expected sort() cost: 28.529325013
Comparing 20 to 10
Comparing 30 to 20
Comparing 50 to 30
Comparing 20 to 50
Comparing 20 to 30
Comparing 20 to 20
Comparing 5 to 20
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 10 to 20
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
18 comparisons and 0 hashes
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
3 comparisons and 0 hashes
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
3 comparisons and 0 hashes
Comparing 50 to 20
Comparing 50 to 30
Comparing 50 to 50
3 comparisons and 0 hashes
==================================================
Hashing 20
Hashing 30
Hashing 40
Hashing 300
Hashing 400
Hashing 500
Hashing 300
Comparing 300 to 300
Hashing 400
Comparing 400 to 400
Hashing 5
Hashing 10
Hashing 15
Hashing 20
Comparing 20 to 20
Hashing 10
Hashing 20
Hashing 30
Hashing 50
Hashing 20
Comparing 20 to 20
Hashing 5
Hashing 10
Comparing 10 to 10
Hashing 15
Hashing 20
Comparing 20 to 20
3 comparisons and 9 hashes
>>> otherdata
[20, 30, 40, 300, 400, 500, 300, 400, 5, 10, 15, 20]
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj151/instrument.py =========
Comparing 111 to 10
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
Comparing 111 to 20
Comparing 111 to 5
Comparing 111 to 10
Comparing 111 to 15
Comparing 111 to 20
False
9 comparisons and 0 hashes
Comparing 20 to 10
Comparing 20 to 20
True
2 comparisons and 0 hashes
Comparing 50 to 10
Comparing 50 to 20
Comparing 50 to 30
True
3 comparisons and 0 hashes
Expected sort() cost: 28.529325013
Comparing 20 to 10
Comparing 30 to 20
Comparing 50 to 30
Comparing 20 to 50
Comparing 20 to 30
Comparing 20 to 20
Comparing 5 to 20
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 10 to 20
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
18 comparisons and 0 hashes
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
3 comparisons and 0 hashes
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
3 comparisons and 0 hashes
Comparing 50 to 20
Comparing 50 to 30
Comparing 50 to 50
3 comparisons and 0 hashes
==================================================
Hashing 20
Hashing 30
Hashing 40
Hashing 300
Hashing 400
Hashing 500
Hashing 300
Comparing 300 to 300
Hashing 400
Comparing 400 to 400
Hashing 5
Hashing 10
Hashing 15
Hashing 20
Comparing 20 to 20
Hashing 10
Hashing 20
Hashing 30
Hashing 50
Hashing 20
Comparing 20 to 20
Hashing 5
Hashing 10
Comparing 10 to 10
Hashing 15
Hashing 20
Comparing 20 to 20
3 comparisons and 9 hashes
Comparing 111 to 10
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
Comparing 111 to 20
Comparing 111 to 5
Comparing 111 to 10
Comparing 111 to 15
Comparing 111 to 20
False
9 comparisons and 0 hashes
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj151/instrument.py =========
Comparing 111 to 10
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
Comparing 111 to 20
Comparing 111 to 5
Comparing 111 to 10
Comparing 111 to 15
Comparing 111 to 20
False
9 comparisons and 0 hashes
Comparing 20 to 10
Comparing 20 to 20
True
2 comparisons and 0 hashes
Comparing 50 to 10
Comparing 50 to 20
Comparing 50 to 30
True
3 comparisons and 0 hashes
Expected sort() cost: 28.529325013
Comparing 20 to 10
Comparing 30 to 20
Comparing 50 to 30
Comparing 20 to 50
Comparing 20 to 30
Comparing 20 to 20
Comparing 5 to 20
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 10 to 20
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
18 comparisons and 0 hashes
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
3 comparisons and 0 hashes
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
3 comparisons and 0 hashes
Comparing 50 to 20
Comparing 50 to 30
Comparing 50 to 50
3 comparisons and 0 hashes
==================================================
Hashing 20
Hashing 30
Hashing 40
Hashing 300
Hashing 400
Hashing 500
Hashing 300
Comparing 300 to 300
Hashing 400
Comparing 400 to 400
Hashing 5
Hashing 10
Hashing 15
Hashing 20
Comparing 20 to 20
Hashing 10
Hashing 20
Hashing 30
Hashing 50
Hashing 20
Comparing 20 to 20
Hashing 5
Hashing 10
Comparing 10 to 10
Hashing 15
Hashing 20
Comparing 20 to 20
3 comparisons and 9 hashes
Hashing 111
False
0 comparisons and 1 hashes
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj151/instrument.py =========
Comparing 111 to 10
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
Comparing 111 to 20
Comparing 111 to 5
Comparing 111 to 10
Comparing 111 to 15
Comparing 111 to 20
False
9 comparisons and 0 hashes
Comparing 20 to 10
Comparing 20 to 20
True
2 comparisons and 0 hashes
Comparing 50 to 10
Comparing 50 to 20
Comparing 50 to 30
True
3 comparisons and 0 hashes
Expected sort() cost: 28.529325013
Comparing 20 to 10
Comparing 30 to 20
Comparing 50 to 30
Comparing 20 to 50
Comparing 20 to 30
Comparing 20 to 20
Comparing 5 to 20
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 10 to 20
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
18 comparisons and 0 hashes
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
3 comparisons and 0 hashes
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
3 comparisons and 0 hashes
Comparing 50 to 20
Comparing 50 to 30
Comparing 50 to 50
3 comparisons and 0 hashes
==================================================
Hashing 20
Hashing 30
Hashing 40
Hashing 300
Hashing 400
Hashing 500
Hashing 300
Comparing 300 to 300
Hashing 400
Comparing 400 to 400
Hashing 5
Hashing 10
Hashing 15
Hashing 20
Comparing 20 to 20
Hashing 10
Hashing 20
Hashing 30
Hashing 50
Hashing 20
Comparing 20 to 20
Hashing 5
Hashing 10
Comparing 10 to 10
Hashing 15
Hashing 20
Comparing 20 to 20
3 comparisons and 9 hashes
Hashing 111
False
0 comparisons and 1 hashes
Hashing 20
Comparing 20 to 20
True
1 comparisons and 1 hashes
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj151/instrument.py =========
Comparing 111 to 10
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
Comparing 111 to 20
Comparing 111 to 5
Comparing 111 to 10
Comparing 111 to 15
Comparing 111 to 20
False
9 comparisons and 0 hashes
Comparing 20 to 10
Comparing 20 to 20
True
2 comparisons and 0 hashes
Comparing 50 to 10
Comparing 50 to 20
Comparing 50 to 30
True
3 comparisons and 0 hashes
Expected sort() cost: 28.529325013
Comparing 20 to 10
Comparing 30 to 20
Comparing 50 to 30
Comparing 20 to 50
Comparing 20 to 30
Comparing 20 to 20
Comparing 5 to 20
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 10 to 20
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
18 comparisons and 0 hashes
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
3 comparisons and 0 hashes
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
3 comparisons and 0 hashes
Comparing 50 to 20
Comparing 50 to 30
Comparing 50 to 50
3 comparisons and 0 hashes
==================================================
Hashing 20
Hashing 30
Hashing 40
Hashing 300
Hashing 400
Hashing 500
Hashing 300
Comparing 300 to 300
Hashing 400
Comparing 400 to 400
Hashing 5
Hashing 10
Hashing 15
Hashing 20
Comparing 20 to 20
Hashing 10
Hashing 20
Hashing 30
Hashing 50
Hashing 20
Comparing 20 to 20
Hashing 5
Hashing 10
Comparing 10 to 10
Hashing 15
Hashing 20
Comparing 20 to 20
3 comparisons and 9 hashes
Hashing 111
False
0 comparisons and 1 hashes
Hashing 20
Comparing 20 to 20
True
1 comparisons and 1 hashes
Hashing 50
True
0 comparisons and 1 hashes
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj151/instrument.py =========
Comparing 111 to 10
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
Comparing 111 to 20
Comparing 111 to 5
Comparing 111 to 10
Comparing 111 to 15
Comparing 111 to 20
False
9 comparisons and 0 hashes
Comparing 20 to 10
Comparing 20 to 20
True
2 comparisons and 0 hashes
Comparing 50 to 10
Comparing 50 to 20
Comparing 50 to 30
True
3 comparisons and 0 hashes
Expected sort() cost: 28.529325013
Comparing 20 to 10
Comparing 30 to 20
Comparing 50 to 30
Comparing 20 to 50
Comparing 20 to 30
Comparing 20 to 20
Comparing 5 to 20
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 10 to 20
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
18 comparisons and 0 hashes
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
3 comparisons and 0 hashes
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
3 comparisons and 0 hashes
Comparing 50 to 20
Comparing 50 to 30
Comparing 50 to 50
3 comparisons and 0 hashes
==================================================
Hashing 20
Hashing 30
Hashing 40
Hashing 300
Hashing 400
Hashing 500
Hashing 300
Comparing 300 to 300
Hashing 400
Comparing 400 to 400
Hashing 5
Hashing 10
Hashing 15
Hashing 20
Comparing 20 to 20
Hashing 10
Hashing 20
Hashing 30
Hashing 50
Hashing 20
Comparing 20 to 20
Hashing 5
Hashing 10
Comparing 10 to 10
Hashing 15
Hashing 20
Comparing 20 to 20
3 comparisons and 9 hashes
Hashing 111
False
0 comparisons and 1 hashes
Hashing 20
Comparing 20 to 20
True
1 comparisons and 1 hashes
Hashing 50
True
0 comparisons and 1 hashes
Using sets is MUCH cheaper than building them
0 comparisons and 0 hashes
>>> dict.fromkeys(t)
{50: None, 20: None, 5: None, 10: None, 30: None, 15: None}
>>> dict.fromkeys(t, 0)
{50: 0, 20: 0, 5: 0, 10: 0, 30: 0, 15: 0}
>>> dict.fromkeys(t, None)
{50: None, 20: None, 5: None, 10: None, 30: None, 15: None}
>>> dict.fromkeys(t, '')
{50: '', 20: '', 5: '', 10: '', 30: '', 15: ''}
>>> dict.fromkeys(t, 'unknown')
{50: 'unknown', 20: 'unknown', 5: 'unknown', 10: 'unknown', 30: 'unknown', 15: 'unknown'}
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj151/instrument.py =========
Comparing 111 to 10
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
Comparing 111 to 20
Comparing 111 to 5
Comparing 111 to 10
Comparing 111 to 15
Comparing 111 to 20
False
9 comparisons and 0 hashes
Comparing 20 to 10
Comparing 20 to 20
True
2 comparisons and 0 hashes
Comparing 50 to 10
Comparing 50 to 20
Comparing 50 to 30
True
3 comparisons and 0 hashes
Expected sort() cost: 28.529325013
Comparing 20 to 10
Comparing 30 to 20
Comparing 50 to 30
Comparing 20 to 50
Comparing 20 to 30
Comparing 20 to 20
Comparing 5 to 20
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 10 to 20
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
18 comparisons and 0 hashes
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
3 comparisons and 0 hashes
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
3 comparisons and 0 hashes
Comparing 50 to 20
Comparing 50 to 30
Comparing 50 to 50
3 comparisons and 0 hashes
==================================================
Hashing 20
Hashing 30
Hashing 40
Hashing 300
Hashing 400
Hashing 500
Hashing 300
Comparing 300 to 300
Hashing 400
Comparing 400 to 400
Hashing 5
Hashing 10
Hashing 15
Hashing 20
Comparing 20 to 20
Hashing 10
Hashing 20
Hashing 30
Hashing 50
Hashing 20
Comparing 20 to 20
Hashing 5
Hashing 10
Comparing 10 to 10
Hashing 15
Hashing 20
Comparing 20 to 20
3 comparisons and 9 hashes
Hashing 111
False
0 comparisons and 1 hashes
Hashing 20
Comparing 20 to 20
True
1 comparisons and 1 hashes
Hashing 50
True
0 comparisons and 1 hashes
Using sets is MUCH cheaper than building them
0 comparisons and 0 hashes
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
3 comparisons and 0 hashes
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj151/instrument.py =========
Comparing 111 to 10
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
Comparing 111 to 20
Comparing 111 to 5
Comparing 111 to 10
Comparing 111 to 15
Comparing 111 to 20
False
9 comparisons and 0 hashes
Comparing 20 to 10
Comparing 20 to 20
True
2 comparisons and 0 hashes
Comparing 50 to 10
Comparing 50 to 20
Comparing 50 to 30
True
3 comparisons and 0 hashes
Expected sort() cost: 28.529325013
Comparing 20 to 10
Comparing 30 to 20
Comparing 50 to 30
Comparing 20 to 50
Comparing 20 to 30
Comparing 20 to 20
Comparing 5 to 20
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 10 to 20
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
18 comparisons and 0 hashes
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
3 comparisons and 0 hashes
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
3 comparisons and 0 hashes
Comparing 50 to 20
Comparing 50 to 30
Comparing 50 to 50
3 comparisons and 0 hashes
==================================================
Hashing 20
Hashing 30
Hashing 40
Hashing 300
Hashing 400
Hashing 500
Hashing 300
Comparing 300 to 300
Hashing 400
Comparing 400 to 400
Hashing 5
Hashing 10
Hashing 15
Hashing 20
Comparing 20 to 20
Hashing 10
Hashing 20
Hashing 30
Hashing 50
Hashing 20
Comparing 20 to 20
Hashing 5
Hashing 10
Comparing 10 to 10
Hashing 15
Hashing 20
Comparing 20 to 20
3 comparisons and 9 hashes
Hashing 111
False
0 comparisons and 1 hashes
Hashing 20
Comparing 20 to 20
True
1 comparisons and 1 hashes
Hashing 50
True
0 comparisons and 1 hashes
Using sets is MUCH cheaper than building them
0 comparisons and 0 hashes
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
3 comparisons and 0 hashes
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
3 comparisons and 0 hashes
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj151/instrument.py =========
Comparing 111 to 10
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
Comparing 111 to 20
Comparing 111 to 5
Comparing 111 to 10
Comparing 111 to 15
Comparing 111 to 20
False
9 comparisons and 0 hashes
Comparing 20 to 10
Comparing 20 to 20
True
2 comparisons and 0 hashes
Comparing 50 to 10
Comparing 50 to 20
Comparing 50 to 30
True
3 comparisons and 0 hashes
Expected sort() cost: 28.529325013
Comparing 20 to 10
Comparing 30 to 20
Comparing 50 to 30
Comparing 20 to 50
Comparing 20 to 30
Comparing 20 to 20
Comparing 5 to 20
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 10 to 20
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
18 comparisons and 0 hashes
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
3 comparisons and 0 hashes
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
3 comparisons and 0 hashes
Comparing 50 to 20
Comparing 50 to 30
Comparing 50 to 50
3 comparisons and 0 hashes
==================================================
Hashing 20
Hashing 30
Hashing 40
Hashing 300
Hashing 400
Hashing 500
Hashing 300
Comparing 300 to 300
Hashing 400
Comparing 400 to 400
Hashing 5
Hashing 10
Hashing 15
Hashing 20
Comparing 20 to 20
Hashing 10
Hashing 20
Hashing 30
Hashing 50
Hashing 20
Comparing 20 to 20
Hashing 5
Hashing 10
Comparing 10 to 10
Hashing 15
Hashing 20
Comparing 20 to 20
3 comparisons and 9 hashes
Hashing 111
False
0 comparisons and 1 hashes
Hashing 20
Comparing 20 to 20
True
1 comparisons and 1 hashes
Hashing 50
True
0 comparisons and 1 hashes
Using sets is MUCH cheaper than building them
0 comparisons and 0 hashes
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
3 comparisons and 0 hashes
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
3 comparisons and 0 hashes
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
3 comparisons and 0 hashes
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
3 comparisons and 0 hashes
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj151/instrument.py =========
Comparing 111 to 10
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
Comparing 111 to 20
Comparing 111 to 5
Comparing 111 to 10
Comparing 111 to 15
Comparing 111 to 20
False
9 comparisons and 0 hashes
Comparing 20 to 10
Comparing 20 to 20
True
2 comparisons and 0 hashes
Comparing 50 to 10
Comparing 50 to 20
Comparing 50 to 30
True
3 comparisons and 0 hashes
Expected sort() cost: 28.529325013
Comparing 20 to 10
Comparing 30 to 20
Comparing 50 to 30
Comparing 20 to 50
Comparing 20 to 30
Comparing 20 to 20
Comparing 5 to 20
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 10 to 20
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
18 comparisons and 0 hashes
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
3 comparisons and 0 hashes
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
3 comparisons and 0 hashes
Comparing 50 to 20
Comparing 50 to 30
Comparing 50 to 50
3 comparisons and 0 hashes
==================================================
Hashing 20
Hashing 30
Hashing 40
Hashing 300
Hashing 400
Hashing 500
Hashing 300
Comparing 300 to 300
Hashing 400
Comparing 400 to 400
Hashing 5
Hashing 10
Hashing 15
Hashing 20
Comparing 20 to 20
Hashing 10
Hashing 20
Hashing 30
Hashing 50
Hashing 20
Comparing 20 to 20
Hashing 5
Hashing 10
Comparing 10 to 10
Hashing 15
Hashing 20
Comparing 20 to 20
3 comparisons and 9 hashes
Hashing 111
False
0 comparisons and 1 hashes
Hashing 20
Comparing 20 to 20
True
1 comparisons and 1 hashes
Hashing 50
True
0 comparisons and 1 hashes
Using sets is MUCH cheaper than building them
0 comparisons and 0 hashes
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
3 comparisons and 0 hashes
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
3 comparisons and 0 hashes
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
3 comparisons and 0 hashes
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
3 comparisons and 0 hashes
Fun for April fools
>>> hash(a)
0
>>> hash(a)
0
>>> hash(a)
0
>>> hash(a)
1
>>> hash(a)
0
>>> 
>>> s
set([50])
>>> list(s)
[50]
>>> a in list(s)
True
>>> a in s
True
>>> a in s
True
>>> a in s
True
>>> a in s
False
>>> a in s
True
>>> a in s
True
>>> a in s
True
>>> # s = {a}
>>> # [- - - - - - - -]
>>> # hash(a) -> 1
>>> # [- a - - - - - -]
>>> # [- 1 - - - - - -]
>>> 
>>> # a in s
>>> # hash(a) -> 1
>>> # h[1] == 1 and a is k[1] or a == k[1]
>>> 
>>> # a in s
>>> # hash(a) -> 0
>>> # h[0] is empty
>>> 
>>> 
>>> 
>>> # Strings cache the hash value
>>> # Int have a very cheap hash
>>> hash(12345)
12345
>>> {1: 'uno', 2: 'dos', 3: 'tres', 4: 'quatro'}
{1: 'uno', 2: 'dos', 3: 'tres', 4: 'quatro'}
>>> 
>>> # tuples don't cache
>>> # frozensets do cache
>>> 
>>> 
>>> # caching cases:  int, str, frozenset
>>> # uncached: everything else
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj151/instrument.py =========
Comparing 111 to 10
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
Comparing 111 to 20
Comparing 111 to 5
Comparing 111 to 10
Comparing 111 to 15
Comparing 111 to 20
False
9 comparisons and 0 hashes
Comparing 20 to 10
Comparing 20 to 20
True
2 comparisons and 0 hashes
Comparing 50 to 10
Comparing 50 to 20
Comparing 50 to 30
True
3 comparisons and 0 hashes
Expected sort() cost: 28.529325013
Comparing 20 to 10
Comparing 30 to 20
Comparing 50 to 30
Comparing 20 to 50
Comparing 20 to 30
Comparing 20 to 20
Comparing 5 to 20
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 10 to 20
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
18 comparisons and 0 hashes
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
3 comparisons and 0 hashes
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
3 comparisons and 0 hashes
Comparing 50 to 20
Comparing 50 to 30
Comparing 50 to 50
3 comparisons and 0 hashes
==================================================
Hashing 20
Hashing 30
Hashing 40
Hashing 300
Hashing 400
Hashing 500
Hashing 300
Comparing 300 to 300
Hashing 400
Comparing 400 to 400
Hashing 5
Hashing 10
Hashing 15
Hashing 20
Comparing 20 to 20
Hashing 10
Hashing 20
Hashing 30
Hashing 50
Hashing 20
Comparing 20 to 20
Hashing 5
Hashing 10
Comparing 10 to 10
Hashing 15
Hashing 20
Comparing 20 to 20
3 comparisons and 9 hashes
Hashing 111
False
0 comparisons and 1 hashes
Hashing 20
Comparing 20 to 20
True
1 comparisons and 1 hashes
Hashing 50
True
0 comparisons and 1 hashes
Using sets is MUCH cheaper than building them
0 comparisons and 0 hashes
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
3 comparisons and 0 hashes
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
3 comparisons and 0 hashes
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
3 comparisons and 0 hashes
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
3 comparisons and 0 hashes
Fun for April fools
We just learned that if a hash is random, the object may become unfindable
There is a hash homomorphism:
If x == y, then hash(x) should equal to the hash(y)
>>> len(names)
6
>>> set(names)
set(['RACHEL', 'Raymond', 'MATTHEW', 'rachel', 'Matthew', 'raymond'])
>>> map(hash, names)
[9209434560778162597, -9091735575445484789, -3515634699177859695, 2729357497184525765, 6811592994604243659, 3415212463549153425]
>>> names
['Raymond', 'rachel', 'MATTHEW', 'raymond', 'RACHEL', 'Matthew']
>>> names[0] != names[3]
True
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj151/instrument.py =========
Comparing 111 to 10
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
Comparing 111 to 20
Comparing 111 to 5
Comparing 111 to 10
Comparing 111 to 15
Comparing 111 to 20
False
9 comparisons and 0 hashes
Comparing 20 to 10
Comparing 20 to 20
True
2 comparisons and 0 hashes
Comparing 50 to 10
Comparing 50 to 20
Comparing 50 to 30
True
3 comparisons and 0 hashes
Expected sort() cost: 28.529325013
Comparing 20 to 10
Comparing 30 to 20
Comparing 50 to 30
Comparing 20 to 50
Comparing 20 to 30
Comparing 20 to 20
Comparing 5 to 20
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 10 to 20
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
18 comparisons and 0 hashes
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
3 comparisons and 0 hashes
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
3 comparisons and 0 hashes
Comparing 50 to 20
Comparing 50 to 30
Comparing 50 to 50
3 comparisons and 0 hashes
==================================================
Hashing 20
Hashing 30
Hashing 40
Hashing 300
Hashing 400
Hashing 500
Hashing 300
Comparing 300 to 300
Hashing 400
Comparing 400 to 400
Hashing 5
Hashing 10
Hashing 15
Hashing 20
Comparing 20 to 20
Hashing 10
Hashing 20
Hashing 30
Hashing 50
Hashing 20
Comparing 20 to 20
Hashing 5
Hashing 10
Comparing 10 to 10
Hashing 15
Hashing 20
Comparing 20 to 20
3 comparisons and 9 hashes
Hashing 111
False
0 comparisons and 1 hashes
Hashing 20
Comparing 20 to 20
True
1 comparisons and 1 hashes
Hashing 50
True
0 comparisons and 1 hashes
Using sets is MUCH cheaper than building them
0 comparisons and 0 hashes
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
3 comparisons and 0 hashes
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
3 comparisons and 0 hashes
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
3 comparisons and 0 hashes
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
3 comparisons and 0 hashes
Fun for April fools
We just learned that if a hash is random, the object may become unfindable
There is a hash homomorphism:
If x == y, then hash(x) should equal to the hash(y)
>>> len(names)
6
>>> map(type, names)
[<class '__main__.Str'>, <class '__main__.Str'>, <class '__main__.Str'>, <class '__main__.Str'>, <class '__main__.Str'>, <class '__main__.Str'>]
>>> set(map(type, names))
set([<class '__main__.Str'>])
>>> len(set(map(type, names)))
1
>>> 
>>> names[0] != names[3]
True
>>> names[0] == names[3]
True
>>> names[0]
'Raymond'
>>> names[3]
'raymond'
>>> 
>>> 
>>> 
>>> 
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj151/instrument.py =========
Comparing 111 to 10
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
Comparing 111 to 20
Comparing 111 to 5
Comparing 111 to 10
Comparing 111 to 15
Comparing 111 to 20
False
9 comparisons and 0 hashes
Comparing 20 to 10
Comparing 20 to 20
True
2 comparisons and 0 hashes
Comparing 50 to 10
Comparing 50 to 20
Comparing 50 to 30
True
3 comparisons and 0 hashes
Expected sort() cost: 28.529325013
Comparing 20 to 10
Comparing 30 to 20
Comparing 50 to 30
Comparing 20 to 50
Comparing 20 to 30
Comparing 20 to 20
Comparing 5 to 20
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 10 to 20
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
18 comparisons and 0 hashes
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
3 comparisons and 0 hashes
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
3 comparisons and 0 hashes
Comparing 50 to 20
Comparing 50 to 30
Comparing 50 to 50
3 comparisons and 0 hashes
==================================================
Hashing 20
Hashing 30
Hashing 40
Hashing 300
Hashing 400
Hashing 500
Hashing 300
Comparing 300 to 300
Hashing 400
Comparing 400 to 400
Hashing 5
Hashing 10
Hashing 15
Hashing 20
Comparing 20 to 20
Hashing 10
Hashing 20
Hashing 30
Hashing 50
Hashing 20
Comparing 20 to 20
Hashing 5
Hashing 10
Comparing 10 to 10
Hashing 15
Hashing 20
Comparing 20 to 20
3 comparisons and 9 hashes
Hashing 111
False
0 comparisons and 1 hashes
Hashing 20
Comparing 20 to 20
True
1 comparisons and 1 hashes
Hashing 50
True
0 comparisons and 1 hashes
Using sets is MUCH cheaper than building them
0 comparisons and 0 hashes
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
3 comparisons and 0 hashes
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
3 comparisons and 0 hashes
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
3 comparisons and 0 hashes
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
3 comparisons and 0 hashes
Fun for April fools
We just learned that if a hash is random, the object may become unfindable
There is a hash homomorphism:
If x == y, then hash(x) should equal to the hash(y)
>>> 
>>> names[0] == names[3]
True
>>> names[0] != names[3]
False
>>> set(names)
set(['RACHEL', 'Raymond', 'MATTHEW', 'rachel', 'Matthew', 'raymond'])
>>> names[0] == names[3]
True
>>> hash(names[0]) == hash(names[3])
False
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj151/instrument.py =========
Comparing 111 to 10
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
Comparing 111 to 20
Comparing 111 to 5
Comparing 111 to 10
Comparing 111 to 15
Comparing 111 to 20
False
9 comparisons and 0 hashes
Comparing 20 to 10
Comparing 20 to 20
True
2 comparisons and 0 hashes
Comparing 50 to 10
Comparing 50 to 20
Comparing 50 to 30
True
3 comparisons and 0 hashes
Expected sort() cost: 28.529325013
Comparing 20 to 10
Comparing 30 to 20
Comparing 50 to 30
Comparing 20 to 50
Comparing 20 to 30
Comparing 20 to 20
Comparing 5 to 20
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 10 to 20
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
18 comparisons and 0 hashes
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
3 comparisons and 0 hashes
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
3 comparisons and 0 hashes
Comparing 50 to 20
Comparing 50 to 30
Comparing 50 to 50
3 comparisons and 0 hashes
==================================================
Hashing 20
Hashing 30
Hashing 40
Hashing 300
Hashing 400
Hashing 500
Hashing 300
Comparing 300 to 300
Hashing 400
Comparing 400 to 400
Hashing 5
Hashing 10
Hashing 15
Hashing 20
Comparing 20 to 20
Hashing 10
Hashing 20
Hashing 30
Hashing 50
Hashing 20
Comparing 20 to 20
Hashing 5
Hashing 10
Comparing 10 to 10
Hashing 15
Hashing 20
Comparing 20 to 20
3 comparisons and 9 hashes
Hashing 111
False
0 comparisons and 1 hashes
Hashing 20
Comparing 20 to 20
True
1 comparisons and 1 hashes
Hashing 50
True
0 comparisons and 1 hashes
Using sets is MUCH cheaper than building them
0 comparisons and 0 hashes
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
3 comparisons and 0 hashes
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
3 comparisons and 0 hashes
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
3 comparisons and 0 hashes
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
3 comparisons and 0 hashes
Fun for April fools
We just learned that if a hash is random, the object may become unfindable
There is a hash homomorphism:
If x == y, then hash(x) should equal to the hash(y)
>>> hash(names[0]) == hash(names[3])
True
>>> names[0] == names[3]
True
>>> set(names)
set(['MATTHEW', 'rachel', 'Raymond'])
>>> 
>>> 
>>> type(names[0])
<class '__main__.Str'>
>>> type(names[0].lower())
<type 'str'>
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/sj151/instrument.py =========
Comparing 111 to 10
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
Comparing 111 to 20
Comparing 111 to 5
Comparing 111 to 10
Comparing 111 to 15
Comparing 111 to 20
False
9 comparisons and 0 hashes
Comparing 20 to 10
Comparing 20 to 20
True
2 comparisons and 0 hashes
Comparing 50 to 10
Comparing 50 to 20
Comparing 50 to 30
True
3 comparisons and 0 hashes
Expected sort() cost: 28.529325013
Comparing 20 to 10
Comparing 30 to 20
Comparing 50 to 30
Comparing 20 to 50
Comparing 20 to 30
Comparing 20 to 20
Comparing 5 to 20
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 10 to 20
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
18 comparisons and 0 hashes
Comparing 111 to 20
Comparing 111 to 30
Comparing 111 to 50
3 comparisons and 0 hashes
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
3 comparisons and 0 hashes
Comparing 50 to 20
Comparing 50 to 30
Comparing 50 to 50
3 comparisons and 0 hashes
==================================================
Hashing 20
Hashing 30
Hashing 40
Hashing 300
Hashing 400
Hashing 500
Hashing 300
Comparing 300 to 300
Hashing 400
Comparing 400 to 400
Hashing 5
Hashing 10
Hashing 15
Hashing 20
Comparing 20 to 20
Hashing 10
Hashing 20
Hashing 30
Hashing 50
Hashing 20
Comparing 20 to 20
Hashing 5
Hashing 10
Comparing 10 to 10
Hashing 15
Hashing 20
Comparing 20 to 20
3 comparisons and 9 hashes
Hashing 111
False
0 comparisons and 1 hashes
Hashing 20
Comparing 20 to 20
True
1 comparisons and 1 hashes
Hashing 50
True
0 comparisons and 1 hashes
Using sets is MUCH cheaper than building them
0 comparisons and 0 hashes
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
3 comparisons and 0 hashes
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
3 comparisons and 0 hashes
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
3 comparisons and 0 hashes
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
3 comparisons and 0 hashes
Fun for April fools
We just learned that if a hash is random, the object may become unfindable
There is a hash homomorphism:
If x == y, then hash(x) should equal to the hash(y)
set(['MATTHEW', 'rachel', 'Raymond'])
>>> 
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj151/download.py ==========
============================ Source: http://sdwa.appliomics.com/u/3967849/sj151/links.txt ===========================
                                    Starting download at Mon Oct 17 17:33:07 2016                                    
304  NOT MODIFIED     http://dl.dropbox.com/u/3967849/shared/FunWithNewerTools.pdf
304  NOT MODIFIED     http://dl.dropbox.com/u/3967849/shared/ps_favicon.ico
200  OK               http://dl.dropbox.com/u/3967849/sj151/instrument.py     --> notes3/instrument.py      (updated) 
200* OK               http://dl.dropbox.com/u/3967849/shared/proverbs_en.txt  --> notes3/proverbs_en.txt    (current) 
200* OK               http://dl.dropbox.com/u/3967849/shared/proverbs_es.txt  --> notes3/proverbs_es.txt    (current) 
304  NOT MODIFIED     http://dl.dropbox.com/u/3967849/sj151/cbitarray.c
200  OK               http://dl.dropbox.com/u/3967849/sj151/day1.py           --> notes3/day1.py            (updated) 
304  NOT MODIFIED     http://dl.dropbox.com/u/3967849/sj151/download.py
304  NOT MODIFIED     http://dl.dropbox.com/u/3967849/shared/mpl_demo.py
304  NOT MODIFIED     http://dl.dropbox.com/u/3967849/shared/ArtOfSubclassing.pdf
304  NOT MODIFIED     http://dl.dropbox.com/u/3967849/shared/unicode.pdf
200* OK               http://dl.dropbox.com/u/3967849/shared/hamlet.txt       --> notes3/hamlet.txt         (current) 
304  NOT MODIFIED     http://dl.dropbox.com/u/3967849/shared/lru_cache.py
304  NOT MODIFIED     http://dl.dropbox.com/u/3967849/shared/bottle.py
200* OK               http://dl.dropbox.com/u/3967849/sj151/links.txt         --> notes3/links.txt          (updated) 
304  NOT MODIFIED     http://dl.dropbox.com/u/3967849/shared/beautifulsoup4-4.1.0.tar.gz
200* OK               http://dl.dropbox.com/u/3967849/shared/the_great_gatsby.txt --> notes3/the_great_gatsby.txt (current) 
304  NOT MODIFIED     http://dl.dropbox.com/u/3967849/shared/CSDMC2010_SPAM.zip
200* OK               http://dl.dropbox.com/u/3967849/shared/words.txt        --> notes3/words.txt          (current) 
304  NOT MODIFIED     http://dl.dropbox.com/u/3967849/shared/using-gdb-pdb.pdf
304  NOT MODIFIED     http://dl.dropbox.com/u/3967849/shared/CoreContainers.pdf
304  NOT MODIFIED     http://dl.dropbox.com/u/3967849/shared/descriptors.pdf
200* OK               http://dl.dropbox.com/u/3967849/shared/big.txt          --> notes3/big.txt            (current) 
>>> # 3 minutes to review the summary slides in notes3/CoreContainers.pdf
>>> # 10 minutes to review: http://sdwa.appliomics.com/u/3967849/sj151/pub/instrument.html
>>> # 2 minutes to install Python-2:  http://bit.ly/py-install

>>> # Class website:   http://bit.ly/python-sj151
>>> 
