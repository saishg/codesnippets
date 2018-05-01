

import urllib
import json



def show_person(name):
    'Extract name and gender from a Facebook profile'
    
    url = 'https://graph.facebook.com/' + name

    u = urllib.urlopen(url)
    person = json.load(u)
    print '{0} {1} is a {2}'.format(person['first_name'], person['last_name'], person['gender'])


if __name__ == '__main__':
    show_person('zuck')
    show_person('raymondh')
    show_person('saishg')
