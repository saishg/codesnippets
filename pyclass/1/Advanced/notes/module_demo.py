'Learn exactly how "import" works and how to customize it'

import marshal
import os
import sys
import urllib

modules = {} # Emulates the sys.modules dictionary which map modname to a module

class Module(object):
    'Emulate the real module objects created by "import"'
    
    def __init__(self, namespace):
        object.__setattr__(self, 'namespace', namespace)

    def __getattr__(self, attr):
        try:
            return self.namespace[attr]
        except KeyError:
            raise AttributeError(attr)

    def __setattr__(self, attr, value):
        self.namespace[attr] = value    

    def __delattr__(self, attr):
        try:
            del self.namespace[attr]
        except KeyError:
            raise AttributeError(attr)

    def __dir__(self):
        return sorted(self.namespace)

    def __repr__(self):
        return '<Module %r from %r>' % (self.__name__, self.__file__)
    
def myimport(modname):
    'Emulate and extend the logic for "import sample"'

    # Load previously imported modules from the cache
    if modname in modules:
        globals()[modname] = modules[modname]
        return

    if modname.endswith('.pyc'):
        # Load from a pyc in the current directory
        fullname = modname
        modname = fullname[:-4]
        with open(fullname, 'rb') as f:
            magic, timestamp, code = f.read(4), f.read(4), marshal.load(f)
    elif modname.startswith('http://'):
        # Load a py file from the internet
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
    namespace['__file__'] = fullname
    namespace['__package__'] = None
    exec code in namespace

    # Wrap the namespace in a module object, storing it in globals and the cache
    module = Module(namespace)
    globals()[modname] = module
    modules[modname] = module

def from_import(modname, *names):
    myimport(modname)
    module = modules[modname]
    for name in names:
        value = getattr(module, name)
        globals()[name] = value
    del globals()[modname]

def myreload(module):
    'Excise the module from the cache and reload from scratch'
    modname = module.__name__
    modules.pop(modname, None)
    myimport(modname)
    return modules[modname]

if __name__ == '__main__':

    # Import sample.py from the current directory
    myimport('sample')
    print type(sample)
    print dir(sample)
    print sample.n
    print sample.cube(11)

    # Import random.py from the standard library
    myimport('random')
    print random.randrange(1000)

    # Import family.pyc from the current directory
    myimport('family.pyc')
    family.show_family('adams', ['lurch', 'morticia'])

    # Import directly from the internet
    myimport('http://users.rcn.com/python/download/puzzle.py')
    
