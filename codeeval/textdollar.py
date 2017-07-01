import sys

NUM_DICT = {
           0 : "Zero",
           1 : "One",
           2 : "Two",
           3 : "Three",
           4 : "Four",
           5 : "Five",
           6 : "Six",
           7 : "Seven",
           8 : "Eighty",
           9 : "Nine",
           10 : "Ten",
           11 : "Eleven",
           12 : "Twelve",
           13 : "Thirteen",
           14 : "Fourteen",
           15 : "Fifteen",
           16 : "Sixteen",
           17 : "Seventeen",
           18 : "Eighteen",
           19 : "Nineteen",
           20 : "Twenty",
           30 : "Thirty",
           40 : "Forty",
           50 : "Fifty",
           60 : "Sixty",
           70 : "Seventy",
           80 : "Eighty",
           90 : "Ninety",
           100 : "$Hundred",
           1000 : "$Thousand",
           1000000 : "$Million",
           1000000000 : "$Billion",
           }

NUM_KEYS = sorted(NUM_DICT.keys(), reverse=True)

def join(str_list):
    string = str_list[0]
    for i in xrange(1, len(str_list)):
        if str_list[i].startswith('$') and str_list[i-1] == '' :
            string += 'One'
        string += str_list[i]
    return string.replace('$', '')

def numtext(N, prefix=False, suffix=False):
    if prefix:
        if N in (0, 1):
            return ''

    if suffix:
        if N == 0:
            return ''

    if N <= 20:
        return NUM_DICT[N]

    for i in NUM_KEYS:
        if i == N:
            return join((NUM_DICT[i], numtext(N%i, suffix=True)))
        elif i < N:
            return join((numtext(N/i, prefix=True), NUM_DICT[i], numtext(N%i, suffix=True)))


def parseFile(filename):
    f = open(filename, 'r')
    for l in f:
        print numtext(int(l)) + "Dollars"

#print numtext(21)
parseFile(sys.argv[1])
