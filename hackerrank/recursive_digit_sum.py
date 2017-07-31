"""
https://www.hackerrank.com/challenges/recursive-digit-sum
"""

CACHE = {}

def num_digits(number):
    digits = 0
    while number:
        number = number / 10
        digits += 1
    return digits

def super_digit(number):
    if number < 10:
        return number

    if number not in CACHE:
        sum_of_digits = 0
        while number:
            sum_of_digits += number % 10
            number = number / 10
            if sum_of_digits > 10:
                sum_of_digits = super_digit(sum_of_digits)
        CACHE[number] = super_digit(sum_of_digits)

    return CACHE[number]

def super_digit_string(number):
    if len(number) <= 2:
        return super_digit(int(number))

    half_len = len(number) / 2
    return super_digit_string(number[:half_len]) + super_digit_string(number[half_len:])

def read_input():
    n, k = raw_input().split()
    return super_digit(super_digit_string(k) * super_digit_string(n))


if __name__ == '__main__':
    print read_input()
#     print super_digit_string('148')
