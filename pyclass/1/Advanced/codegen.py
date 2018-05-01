''' Goal:  Learn to generate code automatically from specs
           as a way to save labor and improve quality.

def parse(data):
    'Parse a variable length record format'
    i = 0
    while i < len(data):
        kind = data[i]
        i += 1
        if 0:
            pass
        elif kind == 'p':
            lastname = str(data[i:i+8]).rstrip()
            i += 8
            age = int(data[i:i+4])
            i += 4
            print dict(kind=kind, lastname=lastname, age=age)
        elif kind == 'c':
            firstname = str(data[i:i+10]).rstrip()
            i += 10
            height = float(data[i:i+12])
            i += 12
            print dict(kind=kind, firstname=firstname, height=height)
        else:
            raise ValueError('Unknown kind: ' + kind)

if 1:
    sample_data = 'pSmith     15pJones      9cRaymond           63.7'
    parse(sample_data)
'''


###########################################
####### Your Turn.    Class Exercise ######

# Hint 1:  start with a debugged working code fragment
# Hint 2:  cut-and-paste, then parameterize
# Hint 3:  feel free to change the original code to make this work easier
# Hint 4:  use multi-line strings with a leading backslash
# Hint 5:  work from inside out
# Hint 6:  arrange your templates in the same order as the original file
# Hint 7:  start with global variables, then move to a function
# Hint 8:  develop using print, then turn into a generator
# Hint 9:  combine the strings and exec

header = '''\
def parse(data):
    'Parse a variable length record format'
    i = 0
    while i < len(data):
        kind = data[i]
        i += 1
        if 0:
            pass
'''

kind_line = '''\
        elif kind == '{kind}':
'''

str_line = '''\
            {fname} = {ftype}(data[i : i + {fwidth}]).rstrip()
            i += {fwidth}
'''

other_line = '''\
            {fname} = {ftype}(data[i : i + {fwidth}])
            i += {fwidth}
'''

pair_template='{fname}={fname}'

dict_line = '''\
            print dict(kind='{kind}', {pairs})
'''

else_line = '''\
            raise ValueError('Unknown kind: ' + {kind})
'''

footer = '''\
        else:
            raise ValueError('Unknown kind: ' + kind)
'''

def generate_parser(record_layout):
    yield header
    for kind, fspecs in record_layout.iteritems():
        yield kind_line.format(kind=kind)
        for fspec in fspecs:
            fname, ftype, fwidth = fspec
            if ftype == 'str':
                yield str_line.format(fname=fname, ftype=ftype, fwidth=fwidth)
            else:
                yield other_line.format(fname=fname, ftype=ftype, fwidth=fwidth)
        pairs = ', '.join(pair_template.format(fname=fname) for fname, ftype, fwidth in fspecs)
        yield dict_line.format(kind=kind, pairs=pairs)
    yield footer


def parse_record_type(record_layout, verbose=False):
    code = ''.join(generate_parser(record_layout))
    if verbose:
        print code
    namespace = {}
    exec code in namespace
    return namespace['parse']



###########################################
#######    Client Code               ######

if __name__ == '__main__':
    import json
    with open('notes/parser.json') as f:
        record_layout = json.load(f)

    parse = parse_record_type(record_layout)
    sample_data = 'pSmith     15pJones      9cRaymond           63.7'
    parse(sample_data)


