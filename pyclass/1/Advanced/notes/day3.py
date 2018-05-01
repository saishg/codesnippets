Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 26 2016, 12:10:39) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj151/dunder_methods.py =======
{'RAYMOND': 'red'}

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj151/dunder_methods.py", line 8, in <module>
    print c['Raymond']
KeyError: 'Raymond'
>>> 'RAYMOND' == 'Raymond'
False
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj151/dunder_methods.py =======
{'raymond': 'red'}

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj151/dunder_methods.py", line 10, in <module>
    print c['Raymond']
KeyError: 'Raymond'
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj151/dunder_methods.py =======
{'raymond': 'red'}
red
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj151/dunder_methods.py =======
{'raymond': 'red'}
red
{}
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj151/dunder_methods.py =======
{'raymond': 'red'}
red
{}

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj151/dunder_methods.py", line 21, in <module>
    print c['ROGER']
  File "/Users/raymond/Dropbox/Public/sj151/dunder_methods.py", line 5, in __getitem__
    return dict.__getitem__(self, key)
KeyError: 'roger'
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj151/dunder_methods.py =======
{'raymond': 'red'}
red
{}

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj151/dunder_methods.py", line 24, in <module>
    print c['ROGER']
  File "/Users/raymond/Dropbox/Public/sj151/dunder_methods.py", line 5, in __getitem__
    return dict.__getitem__(self, key)
  File "/Users/raymond/Dropbox/Public/sj151/dunder_methods.py", line 8, in __missing__
    raise KeyError('Missing key, could be any case variant of {0!r}'.format(key))
KeyError: "Missing key, could be any case variant of 'roger'"
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj151/dunder_methods.py =======
>>> d
{'horses': 6, 'cats': 4, 'dogs': 2}
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj151/dunder_methods.py =======
2
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj151/dunder_methods.py =======
2
0
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj151/dunder_methods.py =======
2
0
1
>>> s = 'hello'
>>> s.replace('l', 'L')
'heLLo'
>>> s . replace ('l', 'L')
'heLLo'
>>> bm = s . replace
>>> bm('l', 'L')
'heLLo'
>>> s.xyz

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    s.xyz
AttributeError: 'str' object has no attribute 'xyz'
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj151/dunder_methods.py =======
{'RAYMOND': 'red'}
>>> e.__class__
<class '__main__.CIDot'>
>>> type(e)
<class '__main__.CIDot'>
>>> e.__dict__
{'RAYMOND': 'red'}
>>> vars(e)
{'RAYMOND': 'red'}
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj151/dunder_methods.py =======
{'RAYMOND': 'red'}
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj151/dunder_methods.py =======

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj151/dunder_methods.py", line 44, in <module>
    e.RAYMOND = 'red'
TypeError: __setattr__() takes exactly 2 arguments (3 given)
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj151/dunder_methods.py =======

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj151/dunder_methods.py", line 44, in <module>
    e.RAYMOND = 'red'
TypeError: __setattr__() takes exactly 2 arguments (3 given)
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj151/dunder_methods.py =======
{'raymond': 'red'}
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj151/dunder_methods.py =======
{'raymond': 'red'}

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj151/dunder_methods.py", line 46, in <module>
    print c.Raymond
NameError: name 'c' is not defined
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj151/dunder_methods.py =======

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj151/dunder_methods.py", line 49, in <module>
    print vars(e)
TypeError: vars() argument must have __dict__ attribute
>>> e
<__main__.CIDot object at 0x10384ddd0>
>>> e.__dict__

Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    e.__dict__
  File "/Users/raymond/Dropbox/Public/sj151/dunder_methods.py", line 41, in __getattribute__
    return object.__getattr__(self, attr)
AttributeError: type object 'object' has no attribute '__getattr__'
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj151/dunder_methods.py =======
{'raymond': 'red'}

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj151/dunder_methods.py", line 50, in <module>
    print c.Raymond
NameError: name 'c' is not defined
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj151/dunder_methods.py =======
{'raymond': 'red'}
red
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj151/dunder_methods.py =======
{'raymond': 'red'}
red
{}
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj151/dunder_methods.py =======
{'raymond': 'red'}
red
{}

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj151/dunder_methods.py", line 58, in <module>
    print e.ROGER
  File "/Users/raymond/Dropbox/Public/sj151/dunder_methods.py", line 41, in __getattribute__
    return object.__getattribute__(self, attr)
AttributeError: 'CIDot' object has no attribute 'roger'
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj151/dunder_methods.py =======
{'raymond': 'red'}
red
{}

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj151/dunder_methods.py", line 61, in <module>
    print e.ROGER
  File "/Users/raymond/Dropbox/Public/sj151/dunder_methods.py", line 44, in __getattr__
    raise AttributeError('Missing attribute, could be any case variant of {0!r}'.format(key))
NameError: global name 'key' is not defined
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj151/dunder_methods.py =======
{'raymond': 'red'}
red
{}

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj151/dunder_methods.py", line 61, in <module>
    print e.ROGER
  File "/Users/raymond/Dropbox/Public/sj151/dunder_methods.py", line 44, in __getattr__
    raise AttributeError('Missing attribute, could be any case variant of {0!r}'.format(attr))
AttributeError: Missing attribute, could be any case variant of 'ROGER'
>>> 
>>> 
>>> class A(object):
	x = 10

	
>>> A.x
10
>>> v = 'x'
>>> A.v

Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    A.v
AttributeError: type object 'A' has no attribute 'v'
>>> 
>>> getattr(A, v)
10
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj151/attrdict.py ==========
>>> 
>>> d
{'rachel': 'banana', 'raymond': 'apple'}
>>> vars(d)
{'matthew': 'orange', 'jill': 'pears'}
>>> d.keys()
['rachel', 'raymond']
>>> d.values()
['banana', 'apple']
>>> d.items()
[('rachel', 'banana'), ('raymond', 'apple')]
>>> d.get('rachel', 'nuts')
'banana'
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj151/attrdict.py ==========
apple
banana
>>> d
{'rachel': 'banana', 'raymond': 'apple'}
>>> vars(d)
{'matthew': 'orange', 'jill': 'pears'}
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj151/attrdict.py ==========
apple
banana
>>> d
{'matthew': 'orange', 'rachel': 'banana', 'raymond': 'apple', 'jill': 'pears'}
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/sj151/attrdict.py ==========
apple
banana
orange
pears
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj151/dunder_methods.py =======
{'raymond': 'red'}
red
{}

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj151/dunder_methods.py", line 63, in <module>
    print e.ROGER
  File "/Users/raymond/Dropbox/Public/sj151/dunder_methods.py", line 47, in __getattr__
    raise AttributeError('Missing attribute, could be any case variant of {0!r}'.format(attr))
AttributeError: Missing attribute, could be any case variant of 'ROGER'
>>> '}
SyntaxError: EOL while scanning string literal
>>> 
>>> 
>>> e.foo()

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    e.foo()
TypeError: foo() takes exactly 2 arguments (1 given)
>>> e.foo(15)
Foo was called with 15
>>> e.FOO(15)
Foo was called with 15
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj151/dunder_methods.py =======
{'raymond': 'red'}
red
{}
Foo was called with 15
Foo was called with 15
>>> # __new__ create the new object
>>> # __init__ puts the data in the object
>>> 
>>> 
>>> class Tuple(tuple):
	def __init__(self, *args):
		self[0] = args

		
>>> t = Tuple([10])

Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    t = Tuple([10])
  File "<pyshell#47>", line 3, in __init__
    self[0] = args
TypeError: 'Tuple' object does not support item assignment
>>> class Tuple(tuple):
	def __new__(cls, *args):
		print 'Creating'
		return tuple.__new__(cls, *args)

	
>>> t = Tuple([10, 20, 30])
Creating
>>> t
(10, 20, 30)
>>> class Tuple(tuple):
	def __new__(cls, seq):
		print 'Creating'
		seq = [x**2 for x in seq]
		return tuple.__new__(cls, seq)

	
>>> Tuple([10, 20, 30])
Creating
(100, 400, 900)
>>> class Tuple(tuple):
	def __new__(cls, seq):
		print 'Creating'
		seq = [x**2 for x in seq]
		return tuple.__new__(cls, seq)
	def __init__(self, seq):
		print 'It is too late to change', self
		print 'We started with', seq

		
>>> Tuple([10, 20, 30])
Creating
It is too late to change (100, 400, 900)
We started with [10, 20, 30]
(100, 400, 900)
>>> class Tuple(tuple):
	def __new__(cls, seq1):
		print 'Creating'
		seq2 = [x**2 for x in seq1]
		print 'New locals:', locals()
		return tuple.__new__(cls, seq2)
	def __init__(self, seq3):
		print 'Init locals:', locals()
		print 'It is too late to change', self
		print 'We started with', seq3

		
>>> Tuple([10, 20, 30])
Creating
New locals: {'seq2': [100, 400, 900], 'seq1': [10, 20, 30], 'cls': <class '__main__.Tuple'>, 'x': 30}
Init locals: {'seq3': [10, 20, 30], 'self': (100, 400, 900)}
It is too late to change (100, 400, 900)
We started with [10, 20, 30]
(100, 400, 900)
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj151/dunder_methods.py =======
Create a new <class '__main__.Everything'> with (44,)
Made an instance at 0x102f4de10
Initializing from: {}
to: {'y': 44}
>>> f(15)

Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    f(15)
TypeError: 'Everything' object is not callable
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj151/dunder_methods.py =======
Create a new <class '__main__.Everything'> with (44,)
Made an instance at 0x102f4ddd0
Initializing from: {}
to: {'y': 44}
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj151/dunder_methods.py =======
Create a new <class '__main__.Everything'> with (44,)
Made an instance at 0x1030e2dd0
Initializing from: {}
to: {'y': 44}
Called with 15
225
>>> f
<__main__.Everything object at 0x1030e2dd0>
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj151/dunder_methods.py =======
Create a new <class '__main__.Everything'> with (44,)
Made an instance at 0x102f4de10
Initializing from: {}
to: {'y': 44}
Called with 15
225

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj151/dunder_methods.py", line 79, in <module>
    print f
  File "/Users/raymond/Dropbox/Public/sj151/dunder_methods.py", line 75, in __repr__
    return '%s(%r)' % (self.__class__.__name__, self.y)
NameError: global name 'self' is not defined
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj151/dunder_methods.py =======
Create a new <class '__main__.Everything'> with (44,)
Made an instance at 0x102f4de10
Initializing from: {}
to: {'y': 44}
Called with 15
225
Everything(44)
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/sj151/dunder_methods.py =======
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj151/family.py ===========
The Starks Family
=================
* Eddard
* Catelyn
* Robb
* John Snow
* Arya
* Rickon
* Bram
* Sansa

>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> import family
>>> type(family)
<type 'module'>
>>> id(family)
4354628752
>>> module.__class__

Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    module.__class__
NameError: name 'module' is not defined
>>> family.__class__
<type 'module'>
>>> family.__name__
'family'
>>> family.__doc__
'Practice patterns of output formatting'
>>> family.__file__
'family.py'
>>> family.__dict__.keys()
['__builtins__', 'show_family', '__file__', '__package__', '__name__', '__doc__']
>>> family.__package__ is None
True
>>> family.__dict__['show_family']
<function show_family at 0x100505500>
>>> family.__dict__['show_family']('simpsons', ['homer', 'marge', 'bart', 'lisa', 'maggie'])
The Simpsons Family
===================
* Homer
* Marge
* Bart
* Lisa
* Maggie

>>> 
>>> 
>>> family.show_family('simpsons', ['homer', 'marge', 'bart', 'lisa', 'maggie'])
The Simpsons Family
===================
* Homer
* Marge
* Bart
* Lisa
* Maggie

>>> 
=============================== RESTART: Shell ===============================
>>> from family import show_family
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'show_family']
>>> show_family('simpsons', ['homer', 'marge', 'bart', 'lisa', 'maggie'])
The Simpsons Family
===================
* Homer
* Marge
* Bart
* Lisa
* Maggie

