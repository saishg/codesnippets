import random

def swap(numbers, i, j):
    numbers[i], numbers[j] = numbers[j], numbers[i]

def quicksort(numbers, start, end):
    if start >= end - 1:
        return

    pivot = start
    i = start + 1
    j = end - 1


    while True:
        while i < end and numbers[pivot] > numbers[i]:
            i += 1

        while j > i and numbers[pivot] < numbers[j]:
            j -= 1

        if i >= j:
            swap(numbers, pivot, i - 1)
            break

        swap(numbers, i, j)

    quicksort(numbers, start, i-1)
    quicksort(numbers, i, end)




if __name__ == '__main__':
    LIMIT = 1000
    for i in range(10):
        numbers = range(LIMIT)
        random.shuffle(numbers)
        quicksort(numbers, 0, len(numbers))
        if numbers != range(LIMIT):
            print "FAILURE", numbers
            break
