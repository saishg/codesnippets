import random

def get_digits(start, number):
    return map(lambda x: chr(ord(start) + x), range(number))

LOWER_CASE = get_digits('a', 26)
UPPER_CASE = get_digits('A', 26)
NUMBERS = get_digits('0', 10)

DIGITS = LOWER_CASE + UPPER_CASE + NUMBERS
DIGITS_MAPS = dict((digit, index) for index, digit in enumerate(DIGITS))
LENGTH = len(DIGITS)


def convert_to_tinyurl(number):
    tinyurl = ''
    while number > 0:
        tinyurl = DIGITS[number % LENGTH] + tinyurl
        number = number / LENGTH
    return tinyurl

def convert_to_number(tinyurl):
    number = 0
    for index, digit in enumerate(reversed(tinyurl)):
#        print digit, DIGITS_MAPS[digit], DIGITS_MAPS[digit] * (LENGTH ** index)
        number += DIGITS_MAPS[digit] * (LENGTH ** index)
    return number


if __name__ == '__main__':
    VALUE = random.randrange(10 ** 6, 10 ** 15)
    print VALUE, convert_to_tinyurl(VALUE)
    print VALUE == convert_to_number(convert_to_tinyurl(VALUE))


