from bloomfilter import BloomFilter
import pickle
import re

def make_checker():
    try:
        with open('words.pcl', 'rb') as f:
            return pickle.load(f)
    except IOError:
        pass
   
    with open('notes/words.txt') as f:
        bf = BloomFilter(f.read().lower().split(), population=4000000, probes=10)

    with open('words.pcl', 'wb') as f:
        pickle.dump(bf, f)

    return bf

def spell_check(text, checker):
    print 'Misspelled:'
    print '-----------'
    for word in re.findall(r"[a-z\-\']+", text.lower()):
        if word not in checker:
            print word

if __name__ == '__main__':

    correct_words = '''
        a aid all an army assistance bad be
        beautiful by child children come country
        flag for from go going good help is later
        man many men my no now of our some state
        the their to ugly was with woman women
    '''

    text = '''
            Now, iss the tymme for all
            guhd ood men tooo comee to the
            ayd of thur country and city.
    '''

    checker = make_checker()
    spell_check(text, checker)






