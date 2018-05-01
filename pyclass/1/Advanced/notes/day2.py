Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 26 2016, 12:10:39) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 

>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/spell_check.py ========
Now,
iss
the
tymme
for
all
guhd
men
tooo
comee
to
the
ayd
of
thur
country
and
city.
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/spell_check.py ========
Now,
iss
the
tymme
for
all
guhd
men
tooo
comee
to
the
ayd
of
thur
country
and
city.
>>> # \w  <-- Wrong!
>>> # \W  <-- More Wrong!
>>> re.findall(r'\w+', "Don't you forget about me")
['Don', 't', 'you', 'forget', 'about', 'me']
>>> re.findall(r'\w+', "Re-invent yourself")
['Re', 'invent', 'yourself']
>>> re.findall(r'\w+', "1. Count the words")
['1', 'Count', 'the', 'words']
>>> re.findall(r'\w+', "Dunder __ methods __")
['Dunder', '__', 'methods', '__']
>>> # Two false positives:   numbers and underscores
>>> # Two false negatives:   apostrophes and hyphens
>>> re.findall(r"[A-Za-z\-\']+", "Don't you forget about me")
["Don't", 'you', 'forget', 'about', 'me']
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/spell_check.py ========
now
iss
the
tymme
for
all
guhd
men
tooo
comee
to
the
ayd
of
thur
country
and
city
>>> # a in s       s.__contains__(a)
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/spell_check.py ========
Misspelled:
-----------
iss
tymme
guhd
tooo
comee
ayd
thur
and
city
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/spell_check.py ========
Misspelled:
-----------
iss
tymme
guhd
tooo
comee
ayd
thur
and
city
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/spell_check.py ========
Misspelled:
-----------
iss
tymme
guhd
ood
tooo
comee
ayd
thur
and
city
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/spell_check.py ========
Misspelled:
-----------
iss
tymme
guhd
ood
tooo
comee
ayd
thur
and
city
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/spell_check.py ========
Misspelled:
-----------
iss
tymme
guhd
ood
tooo
comee
ayd
thur
>>> 
>>> f
<closed file 'notes3/words.txt', mode 'r' at 0x102fc4c00>
>>> type(correct)
<type 'list'>
>>> len(correct)
235886
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/spell_check.py ========
Misspelled:
-----------

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj151/spell_check.py", line 28, in <module>
    if word not in correct:
TypeError: argument of type 'NoneType' is not iterable
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/spell_check.py ========
Misspelled:
-----------
iss
tymme
guhd
ood
tooo
comee
ayd
thur
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/spell_check.py ========
Misspelled:
-----------
iss
tymme
guhd
ood
tooo
comee
ayd
thur
>>> from math import pi
>>> from math import *
>>> import pi

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    import pi
ImportError: No module named pi
>>> 
>>> import math
>>> math.cos(3)
-0.9899924966004454
>>> 
=============================== RESTART: Shell ===============================
>>> import math
>>> math.cos(3.0)
-0.9899924966004454
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> import random            # The entire loads in memory
>>>                          # The word "random" in globals in bound the module object
                         
>>> random.randrange(200)
74
>>> 
=============================== RESTART: Shell ===============================
>>> from random import randrange        # The entire loads in memory
>>>                                     # The word "randrange" in globals in bound to the function object
                                    
>>> randrange
<bound method Random.randrange of <random.Random object at 0x10110f820>>
>>> 
>>> # The presence of __init__.py
>>> #     It allows the directory to do a package import
>>> 
>>> 
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>> type(checker)

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    type(checker)
NameError: name 'checker' is not defined
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/spell_check.py ========
Misspelled:
-----------
iss
tymme
guhd
ood
tooo
comee
ayd
thur
>>> type(checker)
<type 'list'>
>>> len(checker)
235886
>>> len(checker) // 2
117943
>>> len(checker)
235886
>>> 
>>> 
>>> cw = 10000
>>> iw =    50
>>> 
>>> cw * len(checker) // 2 + iw * len(checker)
1191224300
>>> 
>>> 
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/spell_check.py ========
Misspelled:
-----------
iss
tymme
guhd
ood
tooo
comee
ayd
thur
>>> 235000 # hashes
235000
>>> # 1 compare per duplicate
>>> cw = 10000
>>> # 10050 hashes   10000 compares
>>> text = set(re.findall(r"[a-z\-\']+", text.lower()))
>>> text - checker
set(['tymme', 'ood', 'iss', 'tooo', 'thur', 'comee', 'ayd', 'guhd'])
>>> 
>>> def mymin(a, b):
	return a if a < b else b

>>> mymin(10, 20)
10
>>> mymin(20, 10)
10
>>> min(10, 20)
10
>>> min(20, 10)
10
>>> type(mymin)
<type 'function'>
>>> type(min)
<type 'builtin_function_or_method'>
>>> text - checker
set(['tymme', 'ood', 'iss', 'tooo', 'thur', 'comee', 'ayd', 'guhd'])
>>> 
>>> 
>>> 
>>> 
>>> from random import *
>>> random()
0.10966456482628506
>>> seed(8675309)
>>> random()
0.40224696110279223
>>> #                                    0.0 <= x < 1.0
>>> random() * 100
51.02471779215914
>>> #                                    0.0 <= x < 100.0
>>> 
>>> # How do you turn a float into a integer
>>> int(3.14)
3
>>> # There are many ways
>>> # Model of floating point number:      sign integer plus a signed fraction
>>> #                                      \-- int ---/        \-- frac --/
>>> x = 3.14; int(x)
3
>>> x = -3.14; int(x)
-3
>>> x = 3.14; int(x);  x - int(x)
3
0.14000000000000012
>>> x = -3.14; int(x);  x - int(x)
-3
-0.14000000000000012
>>> # int is an odd function:  int(-x) == -int(x)     symmetric around the origin
>>> type(int(x))
<type 'int'>
>>> # int() returns an int
>>> 
>>> from math import ceil, floor
>>> x = 3.14; floor(x)
3.0
>>> x = -3.14; floor(x)
-4.0
>>> x = 3.14; ceil(x)
4.0
>>> x = -3.14; ceil(x)
-3.0
>>> ceil(3.0) == floor(3.0)
True
>>> ceil(-3.0) == floor(-3.0)
True
>>> type(floor(3.14))
<type 'float'>
>>> # ceil and floor are assymetric about the origin.  Usually but not always differ by 1.
>>> # they return floats that integral
>>> 
>>> x = 3.14; round(x)
3.0
>>> x = 3.94; round(x)
4.0
>>> x = -3.14; round(x)
-3.0
>>> x = -3.94; round(x)
-4.0
>>> # round returns a float an is an odd function:  round(x) == -round(x)
>>> x = 3.5; round(x)
4.0
>>> x = 4.5; round(x)
5.0
>>> x = -3.5; round(x)
-4.0
>>> x = -4.5; round(x)
-5.0
>>> # rounding rule:  round-half-away-from-zero
>>> 
>>> 
>>> # In Python 3:  int, ceil, floor, and round are all ways of producing ints
>>> # The new rounding rule:  round-half-even   banker's rounding
>>> 
>>> # round x:  int(x + (0.5) * math.copysign(x))
>>> # RDH
>>> 
>>> 
>>> 
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/spell_check.py ========
Misspelled:
-----------
iss
tymme
guhd
ood
tooo
comee
ayd
thur
>>> type(checker)
<type 'set'>
>>> text = set(re.findall(r"[a-z\-\']+", text.lower()))
>>> text
set(['and', 'tymme', 'all', 'to', 'for', 'ood', 'iss', 'tooo', 'men', 'thur', 'country', 'comee', 'of', 'ayd', 'guhd', 'the', 'now', 'city'])
>>> text - checker
set(['tymme', 'ood', 'iss', 'tooo', 'thur', 'comee', 'ayd', 'guhd'])
>>> 
>>> 
>>> from random import *
>>> 
>>> int(random() * 100)                    # 0 <= x < 100
19
>>> # 7 +/- 2
>>> # chunking
>>> 
>>> range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(2, 10)
[2, 3, 4, 5, 6, 7, 8, 9]
>>> range(2, 10, 3)
[2, 5, 8]
>>> # START STOP STEP
>>> # API design principle:  bridge off of what people already know
>>> randrange(100)
99
>>> range(100)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> randrange(100)
47
>>> range(1000, 2000, 100)
[1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900]
>>> randrange(1000, 2000, 100)
1000
>>> randrange(1000, 2000, 100)
1400
>>> randrange(1000, 2000, 100)
1200
>>> 
>>> outcomes = 'win lose draw'.split()
>>> outcomes
['win', 'lose', 'draw']
>>> len(outcomes)
3
>>> outcomes[0]
'win'
>>> outcomes[1]
'lose'
>>> outcomes[2]
'draw'
>>> [0, 1, 2]
[0, 1, 2]
>>> 
>>> 
>>> 
>>> from random import *
>>> outcomes = 'win lose draw'.split()
>>> outcomes[int(random() * len(outcomes))]
'win'
>>> outcomes[randrange(len(outcomes))]
'win'
>>> choice(outcomes)
'draw'
>>> 
>>> [choice(outcomes) for i in range(10)]
['win', 'win', 'lose', 'lose', 'win', 'draw', 'draw', 'draw', 'win', 'win']
>>> results = [choice(outcomes) for i in range(10)]
>>> 'abracadbra'.count('a')
4
>>> 'abracadbra'.count('b')
2
>>> 'abracadbra'.count('z')
0
>>> len(results)
10
>>> results.counts('win')

