# https://www.careercup.com/question?id=5529855880855552
# Print numbers satisfying (2 ^ i * 5 ^ j) in ascending order up to N

import math
import heapq

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
    POWERS = set()

    I_LIMIT = int(math.log(N, 2)) + 1
    J_LIMIT = int(math.log(N, 5)) + 1

    for i in range(I_LIMIT):
        for j in range(J_LIMIT):
            result = (2 ** i) * (5 ** j)
            if result > N:
                break
            POWERS.add(result)
    return sorted(POWERS)

########### SOLUTION 3 (copied) ############
def get_sorted3(N):
    minHeap = [(1, 0, 0)]
    seen = set()
    res = []

    while minHeap:
        product, i, j = heapq.heappop(minHeap)
        seen.add((i, j))
        res.append(product)
        nextIndices = [(i + 1, j), (i, j + 1)]

        for nextI, nextJ in nextIndices:
            if (nextI, nextJ) not in seen:
                nextProduct = product * 2 if nextI > i else product * 5
                if nextProduct <= N:
                    heapq.heappush(minHeap, (nextProduct, i + 1, j))
    return res

if __name__ == '__main__':
    LIMIT = 1000000000000000000000
#    print get_sorted(LIMIT)
#    print get_sorted2(LIMIT)
    print get_sorted3(LIMIT)
    
