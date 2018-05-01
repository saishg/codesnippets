# Emulate "import sample"

import os
import sys

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

    # Load from py in the current directory
    filename = modname + '.py'
    for dirname in sys.path:
        fullname = os.path.join(dirname, filename)
        try:
            with open(fullname) as f:
                code = f.read()
            break
        except IOError:
            pass
    else:
        raise ImportError(modname)

    # Exec the code in a namespace
    namespace = {}
    namespace['__name__'] = modname
    namespace['__file__'] = filename
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

    myreload(sample)
    from_import('sample', 'n', 'cube')

    myimport('random')
    print random.randrange(100)
