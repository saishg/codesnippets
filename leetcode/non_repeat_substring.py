# https://leetcode.com/problems/longest-substring-without-repeating-characters/



def get_substring(string):
    longest_substring = ''
    start_index = 0
    end_index = 0
    CACHE = {}

    while end_index < len(string):
        end_char = string[end_index]
        if end_char in CACHE:
            start_index = max(start_index, CACHE[end_char] + 1)
        CACHE[end_char] = end_index
        end_index += 1
        if end_index - start_index > len(longest_substring):
            longest_substring = string[start_index : end_index]

    return longest_substring


if __name__ == '__main__':
#    print get_substring('abcdaedddddfd')
#    print get_substring('abcabcbb')
    print get_substring('abbbbbbbbbba')
