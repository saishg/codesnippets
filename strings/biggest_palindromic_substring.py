

INPUT = "sanfranciscoxxyxxabcdefghijkllkjihgfedcblasvegas"

def find_odd_palindrome(index):
    for i in range(min(index, len(INPUT)-index)):
        if INPUT[index-i] != INPUT[index+i]:
            break
    else:
        return ''
    return INPUT[index-i+1 : index+i]

def find_even_palindrome(index):
    if index != len(INPUT) - 1:
        if INPUT[index] == INPUT[index + 1]:
            for i in range(min(index, len(INPUT)-index-1)):
                if index - i < 0 or index + i + 1 >= len(INPUT):
                    break
                if INPUT[index-i] != INPUT[index+i+1]:
                    break
            else:
                 return ''
            return INPUT[index-i+1 : index+i+1]
    return ''

for i in xrange(len(INPUT)):
    palindrome = find_odd_palindrome(i)
    if len(palindrome) > 1:
        print palindrome
    palindrome = find_even_palindrome(i)
    if len(palindrome) > 2:
        print palindrome