>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj151/sample.py ===========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
Happy!
>>> 
=============================== RESTART: Shell ===============================
>>> import sample
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'sample']
>>> type(sample)
<type 'module'>
>>> sample.__class__
<type 'module'>
>>> sample.__name__
'sample'
>>> sample.__doc__
'A simple demonstration of Python'
>>> sample.__file__
'sample.py'
>>> sample.__package__ is None
True
>>> sample.__dict__.keys()
['squares', '__builtins__', '__file__', 'n', 'i', 'cube', '__name__', '__package__', '__doc__']
>>> 
>>> sample.__dict__['n']
20
>>> sample.n
20
>>> dir(sample)
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cube', 'i', 'n', 'squares']
>>> sorted(sample.__dict__.keys())
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cube', 'i', 'n', 'squares']
>>> sample.__dict__
{'squares': [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361], '__builtins__': {'bytearray': <type 'bytearray'>, 'IndexError': <type 'exceptions.IndexError'>, 'all': <built-in function all>, 'help': Type help() for interactive help, or help(object) for help about object., 'vars': <built-in function vars>, 'SyntaxError': <type 'exceptions.SyntaxError'>, 'unicode': <type 'unicode'>, 'UnicodeDecodeError': <type 'exceptions.UnicodeDecodeError'>, 'memoryview': <type 'memoryview'>, 'isinstance': <built-in function isinstance>, 'copyright': Copyright (c) 2001-2016 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved., 'NameError': <type 'exceptions.NameError'>, 'BytesWarning': <type 'exceptions.BytesWarning'>, 'dict': <type 'dict'>, 'input': <built-in function input>, 'oct': <built-in function oct>, 'bin': <built-in function bin>, 'SystemExit': <type 'exceptions.SystemExit'>, 'StandardError': <type 'exceptions.StandardError'>, 'format': <built-in function format>, 'repr': <built-in function repr>, 'sorted': <built-in function sorted>, 'False': False, 'RuntimeWarning': <type 'exceptions.RuntimeWarning'>, 'list': <type 'list'>, 'iter': <built-in function iter>, 'reload': <built-in function reload>, 'Warning': <type 'exceptions.Warning'>, '__package__': None, 'round': <built-in function round>, 'dir': <built-in function dir>, 'cmp': <built-in function cmp>, 'set': <type 'set'>, 'bytes': <type 'str'>, 'reduce': <built-in function reduce>, 'intern': <built-in function intern>, 'issubclass': <built-in function issubclass>, 'Ellipsis': Ellipsis, 'EOFError': <type 'exceptions.EOFError'>, 'locals': <built-in function locals>, 'BufferError': <type 'exceptions.BufferError'>, 'slice': <type 'slice'>, 'FloatingPointError': <type 'exceptions.FloatingPointError'>, 'sum': <built-in function sum>, 'getattr': <built-in function getattr>, 'abs': <built-in function abs>, 'exit': Use exit() or Ctrl-D (i.e. EOF) to exit, 'print': <built-in function print>, 'True': True, 'FutureWarning': <type 'exceptions.FutureWarning'>, 'ImportWarning': <type 'exceptions.ImportWarning'>, 'None': None, 'hash': <built-in function hash>, 'ReferenceError': <type 'exceptions.ReferenceError'>, 'len': <built-in function len>, 'credits':     Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information., 'frozenset': <type 'frozenset'>, '__name__': '__builtin__', 'ord': <built-in function ord>, 'super': <type 'super'>, '_': None, 'TypeError': <type 'exceptions.TypeError'>, 'license': Type license() to see the full license text, 'KeyboardInterrupt': <type 'exceptions.KeyboardInterrupt'>, 'UserWarning': <type 'exceptions.UserWarning'>, 'filter': <built-in function filter>, 'range': <built-in function range>, 'staticmethod': <type 'staticmethod'>, 'SystemError': <type 'exceptions.SystemError'>, 'BaseException': <type 'exceptions.BaseException'>, 'pow': <built-in function pow>, 'RuntimeError': <type 'exceptions.RuntimeError'>, 'float': <type 'float'>, 'MemoryError': <type 'exceptions.MemoryError'>, 'StopIteration': <type 'exceptions.StopIteration'>, 'globals': <built-in function globals>, 'divmod': <built-in function divmod>, 'enumerate': <type 'enumerate'>, 'apply': <built-in function apply>, 'LookupError': <type 'exceptions.LookupError'>, 'open': <built-in function open>, 'quit': Use quit() or Ctrl-D (i.e. EOF) to exit, 'basestring': <type 'basestring'>, 'UnicodeError': <type 'exceptions.UnicodeError'>, 'zip': <built-in function zip>, 'hex': <built-in function hex>, 'long': <type 'long'>, 'next': <built-in function next>, 'ImportError': <type 'exceptions.ImportError'>, 'chr': <built-in function chr>, 'xrange': <type 'xrange'>, 'type': <type 'type'>, '__doc__': "Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices.", 'Exception': <type 'exceptions.Exception'>, 'tuple': <type 'tuple'>, 'UnicodeTranslateError': <type 'exceptions.UnicodeTranslateError'>, 'reversed': <type 'reversed'>, 'UnicodeEncodeError': <type 'exceptions.UnicodeEncodeError'>, 'IOError': <type 'exceptions.IOError'>, 'hasattr': <built-in function hasattr>, 'delattr': <built-in function delattr>, 'setattr': <built-in function setattr>, 'raw_input': <built-in function raw_input>, 'SyntaxWarning': <type 'exceptions.SyntaxWarning'>, 'compile': <built-in function compile>, 'ArithmeticError': <type 'exceptions.ArithmeticError'>, 'str': <type 'str'>, 'property': <type 'property'>, 'GeneratorExit': <type 'exceptions.GeneratorExit'>, 'int': <type 'int'>, '__import__': <built-in function __import__>, 'KeyError': <type 'exceptions.KeyError'>, 'coerce': <built-in function coerce>, 'PendingDeprecationWarning': <type 'exceptions.PendingDeprecationWarning'>, 'file': <type 'file'>, 'EnvironmentError': <type 'exceptions.EnvironmentError'>, 'unichr': <built-in function unichr>, 'id': <built-in function id>, 'OSError': <type 'exceptions.OSError'>, 'DeprecationWarning': <type 'exceptions.DeprecationWarning'>, 'min': <built-in function min>, 'UnicodeWarning': <type 'exceptions.UnicodeWarning'>, 'execfile': <built-in function execfile>, 'any': <built-in function any>, 'complex': <type 'complex'>, 'bool': <type 'bool'>, 'ValueError': <type 'exceptions.ValueError'>, 'NotImplemented': NotImplemented, 'map': <built-in function map>, 'buffer': <type 'buffer'>, 'max': <built-in function max>, 'object': <type 'object'>, 'TabError': <type 'exceptions.TabError'>, 'callable': <built-in function callable>, 'ZeroDivisionError': <type 'exceptions.ZeroDivisionError'>, 'eval': <built-in function eval>, '__debug__': True, 'IndentationError': <type 'exceptions.IndentationError'>, 'AssertionError': <type 'exceptions.AssertionError'>, 'classmethod': <type 'classmethod'>, 'UnboundLocalError': <type 'exceptions.UnboundLocalError'>, 'NotImplementedError': <type 'exceptions.NotImplementedError'>, 'AttributeError': <type 'exceptions.AttributeError'>, 'OverflowError': <type 'exceptions.OverflowError'>}, '__file__': 'sample.py', 'n': 20, 'i': 19, 'cube': <function cube at 0x100505500>, '__name__': 'sample', '__package__': None, '__doc__': 'A simple demonstration of Python'}
>>> globals().keys()
['__builtins__', '__package__', 'sample', '__name__', '__doc__']
>>> 
>>> 
>>> sample.__dict__
{'squares': [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361], '__builtins__': {'bytearray': <type 'bytearray'>, 'IndexError': <type 'exceptions.IndexError'>, 'all': <built-in function all>, 'help': Type help() for interactive help, or help(object) for help about object., 'vars': <built-in function vars>, 'SyntaxError': <type 'exceptions.SyntaxError'>, 'unicode': <type 'unicode'>, 'UnicodeDecodeError': <type 'exceptions.UnicodeDecodeError'>, 'memoryview': <type 'memoryview'>, 'isinstance': <built-in function isinstance>, 'copyright': Copyright (c) 2001-2016 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved., 'NameError': <type 'exceptions.NameError'>, 'BytesWarning': <type 'exceptions.BytesWarning'>, 'dict': <type 'dict'>, 'input': <built-in function input>, 'oct': <built-in function oct>, 'bin': <built-in function bin>, 'SystemExit': <type 'exceptions.SystemExit'>, 'StandardError': <type 'exceptions.StandardError'>, 'format': <built-in function format>, 'repr': <built-in function repr>, 'sorted': <built-in function sorted>, 'False': False, 'RuntimeWarning': <type 'exceptions.RuntimeWarning'>, 'list': <type 'list'>, 'iter': <built-in function iter>, 'reload': <built-in function reload>, 'Warning': <type 'exceptions.Warning'>, '__package__': None, 'round': <built-in function round>, 'dir': <built-in function dir>, 'cmp': <built-in function cmp>, 'set': <type 'set'>, 'bytes': <type 'str'>, 'reduce': <built-in function reduce>, 'intern': <built-in function intern>, 'issubclass': <built-in function issubclass>, 'Ellipsis': Ellipsis, 'EOFError': <type 'exceptions.EOFError'>, 'locals': <built-in function locals>, 'BufferError': <type 'exceptions.BufferError'>, 'slice': <type 'slice'>, 'FloatingPointError': <type 'exceptions.FloatingPointError'>, 'sum': <built-in function sum>, 'getattr': <built-in function getattr>, 'abs': <built-in function abs>, 'exit': Use exit() or Ctrl-D (i.e. EOF) to exit, 'print': <built-in function print>, 'True': True, 'FutureWarning': <type 'exceptions.FutureWarning'>, 'ImportWarning': <type 'exceptions.ImportWarning'>, 'None': None, 'hash': <built-in function hash>, 'ReferenceError': <type 'exceptions.ReferenceError'>, 'len': <built-in function len>, 'credits':     Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information., 'frozenset': <type 'frozenset'>, '__name__': '__builtin__', 'ord': <built-in function ord>, 'super': <type 'super'>, '_': None, 'TypeError': <type 'exceptions.TypeError'>, 'license': Type license() to see the full license text, 'KeyboardInterrupt': <type 'exceptions.KeyboardInterrupt'>, 'UserWarning': <type 'exceptions.UserWarning'>, 'filter': <built-in function filter>, 'range': <built-in function range>, 'staticmethod': <type 'staticmethod'>, 'SystemError': <type 'exceptions.SystemError'>, 'BaseException': <type 'exceptions.BaseException'>, 'pow': <built-in function pow>, 'RuntimeError': <type 'exceptions.RuntimeError'>, 'float': <type 'float'>, 'MemoryError': <type 'exceptions.MemoryError'>, 'StopIteration': <type 'exceptions.StopIteration'>, 'globals': <built-in function globals>, 'divmod': <built-in function divmod>, 'enumerate': <type 'enumerate'>, 'apply': <built-in function apply>, 'LookupError': <type 'exceptions.LookupError'>, 'open': <built-in function open>, 'quit': Use quit() or Ctrl-D (i.e. EOF) to exit, 'basestring': <type 'basestring'>, 'UnicodeError': <type 'exceptions.UnicodeError'>, 'zip': <built-in function zip>, 'hex': <built-in function hex>, 'long': <type 'long'>, 'next': <built-in function next>, 'ImportError': <type 'exceptions.ImportError'>, 'chr': <built-in function chr>, 'xrange': <type 'xrange'>, 'type': <type 'type'>, '__doc__': "Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices.", 'Exception': <type 'exceptions.Exception'>, 'tuple': <type 'tuple'>, 'UnicodeTranslateError': <type 'exceptions.UnicodeTranslateError'>, 'reversed': <type 'reversed'>, 'UnicodeEncodeError': <type 'exceptions.UnicodeEncodeError'>, 'IOError': <type 'exceptions.IOError'>, 'hasattr': <built-in function hasattr>, 'delattr': <built-in function delattr>, 'setattr': <built-in function setattr>, 'raw_input': <built-in function raw_input>, 'SyntaxWarning': <type 'exceptions.SyntaxWarning'>, 'compile': <built-in function compile>, 'ArithmeticError': <type 'exceptions.ArithmeticError'>, 'str': <type 'str'>, 'property': <type 'property'>, 'GeneratorExit': <type 'exceptions.GeneratorExit'>, 'int': <type 'int'>, '__import__': <built-in function __import__>, 'KeyError': <type 'exceptions.KeyError'>, 'coerce': <built-in function coerce>, 'PendingDeprecationWarning': <type 'exceptions.PendingDeprecationWarning'>, 'file': <type 'file'>, 'EnvironmentError': <type 'exceptions.EnvironmentError'>, 'unichr': <built-in function unichr>, 'id': <built-in function id>, 'OSError': <type 'exceptions.OSError'>, 'DeprecationWarning': <type 'exceptions.DeprecationWarning'>, 'min': <built-in function min>, 'UnicodeWarning': <type 'exceptions.UnicodeWarning'>, 'execfile': <built-in function execfile>, 'any': <built-in function any>, 'complex': <type 'complex'>, 'bool': <type 'bool'>, 'ValueError': <type 'exceptions.ValueError'>, 'NotImplemented': NotImplemented, 'map': <built-in function map>, 'buffer': <type 'buffer'>, 'max': <built-in function max>, 'object': <type 'object'>, 'TabError': <type 'exceptions.TabError'>, 'callable': <built-in function callable>, 'ZeroDivisionError': <type 'exceptions.ZeroDivisionError'>, 'eval': <built-in function eval>, '__debug__': True, 'IndentationError': <type 'exceptions.IndentationError'>, 'AssertionError': <type 'exceptions.AssertionError'>, 'classmethod': <type 'classmethod'>, 'UnboundLocalError': <type 'exceptions.UnboundLocalError'>, 'NotImplementedError': <type 'exceptions.NotImplementedError'>, 'AttributeError': <type 'exceptions.AttributeError'>, 'OverflowError': <type 'exceptions.OverflowError'>}, '__file__': 'sample.py', 'n': 20, 'i': 19, 'cube': <function cube at 0x100505500>, '__name__': 'sample', '__package__': None, '__doc__': 'A simple demonstration of Python'}
>>> 
>>> 
>>> 
>>> sample.__dict__.keys()
['squares', '__builtins__', '__file__', 'n', 'i', 'cube', '__name__', '__package__', '__doc__']
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj151/sample.py ===========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
['squares', '__builtins__', '__file__', '__package__', 'i', 'cube', '__name__', 'n', '__doc__']
Happy!
>>> # To get to sample's namespace externally:
>>> #     sample.__dict__
>>> #     vars(sample)
>>> # But inside the module, it called:
>>> #     globals()
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj151/sample.py ===========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
Happy!
>>> sample.__doc__

Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    sample.__doc__
NameError: name 'sample' is not defined
>>> 
>>> 
>>> import sample
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
>>> sample.__doc__
'A simple demonstration of Python'
>>> sample.n
20
>>> sample.squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
>>> sample.cube(11)
1331
>>> 
>>> 
>>> import sample
>>> import http://users.rcn.com/python/puzzle.py
SyntaxError: invalid syntax
>>> import parse.json

Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    import parse.json
ImportError: No module named json
>>> import random
>>> random.randrange()

Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    random.randrange()
TypeError: randrange() takes at least 2 arguments (1 given)
>>> random.randrange(50)
47
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
'A simple demonstration of Python'

