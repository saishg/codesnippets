# https://www.careercup.com/question?id=5682428306784256

DICTIONARY = sorted(["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"], key=lambda x:len(x), reverse=True)
USED = [False for j in range(len(DICTIONARY))]


def find_min_breaks(string, words=()):
    if string == '':
        return words

    min_result = None
    for index, dict_word in enumerate(DICTIONARY):
        if not USED[index] and string.startswith(dict_word):
            USED[index] = True
            result = find_min_breaks(string[len(dict_word):], words + (dict_word,))
            if result and (min_result is None or len(result) < len(min_result)):
                min_result = result
            USED[index] = False
    return min_result



if __name__ == '__main__':
    print find_min_breaks('CatMat')
    print find_min_breaks('DogCatMog')
