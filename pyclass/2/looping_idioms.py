import itertools

names = 'raymond rachel matthew'.split()
colors = 'red blue yellow green'.split()
cities = 'austin dallas chicago austin dallas chicago'.split()


print 'Task 1: show the colors in uppercase'
for color in colors:
    print color.upper()

print '=============='

print 'Task 2: show the names and the position of each name in the list'
for i, name in enumerate(names, 1):
    print '{0} -> {1}'.format(i, name)

print '=============='

print 'Task 3: show the colors in reverse order'
for color in reversed(colors):
    print color

print '=============='

print 'Task 4: display the names with corresponding colors, ignoring mismatches'
for name, color in itertools.izip(names, colors):
    print name, color

print '--------------'    
for name, color in itertools.izip_longest(names, colors, fillvalue='unknown'):
    print name, color
    
print '=============='

print 'Task 5: show the colors alphabetically'
for color in sorted(colors):
    print color.title()

print '=============='

print 'Task 6: show the colors by length of word'
print sorted(colors, key=len)

print '=============='

print 'Task 7: show the colors by next-to-last letter of word'
print sorted(colors, key=lambda x:x[-2])

print '=============='

print 'Task 8: show cities without duplicates'
for city in sorted(set(cities)):
    print city.upper()

print '=============='


























    
