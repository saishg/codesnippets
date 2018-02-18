# https://leetcode.com/problems/regular-expression-matching/description/
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
#
# The matching should cover the entire input string (not partial).
#
# Some examples:
# isMatch("aa","a") -> false
# isMatch("aa","aa") -> true
# isMatch("aaa","aa") -> false
# isMatch("aa", "a*") -> true
# isMatch("aa", ".*") -> true
# isMatch("ab", ".*") -> true
# isMatch("aab", "c*a*b") -> true

CACHE = {}

def isMatch(string, pattern):
        if (string, pattern) in CACHE:
            return CACHE[(string, pattern)]

        if string == pattern:
            return True

        if pattern.startswith('*'):
            return False

        if '*' not in pattern and '.' not in pattern and string != pattern:
            return False

        if len(string) and (string[0] == pattern[0] or pattern[0] == '.'):
            if isMatch(string[1:], pattern[1:]):
                CACHE[(string, pattern)] = True
                return True
            if len(pattern) > 1 and pattern[1] == '*':
                if isMatch(string[1:], pattern):
                    CACHE[(string, pattern)] = True
                    return True
                if isMatch(string[1:], pattern[2:]):
                    CACHE[(string, pattern)] = True
                    return True

        if len(pattern) > 1 and pattern[1] == '*':
            if isMatch(string, pattern[2:]):
                CACHE[(string, pattern)] = True
                return True

        CACHE[(string, pattern)] = False
        return False


if __name__ == '__main__':
    print "a, aa -> False", isMatch('a', 'aa')
    print "aa, aa -> True", isMatch('aa', 'aa')
    print "aaa, aa -> False", isMatch('aaa', 'aa')
    print "aaa, a* -> True", isMatch('aaa', 'a*')
    print "aaa, .* -> True", isMatch('aaa', '.*')
    print "ab, .* -> True", isMatch('ab', '.*')
    print "aab, c*a*b* -> True", isMatch('aab', 'c*a*b*')
    print "abcd, d* -> False", isMatch('abcd', 'd*')
    print "abc, a.c -> True", isMatch('abc', 'a.c')
    print "aaa, ab*a -> False", isMatch('aaa', 'ab*a')
    print "a, ab* -> True", isMatch('a', 'ab*')
    print "aaaaaaaaab, a*a*a*a*a*a*a*a*a*a*c -> False", isMatch('aaaaaaaaab', 'a*a*a*a*a*a*a*a*a*a*c') # slow !
    print "aaaaaaaaab, a*.*a*.*a*.*a*.*a*.*c -> False", isMatch('aaaaaaaaab', 'a*.*a*.*a*.*a*.*a*.*a*.*a*.*c') # slow !

