# https://leetcode.com/problems/integer-to-roman/description/
# Given an integer, convert it to a roman numeral.
# Input is guaranteed to be within the range from 1 to 3999.

def convert(num):
    if num == 0:
        return ''
    if num < 4:
        return 'I' + convert(num - 1)
    elif num == 4:
        return 'IV'
    elif num < 9:
        return 'V' + convert(num - 5)
    elif num == 9:
        return 'IX'
    elif num < 40:
        return 'X' + convert(num - 10)
    elif num < 50:
        return 'XL' + convert(num - 40)
    elif num < 90:
        return 'L' + convert(num - 50)
    elif num < 100:
        return 'XC' + convert(num - 90)
    elif num < 400:
        return 'C' + convert(num - 100)
    elif num < 450:
        return 'CD' + convert(num - 400)
    elif num < 490:
        return 'CDL' + convert(num - 450)
    elif num < 500:
        return 'CD' + convert(num - 400)
    elif num < 900:
        return 'D' + convert(num - 500)
    elif num < 1000:
        return 'CM' + convert(num - 900)
    else:
        return 'M' + convert(num - 1000)


print convert(490)
print convert(990)
print convert(1001)
