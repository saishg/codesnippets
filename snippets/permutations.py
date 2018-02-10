"""
Generate N-sized permutations of characters from the CHARSET
For example, with "abc" as the CHARSET and N = 2,
the following are the permutations:
1. ab
2. ac
3. ba
4. bc
5. ca
6. cb

The order of characters does not matter in a permutation, so
ab is not the same as ba. Both are generated, but in alphabetical order
"""

N = 3
CHARSET = "abcd"

def permutation(count, string=""):
    if count == 0:
        print string
        return

    for letter in CHARSET:
        if letter not in string:
            permutation(count - 1, string + letter)

if __name__ == '__main__':
    permutation(N)


