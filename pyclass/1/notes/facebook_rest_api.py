'Demonstrate typical use of a REST API, in this case we access Facebook'

# The Facebook REST API is documented at:
# https://developers.facebook.com/docs/graph-api

import json
import urllib

root = 'https://graph.facebook.com/'

def show_person(node):
    'Extract name and gender from a Facebook node'
    url = root + node
    u = urllib.urlopen(url)
    person = json.load(u)
    print '%s %s is a %s.' % (person['first_name'], person['last_name'], person['gender'])

if __name__ == '__main__':

    show_person('raymondh')
    show_person('zuck')
