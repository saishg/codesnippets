# https://leetcode.com/problems/word-ladder/description/

WORDMAP = {}
VISITED = set()

def wordStep(word1, word2):
    if word1 == word2:
        return False
    
    foundDiff = False
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            if foundDiff:
                return False
            else:
                foundDiff = True
    
    return True

def mapWords(word1, word2):
    if wordStep(word1, word2):
        WORDMAP[word1].add(word2)
        WORDMAP[word2].add(word1)

def findShortest(beginWord, endWord):
    FWD_BFS = [beginWord]
    REV_BFS = [endWord]
    FWD_DISTANCE = 1
    REV_DISTANCE = 0

    while FWD_BFS and REV_BFS:
        FWD_DISTANCE += 1
        for i in range(len(FWD_BFS)):
            word = FWD_BFS.pop(0)
            VISITED.add(word)
            for nextWord in WORDMAP[word]:
                if nextWord in REV_BFS:
                    return FWD_DISTANCE + REV_DISTANCE
                if nextWord not in VISITED:
                    FWD_BFS.append(nextWord)

        REV_DISTANCE += 1
        for i in range(len(REV_BFS)):
            word = REV_BFS.pop(0)
            VISITED.add(word)
            for nextWord in WORDMAP[word]:
                if nextWord in FWD_BFS:
                    return FWD_DISTANCE + REV_DISTANCE
                if nextWord not in VISITED:
                    REV_BFS.append(nextWord)
    return -1
    
    
def ladderLength(beginWord, endWord, wordList):
    """
    :type beginWord: str
    :type endWord: str
    :type wordList: List[str]
    :rtype: int
    """
    global WORDMAP
    WORDMAP = {}
    wordList.append(beginWord)
    wordList.append(endWord)
    
    for word in wordList:
        WORDMAP[word] = set()

    for word in wordList:
        for mappedWord in WORDMAP:
            mapWords(mappedWord, word)
            
    return findShortest(beginWord, endWord)
    
if __name__ == '__main__':
    wordList = ["hot","dot","dog","lot","log","cog"]
    print ladderLength("hit", "cog", wordList)
#    print ladderLength("hot", "dog", wordList)
