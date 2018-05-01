''' Goal:  Become a black belt with properties

Fundamental action:  Converts attribute lookup like a.x into method access like a.m()

Mechanism:  It reprograms the dot, but that can only be done in new-style classes.

'''

from __future__ import division
from validators import validate_percentage



class PriceRange(object):
    
    def __init__(self, symbol, low, high):
        self.symbol = symbol
        self.low = low
        self.high = high

    @property
    def midpoint(self):
         return (self.low + self.high) / 2

    def __repr__(self):
        return '%s(symbol=%r, low=%r, high=%r)' % \
               (self.__class__.__name__, self.symbol, self.low, self.high)


    # Managed attributes

    @property
    def low(self):
        return self._low

    @low.setter
    def low(self, low):
        validate_percentage(low)
        self._low = low

    @property
    def high(self):
        return self._high

    @high.setter
    def high(self, high):
        validate_percentage(high)
        self._high = high

p = PriceRange('CSCO', 25, 32)
