'A cute way of making dicts using metaclasses'


def dict_meta(name, bases, mapping):
    return mapping


class hettingers:

    __metaclass__ = dict_meta

    raymond = 'red'
    rachel = 'blue'
    matthew = 'yellow'


class simpsons:
    __metaclass__ = dict_meta
    homer = 'doh!'
    marge = 'grrrr!'
    bart = 'cowabunga!'
    lisa = 'Baaaarrrrt!'
    maggie = '<sucking noises>'

print hettingers
print simpsons