n = 20

squares = [i**2 for i in xrange(n)]

print 'The sum of squares is %d' % sum(squares)

def cube(x):
    return x ** 3

print map(cube, range(n))

if __name__ == '__main__':
    print 'Happy!'

>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
'A simple demonstration of Python'

n = 20

squares = [i**2 for i in xrange(n)]

print 'The sum of squares is %d' % sum(squares)

def cube(x):
    return x ** 3

print map(cube, range(n))

if __name__ == '__main__':
    print 'Happy!'

>>> import sample
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
>>> sample.__dict__.keys()
['squares', '__builtins__', '__file__', 'n', 'i', 'cube', '__name__', '__package__', '__doc__']
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
>>> namespace
{'squares': [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361], 'i': 19, '__file__': 'sample.py', 'n': 20, 'cube': <function cube at 0x1005050c8>, '__name__': 'sample', '__package__': None, '__doc__': 'A simple demonstration of Python'}
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
{'__doc__': 'A simple demonstration of Python',
 '__file__': 'sample.py',
 '__name__': 'sample',
 '__package__': None,
 'cube': <function cube at 0x1005050c8>,
 'i': 19,
 'n': 20,
 'squares': [0,
             1,
             4,
             9,
             16,
             25,
             36,
             49,
             64,
             81,
             100,
             121,
             144,
             169,
             196,
             225,
             256,
             289,
             324,
             361]}
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
>>> namespace.keys()
['squares', '__builtins__', '__file__', 'n', 'i', 'cube', '__name__', '__package__', '__doc__']
>>> sorted(namespace.keys())
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cube', 'i', 'n', 'squares']
>>> import sample
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
>>> dir(sample)
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cube', 'i', 'n', 'squares']
>>> sorted(namespace.keys())
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cube', 'i', 'n', 'squares']
>>> namespace
{'squares': [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361], '__builtins__': {'bytearray': <type 'bytearray'>, 'IndexError': <type 'exceptions.IndexError'>, 'all': <built-in function all>, 'help': Type help() for interactive help, or help(object) for help about object., 'vars': <built-in function vars>, 'SyntaxError': <type 'exceptions.SyntaxError'>, 'unicode': <type 'unicode'>, 'UnicodeDecodeError': <type 'exceptions.UnicodeDecodeError'>, 'memoryview': <type 'memoryview'>, 'isinstance': <built-in function isinstance>, 'copyright': Copyright (c) 2001-2016 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved., 'NameError': <type 'exceptions.NameError'>, 'BytesWarning': <type 'exceptions.BytesWarning'>, 'dict': <type 'dict'>, 'input': <built-in function input>, 'oct': <built-in function oct>, 'bin': <built-in function bin>, 'SystemExit': <type 'exceptions.SystemExit'>, 'StandardError': <type 'exceptions.StandardError'>, 'format': <built-in function format>, 'repr': <built-in function repr>, 'sorted': <built-in function sorted>, 'False': False, 'RuntimeWarning': <type 'exceptions.RuntimeWarning'>, 'list': <type 'list'>, 'iter': <built-in function iter>, 'reload': <built-in function reload>, 'Warning': <type 'exceptions.Warning'>, '__package__': None, 'round': <built-in function round>, 'dir': <built-in function dir>, 'cmp': <built-in function cmp>, 'set': <type 'set'>, 'bytes': <type 'str'>, 'reduce': <built-in function reduce>, 'intern': <built-in function intern>, 'issubclass': <built-in function issubclass>, 'Ellipsis': Ellipsis, 'EOFError': <type 'exceptions.EOFError'>, 'locals': <built-in function locals>, 'BufferError': <type 'exceptions.BufferError'>, 'slice': <type 'slice'>, 'FloatingPointError': <type 'exceptions.FloatingPointError'>, 'sum': <built-in function sum>, 'getattr': <built-in function getattr>, 'abs': <built-in function abs>, 'exit': Use exit() or Ctrl-D (i.e. EOF) to exit, 'print': <built-in function print>, 'True': True, 'FutureWarning': <type 'exceptions.FutureWarning'>, 'ImportWarning': <type 'exceptions.ImportWarning'>, 'None': None, 'hash': <built-in function hash>, 'ReferenceError': <type 'exceptions.ReferenceError'>, 'len': <built-in function len>, 'credits':     Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information., 'frozenset': <type 'frozenset'>, '__name__': '__builtin__', 'ord': <built-in function ord>, 'super': <type 'super'>, '_': None, 'TypeError': <type 'exceptions.TypeError'>, 'license': Type license() to see the full license text, 'KeyboardInterrupt': <type 'exceptions.KeyboardInterrupt'>, 'UserWarning': <type 'exceptions.UserWarning'>, 'filter': <built-in function filter>, 'range': <built-in function range>, 'staticmethod': <type 'staticmethod'>, 'SystemError': <type 'exceptions.SystemError'>, 'BaseException': <type 'exceptions.BaseException'>, 'pow': <built-in function pow>, 'RuntimeError': <type 'exceptions.RuntimeError'>, 'float': <type 'float'>, 'MemoryError': <type 'exceptions.MemoryError'>, 'StopIteration': <type 'exceptions.StopIteration'>, 'globals': <built-in function globals>, 'divmod': <built-in function divmod>, 'enumerate': <type 'enumerate'>, 'apply': <built-in function apply>, 'LookupError': <type 'exceptions.LookupError'>, 'open': <built-in function open>, 'quit': Use quit() or Ctrl-D (i.e. EOF) to exit, 'basestring': <type 'basestring'>, 'UnicodeError': <type 'exceptions.UnicodeError'>, 'zip': <built-in function zip>, 'hex': <built-in function hex>, 'long': <type 'long'>, 'next': <built-in function next>, 'ImportError': <type 'exceptions.ImportError'>, 'chr': <built-in function chr>, 'xrange': <type 'xrange'>, 'type': <type 'type'>, '__doc__': "Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices.", 'Exception': <type 'exceptions.Exception'>, 'tuple': <type 'tuple'>, 'UnicodeTranslateError': <type 'exceptions.UnicodeTranslateError'>, 'reversed': <type 'reversed'>, 'UnicodeEncodeError': <type 'exceptions.UnicodeEncodeError'>, 'IOError': <type 'exceptions.IOError'>, 'hasattr': <built-in function hasattr>, 'delattr': <built-in function delattr>, 'setattr': <built-in function setattr>, 'raw_input': <built-in function raw_input>, 'SyntaxWarning': <type 'exceptions.SyntaxWarning'>, 'compile': <built-in function compile>, 'ArithmeticError': <type 'exceptions.ArithmeticError'>, 'str': <type 'str'>, 'property': <type 'property'>, 'GeneratorExit': <type 'exceptions.GeneratorExit'>, 'int': <type 'int'>, '__import__': <built-in function __import__>, 'KeyError': <type 'exceptions.KeyError'>, 'coerce': <built-in function coerce>, 'PendingDeprecationWarning': <type 'exceptions.PendingDeprecationWarning'>, 'file': <type 'file'>, 'EnvironmentError': <type 'exceptions.EnvironmentError'>, 'unichr': <built-in function unichr>, 'id': <built-in function id>, 'OSError': <type 'exceptions.OSError'>, 'DeprecationWarning': <type 'exceptions.DeprecationWarning'>, 'min': <built-in function min>, 'UnicodeWarning': <type 'exceptions.UnicodeWarning'>, 'execfile': <built-in function execfile>, 'any': <built-in function any>, 'complex': <type 'complex'>, 'bool': <type 'bool'>, 'ValueError': <type 'exceptions.ValueError'>, 'NotImplemented': NotImplemented, 'map': <built-in function map>, 'buffer': <type 'buffer'>, 'max': <built-in function max>, 'object': <type 'object'>, 'TabError': <type 'exceptions.TabError'>, 'callable': <built-in function callable>, 'ZeroDivisionError': <type 'exceptions.ZeroDivisionError'>, 'eval': <built-in function eval>, '__debug__': True, 'IndentationError': <type 'exceptions.IndentationError'>, 'AssertionError': <type 'exceptions.AssertionError'>, 'classmethod': <type 'classmethod'>, 'UnboundLocalError': <type 'exceptions.UnboundLocalError'>, 'NotImplementedError': <type 'exceptions.NotImplementedError'>, 'AttributeError': <type 'exceptions.AttributeError'>, 'OverflowError': <type 'exceptions.OverflowError'>}, '__file__': 'sample.py', 'n': 20, 'i': 19, 'cube': <function cube at 0x1005050c8>, '__name__': 'sample', '__package__': None, '__doc__': 'A simple demonstration of Python'}
>>> sample.__dict__
{'squares': [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361], '__builtins__': {'bytearray': <type 'bytearray'>, 'IndexError': <type 'exceptions.IndexError'>, 'all': <built-in function all>, 'help': Type help() for interactive help, or help(object) for help about object., 'vars': <built-in function vars>, 'SyntaxError': <type 'exceptions.SyntaxError'>, 'unicode': <type 'unicode'>, 'UnicodeDecodeError': <type 'exceptions.UnicodeDecodeError'>, 'memoryview': <type 'memoryview'>, 'isinstance': <built-in function isinstance>, 'copyright': Copyright (c) 2001-2016 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved., 'NameError': <type 'exceptions.NameError'>, 'BytesWarning': <type 'exceptions.BytesWarning'>, 'dict': <type 'dict'>, 'input': <built-in function input>, 'oct': <built-in function oct>, 'bin': <built-in function bin>, 'SystemExit': <type 'exceptions.SystemExit'>, 'StandardError': <type 'exceptions.StandardError'>, 'format': <built-in function format>, 'repr': <built-in function repr>, 'sorted': <built-in function sorted>, 'False': False, 'RuntimeWarning': <type 'exceptions.RuntimeWarning'>, 'list': <type 'list'>, 'iter': <built-in function iter>, 'reload': <built-in function reload>, 'Warning': <type 'exceptions.Warning'>, '__package__': None, 'round': <built-in function round>, 'dir': <built-in function dir>, 'cmp': <built-in function cmp>, 'set': <type 'set'>, 'bytes': <type 'str'>, 'reduce': <built-in function reduce>, 'intern': <built-in function intern>, 'issubclass': <built-in function issubclass>, 'Ellipsis': Ellipsis, 'EOFError': <type 'exceptions.EOFError'>, 'locals': <built-in function locals>, 'BufferError': <type 'exceptions.BufferError'>, 'slice': <type 'slice'>, 'FloatingPointError': <type 'exceptions.FloatingPointError'>, 'sum': <built-in function sum>, 'getattr': <built-in function getattr>, 'abs': <built-in function abs>, 'exit': Use exit() or Ctrl-D (i.e. EOF) to exit, 'print': <built-in function print>, 'True': True, 'FutureWarning': <type 'exceptions.FutureWarning'>, 'ImportWarning': <type 'exceptions.ImportWarning'>, 'None': None, 'hash': <built-in function hash>, 'ReferenceError': <type 'exceptions.ReferenceError'>, 'len': <built-in function len>, 'credits':     Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information., 'frozenset': <type 'frozenset'>, '__name__': '__builtin__', 'ord': <built-in function ord>, 'super': <type 'super'>, '_': None, 'TypeError': <type 'exceptions.TypeError'>, 'license': Type license() to see the full license text, 'KeyboardInterrupt': <type 'exceptions.KeyboardInterrupt'>, 'UserWarning': <type 'exceptions.UserWarning'>, 'filter': <built-in function filter>, 'range': <built-in function range>, 'staticmethod': <type 'staticmethod'>, 'SystemError': <type 'exceptions.SystemError'>, 'BaseException': <type 'exceptions.BaseException'>, 'pow': <built-in function pow>, 'RuntimeError': <type 'exceptions.RuntimeError'>, 'float': <type 'float'>, 'MemoryError': <type 'exceptions.MemoryError'>, 'StopIteration': <type 'exceptions.StopIteration'>, 'globals': <built-in function globals>, 'divmod': <built-in function divmod>, 'enumerate': <type 'enumerate'>, 'apply': <built-in function apply>, 'LookupError': <type 'exceptions.LookupError'>, 'open': <built-in function open>, 'quit': Use quit() or Ctrl-D (i.e. EOF) to exit, 'basestring': <type 'basestring'>, 'UnicodeError': <type 'exceptions.UnicodeError'>, 'zip': <built-in function zip>, 'hex': <built-in function hex>, 'long': <type 'long'>, 'next': <built-in function next>, 'ImportError': <type 'exceptions.ImportError'>, 'chr': <built-in function chr>, 'xrange': <type 'xrange'>, 'type': <type 'type'>, '__doc__': "Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices.", 'Exception': <type 'exceptions.Exception'>, 'tuple': <type 'tuple'>, 'UnicodeTranslateError': <type 'exceptions.UnicodeTranslateError'>, 'reversed': <type 'reversed'>, 'UnicodeEncodeError': <type 'exceptions.UnicodeEncodeError'>, 'IOError': <type 'exceptions.IOError'>, 'hasattr': <built-in function hasattr>, 'delattr': <built-in function delattr>, 'setattr': <built-in function setattr>, 'raw_input': <built-in function raw_input>, 'SyntaxWarning': <type 'exceptions.SyntaxWarning'>, 'compile': <built-in function compile>, 'ArithmeticError': <type 'exceptions.ArithmeticError'>, 'str': <type 'str'>, 'property': <type 'property'>, 'GeneratorExit': <type 'exceptions.GeneratorExit'>, 'int': <type 'int'>, '__import__': <built-in function __import__>, 'KeyError': <type 'exceptions.KeyError'>, 'coerce': <built-in function coerce>, 'PendingDeprecationWarning': <type 'exceptions.PendingDeprecationWarning'>, 'file': <type 'file'>, 'EnvironmentError': <type 'exceptions.EnvironmentError'>, 'unichr': <built-in function unichr>, 'id': <built-in function id>, 'OSError': <type 'exceptions.OSError'>, 'DeprecationWarning': <type 'exceptions.DeprecationWarning'>, 'min': <built-in function min>, 'UnicodeWarning': <type 'exceptions.UnicodeWarning'>, 'execfile': <built-in function execfile>, 'any': <built-in function any>, 'complex': <type 'complex'>, 'bool': <type 'bool'>, 'ValueError': <type 'exceptions.ValueError'>, 'NotImplemented': NotImplemented, 'map': <built-in function map>, 'buffer': <type 'buffer'>, 'max': <built-in function max>, 'object': <type 'object'>, 'TabError': <type 'exceptions.TabError'>, 'callable': <built-in function callable>, 'ZeroDivisionError': <type 'exceptions.ZeroDivisionError'>, 'eval': <built-in function eval>, '__debug__': True, 'IndentationError': <type 'exceptions.IndentationError'>, 'AssertionError': <type 'exceptions.AssertionError'>, 'classmethod': <type 'classmethod'>, 'UnboundLocalError': <type 'exceptions.UnboundLocalError'>, 'NotImplementedError': <type 'exceptions.NotImplementedError'>, 'AttributeError': <type 'exceptions.AttributeError'>, 'OverflowError': <type 'exceptions.OverflowError'>}, '__file__': '/Users/raymond/Dropbox/Public/sj151/sample.pyc', 'n': 20, 'i': 19, 'cube': <function cube at 0x100505500>, '__name__': 'sample', '__package__': None, '__doc__': 'A simple demonstration of Python'}
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
>>> type(sample)
<type 'dict'>
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cube', 'i', 'n', 'squares']
20
1331
>>> type(sample)
<type 'dict'>
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
<type 'dict'>
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cube', 'i', 'n', 'squares']
20
1331
>>> import sample
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
>>> type(sample)
<type 'module'>
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 24, in <module>
    sample = myimport('sample')
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 19, in myimport
    return modue
