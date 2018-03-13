# https://www.careercup.com/question?id=5158272756613120
# Find the longest substring with k distinct characters


def get_longest_substring(string, k):
    char_dict = {}
    distinct_char = 0
    start_index = 0
    end_index = 0
    longest_substring = ''

    for end_index in range(len(string)):
        end_char = string[end_index]
        if char_dict.get(end_char, 0) == 0:
            char_dict[end_char] = 1
            distinct_char += 1
            while distinct_char > k:
                start_char = string[start_index]
                start_index += 1
                char_dict[start_char] -= 1
                if char_dict[start_char] == 0:
#                    print start_char, "removed"
                    distinct_char -= 1
        else:
            char_dict[end_char] += 1

#        print string[start_index:end_index+1], distinct_char
        new_substring = string[start_index:end_index+1]
        if len(new_substring) > len(longest_substring):
            longest_substring = new_substring

    return longest_substring


    



if __name__ == '__main__':
#    print get_longest_substring("aaaaaaaaaaabbbbbbbbbbb", 2)
#    print get_longest_substring("asdfrtttt", 3)
    print get_longest_substring("asdaffffffffffffaratttt", 3)
