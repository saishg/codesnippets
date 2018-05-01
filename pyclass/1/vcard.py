"""
"""


import csv
import urllib


vcard_template = """
BEGIN:VCARD
VERSION:2.1
N:{lname};{fname}
FN:{fname} {lname}
ORG:Bubba Gump Shrimp Co.
TITLE:{title}
PHOTO;GIF:http://www.example.com/dir_photos/my_photo.gif
TEL;WORK;VOICE:{phone}
ADR;WORK:;;100 Waters Edge;Baytown;LA;30314;United States of America
LABEL;WORK;ENCODING=QUOTED-PRINTABLE:100 Waters Edge=0D=0ABaytown, LA 30314=0D=0AUnited States of America
ADR;HOME:;;42 Plantation St.;Baytown;LA;30314;United States of America
LABEL;HOME;ENCODING=QUOTED-PRINTABLE:42 Plantation St.=0D=0ABaytown, LA 30314=0D=0AUnited States of America
EMAIL;PREF;INTERNET:{email}
REV:20080424T195243Z
END:VCARD
"""

# Company website to store all the vcards
vcard_url_template = 'https://dl.dropboxusercontent.com/u/3967849/vcard/{fname}_{lname}.vcf'


qrroot = 'https://chart.googleapis.com/chart?'
qrquery = {'cht': 'qr', 'chs': '300x300', 'chl': None}

with open('notes/raisin_team.csv') as f:
    for lname, fname, title, email, phone in csv.reader(f):
#        vcard = vcard_template.format(lname=lname, fname=fname, title=title, email=email, phone=phone)

            
        vcard_url = vcard_url_template.format(fname=fname, lname=lname)
        qrquery['chl'] = vcard_url
        qrurl = qrroot + urllib.urlencode(qrquery)


        filename = 'vcf/{fname}_{lname}.png'.format(fname=fname, lname=lname)
        with open(filename, 'w') as vfile:
            u = urllib.urlopen(qrurl)
            vfile.write(u.read())



