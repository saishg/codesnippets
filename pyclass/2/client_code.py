"Show-off circuitous from a user's point of view"

from __future__ import division
from circuitous import Circle
from random import random, seed
import pprint
import math

c = Circle(10)
print u'Tutotial for Circuitous\N{trade mark sign}'
print 'Using Circle version %d.%d' % Circle.version[:2]
print 'A circle with a radius of', c.radius
print 'has an area of', c.area()
print


######### ACADEMIC FRIENDS ##########

n = 10
jenny = 8675309
print 'DARPA Grant Proposal'
print 'to study the average area of circles'
print 'using Circle version %d.%d' % Circle.version[:2]
print 'prliminary study using %d random circles' % n
print "seeded using Jenny's number:", jenny
seed(jenny)
circles = [Circle(random()) for i in xrange(n)]
areas = [circle.area() for circle in circles]
average_area = sum(areas) / n
print 'The average area is %.1f' % average_area



###### Rubber Sheet Company ##########

cut_template = [0.1, 0.2, 0.7]
print 'Spec sheet for the cut template:', cut_template
circles = [Circle(cut_radius) for cut_radius in cut_template]
for i, circle in enumerate(circles, 1):
    print 'Circle #%d' % i
    print 'A rubber circle with a cut radius of', circle.radius
    print 'has a perimeter of', circle.perimeter()
    print 'a cold area of', circle.area()
    circle.radius *= 1.1
    print 'and a warm area of', circle.area()
    print


###### National Tire Chain ##########

class Tire(Circle):
    'Circle analytics specialed for tires'

    RUBBER_RATIO = 1.25

    def perimeter(self):
        'Perimeter correct for the rubber on a tire'
        return Circle.perimeter(self) * self.RUBBER_RATIO

    __perimeter = perimeter

t = Tire(30)
print 'A tire with an inner radius of', t.radius
print 'has an inner area of', t.area()
print 'and an odometer corrected outer perimeter of', t.perimeter()
print


class MonsterTire(Tire):
    RUBBER_RATIO = 1.50

m = MonsterTire(30)
print 'Monster Tire has an odometer corrected outer perimeter of', m.perimeter()


###### National Trucking Company ##########

print u'An inclinometer reading of 5\N{degree sign}',
print 'is a %.1f%% grade' % Circle.angle_to_grade(5)
print

###### National Graphics Company ##########

c = Circle.from_bbd(25)
print 'A circle with a bounding box diagonal of 25'
print 'has a radius of', c.radius
print 'and perimeter of', c.perimeter()
print
