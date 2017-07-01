#!/bin/python

import sys

class Tower:
    def __init__(self, line):
        self._blocks = map(int, line.split())
        self._sum = sum(self._blocks)
    
    def sum(self):
        return self._sum
    
    def pop(self, height):
        while self._sum > height:
            self._sum -= self._blocks.pop(0)
        
    def blocks(self):
        return len(self._blocks)
    
    def compare(self, t):
        height_difference = self.sum() - t.sum()
        if height_difference == 0:
            for block1, block2 in zip(self._blocks, t._blocks):
                if block1 != block2:
                    return block1 - block2
            return self.blocks() - t.blocks()
        else:
            return height_difference
    



n1,n2,n3 = raw_input().strip().split(' ')
n1,n2,n3 = [int(n1),int(n2),int(n3)]
h1 = Tower(raw_input())
h2 = Tower(raw_input())
h3 = Tower(raw_input())

def compare_towers(t1, t2):
    return t1.compare(t2)
    

while True:
    if 0 in [h1.sum(), h2.sum(), h2.sum()]:
        print 0
        break
    if h1.sum() == h2.sum() == h3.sum():
        print h1.sum()
        break
    h1, h2, h3 = sorted([h1, h2, h3], cmp=compare_towers, reverse=True)
#    print sum(h1), sum(h2), sum(h3)
    h1.pop(h3.sum())

