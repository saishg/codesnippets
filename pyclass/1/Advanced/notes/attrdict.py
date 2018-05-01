'Goal:  Make a dictionary where we can use a dot in addition to the usual square brackets'

class AttrDict(dict):

    def __getattr__(self, attr):
        return self[attr]

    def __setattr__(self, attr, value):
        self[attr] = value

if 0:
    d = AttrDict()
    d['raymond'] = 'apple'
    d['rachel'] = 'banana'
    d.matthew = 'orange'
    d.jill = 'pears'

    print d.raymond
    print d.rachel
    print d['matthew']
    print d['jill']

