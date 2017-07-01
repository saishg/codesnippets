import sys

def parseFile(filename):
    f = open(filename, 'r')
    for l in f:
        l = l.replace('^', '**')
        s = eval(l)
        if isinstance(s, float):
            f = "%0.5f" % s
            if f.endswith('.00000'):
                print int(s)
            else:
                print f
        else:
            print s


parseFile(sys.argv[1])

