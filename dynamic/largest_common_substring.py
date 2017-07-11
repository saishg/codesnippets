

STR1 = "sanfranciscoabcdefghijklasvegas"
STR2 = "abcxyzvegasuchafranciscolongstrings"

def iterative():
    MAX = 0
    SUBSTR = ""
    for i in range(len(STR1)):
        for j in range(len(STR2)):
            count = 0
            ii, jj = i, j
            while ii < len(STR1) and jj < len(STR2) and STR1[ii] == STR2[jj]:
                count += 1
                ii += 1
                jj += 1
            if count > MAX:
                MAX = count
                SUBSTR = STR1[i:i+count]
    return SUBSTR



def dynamic():
    MAX = 0
    SUBSTR = ""
    CACHE = [[0] * len(STR2) for i in range(len(STR1))]
    for i in range(len(STR1)):
        for j in range(len(STR2)):
            if STR1[i] == STR2[j]:
                CACHE[i][j] = CACHE[i-1][j-1] + 1
                if CACHE[i][j] > MAX:
                    MAX = CACHE[i][j]
                    SUBSTR = STR1[i+1-MAX : i+1]
    return SUBSTR



if __name__ == '__main__':
    print iterative()
    print dynamic()
