# https://www.careercup.com/question?id=5761370824900608

def starts_with_palindrome(word, start):
    end = len(word) - 1
    while end > start:
        if word[start] != word[end]:
            return False
        start += 1
        end -= 1
    return True

def get_complements(word):
    reversed_word = ''.join(reversed(word))
    palindromic_complements = set()

    for start in range(len(reversed_word)-1, -1, -1):
        if starts_with_palindrome(reversed_word, start):
            palindromic_complements.add(reversed_word[:start])

    palindromic_complements.add(reversed_word[:-1])
    palindromic_complements.add(reversed_word)
    return palindromic_complements

def get_palindromic_combinations(word_list):
    word_list = set(word_list)

    PALINDROMIC_COMPLEMENTS = {}
    for word in word_list:
        PALINDROMIC_COMPLEMENTS[word] = get_complements(word)

    for word, complements in PALINDROMIC_COMPLEMENTS.iteritems():
        for complement in complements:
            if complement in word_list:
                print word, "+", complement

if __name__ == '__main__':
    get_palindromic_combinations(['none', 'xenon', 'xexenon'])
    get_palindromic_combinations(['a', 'aa', 'aaa', 'aaaa'])
