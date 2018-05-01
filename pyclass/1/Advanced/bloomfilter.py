from random import *
import bitarray

class BloomFilter(object):

    def __init__(self, iterable=(), population=56, probes=6):
        self.population = range(population)
        self.probes = probes
        self.data = bitarray.BitArray(population)
        for name in iterable:
            self.add(name)

    def add(self, name):
        seed(name)
        lucky = sample(self.population, self.probes)
        for i in lucky:
            self.data[i] = 1

    def __contains__(self, name):
        seed(name)
        lucky = sample(self.population, self.probes)
        return all(self.data[i] for i in lucky)


if __name__ == '__main__':
    hettingers = BloomFilter('raymond rachel matthew ramon gayle dennis sharon'.split())
    print 'lisa' in hettingers
    print 'rachel' in hettingers
