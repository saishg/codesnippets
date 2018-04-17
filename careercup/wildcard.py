# https://www.careercup.com/question?id=5676259794223104

# c*w matches caw, caww, cauw, but not cw or car

def match(haystack, needle):
    if not haystack and not needle:
        return True
    elif not haystack or not needle:
        return False
    elif needle[0] == '*':
        return match(haystack[1:], needle) or \
               match(haystack[1:], needle[1:]) or \
               match(haystack, needle[1:])
    elif needle[0] == haystack[0]:
        return match(haystack[1:], needle[1:])
    else:
       return False


if __name__ == '__main__':
    print "car, car:", match('car', 'car')
    print "carrot, car:", match('carrot', 'car')
    print "carrot, c*t:", match('carrot', 'c*t')
    print "carrot, carr*t:", match('carrot', 'carr*t')
    print "carrot, carr*a:", match('carrot', 'carr*a')
    print "carrot, c*:", match('carrot', 'c*')
    print "cw, c*w:", match('cw', 'c*w')


