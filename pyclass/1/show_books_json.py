"""
json.loads(str) -> python objects
"""

import json


with open('notes/books.json') as f:
    catalog = json.load(f)


print '1. Book Identifers'

for bookid in sorted(catalog):
    print bookid

print
print '2. Book Titles'

for bookinfo in catalog.values():
    print bookinfo['title']

print
print '3. bk107 Title and Description'

book = catalog['bk107']
print book['title'], ":", book['description']

print
print '4. Author and price of Computer books'


for bookinfo in catalog.values():
    if bookinfo['genre'].lower() == 'computer':
        print bookinfo['author'], "$", bookinfo['price']

print
print '5. Metadata for bk104'

book = catalog['bk104']
for tag, value in book.items():
    print tag.upper(), value
    
