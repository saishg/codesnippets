

import math

pi = 3.141592


def area_circle(radius):
    """Compute area of the a circle

       For example:
       >>> area_circle(10)
       314.1592
    """
    return pi * radius**2.0


def area_triangle(base, height):
    """Compute area of a triangle

       For example:
       >>> area_triangle(10, 20)
       100.0
    """
    if base < 0.0 or height < 0.0:
        raise RuntimeError('Imaginary numbers not allowed')
    return base * height / 2.0

def quadratic(a, b, c):
    """ Return the two roots of the quadratic equation
        ax^2 + bx + c = 0
        
        Written in Python as:
        a*x**2.0 + b*x + c == 0.0

        For example:
        >>> quadratic(6, 28, 30)
        (-1.6666666666666667, -3.0)
    """
    discriminant = math.sqrt(b**2.0 - 4.0*a*c)
    x1 = (-b + discriminant) / (2.0 * a)
    x2 = (-b - discriminant) / (2.0 * a)
    return x1, x2


if __name__ == '__main__':
     import doctest
     print doctest.testmod()