NameError: name 'modue' is not defined
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
<class '__main__.Module'>
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cube', 'i', 'n', 'squares']
20
1331
>>> 
import sample
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
>>> sample.__dict__.keys()
['squares', '__builtins__', '__file__', 'n', 'i', 'cube', '__name__', '__package__', '__doc__']
>>> 
>>> sample.n
20
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
<class '__main__.Module'>
20
1331
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
<class '__main__.Module'>

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 32, in <module>
    print sample.n
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattribute__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattribute__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattribute__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattribute__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattribute__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattribute__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattribute__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattribute__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattribute__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattribute__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattribute__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattribute__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattribute__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattribute__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattribute__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattribute__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattribute__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattribute__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattribute__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattribute__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattribute__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattribute__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattribute__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattribute__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattribute__
    return self.namespace[attr]

=============================== RESTART: Shell ===============================
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
<class '__main__.Module'>
20
1331
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 32, in <module>
    sample = myimport('sample')
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 26, in myimport
    module = Module(namespace)
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 6, in __init__
    self.namespace = namespace
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 12, in __setattr__
    self.namespace[attr] = value
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattr__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattr__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattr__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattr__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattr__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattr__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattr__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattr__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattr__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattr__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattr__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattr__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattr__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattr__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattr__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattr__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattr__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattr__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattr__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattr__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattr__
    return self.namespace[attr]
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattr__
    return self.namespace[attr]

