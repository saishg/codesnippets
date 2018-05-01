
from xml.etree.ElementTree import parse

doc = parse('page.xml')
print doc.find('div/a[@id="123"]').text
