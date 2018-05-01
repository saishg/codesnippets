''' A true, but old tale of Python
    involving commas, brothers-in-law, raisins,
    checkerboards, and business cards.
'''

import csv
import urllib

vcard_template = '''BEGIN:VCARD
VERSION:3.0
N:%s;%s
FN:%s %s
ORG:Raisins R Us, Inc
TITLE:%s
TEL;TYPE=WORK,VOICE:%s
LABEL;TYPE=WORK:100 Flat Grape Dr\nFresno, CA 95555\nUnited States of America
EMAIL;TYPE=PREF,INTERNET:%s
REV:2014-04-24T19:52:43Z
END:VCARD
'''

# Google REST API for QR Codes is documented at:
# https://developers.google.com/chart/infographics/docs/qr_codes?hl=fr
root = 'https://chart.googleapis.com/chart?'

# Company website to store all the vcards
# Typically:   http://vcard.raisins.example.com/
website = 'https://dl.dropboxusercontent.com/u/3967849/vcard/'

with open('notes/raisin_team.csv') as f:
    for lname, fname, title, email, phone in csv.reader(f):
        vcard = vcard_template % (lname, fname, fname, lname, title, phone, email)

        filename = '%s_%s.vcf' % (fname, lname)
        with open(filename, 'w') as vfile:
            vfile.write(vcard)

        link = website + filename
        
        query = {'cht': 'qr', 'chs': '300x300', 'chl': link}
        url = root + urllib.urlencode(query)
        u = urllib.urlopen(url)
        image = u.read()

        filename = '%s_%s.png' % (fname, lname)
        with open(filename, 'w') as ifile:
            ifile.write(image)


