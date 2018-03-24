# https://www.careercup.com/question?id=5759325447389184
# Given 2 input arrays, return True if the words in the first array are sorted
# as per the ordering in the second array

def is_sorted(array, ordering):
    INDEX = {}

    for index, char in enumerate(ordering):
        INDEX[char] = index

    for i in range(len(array) - 1):
        word1 = array[i]
        word2 = array[i + 1]

        index = 0
        while index < len(word1) and index < len(word2):
            if INDEX[word1[index]] < INDEX[word2[index]]:
                break
            elif INDEX[word1[index]] > INDEX[word2[index]]:
                return False
            else:
                index += 1
        else:
            if len(word1) > len(word2):
                return False

    return True


def is_sorted2(array, ordering):
    INDEX = {}
    for index, char in enumerate(ordering):
        INDEX[char] = index

    BASE = len(ordering)
    previous_score = 0

    for word in array:
        score = 0
        for char in word:
            score = score * BASE + INDEX[char]
        if score < previous_score:
            return False
        else:
            previous_score = score
    return True

            


if __name__ == '__main__':
    print is_sorted2(['cc', 'cb', 'bb', 'ac'], ['c', 'b', 'a'])
    print is_sorted2(['cc', 'cb', 'bb', 'ac'], ['b', 'c', 'a'])
    print is_sorted2(['ccc', 'ccc', 'aaab', 'aaa'], ['b', 'c', 'a'])
    print is_sorted2(['ccc', 'ccc', 'aaa', 'aaab'], ['b', 'c', 'a'])
