# https://www.careercup.com/question?id=15489754

ARRAY = [5, 6, 7, 8, 9, 10, 11, 1, 2, 3, 4]
OFFSET = 4
LENGTH = len(ARRAY)


def x(index):
    return (index - OFFSET) % LENGTH



def binary_search(value, start=0, end=LENGTH):
    if start >= end:
       return False
    middle = (start + end) / 2
#    print middle, ARRAY[x(middle)]
    if ARRAY[x(middle)] == value:
        print "=", x(middle)
        return True
    elif middle < value:
        return binary_search(value, middle + 1, end)
    else:
        return binary_search(value, start, middle)


if __name__ == '__main__':
    binary_search(1)

