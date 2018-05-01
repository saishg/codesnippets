''' Demonstrate basics of XML Parsing.

    There are many tools:  DOM SAX ElementTree LXML.
    We'll work with ElementTree:

    parse(str or file)               -> ElementTree
    ET.getroot()                     -> Element
    E.tag                            -> first word in the opener
    E.text                           -> words between opener and closer
    E.get(attr)                      -> attribute value
    E.find(tag)                      -> a SINGLE subelement
    E.findall(tag)                   -> Multiple MATCHING subelements
    for se in E                      -> ALL subelements (unrestricted)

Standard Mini-language called XPATH:

    .                        current element
    ..                       parent element
    *                        all immediate sub-elements
    tag                      first immediate child with the given tag
    tag/subtag               child's child
    tag//subtag              any level of descendant from a given child
    [0]                      first child
    [@attr]                  first child that has a given attribute
    [@attr=value]            first child that has an attribute/value pair

'''


from xml.etree.ElementTree import parse

catalog = parse('notes/books.xml').getroot()

print '1. Book Identifiers'
for book in catalog:
    print book.get('id')

print
print '2 (a). Book Titles'
for book in catalog:
    print book.find('title').text

print
print '2 (b). Book Titles'
for title in catalog.findall('book/title'):
    print title.text

print
print '3. bk107 Title and Description'
book = catalog.find('book[@id="bk107"]')
print book.find('title').text, ":", book.find('description').text

print
print '4. Author and price of Computer books'
for book in catalog.findall('book'):
    if book.find('genre').text.lower() == 'computer':
        print book.find('author').text, "$", book.find('price').text

print
print '5. Metadata for bk104'
book = catalog.find('book[@id="bk104"]')
for md in book:
    print md.tag.upper(), md.text
