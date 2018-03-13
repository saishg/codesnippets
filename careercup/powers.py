# https://www.careercup.com/question?id=5529855880855552
# Print numbers satisfying (2 ^ i * 5 ^ j) in ascending order up to N

import math

########### SOLUTION 1 (slower) ############
CACHE = {}

def function(i, j):
    if (i, j) not in CACHE:
        CACHE[(i, j)] = (2 ** i) * (5 ** j)
    return CACHE[(i, j)]


def merge(list1, list2):
    # implement a proper merge
    return sorted(set(list1 + list2))

def get_sorted(N, i=0, j=0):
    result = function(i, j)
    if result > N:
        return []

    list1 = get_sorted(N, i + 1, j)
    list2 = get_sorted(N, i, j + 1)
    return [result] + merge(list1, list2)


########### SOLUTION 2 (faster) ############
def get_sorted2(N):
    CACHE2 = {}

    I_LIMIT = int(math.log(N, 2)) + 1
    J_LIMIT = int(math.log(N, 5)) + 1

    for i in range(I_LIMIT):
        for j in range(J_LIMIT):
            if (i, j) not in CACHE2:
                result = (2 ** i) * (5 ** j)
                if result > N:
                    break
                CACHE2[(i, j)] = result
    return sorted(CACHE2.values())


if __name__ == '__main__':
#    print get_sorted(100000000000)
    print get_sorted2(100000000000)
    
