''' Monkey patching is making variable assignments into some other namespace.
'''

import algebra
import math

algebra.pi = math.pi                            # Monkey Patch



original_area_triangle = algebra.area_triangle  # 1. Save the original

def better_area_triangle(base, height):         # 2. Write wrapper
    try:
        return original_area_triangle(base, height)
    except RuntimeError:
        raise ValueError('Illegal base and height. No negatives allowed')

algebra.area_triangle = better_area_triangle    # 3. Monkey patch the wrapper back



original_sqrt = math.sqrt

def better_sqrt(x):
    if x >= 0.0:
        return original_sqrt(x)
    return original_sqrt(-x) * 1j

math.sqrt = better_sqrt

    
if __name__ == '__main__':
    print u'I have on good authority that \N{greek small letter pi} is', algebra.pi
    print 'The area of a circle with raidus 10 is:', algebra.area_circle(10)
    try:
        print 'The area of the 1st triangle is:', algebra.area_triangle(5, 40)
        print 'The area of the 2nd triangle is:', algebra.area_triangle(5, -40)
    except ValueError:
        print 'Sorry about the negative value'
        
    print 'Solution to 12x^2 + 23x + 10 is:',
    print algebra.quadratic(a=12, b=23, c=10)
    print 'Solution to 12x^2 + 8x + 10 is:',
    print algebra.quadratic(a=12, b=8, c=10)