=============================== RESTART: Shell ===============================
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
<class '__main__.Module'>
20
1331
>>> sample.y = 555
>>> sample.namespace['y']
555
>>> sample.y
555
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
<class '__main__.Module'>
20
1331
>>> sample.__dict__
{'namespace': {'squares': [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361], '__builtins__': {'bytearray': <type 'bytearray'>, 'IndexError': <type 'exceptions.IndexError'>, 'all': <built-in function all>, 'help': Type help() for interactive help, or help(object) for help about object., 'vars': <built-in function vars>, 'SyntaxError': <type 'exceptions.SyntaxError'>, 'unicode': <type 'unicode'>, 'UnicodeDecodeError': <type 'exceptions.UnicodeDecodeError'>, 'memoryview': <type 'memoryview'>, 'isinstance': <built-in function isinstance>, 'copyright': Copyright (c) 2001-2016 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved., 'NameError': <type 'exceptions.NameError'>, 'BytesWarning': <type 'exceptions.BytesWarning'>, 'dict': <type 'dict'>, 'input': <built-in function input>, 'oct': <built-in function oct>, 'bin': <built-in function bin>, 'SystemExit': <type 'exceptions.SystemExit'>, 'StandardError': <type 'exceptions.StandardError'>, 'format': <built-in function format>, 'repr': <built-in function repr>, 'sorted': <built-in function sorted>, 'False': False, 'RuntimeWarning': <type 'exceptions.RuntimeWarning'>, 'list': <type 'list'>, 'iter': <built-in function iter>, 'reload': <built-in function reload>, 'Warning': <type 'exceptions.Warning'>, '__package__': None, 'round': <built-in function round>, 'dir': <built-in function dir>, 'cmp': <built-in function cmp>, 'set': <type 'set'>, 'bytes': <type 'str'>, 'reduce': <built-in function reduce>, 'intern': <built-in function intern>, 'issubclass': <built-in function issubclass>, 'Ellipsis': Ellipsis, 'EOFError': <type 'exceptions.EOFError'>, 'locals': <built-in function locals>, 'BufferError': <type 'exceptions.BufferError'>, 'slice': <type 'slice'>, 'FloatingPointError': <type 'exceptions.FloatingPointError'>, 'sum': <built-in function sum>, 'getattr': <built-in function getattr>, 'abs': <built-in function abs>, 'exit': Use exit() or Ctrl-D (i.e. EOF) to exit, 'print': <built-in function print>, 'True': True, 'FutureWarning': <type 'exceptions.FutureWarning'>, 'ImportWarning': <type 'exceptions.ImportWarning'>, 'None': None, 'hash': <built-in function hash>, 'ReferenceError': <type 'exceptions.ReferenceError'>, 'len': <built-in function len>, 'credits':     Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information., 'frozenset': <type 'frozenset'>, '__name__': '__builtin__', 'ord': <built-in function ord>, 'super': <type 'super'>, '_': None, 'TypeError': <type 'exceptions.TypeError'>, 'license': Type license() to see the full license text, 'KeyboardInterrupt': <type 'exceptions.KeyboardInterrupt'>, 'UserWarning': <type 'exceptions.UserWarning'>, 'filter': <built-in function filter>, 'range': <built-in function range>, 'staticmethod': <type 'staticmethod'>, 'SystemError': <type 'exceptions.SystemError'>, 'BaseException': <type 'exceptions.BaseException'>, 'pow': <built-in function pow>, 'RuntimeError': <type 'exceptions.RuntimeError'>, 'float': <type 'float'>, 'MemoryError': <type 'exceptions.MemoryError'>, 'StopIteration': <type 'exceptions.StopIteration'>, 'globals': <built-in function globals>, 'divmod': <built-in function divmod>, 'enumerate': <type 'enumerate'>, 'apply': <built-in function apply>, 'LookupError': <type 'exceptions.LookupError'>, 'open': <built-in function open>, 'quit': Use quit() or Ctrl-D (i.e. EOF) to exit, 'basestring': <type 'basestring'>, 'UnicodeError': <type 'exceptions.UnicodeError'>, 'zip': <built-in function zip>, 'hex': <built-in function hex>, 'long': <type 'long'>, 'next': <built-in function next>, 'ImportError': <type 'exceptions.ImportError'>, 'chr': <built-in function chr>, 'xrange': <type 'xrange'>, 'type': <type 'type'>, '__doc__': "Built-in functions, exceptions, and other objects.\n\nNoteworthy: None is the `nil' object; Ellipsis represents `...' in slices.", 'Exception': <type 'exceptions.Exception'>, 'tuple': <type 'tuple'>, 'UnicodeTranslateError': <type 'exceptions.UnicodeTranslateError'>, 'reversed': <type 'reversed'>, 'UnicodeEncodeError': <type 'exceptions.UnicodeEncodeError'>, 'IOError': <type 'exceptions.IOError'>, 'hasattr': <built-in function hasattr>, 'delattr': <built-in function delattr>, 'setattr': <built-in function setattr>, 'raw_input': <built-in function raw_input>, 'SyntaxWarning': <type 'exceptions.SyntaxWarning'>, 'compile': <built-in function compile>, 'ArithmeticError': <type 'exceptions.ArithmeticError'>, 'str': <type 'str'>, 'property': <type 'property'>, 'GeneratorExit': <type 'exceptions.GeneratorExit'>, 'int': <type 'int'>, '__import__': <built-in function __import__>, 'KeyError': <type 'exceptions.KeyError'>, 'coerce': <built-in function coerce>, 'PendingDeprecationWarning': <type 'exceptions.PendingDeprecationWarning'>, 'file': <type 'file'>, 'EnvironmentError': <type 'exceptions.EnvironmentError'>, 'unichr': <built-in function unichr>, 'id': <built-in function id>, 'OSError': <type 'exceptions.OSError'>, 'DeprecationWarning': <type 'exceptions.DeprecationWarning'>, 'min': <built-in function min>, 'UnicodeWarning': <type 'exceptions.UnicodeWarning'>, 'execfile': <built-in function execfile>, 'any': <built-in function any>, 'complex': <type 'complex'>, 'bool': <type 'bool'>, 'ValueError': <type 'exceptions.ValueError'>, 'NotImplemented': NotImplemented, 'map': <built-in function map>, 'buffer': <type 'buffer'>, 'max': <built-in function max>, 'object': <type 'object'>, 'TabError': <type 'exceptions.TabError'>, 'callable': <built-in function callable>, 'ZeroDivisionError': <type 'exceptions.ZeroDivisionError'>, 'eval': <built-in function eval>, '__debug__': True, 'IndentationError': <type 'exceptions.IndentationError'>, 'AssertionError': <type 'exceptions.AssertionError'>, 'classmethod': <type 'classmethod'>, 'UnboundLocalError': <type 'exceptions.UnboundLocalError'>, 'NotImplementedError': <type 'exceptions.NotImplementedError'>, 'AttributeError': <type 'exceptions.AttributeError'>, 'OverflowError': <type 'exceptions.OverflowError'>}, '__file__': 'sample.py', 'n': 20, 'i': 19, 'cube': <function cube at 0x103054aa0>, '__name__': 'sample', '__package__': None, '__doc__': 'A simple demonstration of Python'}}
>>> 
>>> 
>>> 
>>> dir(sample)
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattr__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'namespace']
>>> 
>>> sample.namespace.keys()
['squares', '__builtins__', '__file__', 'n', 'i', 'cube', '__name__', '__package__', '__doc__']
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
<class '__main__.Module'>
20
1331
>>> # __dict__      how the module instance works
>>> # namespace     where the user information is
>>> 
>>> # By default, the dot works on __dict__, the
>>> # instance dictionary
>>> 
>>> # We've intercepted the dot with
>>> # __getattr__ __setattr__ __delattr__
>>> # to use the namespace dict instead
>>> 
>>> sample.__dict__.keys()
['namespace']
>>> sample.namespace.keys()
['squares', '__builtins__', '__file__', 'n', 'i', 'cube', '__name__', '__package__', '__doc__']
>>> 
>>> 
>>> import sample
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
>>> dir(sample)
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cube', 'i', 'n', 'squares']
>>> 
>>> 
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
<class '__main__.Module'>
20
1331
>>> dir(sample)
['__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattr__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'namespace']
>>> # len(s)           --> s.__len__()
>>> # pow(a, b)        --> a.__pow__(b)
>>> # repr(a)          --> a.__repr__() -> default
>>> class A:
	pass

>>> A()
<__main__.A instance at 0x1027af8c0>
>>> repr(A())
'<__main__.A instance at 0x1027a97a0>'
>>> '<__main__.A instance at 0x1027a97a0>'
'<__main__.A instance at 0x1027a97a0>'
>>> 
>>> 
>>> # len(s)           --> s.__len__()
>>> # pow(a, b)        --> a.__pow__(b)
>>> # repr(a)          --> a.__repr__() -> default
>>> # dir(a)           --> a.__dir__()  -> sorted(a.__dict__)
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
<class '__main__.Module'>
20
1331
>>> # Tweet:  sorted(d) <-- sorted(d.keys())__dir__()
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
<class '__main__.Module'>
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cube', 'i', 'n', 'squares']
20
1331
>>> 
>>> 
>>> sample
<__main__.Module object at 0x104162dd0>
>>> import sample
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
>>> sample
<module 'sample' from '/Users/raymond/Dropbox/Public/sj151/sample.pyc'>
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
<class '__main__.Module'>
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cube', 'i', 'n', 'squares']
20
1331
>>> sample
<Module 'sample' from 'sample.py'>
>>> sample.xyz

Traceback (most recent call last):
  File "<pyshell#200>", line 1, in <module>
    sample.xyz
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 9, in __getattr__
    return self.namespace[attr]
KeyError: 'xyz'
>>> import sample
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
>>> sample.xyz

Traceback (most recent call last):
  File "<pyshell#202>", line 1, in <module>
    sample.xyz
AttributeError: 'module' object has no attribute 'xyz'
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
<class '__main__.Module'>
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cube', 'i', 'n', 'squares']
20
1331
>>> sample.xyz

Traceback (most recent call last):
  File "<pyshell#203>", line 1, in <module>
    sample.xyz
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 13, in __getattr__
    raise AttributeError(attr)
AttributeError: xyz
>>> import sample
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
>>> globals()['sample'].n
20
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
<class '__main__.Module'>
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cube', 'i', 'n', 'squares']
20
1331
>>> 
=============================== RESTART: Shell ===============================
>>> import sample
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
>>> import sample
>>> import sys
>>> type(sys.modules)
<type 'dict'>
>>> # modname -> module_object
>>> sys.modules.keys()
['heapq', 'code', 'tkFileDialog', 'functools', 'random', 'subprocess', 'sysconfig', 'idlelib.macosxSupport', 'idlelib.PyParse', 'tkSimpleDialog', 'encodings.encodings', 'idlelib.MultiStatusBar', 'idlelib.keybindingDialog', 'idlelib.__future__', 'idlelib.socket', 'idlelib.ReplaceDialog', 'idlelib.UndoDelegator', 'idlelib.tkSimpleDialog', 'idlelib.cPickle', 'imp', 'idlelib.SearchDialogBase', 'collections', 'idlelib.MultiCall', 'idlelib.ColorDelegator', 'zipimport', 'string', 'SocketServer', 'encodings.utf_8', 'idlelib.string', 'idlelib.SearchEngine', 'idlelib.bdb', 'idlelib.SocketServer', 'ConfigParser', 'idlelib.tkFileDialog', 'idlelib.webbrowser', 'idlelib.textwrap', 'idlelib.configSectionNameDialog', 'signal', 'idlelib.IOBinding', 'idlelib.configDialog', 'idlelib.pipes', 'threading', 'token', 'tkMessageBox', 'idlelib.warnings', 'shlex', 'gc', 'idlelib.struct', 'idlelib.help', 'cStringIO', 'google', 'locale', 'idlelib.Bindings', 'idlelib.threading', 'idlelib.TreeWidget', 'idlelib.rpc', 'idlelib.re', 'idlelib.SearchDialog', 'HTMLParser', 'idlelib.tkColorChooser', 'encodings', 'idlelib.RemoteDebugger', 'idlelib.tempfile', 'idlelib.Percolator', 'idlelib.codecs', 'abc', 'tkFont', '_tkinter', 'idlelib.tkFont', 'pipes', 'idlelib.textView', 're', 'idlelib.RemoteObjectBrowser', 'idlelib.platform', 'idlelib.imp', 'idlelib.locale', 'idlelib.thread', 'math', 'idlelib.fnmatch', 'fcntl', 'idlelib.Debugger', 'Tkinter', 'mpl_toolkits', 'idlelib.traceback', 'idlelib.marshal', 'UserDict', 'idlelib.copy', 'Queue', 'fnmatch', 'idlelib.StackViewer', 'codecs', 'idlelib.__builtin__', 'idlelib.copy_reg', 'paste', 'idlelib.GrepDialog', 'struct', '_functools', '_locale', 'idlelib.AutoComplete', 'socket', 'thread', 'idlelib.time', 'traceback', 'ndg', 'weakref', 'tempfile', 'itertools', 'ats', 'idlelib.CallTipWindow', 'os', 'marshal', '__future__', 'idlelib.AutoCompleteWindow', '_collections', 'idlelib.code', '_sre', 'idlelib.Delegator', '__builtin__', 'markupbase', 'idlelib.FileList', 'idlelib.signal', 'operator', 'idlelib.ObjectBrowser', 'select', 'idlelib.os', '_heapq', 'idlelib.ZoomHeight', 'idlelib.ConfigParser', 'posixpath', 'platform', 'errno', 'idlelib.getopt', '_socket', 'binascii', 'sre_constants', 'os.path', '_random', 'idlelib.WidgetRedirector', 'idlelib.PyShell', 'idlelib.tkMessageBox', '_warnings', 'cPickle', 'encodings.__builtin__', 'idlelib.IdleHistory', '_codecs', 'tokenize', '_osx_support', 'webbrowser', 'idlelib.repr', 'idlelib.idlelib', 'copy', 'idlelib.Queue', '_sysconfigdata', '_struct', 'idlelib.aboutDialog', 'hashlib', 'idlelib.configHelpSourceEdit', 'keyword', 'idlelib.keyword', 'repr', 'idlelib.__main__', 'idlelib.sys', 'posix', 'encodings.aliases', 'idlelib.HTMLParser', 'exceptions', 'sre_parse', 'pickle', 'copy_reg', 'sre_compile', '_hashlib', 'idlelib.io', 'site', 'sample', 'SimpleDialog', 'idlelib.dynOptionMenuWidget', 'io', '__main__', 'idlelib.OutputWindow', 'idlelib.types', 'idlelib.EditorWindow', 'tkCommonDialog', 'strop', 'linecache', 'idlelib.tokenize', 'encodings.codecs', '_abcoll', 'idlelib.HyperParser', 'getopt', 'idlelib.linecache', 'genericpath', 'stat', '_ssl', 'warnings', 'idlelib.tabbedpages', 'textwrap', 'sys', 'idlelib.Tkinter', 'idlelib.CallTips', 'idlelib.configHandler', 'idlelib.select', 'codeop', 'idlelib.SimpleDialog', 'tkColorChooser', 'types', 'idlelib.ScrolledList', '_weakref', 'bdb', 'idlelib', 'Tkconstants', '_io', '_weakrefset', 'time', 'idlelib.WindowList', 'idlelib.run']
>>> 
>>> 
>>> import sample
>>> import sys
>>> del sys.modules['sample']
>>> import sample
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
>>> del sys.modules['sample']
>>> import sample
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
>>> sys.modules['sample'].n
20
>>> sys.modules['sample'].cube(30)
27000
>>> sys.modules['sample'] == sample
True
>>> sys.modules['sample'] is sample
True
>>> 
>>> 
>>> del sys.modules['sample']
>>> import sample
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
>>> 
>>> reload(sample)
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
<module 'sample' from 'sample.pyc'>
>>> reload(sample)
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
<module 'sample' from 'sample.pyc'>
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
<class '__main__.Module'>
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cube', 'i', 'n', 'squares']
20
1331
>>> myimport('sample')
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
>>> myimport('sample')
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
>>> 
=============================== RESTART: Shell ===============================
>>> import sample
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
>>> import sample
>>> del sample
>>> sample.n

Traceback (most recent call last):
  File "<pyshell#236>", line 1, in <module>
    sample.n
NameError: name 'sample' is not defined
>>> import sample
>>> sample.n
20
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
<class '__main__.Module'>
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cube', 'i', 'n', 'squares']
20
1331
>>> 
>>> myimport('sample')
>>> myimport('sample')
>>> modules
{'sample': <Module 'sample' from 'sample.py'>}
>>> del modules['sample']
>>> myimport('sample')
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
<class '__main__.Module'>
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cube', 'i', 'n', 'squares']
20
1331
>>> reload(sample)

Traceback (most recent call last):
  File "<pyshell#245>", line 1, in <module>
    reload(sample)
TypeError: reload() argument must be module
>>> myreload(sample)
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
<Module 'sample' from 'sample.py'>
>>> myreload(sample)
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
<Module 'sample' from 'sample.py'>
>>> myreload(sample)
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
<Module 'sample' from 'sample.py'>
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> from sample import cube
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'cube']
>>> from sample import cube, n
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'cube', 'n']
>>> 
>>> 
>>> 
>>> def f(a, b, *args):
	print a
	print b
	print args

	
>>> f(10, 20, 30, 40, 50)
10
20
(30, 40, 50)
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
<class '__main__.Module'>
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cube', 'i', 'n', 'squares']
20
1331
>>> 
>>> 
>>> from_import('sample', 'n', 'cube')
>>> dir()
['Module', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cube', 'from_import', 'modules', 'myimport', 'myreload', 'n']
>>> n
20
>>> cube(11)
1331
>>> 
>>> 
>>> 
>>> from sample import n, cube
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
>>> 
=============================== RESTART: Shell ===============================
>>> 
>>> 


>>> 







>>> 





>>> 
>>> # from sample import n, cube
>>> import sample
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'sample']
>>> name = 'n'
>>> getattr(sample, name)
20
>>> globals()[name] = getattr(sample, name)
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'n', 'name', 'sample']
>>> name = 'cube'
>>> globals()[name] = getattr(sample, name)
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'cube', 'n', 'name', 'sample']
>>> del globals()['sample']
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'cube', 'n', 'name']
>>> 
=============================== RESTART: Shell ===============================
>>> from sample import n, cube
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'cube', 'n']
>>> 
>>> 
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> import sample
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'sample']
>>> type(sample)
<type 'module'>
>>> sample.n
20
>>> sample.cube(15)
3375
>>> 
=============================== RESTART: Shell ===============================
>>> from sample import n, cube
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'cube', 'n']
>>> import sys
>>> sys.modules['sample']
<module 'sample' from 'sample.pyc'>
>>> 
=============================== RESTART: Shell ===============================
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
<class '__main__.Module'>
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cube', 'i', 'n', 'squares']
20
1331
>>> 
>>> 
>>> # from sample import n, cube
>>> myimport('sample')                       # "sample" -> <Module 'sample'>
>>> sample
<Module 'sample' from 'sample.py'>
>>> type(sample)
<class '__main__.Module'>
>>> sample.n
20
>>> sample.cube(10)
1000
>>> 
>>> # from sample import n, cube
>>> myimport('sample')                       # "sample" -> <Module 'sample'>
>>> n = sample.n
>>> cube = sample.cube
>>> del sample
>>> 
>>> n
20
>>> cube
<function cube at 0x101f54d70>
>>> cube = sample.cube

Traceback (most recent call last):
  File "<pyshell#322>", line 1, in <module>
    cube = sample.cube
NameError: name 'sample' is not defined
>>> 
>>> 
>>> import sample
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
>>> cube = sample.cube
>>> name = 'n'
>>> sample.name

Traceback (most recent call last):
  File "<pyshell#328>", line 1, in <module>
    sample.name
AttributeError: 'module' object has no attribute 'name'
>>> getattr(sample, name)
20
>>> globals()[name] = getattr(sample, name)
>>> 
=============================== RESTART: Shell ===============================
>>> from sample import cube
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
>>> import sample
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'cube', 'sample']
>>> 
>>> 
>>> import math
>>> math.sin(3.0 * math.pi * math.sqrt(3.5)) + math.cos(3.0 * math.pi * math.sqrt(5.5))
-1.9319505249158762
>>> 
>>> from math import sin, pi, sqrt, cos
>>> sin(3.0 * pi * sqrt(3.5)) + cos(3.0 * pi * sqrt(5.5))
-1.9319505249158762
>>> 
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> d = {'n': 10}
>>> e = {}
>>> e.update(d)
>>> e
{'n': 10}
>>> 
>>> d
{'n': 10}
>>> e
{'n': 10}
>>> d['n'] = 11
>>> e
{'n': 10}
>>> 
>>> 
>>> 
>>> x = 10
>>> y = x
>>> x = 11
>>> y
10
>>> 
>>> 
>>> def f():
	x  = 10
	y = x + 1

	
>>> def g():
	x = 20
	y = x + 2

	
>>> g()
>>> def f():
	x  = 10
	y = x + 1
	return x, y

>>> def g():
	x = 20
	y = x + 2
	return x, y

>>> f()
(10, 11)
>>> g()
(20, 22)
>>> f()
(10, 11)
>>> 
>>> 
>>> 
>>> import math
>>> import sys
>>> sys.modules['math'] is math
True
>>> mypi = math.pi
>>> 
>>> math.pi
3.141592653589793
>>> sys.modules['math'].pi
3.141592653589793
>>> mypi
3.141592653589793
>>> 
>>> math.pi = 3.2
>>> math.pi
3.2
>>> sys.modules['math'].pi
3.2
>>> mypi
3.141592653589793
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> from math import pi
>>> import sys
>>> sys.modules['math'].pi = 3.2
>>> pi
3.141592653589793
>>> 
>>> x = 3.14159
>>> y = x
>>> x = 3.2
>>> y
3.14159
>>> import random
>>> random.randrange(100)
4
>>> myimport('random')

