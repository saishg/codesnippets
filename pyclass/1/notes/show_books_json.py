''' Teach JSON Parsing and practice dictionary skills.

    json.loads(str) -> python objects        # this is what is meant by parsing

    d.keys()  d.values()   d.items()   d[k]
'''

import json

with open('notes/books.json') as f:
    catalog = json.load(f)

print 'Task 1:  Show the book identifiers'
for book_id in sorted(catalog):
    print book_id

print 'Task 2:  Show titles of all books'
for book in catalog.values():
    print book['title']

print 'Task 3:  Title and description of bk105'
book = catalog['bk105']
print book['title']
print book['description']

print 'Task 4:  Author and price of computer books'
for book in catalog.values():
    if book['genre'].lower() == 'computer':
        print book['author']
        print book['price']
        print

print 'Task 5:  All metadata for bk104'
book = catalog['bk104']
for tag, value in book.items():
    print tag.upper()
    print value
    print
