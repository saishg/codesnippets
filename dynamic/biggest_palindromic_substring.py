import pprint


STR = 'scbaabcdbcbbcsan'
#STR = 'cbaabcdbcbbc'
#STR = 'abcdabadda'

def get_matrix():
    matrix = []
    row = [0] * len(STR)
    for i in range(len(STR)):
        matrix.append(list(row))
    return matrix

def get_palindrome():
    MATRIX = get_matrix()
    LENGTH = len(STR)

    for i in range(LENGTH):
        MATRIX[i][i] = 1

    for i in range(LENGTH):
        for j in range(LENGTH - i):
            if j == i+j:
                MATRIX[j][j+i] = 1
            elif STR[j] == STR[j+i]:
                MATRIX[j][j+i] = MATRIX[j+1][j+i-1] + 2
    pprint.pprint(MATRIX)

    MAX = 1
    SUBSTR = ''
    for i in range(LENGTH):
       for j in range(LENGTH):
           if MATRIX[i][j] > MAX:
               MAX = MATRIX[i][j]
               SUBSTR = STR[i+1:MAX+1]
               print MAX, i, j, SUBSTR

if __name__ == '__main__':
    get_palindrome()

