# https://www.careercup.com/question?id=5093369735806976
# ABC -> 1BC, 2C, 3, A1C, AB1, A2 (11C is invalid as two numbers cannot occur side-by-side)


def abbreviate(string, abbr=''):
    if not string:
        print abbr
        return

    previous = ''
    if abbr:
        previous = abbr[-1]

    if not previous.isdigit():
        for index in range(1, len(string) + 1):
            abbreviate(string[index:], abbr + str(index))

    abbreviate(string[1:], abbr + string[0])




if __name__ == '__main__':
    abbreviate('ABC')