Traceback (most recent call last):
  File "<pyshell#408>", line 1, in <module>
    myimport('random')
NameError: name 'myimport' is not defined
>>> 
>>> 
>>> import sample
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
>>> sample.__file__
'sample.py'
>>> import random
>>> random.__file__
'/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/random.pyc'
>>> 
>>> 
>>> import sys
>>> sys.path
['', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7', '/Users/raymond/Dropbox/Public/sj151', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/readline-6.2.4.1-py2.7-macosx-10.7-intel.egg', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/ats_py2-1.0.4-py2.7.egg', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python27.zip', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-darwin', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac/lib-scriptpackages', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-old', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload', '/Users/raymond/Library/Python/2.7/lib/python/site-packages', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages', '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/PIL', '/Library/Python/2.7/site-packages', '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python', '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/PyObjC']
>>> from pprint import pprint
>>> import sys
>>> pprint(sys.path)
['',
 '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7',
 '/Users/raymond/Dropbox/Public/sj151',
 '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/readline-6.2.4.1-py2.7-macosx-10.7-intel.egg',
 '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/ats_py2-1.0.4-py2.7.egg',
 '/Library/Frameworks/Python.framework/Versions/2.7/lib/python27.zip',
 '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7',
 '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-darwin',
 '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac',
 '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/plat-mac/lib-scriptpackages',
 '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk',
 '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-old',
 '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload',
 '/Users/raymond/Library/Python/2.7/lib/python/site-packages',
 '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages',
 '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/site-packages/PIL',
 '/Library/Python/2.7/site-packages',
 '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python',
 '/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/PyObjC']
>>> dirname = '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7'
>>> type(dirname)
<type 'str'>
>>> # Don't think of this as a string!
>>> dirname.upper()
'/LIBRARY/FRAMEWORKS/PYTHON.FRAMEWORK/VERSIONS/2.7/LIB/PYTHON2.7'
>>> # Manipulate paths with different tools
>>> 
>>> import os
>>> dirname = '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7'
>>> filename = 'random.py'
>>> os.path.join(dirname, filename)
'/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/random.py'
>>> fullname = os.path.join(dirname, filename)
>>> fullname
'/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/random.py'
>>> os.basename(fullname)

Traceback (most recent call last):
  File "<pyshell#434>", line 1, in <module>
    os.basename(fullname)
AttributeError: 'module' object has no attribute 'basename'
>>> os.path.basename(fullname)
'random.py'
>>> os.path.dirname(fullname)
'/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7'
>>> os.path.split(fullname)
('/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7', 'random.py')
>>> os.path.splitext(fullname)
('/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/random', '.py')
>>> 
>>> open('tmpx.py')

Traceback (most recent call last):
  File "<pyshell#440>", line 1, in <module>
    open('tmpx.py')
IOError: [Errno 2] No such file or directory: 'tmpx.py'
>>> open('tmpx.py', 'w').close()
>>> os.remove('tmpx.py')
>>> os.remove('tmpx.py')

Traceback (most recent call last):
  File "<pyshell#443>", line 1, in <module>
    os.remove('tmpx.py')
OSError: [Errno 2] No such file or directory: 'tmpx.py'
>>> 
>>> 
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
<class '__main__.Module'>
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cube', 'i', 'n', 'squares']
20
1331

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 81, in <module>
    myimport('random')
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 42, in myimport
    with open(filename) as f:
IOError: [Errno 2] No such file or directory: 'random.py'
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
<class '__main__.Module'>
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cube', 'i', 'n', 'squares']
20
1331

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 81, in <module>
    myimport('random')
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 42, in myimport
    with open(filename) as f:
IOError: [Errno 2] No such file or directory: 'random.py'
>>> 
>>> 
>>> 
>>> 
>>> # if else
>>> # try else
>>> # for else
>>> # while else
>>> 
>>> 
>>> house = [None, None, 'keys', None]
>>> not_found = True
>>> for room in house:
	if room == 'keys':
		print 'Happy!'
		break

	
Happy!
>>> for room in house:
	if room == 'keys':
		print 'Happy!'
		found = True
		break

	
Happy!

>>> 


>>> 


>>> 












>>> 





>>> found = False
>>> house = [None, None, 'keys', None]
>>> for room in house:
	if room == 'keys':
		print 'Happy!'
		found = True
		break

	
Happy!
>>> if not found:
	print 'Sad!'

	
>>> house = [None] * 4
>>> found = False
>>> for room in house:
	if room == 'keys':
		print 'Happy!'
		found = True
		break

	
>>> if not found:
	print 'Sad!'

	
Sad!
>>> house = [None] * 4
>>> for room in house:
	if room == 'keys':
		print 'Happy!'
		break
else:                                # This runs when the loop finishes normally without a break
	print 'Sad!'

	
Sad!
>>> house = [None, None, 'keys', None]
>>> for room in house:
	if room == 'keys':
		print 'Happy!'
		break
else:                                # This runs when the loop finishes normally without a break
	print 'Sad!'

	
Happy!
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
<class '__main__.Module'>
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cube', 'i', 'n', 'squares']
20
1331
9
>>> dir()
['Module', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'from_import', 'modules', 'myimport', 'myreload', 'os', 'random', 'sample', 'sys']
>>> myimport('xyzpdq')

Traceback (most recent call last):
  File "<pyshell#492>", line 1, in <module>
    myimport('xyzpdq')
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 54, in myimport
    raise ImportError(modname)
ImportError: xyzpdq
>>> import family
>>> 
>>> 
>>> 
>>> s = [10, 20, 'hello']
>>> import marshal
>>> t = marshal.dumps(s)
>>> type(s)
<type 'list'>
>>> type(t)
<type 'str'>
>>> u = marshal.loads(t)
>>> u
[10, 20, 'hello']
>>> type(u)
<type 'list'>
>>> # magic (4 bytes) and matches a specific micro-release of python
>>> # timestamp (4 bytes) when the pyc was created.
>>> 
>>> # import sample    -> sample.pyc
>>> # import sample    -> sample.pyc
>>> 
>>> # If a pyc exists, we check that is magic number is the same as the current python
>>> # and that timestamp is newer than the .py file.
>>> 
>>> 
>>> import family
>>> dir(family)
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'show_family']
>>> family.show_family('hettingers', ['raymond', 'rachel', 'matthew'])
The Hettingers Family
=====================
* Raymond
* Rachel
* Matthew

>>> family.__file__
'/Users/raymond/Dropbox/Public/sj151/family.pyc'
>>> 
=============================== RESTART: Shell ===============================
>>> with open('family.pyc', 'rb') as f:
	pyc = f.read()

	
>>> type(pyc)
<type 'str'>
>>> import marshal
>>> code = marshal.loads(pyc[8:])
>>> code
<code object <module> at 0x1036081b0, file "family.py", line 1>
>>> exec code
The Starks Family
=================
* Eddard
* Catelyn
* Robb
* John Snow
* Arya
* Rickon
* Bram
* Sansa

>>> # exec string       compile the string    runs the compiles code
>>> # exec code
>>> 
>>> 
>>> 
>>> s = '''
"fun stuff"

n = 10

def welcome():
    print "hello"
'''
>>> code = compile(s, 'homegrown', 'exec')
>>> code
<code object <module> at 0x1035f8d30, file "homegrown", line 2>
>>> exec code
>>> n
10
>>> welcome()
hello
>>> __doc__
'fun stuff'
>>> 
>>> t = marshal.dumps(code)
>>> type(t)
<type 'str'>
>>> del code, s, n, welcome, __doc__
>>> type(t)
<type 'str'>
>>> 
>>> code = marshal.loads(t)
>>> exec code
>>> n
10
>>> welcome()
hello
>>> import family
>>> import family.pyc

Traceback (most recent call last):
  File "<pyshell#557>", line 1, in <module>
    import family.pyc
ImportError: No module named pyc
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
<class '__main__.Module'>
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cube', 'i', 'n', 'squares']
20
1331
677

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 97, in <module>
    myimport('family.pyc')
  File "/Users/raymond/Dropbox/Public/sj151/module_demo.py", line 54, in myimport
    raise ImportError(modname)
ImportError: family.pyc
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
<class '__main__.Module'>
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cube', 'i', 'n', 'squares']
20
1331
842
The Adams Family
================
* Lurch
* Morticia

None
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
<class '__main__.Module'>
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cube', 'i', 'n', 'squares']
20
1331
550
The Adams Family
================
* Lurch
* Morticia

>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/sj151/puzzle.py ===========
['']
[(0, 0, 8), (0, 5, 3), (3, 2, 3), (0, 2, 6), (2, 0, 6), (2, 5, 1), (3, 4, 1), (0, 4, 4)]
['', '7', '76', '765', '7654', '76543', '765432', '7654321', '76543210']
[
        0
      1   1
    1   1   1
  1   1   1   1
1   1   1   1   1
, 
        1
      0   1
    0   1   1
  1   1   1   1
1   1   1   1   1
, 
        1
      0   1
    1   0   0
  1   1   1   1
1   1   1   1   1
, 
        1
      1   1
    0   0   0
  0   1   1   1
1   1   1   1   1
, 
        0
      0   1
    1   0   0
  0   1   1   1
1   1   1   1   1
, 
        0
      0   1
    1   1   0
  0   0   1   1
1   0   1   1   1
, 
        0
      0   1
    1   1   0
  0   0   1   1
1   1   0   0   1
, 
        0
      0   1
    1   1   0
  0   0   1   1
0   0   1   0   1
, 
        0
      0   1
    1   1   1
  0   0   1   0
0   0   1   0   0
, 
        0
      0   0
    1   1   0
  0   0   1   1
0   0   1   0   0
, 
        0
      0   0
    1   1   1
  0   0   0   1
0   0   0   0   0
, 
        0
      0   1
    1   1   0
  0   0   0   0
0   0   0   0   0
, 
        0
      0   1
    0   0   1
  0   0   0   0
0   0   0   0   0
, 
        1
      0   0
    0   0   0
  0   0   0   0
0   0   0   0   0
]
[wwww...bbbb, wwww..b.bbb, www.w.b.bbb, www.wb..bbb, ww.wwb..bbb, ww.wwb.b.bb, ww.w.bwb.bb, ww.wb.wb.bb, ww..bwwb.bb, ww.b.wwb.bb, ww.b.w.bwbb, wwb..w.bwbb, w.bw.w.bwbb, w.bw.wb.wbb, .wbw.wb.wbb, bw.w.wb.wbb, b.ww.wb.wbb, b.wwbw..wbb, b.wwb.w.wbb, b.wwb.wbw.b, b.w.bwwbw.b, b.w.bwwbwb., b.w.bwwb.bw, b.wb.wwb.bw, b.wb.w.bwbw, bbw..w.bwbw, bbw...wbwbw, bbw..bw.wbw, bb.w.bw.wbw, bb.w.bwbw.w, bb..wbwbw.w, bb.bw.wbw.w, bb.bw.wb.ww, bbb.w.wb.ww, bbb.w..bwww, bbb.w.b.www, bbb..wb.www, bbb.bw..www, bbb.b.w.www, bbbb..w.www, bbbb...wwww]
[SCDM,, SD,MC, SDM,C, S,MDC, SCM,D, C,MDS, CM,DS, ,MDCS]
[
1122
1133
45..
6788
6799
, 
1122
1133
4.5.
6788
6799
, 
1122
1133
.45.
6788
6799
, 
1122
1133
.4.5
6788
6799
, 
1122
1133
..45
6788
6799
, 
..22
1133
1145
6788
6799
, 
.22.
1133
1145
6788
6799
, 
22..
1133
1145
6788
6799
, 
2233
11..
1145
6788
6799
, 
2233
114.
11.5
6788
6799
, 
2233
11.4
11.5
6788
6799
, 
2233
.114
.115
6788
6799
, 
2233
.114
6115
6788
.799
, 
2233
6114
6115
.788
.799
, 
2233
6114
6115
7.88
7.99
, 
2233
6114
6115
788.
7.99
, 
2233
6114
611.
7885
7.99
, 
2233
611.
6114
7885
7.99
, 
2233
611.
6114
7885
799.
, 
2233
611.
6114
788.
7995
, 
2233
611.
611.
7884
7995
, 
2233
6.11
6.11
7884
7995
, 
2233
.611
.611
7884
7995
, 
2233
.611
7611
7884
.995
, 
2233
7611
7611
.884
.995
, 
2233
7611
7611
88.4
.995
, 
2233
7611
7611
884.
.995
, 
2233
7611
7611
8845
.99.
, 
2233
7611
7611
8845
..99
, 
2233
7611
7611
..45
8899
, 
2233
7611
7611
.4.5
8899
, 
2233
7611
7611
4..5
8899
, 
2233
7611
7611
4.5.
8899
, 
2233
7611
7611
45..
8899
, 
2233
76..
7611
4511
8899
, 
22..
7633
7611
4511
8899
, 
.22.
7633
7611
4511
8899
, 
722.
7633
.611
4511
8899
, 
7.22
7633
.611
4511
8899
, 
7.22
7633
4611
.511
8899
, 
7.22
7633
4611
5.11
8899
, 
7.22
7.33
4611
5611
8899
, 
.722
.733
4611
5611
8899
, 
.722
4733
.611
5611
8899
, 
4722
.733
.611
5611
8899
, 
4722
.733
5611
.611
8899
, 
4722
5733
.611
.611
8899
, 
4722
5733
6.11
6.11
8899
, 
4.22
5733
6711
6.11
8899
, 
.422
5733
6711
6.11
8899
, 
5422
.733
6711
6.11
8899
, 
5422
..33
6711
6711
8899
, 
5422
.33.
6711
6711
8899
, 
5422
33..
6711
6711
8899
, 
54..
3322
6711
6711
8899
, 
5.4.
3322
6711
6711
8899
, 
.54.
3322
6711
6711
8899
, 
.5.4
3322
6711
6711
8899
, 
..54
3322
6711
6711
8899
, 
3354
..22
6711
6711
8899
, 
3354
6.22
6711
.711
8899
, 
3354
622.
6711
.711
8899
, 
335.
6224
6711
.711
8899
, 
33.5
6224
6711
.711
8899
, 
.335
6224
6711
.711
8899
, 
6335
6224
.711
.711
8899
, 
6335
6224
7.11
7.11
8899
, 
6335
6224
711.
711.
8899
, 
6335
622.
7114
711.
8899
, 
633.
6225
7114
711.
8899
, 
6.33
6225
7114
711.
8899
, 
6.33
6225
711.
7114
8899
, 
6.33
622.
7115
7114
8899
, 
6.33
6.22
7115
7114
8899
, 
.633
.622
7115
7114
8899
, 
.633
7622
7115
.114
8899
, 
7633
7622
.115
.114
8899
, 
7633
7622
11.5
11.4
8899
, 
7633
7622
115.
11.4
8899
, 
7633
7622
1154
11..
8899
, 
7633
7622
1154
1199
88..
, 
7633
7622
1154
1199
.88.
, 
7633
7622
1154
1199
..88
, 
7633
7622
..54
1199
1188
]
>>> 
>>> 
>>> import http://users.rcn.com/python/download/puzzle.py
SyntaxError: invalid syntax
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/sj151/module_demo.py ========
The sum of squares is 2470
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]
<class '__main__.Module'>
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cube', 'i', 'n', 'squares']
20
1331
29
The Adams Family
================
* Lurch
* Morticia

