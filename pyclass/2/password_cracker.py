###### Security Code #######

from pprint import pprint
import hashlib
import itertools


userpass = {}

def digest(password):
    salt = 'the life expectancy of a stark, targyrian, or lannister is very short'
    result = password + salt
    for i in range(10000):
        result = hashlib.sha512(result + str(i)).hexdigest()
    return result

def is_strong(password):
    if len(password) < 6:
        return False
    elif not any(c.isupper() for c in password):
        return False
    elif not any(c.islower() for c in password):
        return False
    elif not any(c.isdigit() for c in password):
        return False
    return True
    

def new_account(username, password):
    if not is_strong(password):
        raise ValueError('%s: Password must be strong' % (username,))
    userpass[username] = digest(password)


def verify(username, password):
    return userpass[username] == digest(password)


### Cracker code 1 ####

rainbow = {}    # md5: password

def make_rainbow():
    with open('notes2/common_passwords.txt') as f:
        for line in f:
            password, count = line.split(',')
            hashpass = digest(password)
            rainbow[hashpass] = password

def cracker(userpass, rainbow):
    for username, hashpass in userpass.items():
        if hashpass in rainbow:
            print username, rainbow[hashpass]


### Cracker code 2 ####
            
def search_common(userpass):
    passuser = {hashpass: user for user, hashpass in userpass.items()}
    short_num_variants = map(str, range(10)) + ['']
    num_variants = map(str, range(1000)) + ['']
    with open('notes2/common_passwords.txt') as f:
        for line in f:
            password, count = line.split(',')
            case_variants = [password.lower(), password.upper(), password.title()]
            for parts in itertools.product(short_num_variants, case_variants, num_variants):
                password = ''.join(parts)
                hashpass = digest(password)
                if hashpass in passuser:
                    print passuser[hashpass], password


if __name__ == '__main__':
    new_account('raymondh', 'Superman7')
    new_account('jeff', 'Cisco1')
    new_account('denis', '1Sharapova')
    new_account('ai', 'Brazil1')
    new_account('steven', 'Seahawks12')
    print 'Accounts created'

    if verify('jeff', 'Cisco1'):
        print 'jeff logged in'
    else:
        print 'jeff cannot log in'

    if verify('steven', 'Seahawks12'):
        print 'steven logged in'
    else:
        print 'steven cannot log in'

#    make_rainbow()
#    cracker(userpass, rainbow)
#    search_common(userpass)

