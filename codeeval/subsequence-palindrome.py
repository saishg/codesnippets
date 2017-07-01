

class Palindrome:

    def __init__(self, word, start):
        self.word = word
        self.start = start
        self.end = start + len(word)




def find_palindromes(word, start=0):
    c = word[0]
    if word.rfind(c) != 0:
        find_palindrome(word[1:], start+1)
    else
        find_palindrom(word[1:], start+1)



