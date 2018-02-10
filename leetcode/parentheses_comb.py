LIST = []

def gen(nopen, nclose=None, expr=''):
    if nclose is None:
        nclose = nopen

    if nclose == 0:
        LIST.append(expr)
        return

    if nopen > 0:
        gen(nopen - 1, nclose, expr + '(')

    if nopen < nclose:
        gen(nopen, nclose - 1, expr + ')')


gen(3)
print LIST 