['']
[(0, 0, 8), (0, 5, 3), (3, 2, 3), (0, 2, 6), (2, 0, 6), (2, 5, 1), (3, 4, 1), (0, 4, 4)]
['', '7', '76', '765', '7654', '76543', '765432', '7654321', '76543210']
[
        0
      1   1
    1   1   1
  1   1   1   1
1   1   1   1   1
, 
        1
      0   1
    0   1   1
  1   1   1   1
1   1   1   1   1
, 
        1
      0   1
    1   0   0
  1   1   1   1
1   1   1   1   1
, 
        1
      1   1
    0   0   0
  0   1   1   1
1   1   1   1   1
, 
        0
      0   1
    1   0   0
  0   1   1   1
1   1   1   1   1
, 
        0
      0   1
    1   1   0
  0   0   1   1
1   0   1   1   1
, 
        0
      0   1
    1   1   0
  0   0   1   1
1   1   0   0   1
, 
        0
      0   1
    1   1   0
  0   0   1   1
0   0   1   0   1
, 
        0
      0   1
    1   1   1
  0   0   1   0
0   0   1   0   0
, 
        0
      0   0
    1   1   0
  0   0   1   1
0   0   1   0   0
, 
        0
      0   0
    1   1   1
  0   0   0   1
0   0   0   0   0
, 
        0
      0   1
    1   1   0
  0   0   0   0
0   0   0   0   0
, 
        0
      0   1
    0   0   1
  0   0   0   0
0   0   0   0   0
, 
        1
      0   0
    0   0   0
  0   0   0   0
0   0   0   0   0
]
[wwww...bbbb, wwww..b.bbb, www.w.b.bbb, www.wb..bbb, ww.wwb..bbb, ww.wwb.b.bb, ww.w.bwb.bb, ww.wb.wb.bb, ww..bwwb.bb, ww.b.wwb.bb, ww.b.w.bwbb, wwb..w.bwbb, w.bw.w.bwbb, w.bw.wb.wbb, .wbw.wb.wbb, bw.w.wb.wbb, b.ww.wb.wbb, b.wwbw..wbb, b.wwb.w.wbb, b.wwb.wbw.b, b.w.bwwbw.b, b.w.bwwbwb., b.w.bwwb.bw, b.wb.wwb.bw, b.wb.w.bwbw, bbw..w.bwbw, bbw...wbwbw, bbw..bw.wbw, bb.w.bw.wbw, bb.w.bwbw.w, bb..wbwbw.w, bb.bw.wbw.w, bb.bw.wb.ww, bbb.w.wb.ww, bbb.w..bwww, bbb.w.b.www, bbb..wb.www, bbb.bw..www, bbb.b.w.www, bbbb..w.www, bbbb...wwww]
[SCDM,, SD,MC, SDM,C, S,MDC, SCM,D, C,MDS, CM,DS, ,MDCS]
[
1122
1133
45..
6788
6799
, 
1122
1133
4.5.
6788
6799
, 
1122
1133
.45.
6788
6799
, 
1122
1133
.4.5
6788
6799
, 
1122
1133
..45
6788
6799
, 
..22
1133
1145
6788
6799
, 
.22.
1133
1145
6788
6799
, 
22..
1133
1145
6788
6799
, 
2233
11..
1145
6788
6799
, 
2233
114.
11.5
6788
6799
, 
2233
11.4
11.5
6788
6799
, 
2233
.114
.115
6788
6799
, 
2233
.114
6115
6788
.799
, 
2233
6114
6115
.788
.799
, 
2233
6114
6115
7.88
7.99
, 
2233
6114
6115
788.
7.99
, 
2233
6114
611.
7885
7.99
, 
2233
611.
6114
7885
7.99
, 
2233
611.
6114
7885
799.
, 
2233
611.
6114
788.
7995
, 
2233
611.
611.
7884
7995
, 
2233
6.11
6.11
7884
7995
, 
2233
.611
.611
7884
7995
, 
2233
.611
7611
7884
.995
, 
2233
7611
7611
.884
.995
, 
2233
7611
7611
88.4
.995
, 
2233
7611
7611
884.
.995
, 
2233
7611
7611
8845
.99.
, 
2233
7611
7611
8845
..99
, 
2233
7611
7611
..45
8899
, 
2233
7611
7611
.4.5
8899
, 
2233
7611
7611
4..5
8899
, 
2233
7611
7611
4.5.
8899
, 
2233
7611
7611
45..
8899
, 
2233
76..
7611
4511
8899
, 
22..
7633
7611
4511
8899
, 
.22.
7633
7611
4511
8899
, 
722.
7633
.611
4511
8899
, 
7.22
7633
.611
4511
8899
, 
7.22
7633
4611
.511
8899
, 
7.22
7633
4611
5.11
8899
, 
7.22
7.33
4611
5611
8899
, 
.722
.733
4611
5611
8899
, 
.722
4733
.611
5611
8899
, 
4722
.733
.611
5611
8899
, 
4722
.733
5611
.611
8899
, 
4722
5733
.611
.611
8899
, 
4722
5733
6.11
6.11
8899
, 
4.22
5733
6711
6.11
8899
, 
.422
5733
6711
6.11
8899
, 
5422
.733
6711
6.11
8899
, 
5422
..33
6711
6711
8899
, 
5422
.33.
6711
6711
8899
, 
5422
33..
6711
6711
8899
, 
54..
3322
6711
6711
8899
, 
5.4.
3322
6711
6711
8899
, 
.54.
3322
6711
6711
8899
, 
.5.4
3322
6711
6711
8899
, 
..54
3322
6711
6711
8899
, 
3354
..22
6711
6711
8899
, 
3354
6.22
6711
.711
8899
, 
3354
622.
6711
.711
8899
, 
335.
6224
6711
.711
8899
, 
33.5
6224
6711
.711
8899
, 
.335
6224
6711
.711
8899
, 
6335
6224
.711
.711
8899
, 
6335
6224
7.11
7.11
8899
, 
6335
6224
711.
711.
8899
, 
6335
622.
7114
711.
8899
, 
633.
6225
7114
711.
8899
, 
6.33
6225
7114
711.
8899
, 
6.33
6225
711.
7114
8899
, 
6.33
622.
7115
7114
8899
, 
6.33
6.22
7115
7114
8899
, 
.633
.622
7115
7114
8899
, 
.633
7622
7115
.114
8899
, 
7633
7622
.115
.114
8899
, 
7633
7622
11.5
11.4
8899
, 
7633
7622
115.
11.4
8899
, 
7633
7622
1154
11..
8899
, 
7633
7622
1154
1199
88..
, 
7633
7622
1154
1199
.88.
, 
7633
7622
1154
1199
..88
, 
7633
7622
..54
1199
1188
]
>>> 
>>> 
>>> 
>>> def twopow(exp):
	return 2 ** exp

>>> def threepow(exp):
	return 3 ** exp

>>> pow_template = '''\
def {name}pow(exp):
	return {base} ** exp
'''
>>> exec pow_template.format(name='four', base=4)
>>> four_pow(5)

Traceback (most recent call last):
  File "<pyshell#574>", line 1, in <module>
    four_pow(5)
NameError: name 'four_pow' is not defined
>>> print pow_template.format(name='four', base=4)
def fourpow(exp):
	return 4 ** exp

>>> fourpow(5)
1024
>>> 
>>> 
>>> def twopow(exp):
	return 2 ** exp

>>> def threepow(exp):
	return 3 ** exp

>>> pow_template = '''\
def {name}pow(exp):
	return {base} ** exp
'''
>>> 
>>> 
>>> # When do you use format() and when you use %-formatting
>>> 
>>> # If %-formatting is clearer, I use it.
>>> # When you need custom format codes, only new-style will work
>>> # When doing metaprogramming, you often have templates that contain pure python code
>>> # which might also need formatting.   If one style for the template and the other for
>>> # it contents
>>> 
>>> 
>>> def happy_family(name):
	print 'The %s family is really happy' % name

	
>>> def sad_family(name):
	print 'The %s family is really sad' % name

	
>>> template = '''\
def {mood}{_family(name):
	print 'The %s family is really {mood}' % name
'''
>>> print template.format(mood='hungry')

Traceback (most recent call last):
  File "<pyshell#603>", line 1, in <module>
    print template.format(mood='hungry')
ValueError: unmatched '{' in format
>>> template = '''\
def {mood}_family(name):
	print 'The %s family is really {mood}' % name
'''
>>> 
>>> 
>>> 
>>> 
>>> template = '''\
def {mood}_family(name):
	print 'The %s family is really {mood}' % name
'''
>>> print template.format(mood='hungry')
def hungry_family(name):
	print 'The %s family is really hungry' % name

>>> template = '''\
def %(mood)s_family(name):
	print 'The %%s family is really %(mood)s}' %% name
'''
>>> template = '''\
def %(mood)s_family(name):
	print 'The %%s family is really %(mood)s' %% name
'''
>>> 
>>> print template % dict(mood='thirsty')
def thirsty_family(name):
	print 'The %s family is really thirsty' % name

>>> 
>>> type(template)
<type 'str'>
>>> dir(template)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
>>> 
>>> 
>>> 
>>> # New-style formatting does much better than old-style:
>>> # Custom format codes for each object
>>> 
>>> import datetime
>>> t = datetime.datetime.now()
>>> t
datetime.datetime(2016, 10, 19, 15, 39, 53, 49480)
>>> 
>>> format(t)
'2016-10-19 15:39:53.049480'
>>> format(t, '!r')
'!r'
>>> print '{0}'.format(t)
2016-10-19 15:39:53.049480
>>> print '{0!r}'.format(t)
datetime.datetime(2016, 10, 19, 15, 39, 53, 49480)
>>> print 'Today is {0:%A}'.format(t)
Today is Wednesday
>>> print 'Today is {0:%A} in {0:%M %Y}'.format(t)
Today is Wednesday in 39 2016
>>> print 'Today is {0:%A} in {0:%B %Y}'.format(t)
Today is Wednesday in October 2016
>>> print 'Today is a {0:%A} in {0:%B %Y}'.format(t)
Today is a Wednesday in October 2016
>>> 
>>> 
>>> 
>>> s = 'the tale of two cities'
>>> i = s.find('two')
>>> i
12
>>> s[i]
't'
>>> s[s.find('two')]
't'
>>> s[s.find('of')]
'o'
>>> s[s.find('w')]
'w'
>>> s[s.find('z')]
's'
>>> s.find('z')
-1
>>> s[-1]
's'
>>> s[s.index('two')]
't'
>>> s[s.index('of')]
'o'
>>> s[s.index('w')]
'w'
>>> s[s.index('z')]

Traceback (most recent call last):
  File "<pyshell#653>", line 1, in <module>
    s[s.index('z')]
ValueError: substring not found
>>> 
>>> 
>>> 
>>> class A(object):
	def __new__(cls, x, y):
		if x < 0 or y < 0:
			return -1
		return object.__new__(cls)
	def __init__(self, x, y):
		self.z = x * y

		
