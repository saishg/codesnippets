# https://leetcode.com/problems/valid-number/description/
# Validate if a given string is numeric.
# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true

def isNumber(s):
    """
    :type s: str
    :rtype: bool
    """
    s = s.strip()
    
    if ' ' in s:
        return False
    
    try:
        int(s)
        return True
    except ValueError:
        pass
    
    try:
        float(s)
        return True
    except ValueError:
        pass
    
    try:
        if 'e' in s:
            num, exp = s.split('e')
            int(num)
            int(exp)
            return True
    except ValueError:
        pass
    
    return False
            
   
print isNumber('1 ') 
print isNumber('3') 
print isNumber('+ 1') 
print isNumber('5e15') 
print isNumber('3.0') 
