''' Demonstrate basics of XML Parsing.

    There are many tools:  DOM SAX ElementTree LXML.
    We'll work with ElementTree:

    parse(str or file)               -> ElementTree
    ET.getroot()                     -> Element
    E.tag                            -> first word in the opener
    E.text                           -> words between opener and closer
    E.get(attr)                      -> attribute value
    E.find(xpath)                    -> a SINGLE subelement
    E.findall(xpath)                 -> Multiple MATCHING subelements
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

Tools:
    XSLT, Schema Validators, CDATA, PCDATA, base64

'''

from xml.etree.ElementTree import parse

catalog = parse('notes/books.xml').getroot()

print 'Task 1:  Show the book identifiers'
for book in catalog:
    print book.get('id')

print 'Task 2:  Show the book titles'
for title in catalog.findall('book/title'):
    print title.text

print 'Task 3:  Show title and desc of bk107'
book = catalog.find('book[@id="bk107"]')
print book.find('title').text
print book.find('description').text

print 'Task 4:  Show author and price of computer books'
for book in catalog:
    if book.find('genre').text.lower() == 'computer':
        print book.find('author').text
        print book.find('price').text
        print

print 'Task 5:  Show all metadata for bk104'
book = catalog.find('book[@id="bk104"]')
for se in book:
    print se.tag.upper()
    print se.text
    print