>>> a = A(10, 20)
>>> a
<__main__.A object at 0x104ac25d0>
>>> a.z
200
>>> a.__dict__
{'z': 200}
>>> a = A(-10, 20)
>>> a
-1
>>> class A(object):
	def __new__(cls, x, y):
		if x < 0 or y < 0:
			return -1
		return object.__new__(cls)
	def __init__(self, x, y):
		self.z = x * y
	def __add__(self, other):
		return str(self.z) + '~' + str(other)

	
>>> A(10, 20) + 3
'200~3'
>>> A(10, -20) + 3
2
>>> class A(object):
	def __new__(cls, x, y):
		if x < 0 or y < 0:
			raise ValueError('negative inputs not supported: %r %r' % (x, y))
		return object.__new__(cls)
	def __init__(self, x, y):
		self.z = x * y
	def __add__(self, other):
		return str(self.z) + '~' + str(other)

	
>>> A(10, 20)
<__main__.A object at 0x104ac2e90>
>>> A(10, 20) + 3
'200~3'
>>> A(10, -20) + 3

Traceback (most recent call last):
  File "<pyshell#682>", line 1, in <module>
    A(10, -20) + 3
  File "<pyshell#679>", line 4, in __new__
    raise ValueError('negative inputs not supported: %r %r' % (x, y))
ValueError: negative inputs not supported: 10 -20
>>> try:
	print A(10, -20) + 3
except ValueError:
	print 'Oops, I did again.  I played with your heart'

	
Oops, I did again.  I played with your heart
>>> 
>>> # "Exceptions are for the exceptional" <-- Partly for speed, partly a cultural norm.
>>> 
>>> 
>>> # Google:    Enormous code base with enormous dependencies -> rebuld times are huge!
>>> # Google:    Many, manys users for every programmer -> programmers are cheap
>>> #                                                   -> hardware
>>> 
>>> # Go Lang:   Designed for very fast compilation, want programmers to write if test
>>> #            for every possible condition.  Paid in programmer time.
>>> 
>>> 
>>> # value, err = somefunc(data)
>>> # if err == 0: solution0
>>> # if err == 1: solution1
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj151/custom_formatting.py =====
IPAddr(171, 0, 1, 15)
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj151/custom_formatting.py =====
stir it up
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj151/custom_formatting.py =====
stir it up
IPAddr(171, 0, 1, 15)
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj151/custom_formatting.py =====
stir it up
IPAddr(171, 0, 1, 15)
stir it up
>>> octets

Traceback (most recent call last):
  File "<pyshell#703>", line 1, in <module>
    octets
NameError: name 'octets' is not defined
>>> octets = (171, 0, 1, 15)
>>> map(str, octets)
['171', '0', '1', '15']
>>> '.'.join(map(str, octets))
'171.0.1.15'
>>> 
>>> format(57, '02x')
'39'
>>> format(11, '02x')
'0b'
>>> format(12, '02x')
'0c'
>>> [format(octet, '02x') for octet in octets]
['ab', '00', '01', '0f']
>>> ':'.join([format(octet, '02x') for octet in octets])
'ab:00:01:0f'
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj151/custom_formatting.py =====
stir it up
IPAddr(171, 0, 1, 15)
171.0.1.15
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj151/custom_formatting.py =====
stir it up
IPAddr(171, 0, 1, 15)
171.0.1.15
ab:00:01:0f
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj151/custom_formatting.py =====
stir it up
IPAddr(171, 0, 1, 15)
171.0.1.15
ab:00:01:0f
The object IPAddr(171, 0, 1, 15) is usually shown as 171.0.1.15 but sometimes as ab:00:01:0f
but some folks just like to stir it up.
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj151/custom_formatting.py =====
stir it up
IPAddr(171, 0, 1, 15)
171.0.1.15
ab:00:01:0f
The object IPAddr(171, 0, 1, 15) is usually shown as 171.0.1.15 but sometimes as ab:00:01:0f
but some folks just like to stir it up.
Today is Wednesday in century 20
>>> 
===== RESTART: /Users/raymond/Dropbox/Public/sj151/custom_formatting.py =====
stir it up
IPAddr(171, 0, 1, 15)
171.0.1.15
ab:00:01:0f
The object IPAddr(171, 0, 1, 15) is usually shown as 171.0.1.15 but sometimes as ab:00:01:0f
but some folks just like to stir it up.
Today is Wednesday in century 20
The answer is 1,234,567,890 today
>>> 
>>> # One-at-a-time  ----  Threading  ----  Async (1thread/1process/nonblocking) --- Forking
>>> # Really good    ----   Apache    ----  Twisted /
>>> 


>>> 


>>> # One-at-a-time  ----  Threading  ----  Async (1thread/1process/nonblocking) --- Forking
>>> # Really good    ----   Apache    ----  Twisted / Tornado / Diesel / asyncio --- Gunicorn
>>> 
>>> 
>>> from time import time
>>> pow(2, 5)                        # Arity of two
32
>>> ord('A')                         # Arity of one
65
>>> time()
1476921593.974061
>>> 
>>> def twopow(exp):
	return pow(2, exp)

>>> twopow(5)
32
>>> from functools import partial
>>> twopow = partial(pow, 2)
>>> twopow(5)
32
>>> thirtytwo = partial(pow, 2, 5)
>>> thirtytwo()
32
>>> from functools import partial
>>> from random import *
>>> 
>>> randrange(1, 7)
5
>>> roll = partial(randrange(1, 7))

Traceback (most recent call last):
  File "<pyshell#740>", line 1, in <module>
    roll = partial(randrange(1, 7))
TypeError: the first argument must be callable
>>> roll = partial(randrange, 1, 7)
>>> 
>>> 
>>> from functools import partial
>>> from random import *
>>> roll = partial(randrange, 1, 7)
>>> roll()
2
>>> roll()
2
>>> roll()
4
>>> roll()
5
>>> f = open('notes3/hamlet.txt')
>>> f.read(10)
'The Traged'
>>> f.read(10)
'y of Hamle'
>>> 
>>> f = open('notes3/hamlet.txt')
>>> br = partial(f.read, 10)
>>> br()
'The Traged'
>>> br()
'y of Hamle'
>>> br()
't, Prince '
>>> br()
'of Denmark'
>>> 
>>> callbacks = [roll, br, roll, rool, thirtytwo, roll]

Traceback (most recent call last):
  File "<pyshell#762>", line 1, in <module>
    callbacks = [roll, br, roll, rool, thirtytwo, roll]
NameError: name 'rool' is not defined
>>> callbacks = [roll, br, roll, roll, thirtytwo, roll]
>>> for callback in callbacks:
	callback()

	
4
'\r\nShakespe'
3
3
32
6
>>> 
>>> 
>>> s = [10, 50, 6, 80, 70, 23, 18]
>>> s.sort()                           # n log n -> n
>>> s.pop(0)                           # n
6
>>> n = _ * 5 - 1
>>> s.append(n)                        # 1
>>> s.sort()                           # O(n)
>>> n = s.pop(0); n                    # n
10
>>> n = _ * 3 + 18
>>> s.append(n)                        # 1
>>> s.sort()                           # O(n)
>>> n = s.pop(0); n                    # n
18
>>> # List of numbers
>>> # Want the smallest number
>>> # Periodically, I add new numbers
>>> 
>>> # ^--- Slowest way to implement this:   s.append(n); s.sort()            n = s.pop(0)
>>> from heapq import *
>>> s = [10, 50, 6, 80, 70, 23, 18]
>>> heapify(s)                         # O(n) -- we only do this once!
>>> n = heappop(s)                     # O(log n)
>>> n = _ * 5 - 1
>>> heappush(s, n)                     # O(log n)
>>> n = heappop(s)                     # O(log n)
>>> n = _ * 3 + 18
>>> heappush(s, n)                     # O(log n)
>>> # ^-- By using heapify, heappush, heappop we move from O(n) per step to O(log n)
>>> #                                                     1000                 10
>>> 
>>> 
>>> 
>>> # Lexicographic sort order
>>> from pprint import pprint
>>> pprint(sorted([
	'raymond',
	'rachel',
	'matthew',
]), width=20)
['matthew',
 'rachel',
 'raymond']
>>> pprint(sorted([
	(70, 1, 2),
	(5, 99, 250),
	(70, 0, 999),
]), width=20)
[(5, 99, 250),
 (70, 0, 999),
 (70, 1, 2)]
>>> pprint(sorted([
	(50, 'teach python'),
	(0, 'wake up'),
	(80, 'go to sleep'),
	(30, 'feed son breakfast'),
	(50, 'go home'),
]), width=50)
[(0, 'wake up'),
 (30, 'feed son breakfast'),
 (50, 'go home'),
 (50, 'teach python'),
 (80, 'go to sleep')]
>>> offset = 12323452345
>>> pprint(sorted([
	(offset+50, 'teach python'),
	(offset+0, 'wake up'),
	(offset+80, 'go to sleep'),
	(offset+30, 'feed son breakfast'),
	(offset+50, 'go home'),
]), width=60)
[(12323452345, 'wake up'),
 (12323452375, 'feed son breakfast'),
 (12323452395, 'go home'),
 (12323452395, 'teach python'),
 (12323452425, 'go to sleep')]
>>> pprint(sorted([
	(offset+50, 'teach python'),
	(offset+0, 'wake up'),
	(offset+80, 'go to sleep'),
	(offset+30, 'feed son breakfast'),
	(offset+60, 'go home'),
]), width=60)
[(12323452345, 'wake up'),
 (12323452375, 'feed son breakfast'),
 (12323452395, 'teach python'),
 (12323452405, 'go home'),
 (12323452425, 'go to sleep')]
>>> import time
>>> time.time()
1476923069.526683
>>> pprint(sorted([
	(time.time()+50, 'teach python'),
	(time.time()+0, 'wake up'),
	(time.time()+80, 'go to sleep'),
	(time.time()+30, 'feed son breakfast'),
	(time.time()+60, 'go home'),
]), width=70)
[(1476923103.127976, 'wake up'),
 (1476923133.127977, 'feed son breakfast'),
 (1476923153.127975, 'teach python'),
 (1476923163.127978, 'go home'),
 (1476923183.127977, 'go to sleep')]
>>> tasks = sorted([
	(time.time()+50, 'teach python'),
	(time.time()+0, 'wake up'),
	(time.time()+80, 'go to sleep'),
	(time.time()+30, 'feed son breakfast'),
	(time.time()+60, 'go home'),
])
>>> 
>>> tasks.pop(0)
(1476923152.990651, 'wake up')
>>> tasks.append((time.time()+1, 'call dad'))
>>> tasks.sort()
>>> tasks.pop(0)
(1476923182.990653, 'feed son breakfast')
>>> 
>>> 
>>> heapify(tasks)
>>> heappop(tasks)
(1476923184.38926, 'call dad')
>>> heappush(tasks, (time.time()+1, 'call mom'))
>>> heappop(tasks)
(1476923202.990648, 'teach python')
>>> heappop(tasks)
(1476923212.990654, 'go home')
>>> heappop(tasks)
(1476923232.990651, 'go to sleep')
>>> heappop(tasks)
(1476923276.652462, 'call mom')
>>> heappop(tasks)

Traceback (most recent call last):
  File "<pyshell#829>", line 1, in <module>
    heappop(tasks)
IndexError: index out of range
>>> 
>>> 
>>> # The primary use for heaps is a priority queue
>>> 
>>> from collections import namedtuple
>>> 
>>> Food = namedtuple('Food', ['name', 'availability', 'calories'])
>>> 
>>> foods = [
	Food('snickers', 'vending machine', 315),
	Food('steak', 'outback', 800),
	Food('trix', 'breakfast', 250),
]
>>> pprint(foods)
[Food(name='snickers', availability='vending machine', calories=315),
 Food(name='steak', availability='outback', calories=800),
 Food(name='trix', availability='breakfast', calories=250)]
>>> 
>>> sum(food.calories for food in foods)
1365
>>> pprint(sorted(foods))
[Food(name='snickers', availability='vending machine', calories=315),
 Food(name='steak', availability='outback', calories=800),
 Food(name='trix', availability='breakfast', calories=250)]
>>> pprint(sorted(foods, key=lambda food: food.calories))
[Food(name='trix', availability='breakfast', calories=250),
 Food(name='snickers', availability='vending machine', calories=315),
 Food(name='steak', availability='outback', calories=800)]
>>> 
>>> import time
>>> x = 20; print x**2
400
>>> 
>>> time.time()
1476923660.827095
>>> time.ctime()
'Wed Oct 19 17:34:24 2016'
>>> time.sleep(5); print 'Done!'
Done!
>>> type(food)

Traceback (most recent call last):
  File "<pyshell#855>", line 1, in <module>
    type(food)
NameError: name 'food' is not defined
>>> type(foods)
<type 'list'>
>>> type(foods[0])
<class '__main__.Food'>
>>> # A named tuple is a factory function for creating new tuple subclasses with named fields
>>> Food = namedtuple('Food', ['name', 'availability', 'calories'])
>>> issubclass(Food, tuple)
True
>>> f = Food(name='trix', availability='breakfast', calories=250)
>>> isinstance(f, Food)
True
>>> isinstance(f, tuple)
True
>>> len(f)
3
>>> f[:2]
('trix', 'breakfast')
>>> f[0]
'trix'
>>> a, b, c = f
>>> f.calories
250
>>> f[2]
250
>>> f
Food(name='trix', availability='breakfast', calories=250)
>>> 
>>> 
>>> 
