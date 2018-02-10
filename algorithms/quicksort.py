import random


def quicksort(numbers):
    if len(numbers) <= 1:
        return numbers

    pivot = numbers.pop(0)
    lower = []
    higher = []

    for i in numbers:
        if i > pivot:
            higher.append(i)
        else:
            lower.append(i)

    return quicksort(lower) + [pivot] + quicksort(higher)


def swap(numbers, index1, index2):
    numbers[index1], numbers[index2] = numbers[index2], numbers[index1]


def quicksort_inplace(numbers, start=0, finish=None):
    if finish is None:
        finish = len(numbers)

#    print "sort", numbers[start:finish]
#    if finish - start == 2:
#        print "just two:", numbers[start:finish], numbers[start], numbers[finish-1]
#        if numbers[finish-1] < numbers[start]:
#            swap(numbers, start, finish-1)
#            print "swapped two:", numbers[start:finish]
#            return
    if finish - start <= 1:
        return

    pivot = start
    start = start + 1
    i = start
    j = finish - 1

    while True:
        while i < finish and numbers[i] < numbers[pivot]:
            i += 1

        while j > start and numbers[j] > numbers[pivot]:
            j -= 1

        if j > i:
            swap(numbers, i, j)
            print numbers
            i += 1
            j -= 1
        else:
            break

    print "==="
    print numbers
    print "swap2", numbers[start-1:finish], pivot, i, j, ":", numbers[pivot], "<->", numbers[i-1]
    swap(numbers, pivot, i-1)
    print numbers
    quicksort_inplace(numbers, start-1, i-1)
    quicksort_inplace(numbers, i, finish)


if __name__ == '__main__':
    numbers = range(10)
    random.shuffle(numbers)
#    numbers = [3, 2, 1, 5, 0, 9, 8, 6, 4, 7]
    print numbers
#    print quicksort(numbers)
    quicksort_inplace(numbers)
    print numbers
