"""
Generate N-sized combinations of characters from the CHARSET
For example, with "abcd" as the CHARSET and N = 3,
    the following are the combinations:
    1. abc
    2. abd
    3. acd
    4. bcd

The order of characters does not matter in a combination, so
abc is same as cab, but only abc is generated because it
appears before cab alphabetically
"""

N = 3
CHARSET = "abcdefg"


def combinations(combstr="", charset=CHARSET):
    if len(combstr) == N:
        print combstr
        return

    for index, c in enumerate(charset):
        combinations(combstr + c, charset[index+1:])


if __name__ == '__main__':
    combinations()
