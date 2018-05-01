# Emulate "import sample"

import codegen
import json
import marshal
import os
import sys
import urllib

modules = {} # Emulates sys.modules

class Module(dict):

    def __init__(self, namespace):
        object.__setattr__(self, 'namespace', namespace)

    def __getattr__(self, attr):
        return self.namespace[attr]

    def __setattr__(self, attr, value):
        self.namespace[attr] = value

    def __delattr__(self, attr):
        del self.namespace[attr]

    def __dir__(self):
        return sorted(self.namespace)

    def __repr__(self):
        return '<Module %r from %r>' % (self.__name__, self.__file__)

def from_import(modname, *names):
    myimport(modname)
    module = modules[modname]
    for name in names:
        value = getattr(module, name)
        globals()[name] = value
    del globals()[modname]

def myimport(modname):
    'Emulate and extend logic for "import <module>"'

    # Load previously imported modules from the cache
    if modname in modules:
        globals()[modname] = modules[modname]
        return

    if modname.endswith('.pyc'):
        fullname = modname
        modname = fullname[:-4]
        with open(fullname, 'rb') as f:
            magic, timestamp, code = f.read(4), f.read(4), marshal.load(f)
    elif modname.endswith('.json'):
        # Load a JSON file and autogenerate code
        fullname = modname
        modname = os.path.splitext(os.path.basename(modname))
        with open(fullname) as f:
            record_layout = json.load(f)
        code = ''.join(codegen.generate_parser(record_layout))
    elif modname.startswith('http://'):
        # Load a py file from the Internet
        fullname = modname
        modname = '__main__'
        u = urllib.urlopen(fullname)
        code = u.read()
        u.close()
    else:
        # Load from py in the current directory
        filename = modname + '.py'
        for dirname in sys.path:
            fullname = os.path.join(dirname, filename)
            try:
                with open(fullname, 'rb') as f:
                    code = f.read()
                break
            except IOError:
                pass
        else:
            raise ImportError(modname)

    # Exec the code in a namespace
    namespace = {}
    namespace['__name__'] = modname
    namespace['__file__'] = fullname
    namespace['__package__'] = None
    exec code in namespace

    module = Module(namespace)
    globals()[modname] = module
    modules[modname] = module

def myreload(module):
    modname = module.__name__
    modules.pop(modname, None)
    myimport(modname)
    return modules[modname]

if __name__ == '__main__':
    # Import sample.py from the current directory
    myimport('sample')

    print '--------------'
    print type(sample)
    print dir(sample)
    print sample.n
    print sample.cube(11)
    print '--------------'

    # reload sample.py from the current directory
    myreload(sample)
    from_import('sample', 'n', 'cube')

    # Import random.py from the current directory
    myimport('random')
    print random.randrange(100)

    # Import family.pyc from the current directory
    myimport('family.pyc')
    print type(family)

    # Import directly from the Internet
    myimport('http://users.rcn.com/python/download/puzzle.py')

    # Import directly from a JSON file and autogenerate the code
    myimport('notes/parser.json')
