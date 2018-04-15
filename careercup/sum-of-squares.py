# https://www.careercup.com/question?id=5666912267665408


def sum_of_squares(number):
    SQUARES = set()

    i = 1
    while i * i < number:
        square = i * i
        if (number - square) in SQUARES:
            return square, number - square
        SQUARES.add(square)
        i += 1
    return None, None



if __name__ == '__main__':
    print sum_of_squares(17)
    print sum_of_squares(25)
