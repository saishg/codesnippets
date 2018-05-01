'''Circuitous(tm)
An Advanced Circle Analytics
'''
from collections import namedtuple
import math

Version = namedtuple('Version', ['major', 'minor', 'micro'])

# New style code
class Circle(object):
    ''' Advanced circle analytic toolkit
    '''

    __slots__ = ['diameter']    # Flyweight Pattern
    
    version = Version(0, 8, 1)
    
    def __init__(self, radius):
        'Create a circle of specified radius'
        self.radius = radius

    def area(self):
        'Compute the area'
        p = self.perimeter()
        radius = p / 2.0 / math.pi
        return math.pi * radius ** 2.0

    def perimeter(self):
        'Compute the perimeter'
        return 2 * math.pi * self.radius

    __perimeter = perimeter

    def __repr__(self):
        return "%s(%r)" % (self.__class__.__name__, self.radius,)

    @staticmethod
    def angle_to_grade(angle):
        'Convert an inclinometer reading in degrees into a percent grade'
        return math.tan(math.radians(angle)) * 100.0

    @classmethod
    def from_bbd(cls, bbd):
        'Construct a new circle from a bounding box diagonal'
        radius = bbd / 2.0 / math.sqrt(2.0)
        return cls(radius)

    @property
    def radius(self):
        return self.diameter / 2.0

    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0

