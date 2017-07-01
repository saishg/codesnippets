import sys

def decode(line):
    string, numbers = line.split('|')
    numbers = map(int, numbers.split())
    decoded_string = ''

    for i in numbers:
        decoded_string += string[i - 1]

    return decoded_string


def parseFile(filename):
    f = open(filename, 'r')
    while True:
        l = f.readline()
        if '|' in l:
            print decode(l)
        else:
            break



parseFile(sys.argv[1])







