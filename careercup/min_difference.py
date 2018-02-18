# https://www.careercup.com/question?id=5140428923863040

def min_diff(list1, list2):
    i = 0
    j = 0
    result = 2 ** 32

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result = min(result, list2[j] - list1[i])
            i += 1
        else:
            result = min(result, list1[i] - list2[j])
            j += 1

    return result


if __name__ == '__main__':
    list1 = [10, 20, 30, 40]
    list2 = [1, 2, 3, 4]
    print min_diff(list1, list2)

