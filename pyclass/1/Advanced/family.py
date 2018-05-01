'Practice patterns of output formatting'

def show_family(lastname, first_names):
    'Display the family members in a nice tabular format'
    print 'The {} Family'.format(lastname.title())
    print '=' * (11 + len(lastname))
    for name in first_names:
        print '* {}'.format(name.title())
    print ''

if __name__ == '__main__':
    show_family(
        lastname = 'starks',
        first_names = ['eddard', 'catelyn', 'robb', 'john snow', 'arya',
                       'rickon', 'bram', 'sansa'])
