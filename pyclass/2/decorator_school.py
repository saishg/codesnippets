import math

def make_visible(orig_func):
    def visible_math(*args):
        print '%s() was called with %r' % (orig_func.__name__, args)
        answer = orig_func(*args)
        print 'the answer is %r' % answer
        return answer
    return visible_math

dispatch = {}

def register(shortname):
    def inner(func):
        dispatch[shortname] = func
        return func
    return inner

def interpreter():
    program = raw_input('Enter a program:')
    fields = program.split()
    x = int(fields[0])
    commands = fields[1:]
    print x,
    for command in commands:
        x = dispatch[command](x)
        print '--(%s)--> %s' % (command, x),
    print


def cache(orig_func):
    answer_cache = {}

    def inner(x):
        if x in answer_cache:
            return answer_cache[x]
        answer = orig_func(x)
        answer_cache[x] = answer
        return answer
    
    return inner
        

##########################################################################

if __name__ == '__main__':
    import time

    @make_visible
    @register('sq')
    def square(x):
        'Compute a value times itself'
        return x * x

    @make_visible
    @register('cu')
    def cube(x):
        'Compute a value times itself thrice'
        return x ** 3

    @make_visible
    @register('co')
    def collatz(x):
        return 3*x+1 if x%2==1 else x//2

    @make_visible
    @register('ha')
    def halve(x):
        return x//2

    @make_visible
    @cache
    def big_func(x):
        'Simulate slow labor intensive function'
        print 'Doing hard work'
        time.sleep(1)
        return x + 1
