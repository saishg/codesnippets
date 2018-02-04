#https://leetcode.com/problems/palindrome-number/description/

def isPalindrome(x):
     """
     :type x: int
     :rtype: bool
     """
     print "Testing for ", x
     y = 0
     while x > y:
         y = y * 10 + x % 10
         x = x / 10
     print x, "==", y
     print x, "==", y/10
     return False


def reverse_int(x):
    z = x
    y = 0
    while x > 0:
        y *= 10
        y += x % 10
        print x, y
        x /= 10
        print x, y
    return y
        

print isPalindrome(1210)
#x = 10001
print x == reverse_int(x)