Traceback (most recent call last):
  File "<pyshell#170>", line 1, in <module>
    results.counts('win')
AttributeError: 'list' object has no attribute 'counts'
>>> results.count('win')
4
>>> results.count('lose')
3
>>> results.count('draw')
3
>>> [result == 'win' for result in results]
[True, False, False, True, False, False, True, False, True, False]
>>> sum([result == 'win' for result in results])
4
>>> 
>>> 
>>> 
>>> from random import *
>>> [choice(outcomes) for i in range(10)]
['lose', 'win', 'win', 'draw', 'draw', 'lose', 'lose', 'win', 'win', 'lose']
>>> # ^--- Sampling WITH replacement
>>> 
>>> sample(outcomes, 2)
['win', 'lose']
>>> # ^--- Sampling WITHOUT replacement
>>> sample(outcomes, 3)
['lose', 'draw', 'win']
>>> sample(outcomes, 4)

Traceback (most recent call last):
  File "<pyshell#186>", line 1, in <module>
    sample(outcomes, 4)
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/random.py", line 323, in sample
    raise ValueError("sample larger than population")
ValueError: sample larger than population
>>> sample(outcomes, 0)
[]
>>> sample(outcomes, 1)
['draw']
>>> 
>>> 
>>> 
>>> 
>>> sample(outcomes, len(outcomes))
['win', 'lose', 'draw']
>>> shuffle(outcomes)
>>> outcomes
['lose', 'draw', 'win']
>>> shuffle(outcomes)
>>> outcomes
['lose', 'draw', 'win']
>>> shuffle(outcomes)
>>> outcomes
['win', 'draw', 'lose']
>>> 
>>> # sample(s, 1)[0]               sample(s, k)              sample(s, len(s))
>>> # choice()                      sample(s, k)              shuffle()
>>> 
>>> sorted(outcomes)
['draw', 'lose', 'win']
>>> sorted(outcomes)[0]
'draw'
>>> sorted(outcomes)[len(outcomes)]

Traceback (most recent call last):
  File "<pyshell#206>", line 1, in <module>
    sorted(outcomes)[len(outcomes)]
IndexError: list index out of range
>>> sorted(outcomes)[len(outcomes) - 1]
'win'
>>> sorted(outcomes)[:2]
['draw', 'lose']
>>> 
>>> 
>>> from heapq import *
>>> s = [10, 5, 18, 7, 1, 41, 12, 87, 16, 2]
>>> sorted(s)
[1, 2, 5, 7, 10, 12, 16, 18, 41, 87]
>>> sorted(s)[0]
1
>>> sorted(s)[-1]
87
>>> sorted(s)[:3]
[1, 2, 5]
>>> sorted(s)[::-1][:3]
[87, 41, 18]
>>> min(s)
1
>>> max(s)
87
>>> nsmallest(3, s)
[1, 2, 5]
>>> nlargest(3, s)
[87, 41, 18]
>>> 
>>> 
>>> 
>>> # min     nsmallest         sorted            nlargest      max
>>> # s[0]    s[:k]               s                s[::-1][:k]   s[-1]
>>> 
>>> # Is there a select by rank?  No
>>> nsmallest(3, s)[-1]
5
>>> 
>>> # Are double colons awesome?  No!
>>> # There are reasonable in the forward direction
>>> 'Raymond Hettinger'[:]
'Raymond Hettinger'
>>> 'Raymond Hettinger'[::2]
'RyodHtigr'
>>> 'Raymond Hettinger'[1::2]
'amn etne'
>>> s = 'Raymond Hettinger'
>>> zip(s[::2], s[1::2])
[('R', 'a'), ('y', 'm'), ('o', 'n'), ('d', ' '), ('H', 'e'), ('t', 't'), ('i', 'n'), ('g', 'e')]
>>> for c in reversed('Raymond Hettinger'[1::2]):
	print c

	
e
n
t
e
 
n
m
a
>>> # For negative slicing, it is clearest to write it in a forward direction
>>> # and then use reversed().
>>> 
>>> 
>>> [choice(outcomes) for i in range(10)]
['win', 'win', 'win', 'lose', 'lose', 'draw', 'lose', 'win', 'lose', 'win']
>>> sample(outcomes, 3)
['lose', 'draw', 'win']
>>> # Sample relies on SEQUENCES:  Indexable with s[0], s[1], ... IndexError and Sizeable len(s)
>>> s = xrange(1000, 2000, 100)
>>> len(s)
10
>>> s[0]
1000
>>> s[1]
1100
>>> s[2]
1200
>>> sample(xrange(1000, 10000, 100), 7)
[9800, 9100, 4800, 5300, 9700, 6700, 2100]
>>> 
>>> sample(xrange(1, 57), 6)
[33, 38, 40, 4, 30, 8]
>>> sorted(sample(xrange(1, 57), 6))
[1, 12, 17, 49, 52, 53]
>>> 
>>> 
>>> from random import *
>>> seed('raymond'); sorted(sample(xrange(1, 57), 6))
[11, 12, 16, 22, 23, 42]
>>> 
>>> 
>>> def myreversed(seq):
	for i in range(len(seq) - 1, -1, -1):
		yield seq[i]

		
>>> list(myreversed('abcdef'))
['f', 'e', 'd', 'c', 'b', 'a']
>>> list(myreversed(xrange(1000, 2000, 100)))
[1900, 1800, 1700, 1600, 1500, 1400, 1300, 1200, 1100, 1000]
>>> # Generator
>>> 
>>> # xrange() in Python 2 was renames to range() in Python 3
>>> xrange(1000, 2000, 100)[:5]

Traceback (most recent call last):
  File "<pyshell#272>", line 1, in <module>
    xrange(1000, 2000, 100)[:5]
