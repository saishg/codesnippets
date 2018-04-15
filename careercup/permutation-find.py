
VALID_CHARS = set('ABCDEF')

def find_first_permutation(string):
    FOUND_VALID_CHAR = {}

    start_index = 0

    for end_index in range(len(string)):
        end_char = string[end_index]
        if end_char not in VALID_CHARS:
            FOUND_VALID_CHAR = {}
            start_index = end_index + 1

        elif end_char not in FOUND_VALID_CHAR:
            FOUND_VALID_CHAR[end_char] = None
            if len(FOUND_VALID_CHAR) == len(VALID_CHARS):
                # print string[start_index:end_index+1]
                return start_index

        else:
            while string[start_index] != end_char:
                del FOUND_VALID_CHAR[string[start_index]]
                start_index += 1
            start_index += 1

    return -1


if __name__ == '__main__':
    print find_first_permutation('ZZZBCDEAFZZZ')
    print find_first_permutation('ABCCDABCFFABCDEE')


