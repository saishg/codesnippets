

SEQ = (1, 2, 3, 2, 6, 8, 9, 15, 22, 2, 3, 4, 5, 6, 11, 4, 7, 29, 5, 6, 7, 8, 9)
#SEQ = (1, 6, 4)

def is_ascending(subseq):
    prev = -1
    for i in subseq:
        if prev > i:
            return False
        else:
           prev = i
    return True
            

def recurse(subseq=(), index=0):
    if index == len(SEQ):
        if is_ascending(subseq):
            return len(subseq)
        else:
            return 0

    return max(recurse(subseq, index+1),
               recurse(subseq + (SEQ[index],), index+1))


if __name__ == '__main__':
    print recurse()
