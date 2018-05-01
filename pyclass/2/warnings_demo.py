import warnings
import math

class RaymondWarning(UserWarning):
    'You can define your own warning categories'


def sqrt(x):
    if x >= 0.0:
        return math.sqrt(x)
    warnings.warn('Taking the square root of a negative number')
    return math.sqrt(-x) * 1j

def user(x):
    warnings.warn('The "user" function is deprecated, use "sqrt" instead', DeprecationWarning)
    return sqrt(x ** 3.0)

warnings.filterwarnings('always', '.*square root.*')
warnings.filterwarnings('once', category=DeprecationWarning)

print user(5)
print user(-5)
warnings.warn('Oops, I did it again.  I played with heart, ...')
print user(6)
warnings.warn('Python is the best!', RaymondWarning)
print user(-6)
print 'Done'