TypeError: sequence index must be integer, not 'slice'
>>> 
>>> hash('raymond')
2729357497184525765
>>> 
=============================== RESTART: Shell ===============================
>>> hash('raymond')
2729357497184525765
>>> len(str(hash('raymond')))
19
>>> import sys
>>> dir(sys)
['__displayhook__', '__doc__', '__egginsert', '__excepthook__', '__name__', '__package__', '__plen', '__stderr__', '__stdin__', '__stdout__', '_clear_type_cache', '_current_frames', '_getframe', '_mercurial', 'api_version', 'argv', 'builtin_module_names', 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_clear', 'exc_info', 'exc_traceback', 'exc_type', 'exc_value', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'getcheckinterval', 'getdefaultencoding', 'getdlopenflags', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'gettrace', 'hexversion', 'long_info', 'maxint', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'py3kwarning', 'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit', 'settrace', 'stderr', 'stdin', 'stdout', 'subversion', 'version', 'version_info', 'warnoptions']
>>> sys.maxint
9223372036854775807
>>> import sys
>>> sys.maxint
9223372036854775807
>>> from random import *
>>> seed('raymond'); sorted(sample(xrange(1, 57), 6))
[11, 12, 16, 22, 23, 42]
>>> 
>>> for name in 'raymond rachel matthew ramon gayle dennis sharon'.split():
	seed(name)
	print sorted(sample(xrange(1, 57), 6)), '<--', name

	
[11, 12, 16, 22, 23, 42] <-- raymond
[9, 17, 30, 32, 45, 55] <-- rachel
[5, 11, 14, 26, 31, 48] <-- matthew
[7, 22, 33, 42, 47, 52] <-- ramon
[5, 7, 20, 21, 34, 56] <-- gayle
[10, 20, 24, 34, 39, 54] <-- dennis
[13, 21, 33, 39, 42, 44] <-- sharon
>>> 
>>> 
>>> from random import *
>>> names = 'raymond rachel matthew ramon gayle dennis sharon'.split()
>>> hettingers = set()
>>> for name in names:
	seed(name)
	hettingers.update(sample(xrange(1, 57), 6))

	
>>> sorted(hettingers)
[5, 7, 9, 10, 11, 12, 13, 14, 16, 17, 20, 21, 22, 23, 24, 26, 30, 31, 32, 33, 34, 39, 42, 44, 45, 47, 48, 52, 54, 55, 56]
>>> len(hettinger)

Traceback (most recent call last):
  File "<pyshell#299>", line 1, in <module>
    len(hettinger)
NameError: name 'hettinger' is not defined
>>> len(hettingers)
31
>>> # Hettinger -> Head Injury
>>> del names
>>> 
>>> hettingers
set([5, 7, 9, 10, 11, 12, 13, 14, 16, 17, 20, 21, 22, 23, 24, 26, 30, 31, 32, 33, 34, 39, 42, 44, 45, 47, 48, 52, 54, 55, 56])
>>> name = 'lisa'
>>> seed(name); set(sample(xrange(1, 57), 6)) <= hettingers
False
>>> seed(name); set(sample(xrange(1, 57), 6)) & hettingers
set([16, 12, 39])
>>> name = 'rachel'
>>> seed(name); set(sample(xrange(1, 57), 6)) <= hettingers
True
>>> 31.0 / 56
0.5535714285714286
>>> (31.0 / 56) ** 6
0.028776767037057886
>>> 1 / _
34.750255256687765
>>> 
>>> names = 'raymond rachel matthew ramon gayle dennis sharon'.split()
>>> hettingers = set()
>>> for name in names:
	seed(name)
	hettingers.update(sample(xrange(100), 10))

	
>>> sorted(hettingers)
[3, 5, 8, 9, 10, 12, 14, 16, 17, 19, 20, 22, 23, 24, 26, 27, 29, 30, 35, 37, 38, 40, 41, 43, 44, 47, 49, 52, 55, 58, 59, 60, 62, 64, 65, 66, 68, 72, 74, 75, 76, 77, 78, 82, 83, 85, 86, 88, 91, 94]
>>> len(hettingers)
50
>>> (0.50) ** 10
0.0009765625
>>> 1 / _
1024.0
>>> name = 'lisa'
>>> seed(name); set(sample(xrange(1, 57), 6)) <= hettingers
False
>>> name = 'rachel'
>>> seed(name); set(sample(xrange(1, 57), 6)) <= hettingers
False
>>> seed(name); set(sample(xrange(1, 100), 10)) <= hettingers
False
>>> seed(name); set(sample(xrange(100), 10)) <= hettingers
True
>>> name = 'lisa'
>>> seed(name); set(sample(xrange(100), 10)) <= hettingers
False
>>> 
>>> # All real hettinger always pass the test
>>> # Filtering out fake hettingers can be made arbitrarily hard
>>> #  probes=6               # more probes means work to detect real hettingers
>>> #  population=1..56       # more population mean digits tattoed on my arm
>>> 
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/bloomfilter.py ========
>>> type(hettingers)
<class '__main__.BloomFilter'>
>>> hettingers.population
56
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/bloomfilter.py ========
>>> hettingers.data
set([])
>>> hettingers.probes
6
>>> hettingers.population
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/bloomfilter.py ========
>>> hettingers.data
set([])
>>> hettingers.population
xrange(56)
>>> hettingers.probes
6
>>> 
>>> import sys
>>> sys.getsizeof(range(1000))
8072
>>> sys.getsizeof(xrange(1000))
40
>>> sys.getsizeof(range(100000))
800072
>>> sys.getsizeof(xrange(100000))
40
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/bloomfilter.py ========
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/bloomfilter.py ========
>>> hettingers.population
xrange(56)
>>> hettingers.probes
6
>>> hettingers.data
set([7, 8, 17, 53, 26, 21])
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/bloomfilter.py ========

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj151/bloomfilter.py", line 20, in <module>
    hettingers.add(hettinger)
NameError: name 'hettinger' is not defined
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/bloomfilter.py ========
>>> hettingers.data
set([4, 6, 8, 9, 10, 11, 12, 13, 15, 16, 19, 20, 21, 22, 23, 25, 29, 30, 31, 32, 33, 38, 41, 43, 44, 46, 47, 51, 53, 54, 55])
>>> hettingers.probes
6
>>> 
>>> 
>>> 
>>> 
>>> d = dict(a=10, b=20, c=30)
>>> e = dict(b=40, c=60, d=80)
>>> for k, v in e.items():
	d[k] = v

	
>>> d
{'a': 10, 'c': 60, 'b': 40, 'd': 80}
>>> 
>>> d = dict(a=10, b=20, c=30)
>>> e = dict(b=40, c=60, d=80)
>>> d.update(e)
>>> d
{'a': 10, 'c': 60, 'b': 40, 'd': 80}
>>> 
>>> 
>>> s = [10, 20, 30]
>>> t = [40, 60, 80]
>>> for x in t:
	s.append(x)

	
>>> s
[10, 20, 30, 40, 60, 80]
>>> 
>>> s = [10, 20, 30]
>>> t = [40, 60, 80]
>>> s.extend(t)
>>> s
[10, 20, 30, 40, 60, 80]
>>> 
>>> 
>>> s = {10, 20, 30, 40}
>>> t = {30, 40, 50, 60}
>>> for x in t:
	s.add(x)

	
>>> s
set([40, 10, 50, 20, 60, 30])
>>> 
>>> 
>>> s = {10, 20, 30, 40}
>>> t = {30, 40, 50, 60}
>>> s.update(t)
>>> s
set([40, 10, 50, 20, 60, 30])
>>> s.update([10, 50, 100, 200])
>>> s
set([100, 40, 10, 200, 50, 20, 60, 30])
>>> # list.extend    dict.update        set.update
>>> 
>>> 
>>> 
>>> s = [10, 20, 30]
>>> t = [40, 60, 80]
>>> s += t
>>> s
[10, 20, 30, 40, 60, 80]
>>> s = [10, 20, 30]
>>> t = [40, 60, 80]
>>> s.extend(t)
>>> s
[10, 20, 30, 40, 60, 80]
>>> 
>>> # The operator form and the spelled-out method name use the same underlying code
>>> # The call itself is faster is with operator form.
>>> 
>>> 
>>> 
>>> 
>>> # Which is clearer operators or spelled-out names:
>>> #     rich.union(tall)
>>> #     rich | tall
>>> 
>>> # Bring over all the RICH people AND bring the TALL ones too.
>>> # Bring over the people who are both RICH and TALL
>>> #      rich & tall
>>> 
>>> 
>>> #   rich.difference(tall)
>>> #   rich - tall
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> list('abcabd')
['a', 'b', 'c', 'a', 'b', 'd']
>>> s = []
>>> for x in 'abcabd':
	s.add(x)

	

Traceback (most recent call last):
  File "<pyshell#441>", line 2, in <module>
    s.add(x)
AttributeError: 'list' object has no attribute 'add'
>>> for x in 'abcabd':
	s.append(x)

	
>>> list()
[]
>>> 
>>> 
>>> set('abracadabra')
set(['a', 'r', 'b', 'c', 'd'])
>>> set()
set([])
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/bloomfilter.py ========
>>> hettingers.data
set([4, 6, 8, 9, 10, 11, 12, 13, 15, 16, 19, 20, 21, 22, 23, 25, 29, 30, 31, 32, 33, 38, 41, 43, 44, 46, 47, 51, 53, 54, 55])
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/bloomfilter.py ========
>>> hettingers.is_member('lisa')
False
>>> hettingers.is_member('rachel')
True
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/bloomfilter.py ========
>>> # 12:30  -->  12:34:56
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/bloomfilter.py ========
True
False
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/bloomfilter.py ========
True
False
>>> 
>>> # len(s)                -->    s.__len__()
>>> # x in s                -->    s.__contains__()    s.__iter__()    s.__getitem__(0)
>>> #                                                TypeError: Not Iterable    IndexError
>>> # TypeError: Not Iterable, the "in" needs __contains__ or __iter__.
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/bloomfilter.py ========

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj151/bloomfilter.py", line 26, in <module>
    print 'rachel' in hettingers
TypeError: argument of type 'BloomFilter' is not iterable
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/bloomfilter.py ========
True
False
>>> names = 'raymond rachel matthew ramon gayle dennis sharon'
>>> len(names)
48
>>> import sys
>>> sys.getsizeof(names)
85
>>> import sys.getsizeof(set())
SyntaxError: invalid syntax
>>> sys.getsizeof(set())
232
>>> sys.getsizeof(55)
24
>>> x = 55
>>> type(x)
<type 'int'>
>>> # struct Py_IntObject {ssize_t refcnt; PyType *__class__; ssize_t value};
>>> # -5 to 256 inclusive
>>> 
>>> 2792 / 85.
32.84705882352941
>>> # O(1) search of bloom filter and O(n) search string
>>> hettingers.data
set([4, 6, 8, 9, 10, 11, 12, 13, 15, 16, 19, 20, 21, 22, 23, 25, 29, 30, 31, 32, 33, 38, 41, 43, 44, 46, 47, 51, 53, 54, 55])
>>> 
>>> 
>>> data = [0] * 56
>>> data
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>> data[4] = 1
>>> data[6] = 1
>>> data
[0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>> for i in hettingers.data:
	data[i] = 1

	
>>> hettingers
<__main__.BloomFilter object at 0x103862d50>
>>> data
[0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1]
>>> data[9]
1
>>> data[14]
0
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/bloomfilter.py ========

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj151/bloomfilter.py", line 30, in <module>
    print 'rachel' in hettingers
TypeError: argument of type 'BloomFilter' is not iterable
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/bloomfilter.py ========
True
False
>>> 'raymond' in hettingers
True
>>> 'rachel' in hettingers
True
>>> 'cindy' in hettingers
False
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/bloomfilter.py ========
True
False
>>> hettingers.population
xrange(56)
>>> hettingers.probes
6
>>> hettingers.data
[0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1]
>>> 
>>> 
>>> all([True, True, True, True])
True
>>> all([True, True, False, True])
False
>>> any([True, True, False, True])
True
>>> any([False, False, False, False])
False
>>> not any([False, False, False, False])
True
>>> # All, Some, and No
>>> #    All men are mortal.  Socrates is a man, there socrates is mortal
>>> 
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/bloomfilter.py ========
True
False
>>> 
>>> # choice  sample   choices randrange
>>> 
>>> hettingers.data
[0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1]
>>> type(_)
<type 'list'>
>>> # fixed length array of pointers to any kind of object
>>> 
>>> # number in the range 0 to 255:  byte
>>> b = bytearray(20)
>>> list(b)
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>> b[5] = 10
>>> list(b)
[0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>> b[5] = 12345

Traceback (most recent call last):
  File "<pyshell#515>", line 1, in <module>
    b[5] = 12345
ValueError: byte must be in range(0, 256)
>>> b[5] = bin

Traceback (most recent call last):
  File "<pyshell#516>", line 1, in <module>
    b[5] = bin
TypeError: an integer or string of size 1 is required
>>> 
>>> 
>>> 
>>> for x in b:
	print x

	
0
0
0
0
0
10
0
0
0
0
0
0
0
0
0
0
0
0
0
0
>>> sum(b)
10
>>> len(b)
20
>>> b[50]

Traceback (most recent call last):
  File "<pyshell#525>", line 1, in <module>
    b[50]
IndexError: bytearray index out of range
>>> 
>>> b = bytearray('hello')
>>> b
bytearray(b'hello')
>>> b[0] = 'H'
>>> b
bytearray(b'Hello')
>>> b.upper()
bytearray(b'HELLO')
>>> b
bytearray(b'Hello')
>>> dir(b)
['__add__', '__alloc__', '__class__', '__contains__', '__delattr__', '__delitem__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'capitalize', 'center', 'count', 'decode', 'endswith', 'expandtabs', 'extend', 'find', 'fromhex', 'index', 'insert', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'pop', 'remove', 'replace', 'reverse', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> b
bytearray(b'Hello')
>>> list(b)
[72, 101, 108, 108, 111]
>>> b = bytearray(5)
>>> b[2] = 65
>>> b
bytearray(b'\x00\x00A\x00\x00')
>>> 
>>> 
>>> s = [72, 101, 108, 108, 111]
>>> t = 'hello'
>>> 
>>> print s
[72, 101, 108, 108, 111]
>>> print t
hello
>>> s = bytearray([72, 101, 108, 108, 111])
>>> t = bytearray('hello')
>>> 
>>> s
bytearray(b'Hello')
>>> t
bytearray(b'hello')
>>> s = [10, 20, 30, 40, 50]
>>> s
[10, 20, 30, 40, 50]
>>> s = bytearray([10, 20, 30, 40, 50])
>>> s
bytearray(b'\n\x14\x1e(2')
>>> list(s)
[10, 20, 30, 40, 50]
>>> s
bytearray(b'\n\x14\x1e(2')
>>> t = bytearray('hello')
>>> u = 'hello'
>>> 
>>> for c in u:
	print c.upper()

	
H
E
L
L
O
>>> t
bytearray(b'hello')
>>> for c in t:
	print c

	
104
101
108
108
111
>>> # Iterates over numbers and displays as if it were a string
>>> b[3]
0
>>> b
bytearray(b'\x00\x00A\x00\x00')
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/bloomfilter.py ========
True
False
>>> hettingers.data
bytearray(b'\x00\x00\x00\x00\x01\x00\x01\x00\x01\x01\x01\x01\x01\x01\x00\x01\x01\x00\x00\x01\x01\x01\x01\x01\x00\x01\x00\x00\x00\x01\x01\x01\x01\x01\x00\x00\x00\x00\x01\x00\x00\x01\x00\x01\x01\x00\x01\x01\x00\x00\x00\x01\x00\x01\x01\x01')
>>> list(hettingers.data)
[0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1]
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/bloomfilter.py ========

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj151/bloomfilter.py", line 26, in <module>
    hettingers = BloomFilter('raymond rachel matthew ramon gayle dennis sharon'.split())
  File "/Users/raymond/Dropbox/Public/sj151/bloomfilter.py", line 10, in __init__
    self.data = bitarray(population)
NameError: global name 'bitarray' is not defined
>>> 
>>> 
>>> 
>>> # 2016 -> Third Milleneum
>>> # 1990 -> Second Milleneum
>>> 
>>> # Bit Flipping  ->   Tricks for the Tools
>>> format(51, '08b')
'00110011'
>>> bin(51)
'0b110011'
>>> format(11, '08b')
'00001011'
>>> bin(11)
'0b1011'
>>> 
>>> 
>>> 
>>> format(51, '08b')
'00110011'
>>> 
>>> 
>>> 0b101
5
>>> 0x101
257
>>> 0o101
65
>>> bin(5)
'0b101'
>>> hex(257)
'0x101'
>>> oct(65)
'0101'
>>> 00101
65
>>> #  00100
>>> #  00110
>>> 
>>> 
>>> 
>>> format(51, '08b')
'00110011'
>>> format(51 >> 1, '08b')       # rshift
'00011001'
>>> format(51 << 1, '08b')       # lshift
'01100110'
>>> format(51 & 1, '08b')        # bitwise-and
'00000001'
>>> format(51 & 17, '08b')       # bitwise-or
'00010001'
>>> format(51 | 17, '08b')       # bitwise-or
'00110011'
>>> format(51 ^ 17, '08b')       # bitwise-xor (either bit set but not both)
'00100010'
>>> format(51 & ~17, '08b')      # bitwise-not with a bitwise-and
'00100010'
>>> ############# Tricks ###################################################
>>> 
>>> format(51, '08b')
'00110011'
>>> # '00110011'
>>> #  76543210
>>> n = 4
>>> format(51 >> n, '08b')
'00000011'
>>> format((51 >> n) & 1, '08b')      # Isolate the n-th bit
'00000001'
>>> 
>>> n = 3
>>> format(51, '08b')
'00110011'
>>> format(1, '08b')
'00000001'
>>> format(1 << n, '08b')
'00001000'
>>> format((1 << n) | 51, '08b')
'00111011'
>>> format(51, '08b')
'00110011'
>>> format((1 << n) | 51, '08b')      # Setting the n-th bit
'00111011'
>>> n = 4
>>> format(1, '08b')
'00000001'
>>> format(1 << n, '08b')
'00010000'
>>> format(~(1 << n) & 51, '08b')
'00100011'
>>> format(51, '08b')
'00110011'
>>> format(~(1 << n) & 51, '08b')     # Unsetting the n-th
'00100011'
>>> # Book:  Hacker's Delight
>>> 
>>> 
>>> # 3 eggs -->  1 carton
>>> # 12 eggs --> 1 carton
>>> # 13 eggs --> 2 cartons
>>> # 23 eggs --> 2 cartons
>>> # 24 eggs --> 2 cartons
>>> # 25 eggs --> 3 cartons
>>> 
>>> 3 // 12
0
>>> 3 // 12 + 1
1
>>> 12 // 12 + 1
2
>>> # Floor division doesn't work well for getting the number of partially filled containers
>>> 
>>> def ceiling_division(eggs, carton_size):
	return (eggs + carton_size - 1) // carton_size

>>> ceiling_division(3, 12)
1
>>> [ceiling_division(eggs, 12) for eggs in [3, 12, 13, 23, 24, 25]]
[1, 1, 2, 2, 2, 3]
>>> 
>>> carton_size = 12
>>> eggs = 13
>>> eggs // carton_size
1
>>> -eggs // carton_size
-2
>>> -(-eggs // carton_size)
2
>>> def ceiling_division(eggs, carton_size):
	return -(-eggs // carton_size)

>>> 
>>> 
>>> ceiling_division(3, 8)
1
>>> ceiling_division(8, 8)
1
>>> ceiling_division(9, 8)
2
>>> ceiling_division(20, 8)
3
>>> bytearray(20)
bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
>>> len(bytearray(20))
20
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj151/bitarray.py ==========
>>> bytearray(20)
bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
>>> len(bytearray(20))
20
>>> len(b)

Traceback (most recent call last):
  File "<pyshell#670>", line 1, in <module>
    len(b)
TypeError: object of type 'BitArray' has no len()
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj151/bitarray.py ==========
20
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj151/bitarray.py ==========
20
>>> len(b.data)
3
>>> b = bytearray(20)
>>> b[11] = 1
>>> #     \---> __setitem__
>>> b[11] = 0
>>> b[50] = 1

Traceback (most recent call last):
  File "<pyshell#676>", line 1, in <module>
    b[50] = 1
IndexError: bytearray index out of range
>>> b[50] = 12345

Traceback (most recent call last):
  File "<pyshell#677>", line 1, in <module>
    b[50] = 12345
IndexError: bytearray index out of range
>>> b[5] = 12345

Traceback (most recent call last):
  File "<pyshell#678>", line 1, in <module>
    b[5] = 12345
ValueError: byte must be in range(0, 256)
>>> import math
>>> math.sqrt('hello')

Traceback (most recent call last):
  File "<pyshell#680>", line 1, in <module>
    math.sqrt('hello')
TypeError: a float is required
>>> math.sqrt(-25)

Traceback (most recent call last):
  File "<pyshell#681>", line 1, in <module>
    math.sqrt(-25)
ValueError: math domain error
>>> 
>>> 
>>> 38 // 5
7
>>> 38 % 5
3
>>> divmod(38, 5)
(7, 3)
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def f():
	return 30 + 40*2

>>> from dis import dis
>>> dis(f)
  2           0 LOAD_CONST               1 (30)
              3 LOAD_CONST               4 (80)
              6 BINARY_ADD          
              7 RETURN_VALUE        
>>> def f():
	return '=' * 10

>>> dis(f)
  2           0 LOAD_CONST               3 ('==========')
              3 RETURN_VALUE        
>>> def f(x):
	return x in (10, 20)

>>> dis(f)
  2           0 LOAD_FAST                0 (x)
              3 LOAD_CONST               3 ((10, 20))
              6 COMPARE_OP               6 (in)
              9 RETURN_VALUE        
>>> def f(x):
	return x in [10, 20]

>>> dis(f)
  2           0 LOAD_FAST                0 (x)
              3 LOAD_CONST               3 ((10, 20))
              6 COMPARE_OP               6 (in)
              9 RETURN_VALUE        
>>> def f(x):
	return x in {10, 20}

>>> dis(f)
  2           0 LOAD_FAST                0 (x)
              3 LOAD_CONST               1 (10)
              6 LOAD_CONST               2 (20)
              9 BUILD_SET                2
             12 COMPARE_OP               6 (in)
             15 RETURN_VALUE        
>>> def f(x):
	return x in frozenset({10, 20})

>>> dis(f)
  2           0 LOAD_FAST                0 (x)
              3 LOAD_GLOBAL              0 (frozenset)
              6 LOAD_CONST               1 (10)
              9 LOAD_CONST               2 (20)
             12 BUILD_SET                2
             15 CALL_FUNCTION            1
             18 COMPARE_OP               6 (in)
             21 RETURN_VALUE        
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj151/bitarray.py ==========
20
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj151/bitarray.py ==========
20
>>> b.data
bytearray(b'\x80@\x00')
>>> list(b.data)
[128, 64, 0]
>>> [format(x, '08b') for x in b.data]
['10000000', '01000000', '00000000']
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj151/bitarray.py ==========
20
>>> b[0]
0
>>> b[7]
1
>>> b[11]
0
>>> b[14]
SyntaxError: invalid syntax
>>> b[14]
SyntaxError: invalid syntax
>>> b[14]
1
>>> b[19]
0
>>> b[20]

Traceback (most recent call last):
  File "<pyshell#723>", line 1, in <module>
    b[20]
  File "/Users/raymond/Dropbox/Public/sj151/bitarray.py", line 23, in __getitem__
    raise IndexError('bitarray index out of range')
IndexError: bitarray index out of range
>>> len(b)
20
>>> b[14]
1
>>> b[-6]
0
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj151/bitarray.py ==========
20
>>> b[-6]
1
>>> b[-6 + 20]
1
>>> b[-25]

Traceback (most recent call last):
  File "<pyshell#729>", line 1, in <module>
    b[-25]
  File "/Users/raymond/Dropbox/Public/sj151/bitarray.py", line 25, in __getitem__
    raise IndexError('bitarray index out of range')
IndexError: bitarray index out of range
>>> 
>>> 
>>> 
>>> list('abc')
['a', 'b', 'c']
>>> tuple('abc')
('a', 'b', 'c')
>>> sorted(set(open('notes3/hamlet.txt')))[:10]
['\r\n', "    'And in part him; but' you may say 'not well:\r\n", "    'Anon he finds him\r\n", "    'As by lot, God wot,'\r\n", "    'But who, O, who had seen the mobled queen--'\r\n", "    'Doubt thou the stars are fire;\r\n", "    'Faith, I must leave thee, love, and shortly too;\r\n", "    'Faith, her privates we.\r\n", "    'Faith, no; as you may season it in the charge\r\n", "    'Faith, there has been much to do on both sides; and\r\n"]
>>> # cat notes3/hamlet.txt | sort | uniq | head
>>> 
>>> 
>>> 
>>> # __iter__
>>> # __getitem__(0)   1  2 3  IndexError    len(s)      Sequence
>>> 
>>> for bit in b:
	print bit

	
0
0
0
0
0
0
0
1
0
0
0
0
0
0
1
0
0
0
0
0
>>> sum(b)
2
>>> min(b)
0
>>> min(b)
0
>>> list(b)
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
>>> map(type, list(b))
[<type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>]
>>> map(str, list(b))
['0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0']
>>> ''.join(map(str, b))
'00000001000000100000'
>>> 
>>> b
<__main__.BitArray object at 0x1017d8e10>
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj151/bitarray.py ==========
20
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
BitArray('00000001000000100000')
>>> b[2] = 1
>>> b
BitArray('00100001000000100000')
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj151/bitarray.py ==========
20
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
BitArray('00000001000000100000')
>>> BitArray(10000)
BitArray('...')
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj151/bitarray.py ==========
20
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
BitArray('00000001000000100000')
>>> b
BitArray('00000001000000100000')
>>> BitArray(10000)
BitArray('0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000...')
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/bloomfilter.py ========
True
False
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/spell_check.py ========
Misspelled:
-----------
iss
tymme
guhd
ood
tooo
comee
ayd
thur
>>> import sys
>>> sys.getsizeof(checker)
8388840
>>> 
>>> len(checker)
234371
>>> sum(map(len, checker)) / float(len(checker))
9.591677297959219
>>> sys.getsizeof('123456789')
46
>>> 8388840 + 46 * 234371
19169906
>>> # 19 Mb
>>> 
>>> # Register   1 clock
>>> # L1 cache   4 clock   32kb
>>> # L2 cache   8-19 clock  256kb
>>> # L3 cache   20-40 clock 6 Mb
>>> # L4 cache   60-80 clock 128Mb
>>> # DRAM       100-200 clock  16Gb
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/spell_check.py ========
Misspelled:
-----------
iss
tymme
guhd
ood
tooo
comee
ayd
thur
>>> import sys
>>> sys.getsizeof(checker.data.data)
500049
>>> # 19 MB -> 500 kB       40x
>>> # words.txt 2.5Mb  O(n)
>>> # 5x               O(1)
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj151/bitarray.py ==========
20
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
BitArray('00000001000000100000')
>>> #     0123               ^- 19
>>> 
>>> format(51, '08b')
'00110011'
>>> # '00110011'
>>> #  76543210
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/spell_check.py ========
Misspelled:
-----------
iss
tymme
guhd
ood
tooo
comee
ayd
thur
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/spell_check.py ========
>>> 
>>> 
>>> s = '''   she sells sea shells by the sea shore
              double rubber baby buggy bumpers
              peter piper picked a peck of pickled peppers
              which witch had which witches wrist watch
'''
>>> len(s)
203
>>> import zlib
>>> c = zlib.compress(s)
>>> len(c)
113
>>> zlib.decompress(c) == s
True
>>> 
>>> import bz2
>>> c = bz2.compress(s)
>>> len(c)
139
>>> bz2.decompress(c) == s
True
>>> # zlib and bz2 both have the same API:  compress and decompress
>>> # For short strings, zlib is faster and compresses better
>>> 
>>> with open('notes3/hamlet.txt') as f:
	play = f.read()

	
>>> type(play)
<type 'str'>
>>> len(play)
202238
>>> import bz2, zlib
>>> with open('notes3/hamlet.txt') as f:
	play = f.read()

	
>>> len(play)
202238
>>> len(zlib.compress(play))
73748
>>> len(bz2.compress(play))
56442
>>> # For long strings, bz2 tends to better.  It is still slower.
>>> 
>>> # A   ->            B         ->         C            t
>>> # A                ->                    C            u
>>> 
>>> # Instincts say, skipping step does less work, therefore u is smaller than t
>>> # If B makes C cheapers, then t > u
>>> # If B makes C cheaper, u is bigger than t
>>> 
>>> # A:  generate a lot of data        B:  sort it         C do many lookups (bisecting)
>>> # A:  generate a lot of data                            C do many lookups (linear search)
>>> 
>>> # A:  generate a lot of data        B:  compress it     C: write to disk or send over a socket
>>> #                                  CPU                     SSD:slow  HD:slower  1Gb Ethernet:slower
>>> #                                  CPU                     SSD:slow  HD:slower  1Gb Ethernet:slower
>>> 
>>> 
>>> # In general, when writing compressible data to disk or sending over a socket,
>>> # you get massive speed boosts by compressing first
>>> len(bz2.compress(zlib.compress(play)))
74443
>>> len(bz2.compress(play))
56442
>>> 
>>> 
>>> 
>>> hansolo = dict(
	rank = 'captain',
	ship = 'falcon',
	friends = ('luke', 'leia', 'chewy'),
	status = 'wanted by jabba the hut',
	speed = 12,
)
>>> type(hansolo)
<type 'dict'>
>>> hansolo.keys()
['status', 'speed', 'ship', 'friends', 'rank']
>>> hansolo['ship']
'falcon'
>>> for friend in hansolo['friends']:
	print "Don't worry Han, %s will save you" % friend.title()

	
Don't worry Han, Luke will save you
Don't worry Han, Leia will save you
Don't worry Han, Chewy will save you
>>> 
>>> import pickle
>>> carbonite = pickle.dumps(hansolo)
>>> del hansolo
>>> type(carbonite)
<type 'str'>
>>> 
>>> hansolo = pickle.loads(carbonite)
>>> type(hansolo)
<type 'dict'>
>>> hansolo.keys()
['status', 'friends', 'ship', 'speed', 'rank']
>>> hansolo['ship']
'falcon'
>>> for friend in hansolo['friends']:
	print "Don't worry Han, %s will save you" % friend.title()

	
Don't worry Han, Luke will save you
Don't worry Han, Leia will save you
Don't worry Han, Chewy will save you
>>> 
>>> 
>>> hansolo
{'status': 'wanted by jabba the hut', 'friends': ('luke', 'leia', 'chewy'), 'ship': 'falcon', 'speed': 12, 'rank': 'captain'}
>>> 
>>> import json
>>> carbonite = json.dumps(hansolo)
>>> del hansolo
>>> json.loads(hansolo)

Traceback (most recent call last):
  File "<pyshell#874>", line 1, in <module>
    json.loads(hansolo)
NameError: name 'hansolo' is not defined
>>> json.loads(carbonite)
{u'status': u'wanted by jabba the hut', u'speed': 12, u'ship': u'falcon', u'friends': [u'luke', u'leia', u'chewy'], u'rank': u'captain'}
>>> # dict, list, unicode, bool, int, float, None
>>> #      tuple    str               decimal
>>> 
>>> # datetime sets  BitArray BloomFilter
>>> 
>>> # JSON is cross-language standard
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/spell_check.py ========
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/spell_check.py ========

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj151/spell_check.py", line 35, in <module>
    checker = make_checker()
  File "/Users/raymond/Dropbox/Public/sj151/spell_check.py", line 6, in make_checker
    with open('words.pcl', 'rb') as f:
IOError: [Errno 2] No such file or directory: 'words.pcl'
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/spell_check.py ========
Misspelled:
-----------
iss
tymme
guhd
ood
tooo
comee
ayd
thur
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/spell_check.py ========

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj151/spell_check.py", line 43, in <module>
    checker = make_checker()
  File "/Users/raymond/Dropbox/Public/sj151/spell_check.py", line 16, in make_checker
    pickle.dump(f)
TypeError: dump() takes at least 2 arguments (1 given)
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/spell_check.py ========

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj151/spell_check.py", line 43, in <module>
    checker = make_checker()
  File "/Users/raymond/Dropbox/Public/sj151/spell_check.py", line 8, in make_checker
    return pickle.load(f)
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/pickle.py", line 1384, in load
    return Unpickler(file).load()
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/pickle.py", line 864, in load
    dispatch[key](self)
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/pickle.py", line 886, in load_eof
    raise EOFError
EOFError
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/spell_check.py ========
Misspelled:
-----------
iss
tymme
guhd
ood
tooo
comee
ayd
thur
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/spell_check.py ========
Misspelled:
-----------
iss
tymme
guhd
ood
tooo
comee
ayd
thur
>>> 
=============================== RESTART: Shell ===============================
>>> x = 10
>>> sorted(globals().keys())
['__builtins__', '__doc__', '__name__', '__package__', 'x']
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'x']
>>> globals()['x'] = 11
>>> x
11
>>> def f(x):
	x = 20

	
>>> f(5)
>>> x
11
>>> def f(x):
	x = 20
	print locals()

	
>>> f(5)
{'x': 20}
>>> globals()['x']
11
>>> # All assignments go into locals
>>> # At the module level, globals and locals are the same dictionary
>>> 
>>> x = 10
>>> globals()['x']
10
>>> locals()['x']
10
>>> globals() == locals()
True
>>> globals() is locals()
True
>>> # All assignments go into locals
>>> # At the module level, globals and locals are the same dictionary
>>> # Lookups:   locals -> globals -> __builtins__ -> NameError
>>> 
>>> x = 10
>>> y = 20
>>> def f():
	y = 30
	z = 40
	w = len('hello')
	print locals()

	
>>> def f():
	y = 30
	z = 40
	w = len('hello')
	return w, x, y, z

>>> f()
(5, 10, 30, 40)
>>> def len(obj):
	return 42

>>> len('hello')
42
>>> f()
(42, 10, 30, 40)
>>> __builtins__.len('hello')
5
>>> len('hello')
42
>>> del len
>>> f()
(5, 10, 30, 40)
>>> xyz

Traceback (most recent call last):
  File "<pyshell#929>", line 1, in <module>
    xyz
NameError: name 'xyz' is not defined
>>> 
>>> 
>>> 
>>> 
>>> # All assignments go into locals
>>> # At the module level, globals and locals are the same dictionary
>>> # Lookups:   locals -> globals -> __builtins__ -> NameError
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'f', 'x', 'y']
>>> # __builtins__ gets added to globals if not already present
>>> 
>>> 
>>> 
>>> choice = raw_input('Choose a game: ')
Choose a game: Global Thermonuclear War
>>> 
>>> 
>>> 30 + 40*2
110
>>> # printf("%d\n", 30 + 40*2);
>>> # scanf
>>> 
>>> expr = raw_input('Enter an expression: ')
Enter an expression: 30 + 40*2
>>> expr
'30 + 40*2'
>>> eval(expr)
110
>>> 
>>> 
>>> # Fortran -- formula translater -- math
>>> # COBOL -- common business oriented language -- common data hierarchies
>>> # LISP -- list processor -- eval
>>> 
>>> 
>>> # eval(str_expr) -> value
>>> eval('x = 10')

Traceback (most recent call last):
  File "<pyshell#960>", line 1, in <module>
    eval('x = 10')
  File "<string>", line 1
    x = 10
      ^
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> exec 'x = 35'
>>> x
35
>>> 
>>> 
>>> 
>>> g = {'x': 100, 'y': 200}
>>> l = {'y': 300}
>>> exec 'z = (x, y, len("hello"))' in g, l
>>> l
{'y': 300, 'z': (100, 300, 5)}
>>> g.keys()
['y', 'x', '__builtins__']
>>> 
>>> 
>>> d = {'y': 500}
>>> exec 'z = y + 55' in d, d
>>> d.keys()
['y', '__builtins__', 'z']
>>> 
>>> d = {'y': 750}
>>> exec 'z = y + 75' in d
>>> d.keys()
['y', '__builtins__', 'z']
>>> d
{'y': 750, '__builtins__': {'bytearray': <type 'bytearray'>, 'IndexError': <type 'exceptions.IndexError'>, 'all': <built-in function all>, 'help': Type help() for interactive help, or help(object) for help about object., 'vars': <built-in function vars>, 'SyntaxError': <type 'exceptions.SyntaxError'>, 'unicode': <type 'unicode'>, 'UnicodeDecodeError': <type 'exceptions.UnicodeDecodeError'>, 'memoryview': <type 'memoryview'>, 'isinstance': <built-in function isinstance>, 'copyright': Copyright (c) 2001-2016 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved., 'NameError': <type 'exceptions.NameError'>, 'BytesWarning': <type 'exceptions.BytesWarning'>, 'dict': <type 'dict'>, 'input': <built-in function input>, 'oct': <built-in function oct>, 'bin': <built-in function bin>, 'SystemExit': <type 'exceptions.SystemExit'>, 'StandardError': <type 'exceptions.StandardError'>, 'format': <built-in function format>, 'repr': <built-in function repr>, 'sorted': <built-in function sorted>, 'False': False, 'RuntimeWarning': <type 'exceptions.RuntimeWarning'>, 'list': <type 'list'>, 'iter': <built-in function iter>, 'reload': <built-in function reload>, 'Warning': <type 'exceptions.Warning'>, '__package__': None, 'round': <built-in function round>, 'dir': <built-in function dir>, 'cmp': <built-in function cmp>, 'set': <type 'set'>, 'bytes': <type 'str'>, 'reduce': <built-in function reduce>, 'intern': <built-in function intern>, 'issubclass': <built-in function issubclass>, 'Ellipsis': Ellipsis, 'EOFError': <type 'exceptions.EOFError'>, 'locals': <built-in function locals>, 'BufferError': <type 'exceptions.BufferError'>, 'slice': <type 'slice'>, 'FloatingPointError': <type 'exceptions.FloatingPointError'>, 'sum': <built-in function sum>, 'getattr': <built-in function getattr>, 'abs': <built-in function abs>, 'exit': Use exit() or Ctrl-D (i.e. EOF) to exit, 'print': <built-in function print>, 'True': True, 'FutureWarning': <type 'exceptions.FutureWarning'>, 'ImportWarning': <type 'exceptions.ImportWarning'>, 'None': None, 'hash': <built-in function hash>, 'ReferenceError': <type 'exceptions.ReferenceError'>, 'len': <built-in function len>, 'credits':     Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information., 'frozenset': <type 'frozenset'>, '__name__': '__builtin__', 'ord': <built-in function ord>, 'super': <type 'super'>, '_': None, 'TypeError': <type 'exceptions.TypeError'>, 'license': Type license() to see the full license text, 'KeyboardInterrupt': <type 'exceptions.KeyboardInterrupt'>, 'UserWarning': <type 'exceptions.UserWarning'>, 'filter': <built-in function filter>, 'range': <built-in function range>, 'staticmethod': <type 'staticmethod'>, 'SystemError': <type 'exceptions.SystemError'>, 'BaseException': <type 'exceptions.BaseException'>, 'pow': <built-in function pow>, 'RuntimeError': <type 'exceptions.RuntimeError'>, 'float': <type 'float'>, 'MemoryError': <type 'exceptions.MemoryError'>, 'StopIteration': <type 'exceptions.StopIteration'>, 'globals': <built-in function globals>, 'divmod': <built-in function divmod>, 'enumerate': <type 'enumerate'>, 'apply': <built-in function apply>, 'LookupError': <type 'exceptions.LookupError'>, 'open': <built-in function open>, 'quit': Use quit() or Ctrl-D (i.e. EOF) to exit, 'basestring': <type 'basestring'>, 'UnicodeError': <type 'exceptions.UnicodeError'>, 'zip': <built-in function zip>, 'hex': <built-in function hex>, 'long': <type 'long'>, 'next': <built-in function next>, 'ImportError': <type 'exceptions.ImportError'>, 'chr': <built-in function chr>, 'xrange': <type 'xrange'>, 'type': <type 'type'>, '__doc__': "Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices.", 'Exception': <type 'exceptions.Exception'>, 'tuple': <type 'tuple'>, 'UnicodeTranslateError': <type 'exceptions.UnicodeTranslateError'>, 'reversed': <type 'reversed'>, 'UnicodeEncodeError': <type 'exceptions.UnicodeEncodeError'>, 'IOError': <type 'exceptions.IOError'>, 'hasattr': <built-in function hasattr>, 'delattr': <built-in function delattr>, 'setattr': <built-in function setattr>, 'raw_input': <built-in function raw_input>, 'SyntaxWarning': <type 'exceptions.SyntaxWarning'>, 'compile': <built-in function compile>, 'ArithmeticError': <type 'exceptions.ArithmeticError'>, 'str': <type 'str'>, 'property': <type 'property'>, 'GeneratorExit': <type 'exceptions.GeneratorExit'>, 'int': <type 'int'>, '__import__': <built-in function __import__>, 'KeyError': <type 'exceptions.KeyError'>, 'coerce': <built-in function coerce>, 'PendingDeprecationWarning': <type 'exceptions.PendingDeprecationWarning'>, 'file': <type 'file'>, 'EnvironmentError': <type 'exceptions.EnvironmentError'>, 'unichr': <built-in function unichr>, 'id': <built-in function id>, 'OSError': <type 'exceptions.OSError'>, 'DeprecationWarning': <type 'exceptions.DeprecationWarning'>, 'min': <built-in function min>, 'UnicodeWarning': <type 'exceptions.UnicodeWarning'>, 'execfile': <built-in function execfile>, 'any': <built-in function any>, 'complex': <type 'complex'>, 'bool': <type 'bool'>, 'ValueError': <type 'exceptions.ValueError'>, 'NotImplemented': NotImplemented, 'map': <built-in function map>, 'buffer': <type 'buffer'>, 'max': <built-in function max>, 'object': <type 'object'>, 'TabError': <type 'exceptions.TabError'>, 'callable': <built-in function callable>, 'ZeroDivisionError': <type 'exceptions.ZeroDivisionError'>, 'eval': <built-in function eval>, '__debug__': True, 'IndentationError': <type 'exceptions.IndentationError'>, 'AssertionError': <type 'exceptions.AssertionError'>, 'classmethod': <type 'classmethod'>, 'UnboundLocalError': <type 'exceptions.UnboundLocalError'>, 'NotImplementedError': <type 'exceptions.NotImplementedError'>, 'AttributeError': <type 'exceptions.AttributeError'>, 'OverflowError': <type 'exceptions.OverflowError'>}, 'z': 825}
>>> 

>>> 
>>> 
>>> d.keys()
['y', '__builtins__', 'z']
>>> globals()
{'d': {'y': 750, '__builtins__': {'bytearray': <type 'bytearray'>, 'IndexError': <type 'exceptions.IndexError'>, 'all': <built-in function all>, 'help': Type help() for interactive help, or help(object) for help about object., 'vars': <built-in function vars>, 'SyntaxError': <type 'exceptions.SyntaxError'>, 'unicode': <type 'unicode'>, 'UnicodeDecodeError': <type 'exceptions.UnicodeDecodeError'>, 'memoryview': <type 'memoryview'>, 'isinstance': <built-in function isinstance>, 'copyright': Copyright (c) 2001-2016 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved., 'NameError': <type 'exceptions.NameError'>, 'BytesWarning': <type 'exceptions.BytesWarning'>, 'dict': <type 'dict'>, 'input': <built-in function input>, 'oct': <built-in function oct>, 'bin': <built-in function bin>, 'SystemExit': <type 'exceptions.SystemExit'>, 'StandardError': <type 'exceptions.StandardError'>, 'format': <built-in function format>, 'repr': <built-in function repr>, 'sorted': <built-in function sorted>, 'False': False, 'RuntimeWarning': <type 'exceptions.RuntimeWarning'>, 'list': <type 'list'>, 'iter': <built-in function iter>, 'reload': <built-in function reload>, 'Warning': <type 'exceptions.Warning'>, '__package__': None, 'round': <built-in function round>, 'dir': <built-in function dir>, 'cmp': <built-in function cmp>, 'set': <type 'set'>, 'bytes': <type 'str'>, 'reduce': <built-in function reduce>, 'intern': <built-in function intern>, 'issubclass': <built-in function issubclass>, 'Ellipsis': Ellipsis, 'EOFError': <type 'exceptions.EOFError'>, 'locals': <built-in function locals>, 'BufferError': <type 'exceptions.BufferError'>, 'slice': <type 'slice'>, 'FloatingPointError': <type 'exceptions.FloatingPointError'>, 'sum': <built-in function sum>, 'getattr': <built-in function getattr>, 'abs': <built-in function abs>, 'exit': Use exit() or Ctrl-D (i.e. EOF) to exit, 'print': <built-in function print>, 'True': True, 'FutureWarning': <type 'exceptions.FutureWarning'>, 'ImportWarning': <type 'exceptions.ImportWarning'>, 'None': None, 'hash': <built-in function hash>, 'ReferenceError': <type 'exceptions.ReferenceError'>, 'len': <built-in function len>, 'credits':     Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information., 'frozenset': <type 'frozenset'>, '__name__': '__builtin__', 'ord': <built-in function ord>, 'super': <type 'super'>, '_': None, 'TypeError': <type 'exceptions.TypeError'>, 'license': Type license() to see the full license text, 'KeyboardInterrupt': <type 'exceptions.KeyboardInterrupt'>, 'UserWarning': <type 'exceptions.UserWarning'>, 'filter': <built-in function filter>, 'range': <built-in function range>, 'staticmethod': <type 'staticmethod'>, 'SystemError': <type 'exceptions.SystemError'>, 'BaseException': <type 'exceptions.BaseException'>, 'pow': <built-in function pow>, 'RuntimeError': <type 'exceptions.RuntimeError'>, 'float': <type 'float'>, 'MemoryError': <type 'exceptions.MemoryError'>, 'StopIteration': <type 'exceptions.StopIteration'>, 'globals': <built-in function globals>, 'divmod': <built-in function divmod>, 'enumerate': <type 'enumerate'>, 'apply': <built-in function apply>, 'LookupError': <type 'exceptions.LookupError'>, 'open': <built-in function open>, 'quit': Use quit() or Ctrl-D (i.e. EOF) to exit, 'basestring': <type 'basestring'>, 'UnicodeError': <type 'exceptions.UnicodeError'>, 'zip': <built-in function zip>, 'hex': <built-in function hex>, 'long': <type 'long'>, 'next': <built-in function next>, 'ImportError': <type 'exceptions.ImportError'>, 'chr': <built-in function chr>, 'xrange': <type 'xrange'>, 'type': <type 'type'>, '__doc__': "Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices.", 'Exception': <type 'exceptions.Exception'>, 'tuple': <type 'tuple'>, 'UnicodeTranslateError': <type 'exceptions.UnicodeTranslateError'>, 'reversed': <type 'reversed'>, 'UnicodeEncodeError': <type 'exceptions.UnicodeEncodeError'>, 'IOError': <type 'exceptions.IOError'>, 'hasattr': <built-in function hasattr>, 'delattr': <built-in function delattr>, 'setattr': <built-in function setattr>, 'raw_input': <built-in function raw_input>, 'SyntaxWarning': <type 'exceptions.SyntaxWarning'>, 'compile': <built-in function compile>, 'ArithmeticError': <type 'exceptions.ArithmeticError'>, 'str': <type 'str'>, 'property': <type 'property'>, 'GeneratorExit': <type 'exceptions.GeneratorExit'>, 'int': <type 'int'>, '__import__': <built-in function __import__>, 'KeyError': <type 'exceptions.KeyError'>, 'coerce': <built-in function coerce>, 'PendingDeprecationWarning': <type 'exceptions.PendingDeprecationWarning'>, 'file': <type 'file'>, 'EnvironmentError': <type 'exceptions.EnvironmentError'>, 'unichr': <built-in function unichr>, 'id': <built-in function id>, 'OSError': <type 'exceptions.OSError'>, 'DeprecationWarning': <type 'exceptions.DeprecationWarning'>, 'min': <built-in function min>, 'UnicodeWarning': <type 'exceptions.UnicodeWarning'>, 'execfile': <built-in function execfile>, 'any': <built-in function any>, 'complex': <type 'complex'>, 'bool': <type 'bool'>, 'ValueError': <type 'exceptions.ValueError'>, 'NotImplemented': NotImplemented, 'map': <built-in function map>, 'buffer': <type 'buffer'>, 'max': <built-in function max>, 'object': <type 'object'>, 'TabError': <type 'exceptions.TabError'>, 'callable': <built-in function callable>, 'ZeroDivisionError': <type 'exceptions.ZeroDivisionError'>, 'eval': <built-in function eval>, '__debug__': True, 'IndentationError': <type 'exceptions.IndentationError'>, 'AssertionError': <type 'exceptions.AssertionError'>, 'classmethod': <type 'classmethod'>, 'UnboundLocalError': <type 'exceptions.UnboundLocalError'>, 'NotImplementedError': <type 'exceptions.NotImplementedError'>, 'AttributeError': <type 'exceptions.AttributeError'>, 'OverflowError': <type 'exceptions.OverflowError'>}, 'z': 825}, 'g': {'y': 200, 'x': 100, '__builtins__': {'bytearray': <type 'bytearray'>, 'IndexError': <type 'exceptions.IndexError'>, 'all': <built-in function all>, 'help': Type help() for interactive help, or help(object) for help about object., 'vars': <built-in function vars>, 'SyntaxError': <type 'exceptions.SyntaxError'>, 'unicode': <type 'unicode'>, 'UnicodeDecodeError': <type 'exceptions.UnicodeDecodeError'>, 'memoryview': <type 'memoryview'>, 'isinstance': <built-in function isinstance>, 'copyright': Copyright (c) 2001-2016 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved., 'NameError': <type 'exceptions.NameError'>, 'BytesWarning': <type 'exceptions.BytesWarning'>, 'dict': <type 'dict'>, 'input': <built-in function input>, 'oct': <built-in function oct>, 'bin': <built-in function bin>, 'SystemExit': <type 'exceptions.SystemExit'>, 'StandardError': <type 'exceptions.StandardError'>, 'format': <built-in function format>, 'repr': <built-in function repr>, 'sorted': <built-in function sorted>, 'False': False, 'RuntimeWarning': <type 'exceptions.RuntimeWarning'>, 'list': <type 'list'>, 'iter': <built-in function iter>, 'reload': <built-in function reload>, 'Warning': <type 'exceptions.Warning'>, '__package__': None, 'round': <built-in function round>, 'dir': <built-in function dir>, 'cmp': <built-in function cmp>, 'set': <type 'set'>, 'bytes': <type 'str'>, 'reduce': <built-in function reduce>, 'intern': <built-in function intern>, 'issubclass': <built-in function issubclass>, 'Ellipsis': Ellipsis, 'EOFError': <type 'exceptions.EOFError'>, 'locals': <built-in function locals>, 'BufferError': <type 'exceptions.BufferError'>, 'slice': <type 'slice'>, 'FloatingPointError': <type 'exceptions.FloatingPointError'>, 'sum': <built-in function sum>, 'getattr': <built-in function getattr>, 'abs': <built-in function abs>, 'exit': Use exit() or Ctrl-D (i.e. EOF) to exit, 'print': <built-in function print>, 'True': True, 'FutureWarning': <type 'exceptions.FutureWarning'>, 'ImportWarning': <type 'exceptions.ImportWarning'>, 'None': None, 'hash': <built-in function hash>, 'ReferenceError': <type 'exceptions.ReferenceError'>, 'len': <built-in function len>, 'credits':     Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information., 'frozenset': <type 'frozenset'>, '__name__': '__builtin__', 'ord': <built-in function ord>, 'super': <type 'super'>, '_': None, 'TypeError': <type 'exceptions.TypeError'>, 'license': Type license() to see the full license text, 'KeyboardInterrupt': <type 'exceptions.KeyboardInterrupt'>, 'UserWarning': <type 'exceptions.UserWarning'>, 'filter': <built-in function filter>, 'range': <built-in function range>, 'staticmethod': <type 'staticmethod'>, 'SystemError': <type 'exceptions.SystemError'>, 'BaseException': <type 'exceptions.BaseException'>, 'pow': <built-in function pow>, 'RuntimeError': <type 'exceptions.RuntimeError'>, 'float': <type 'float'>, 'MemoryError': <type 'exceptions.MemoryError'>, 'StopIteration': <type 'exceptions.StopIteration'>, 'globals': <built-in function globals>, 'divmod': <built-in function divmod>, 'enumerate': <type 'enumerate'>, 'apply': <built-in function apply>, 'LookupError': <type 'exceptions.LookupError'>, 'open': <built-in function open>, 'quit': Use quit() or Ctrl-D (i.e. EOF) to exit, 'basestring': <type 'basestring'>, 'UnicodeError': <type 'exceptions.UnicodeError'>, 'zip': <built-in function zip>, 'hex': <built-in function hex>, 'long': <type 'long'>, 'next': <built-in function next>, 'ImportError': <type 'exceptions.ImportError'>, 'chr': <built-in function chr>, 'xrange': <type 'xrange'>, 'type': <type 'type'>, '__doc__': "Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices.", 'Exception': <type 'exceptions.Exception'>, 'tuple': <type 'tuple'>, 'UnicodeTranslateError': <type 'exceptions.UnicodeTranslateError'>, 'reversed': <type 'reversed'>, 'UnicodeEncodeError': <type 'exceptions.UnicodeEncodeError'>, 'IOError': <type 'exceptions.IOError'>, 'hasattr': <built-in function hasattr>, 'delattr': <built-in function delattr>, 'setattr': <built-in function setattr>, 'raw_input': <built-in function raw_input>, 'SyntaxWarning': <type 'exceptions.SyntaxWarning'>, 'compile': <built-in function compile>, 'ArithmeticError': <type 'exceptions.ArithmeticError'>, 'str': <type 'str'>, 'property': <type 'property'>, 'GeneratorExit': <type 'exceptions.GeneratorExit'>, 'int': <type 'int'>, '__import__': <built-in function __import__>, 'KeyError': <type 'exceptions.KeyError'>, 'coerce': <built-in function coerce>, 'PendingDeprecationWarning': <type 'exceptions.PendingDeprecationWarning'>, 'file': <type 'file'>, 'EnvironmentError': <type 'exceptions.EnvironmentError'>, 'unichr': <built-in function unichr>, 'id': <built-in function id>, 'OSError': <type 'exceptions.OSError'>, 'DeprecationWarning': <type 'exceptions.DeprecationWarning'>, 'min': <built-in function min>, 'UnicodeWarning': <type 'exceptions.UnicodeWarning'>, 'execfile': <built-in function execfile>, 'any': <built-in function any>, 'complex': <type 'complex'>, 'bool': <type 'bool'>, 'ValueError': <type 'exceptions.ValueError'>, 'NotImplemented': NotImplemented, 'map': <built-in function map>, 'buffer': <type 'buffer'>, 'max': <built-in function max>, 'object': <type 'object'>, 'TabError': <type 'exceptions.TabError'>, 'callable': <built-in function callable>, 'ZeroDivisionError': <type 'exceptions.ZeroDivisionError'>, 'eval': <built-in function eval>, '__debug__': True, 'IndentationError': <type 'exceptions.IndentationError'>, 'AssertionError': <type 'exceptions.AssertionError'>, 'classmethod': <type 'classmethod'>, 'UnboundLocalError': <type 'exceptions.UnboundLocalError'>, 'NotImplementedError': <type 'exceptions.NotImplementedError'>, 'AttributeError': <type 'exceptions.AttributeError'>, 'OverflowError': <type 'exceptions.OverflowError'>}}, 'f': <function f at 0x10073f0c8>, '__builtins__': <module '__builtin__' (built-in)>, 'expr': '30 + 40*2', 'l': {'y': 300, 'z': (100, 300, 5)}, '__package__': None, 'x': 35, 'y': 20, '__name__': '__main__', 'choice': 'Global Thermonuclear War', '__doc__': None}
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'choice', 'd', 'expr', 'f', 'g', 'l', 'x', 'y']
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj151/tmp.py ============
I suggested that these results would follow from the assumption that the
fundamental error of regarding functional notions as categorial is not
subject to a corpus of utterance tokens upon which conformity has been
defined by the paired utterance test. This suggests that a descriptively
adequate grammar is, apparently, determined by an abstract underlying
order. Summarizing, then, we assume that relational information may
remedy and, at the same time, eliminate the requirement that branching
is not tolerated within the dominance scope of a complex symbol. It must
be emphasized, once again, that a case of semigrammaticalness of a
different sort is not to be considered in determining the extended
c-command discussed in connection with (34). With this clarification,
the systematic use of complex symbols is rather different from the
levels of acceptability from fairly high (e.g. (99a)) to virtual
gibberish (e.g. (98d)).
>>> 
============ RESTART: /Users/raymond/Dropbox/Public/sj151/tmp.py ============
By combining adjunctions and certain deformations, a descriptively
adequate grammar delimits a general convention regarding the forms of
the grammar. Clearly, relational information is to be regarded as the
requirement that branching is not tolerated within the dominance scope
of a complex symbol. For any transformation which is sufficiently
diversified in application to be of any interest, a case of
semigrammaticalness of a different sort may remedy and, at the same
time, eliminate an abstract underlying order. I suggested that these
results would follow from the assumption that the systematic use of
complex symbols raises serious doubts about an important distinction in
language use. Let us continue to suppose that the earlier discussion of
deviance appears to correlate rather closely with problems of phonemic
and morphological analysis.
>>> 
>>> 
