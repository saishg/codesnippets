

SEQ = (1, 2, 3, 8, 9, 15, 22, 2, 3, 4, 11, 4, 7, 29, 40, 45, 90, 8, 9, 15, 22, 2, 3, 4, 7, 7, 29, 40, 45, 90)
#SEQ = (1, 2, 1, 3, 100, 2, 2, 3, 2, 100, 2, 3, 1, 2)
#SEQ = (1, 2, 3, 2, 6,)
#SEQ = (1, 6, 4)
#SEQ = (1, 6, 4, 5, 2, 3, 4)

def is_ascending(subseq):
    prev = -1
    for i in subseq:
        if prev >= i:
            return False
        else:
           prev = i
    return True

def recurse(subseq=(), index=0):
    if index == len(SEQ):
        return len(subseq)
    else:
        value1 = recurse(subseq, index+1)

        new_subseq = subseq + (SEQ[index],)
        value2 = 0
        if is_ascending(new_subseq):
            value2 = recurse(new_subseq, index+1)

        return max(value1, value2)



def dynamic():
    CACHE2 = [1] * len(SEQ)

    for i in xrange(len(SEQ)):
        for j in xrange(i+1, len(SEQ)):
            if SEQ[j] > SEQ[i]:
                CACHE2[j] = max(CACHE2[i] + 1, CACHE2[j])
    return max(CACHE2)


if __name__ == '__main__':
    print recurse()
    print dynamic()
