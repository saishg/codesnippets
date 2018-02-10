# https://www.careercup.com/question?id=5963620481499136

def reverse_part(group, start, end):
    print start, end
    end -= 1
    while start < end:
        group[start], group[end] = group[end], group[start]
        start += 1
        end -= 1


def reverse_group(group, group_size):
    start = 0
    for end in range(group_size, len(group), group_size):
        reverse_part(group, start, end)
        start = end
    reverse_part(group, start, len(group))

if __name__ == '__main__':
    group = [1, 2, 3, 4, 5, 6, 7, 8]
#    reverse_part(group, 3, 4)
    reverse_group(group, 3)
    print group
