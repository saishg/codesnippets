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

if __name__ == '__main__':
    numbers = range(100)
    random.shuffle(numbers)
    print mergesort(numbers)
