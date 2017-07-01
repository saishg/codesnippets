
charset = "abcd"
used = [0] * len(charset)

LEN = 3

def recur(perm=""):
    if len(perm) == LEN:
        print perm
        return

    for i, c in enumerate(charset):
        if not used[i]:
            used[i] = 1
            recur(perm + c)
            used[i] = 0


def recur2(perm=""):
    if len(perm) == LEN:
        print perm
        return

    for c in charset:
        recur2(perm + c)

def recur3(perm="", start=0):
    if len(perm) == LEN:
        print perm
        return

    end = len(charset)
    for i in range(start, end):
        if not used[i]:
            used[i] = 1
            recur3(perm + charset[i], i+1)
            used[i] = 0



#recur()
#recur2()
recur3()


