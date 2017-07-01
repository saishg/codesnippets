import sys

WORDDICT = {}
WORDLISTBYLENGTH = {}
PRIMARYWORD = "hello"
SOLUTION_LIST = []

def withindistance_equal(word1, word2):
    passed_change = False
    n = len(word1)

    for i in xrange(n):
        if word1[i] != word2[i]:
            if passed_change:
                return False
            else:
                passed_change = True
    else:
        # identical
        return True

def withindistance_unequal(word1, word2):
    if len(word1) > len(word2):
        word1, word2 = word2, word1
    n1, n2 = len(word1), len(word2)

    if n2 - n1 > 1:
        raise KeyError

    passed_change = False
    j = 0
    for i in xrange(n2):
        if j == n1:
            return True
        if word1[j] != word2[i]:
            if passed_change:
                return False
            else:
                passed_change = True
        else:
            j += 1
    else:
        # identical
        return True

def searchlength(n1, word2):
    if n1 not in WORDLISTBYLENGTH:
        return

    n2 = len(word2)
    wordlist = WORDLISTBYLENGTH[n1]
    for word1 in wordlist:
        if not WORDDICT[word1]:
            if n1 == n2:
                if withindistance_equal(word1, word2):
                    SOLUTION_LIST.append(word1)
                    WORDDICT[word1] = True
#                    print word2, word1
            else:
                if withindistance_unequal(word1, word2):
                    SOLUTION_LIST.append(word1)
                    WORDDICT[word1] = True
#                    print word2, word1


def look():
    SOLUTION_LIST.append(PRIMARYWORD)

    index = 0
    while True:
        word = SOLUTION_LIST[index]
        n = len(word)
        searchlength(n-1, word);
        searchlength(n, word);
        searchlength(n+1, word);
        index += 1
        if index >= len(SOLUTION_LIST):
            break


def parseFile(filename):
    f = open(filename, 'r')
    for l in f:
        l = l.strip()
        n = len(l)
        WORDDICT[l] = False
        if n not in WORDLISTBYLENGTH:
            WORDLISTBYLENGTH[n] = []
        WORDLISTBYLENGTH[n].append(l)
    look()
    print len(SOLUTION_LIST) - 1

parseFile(sys.argv[1])

