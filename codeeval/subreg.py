import sys


def findall(string, c):
    i = -1
    while True:
        i = string.find(c, i)
        if i < 0:
            break
        else:
            yield i

def search(haystack, needle):
    if len(needle) > len(haystack)
    if needle[0] != '*':
        for i in xrange(min(len(haystack), len(needle)
        i = 0
        while needle[i] == haystack[i]:
        


def parseFile(filename):
    f = open(filename, 'r')
    for l in f:
        haystack, needle = l.strip().split(',')
        print search(haystack, needle)

parseFile(sys.argv[1])

