# https://www.careercup.com/question?id=5657872336683008

import random

MAPPING = {}
NUM_DIGITS = 4
LOWER_LIMIT = 10 ** (NUM_DIGITS - 1)
UPPER_LIMIT = 10 ** (NUM_DIGITS)

def next_valid_number(number):
    number +=1 
    digits = []
    while number > 0:
        digits.insert(0, number % 10)
        number = number / 10

    previous = -1
    new_number = 0
    for digit in digits:
        if digit == previous:
            digit += 1
        previous = digit
        new_number = new_number * 10 + digit

    return new_number


def generate_mapping():
    number = LOWER_LIMIT
    mapped_number = LOWER_LIMIT
    while True:
        mapped_number = next_valid_number(mapped_number)
        MAPPING[number] = mapped_number
        number += 1
        if mapped_number > UPPER_LIMIT:
            return number

def get_random():
    return MAPPING[random.randrange(LOWER_LIMIT, UPPER_LIMIT)]


if __name__ == '__main__':
    UPPER_LIMIT = generate_mapping()
    for i in range(100):
        print get_random()

