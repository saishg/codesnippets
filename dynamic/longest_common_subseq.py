

STR2 = "abcdefg"
STR1 = "zzacbgafg"


def dynamic():
    CACHE = [[0] * len(STR2) for i in STR1]

    for i in range(len(STR1)):
        for j in range(len(STR2)):
            CACHE[i][j] = max(CACHE[i-1][j], CACHE[i][j-1])
            if STR1[i] == STR2[j]:
#                if STR1[i] == 'g' and STR2[j] == 'g':
#                    print i, j, CACHE[i-1][j-1]
                CACHE[i][j] += 1
    for row in CACHE:
        print row

if __name__ == '__main__':
    dynamic()
