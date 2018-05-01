from collections import Counter, OrderedDict, deque, defaultdict
from pprint import pprint
from itertools import imap
import re

names = ''' tom david raymond rachel matthew susan timothy beatrice
brandon martin darlene daily randal suzy bryce mary rodney davin
bill dave'''.split()

people = 'raymond rachel matthew'.split()
foods = 'steak kale chocolate'.split()
colors = 'red green blue green red purple blue red green red'.split()


###########################

c = Counter(colors)
#print c.most_common(2)

with open('notes2/hamlet.txt') as f:
    play = f.read()

#pprint(Counter(play.lower()).most_common(10))

words = re.findall(r"[a-z\'\-]+", play.lower())
c = Counter(words)
#pprint(c.most_common(10))

pref = OrderedDict()
for person, food in zip(people, foods):
    pref[person] = food
#print pref


print 'Group names by first letter of the name'
d = defaultdict(list)
for name in names:
    feature = name[0]
    d[feature].append(name)
#pprint(dict(d))


print 'Group names by last letter of the name'
d = defaultdict(list)
for name in names:
    feature = name[-1]
    d[feature].append(name)
#pprint(dict(d))


print 'Group names by length of the name'
d = defaultdict(list)
for name in names:
    feature = len(name)
    d[feature].append(name)
#pprint(dict(d))

print 'Group names number of vowels in the name'
d = defaultdict(list)
for name in names:
    feature = sum(imap(name.count, 'aeiouy'))
    d[feature].append(name)
#pprint(dict(d))


# FIFO queue
disney_line = deque(names[:5])
print disney_line.popleft(), 'gets on the ride'
print disney_line.popleft(), 'gets on the ride'
print disney_line.popleft(), 'gets on the ride'
disney_line.append('mary')
disney_line.append('marge')
print disney_line.popleft(), 'gets on the ride'
print disney_line.popleft(), 'gets on the ride'

