# https://www.careercup.com/question?id=5389627422670848


#######################################
# Solution 1

def encode(word):
    key = 0
    MAPPING = {}
    ENCODED_WORD = []
    for char in word:
        if char not in MAPPING:
            MAPPING[char] = key
            key += 1
        ENCODED_WORD.append(MAPPING[char])
    return ENCODED_WORD

def is_isomorphic(word1, word2):
    return encode(word1) == encode(word2)


#######################################
# Solution 2: More efficient, but doesn't handle repeat mappings

def is_isomorphic2(word1, word2):
    if len(word1) != len(word2):
        return False

    MAPPING = {}
    for index, char1 in enumerate(word1):
        char2 = word2[index]

        if char1 not in MAPPING:
           MAPPING[char1] = char2

        if MAPPING[char1] != char2:
            return False

    return True
    

if __name__ == '__main__':
    print is_isomorphic("abcccc", "deffff")
    print is_isomorphic("abc", "fff")

    print is_isomorphic2("abcccc", "deffff")
    print is_isomorphic2("abc", "fff")
