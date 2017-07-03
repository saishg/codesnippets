

INPUT = "sanfranciscoxxyxxabcdefghijkllkjihgfedcblasvegas"
LENGTH = len(INPUT)

def check_palindrome(index1, index2):
    while INPUT[index1] == INPUT[index2]:
        index1 -= 1
        index2 += 1
    palindrome = INPUT[index1+1:index2]
    if len(palindrome) > 1:
        print palindrome

for i in xrange(LENGTH):
    try:
        check_palindrome(i, i)
        check_palindrome(i, i + 1)
    except IndexError:
        pass
