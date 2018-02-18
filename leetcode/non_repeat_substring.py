# https://leetcode.com/problems/longest-substring-without-repeating-characters/



def get_substring(string):
    longest = 0
    longest_substring = ''
    start_index = 0
    end_index = 0
    CACHE = {}

    for end_index, end_char in enumerate(string):
        while end_char in CACHE:
            del CACHE[string[start_index]]
            start_index += 1
        CACHE[end_char] = end_index

        """
        # in case you want the actual subtrsing
        if longest < end_index - start_index + 1:
            longest = end_index - start_index + 1
            longest_substring = string[start_index: end_index + 1]
        """

        longest = max(longest, end_index - start_index + 1)

    return longest


if __name__ == '__main__':
    print get_substring('abcdaedddddfd')
    print get_substring('abcabcbb')
    print get_substring('abbbbbbbbbba')
