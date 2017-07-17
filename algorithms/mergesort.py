import random
import collections


def mergesort(input_list):
    length = len(input_list)
    if length == 1:
        return input_list

    sorted1 = mergesort(input_list[:length/2])
    sorted2 = mergesort(input_list[length/2:])

    output_list = []

    while sorted1 and sorted2:
        if sorted1[0] < sorted2[0]:
            output_list.append(sorted1.pop(0))
        else:
            output_list.append(sorted2.pop(0))

    return output_list + sorted1 + sorted2

def generate_random(num=10):
    for i in xrange(num):
        yield random.randint(0, num * 3)


if __name__ == '__main__':
    print mergesort(collections.deque(generate_random()))
