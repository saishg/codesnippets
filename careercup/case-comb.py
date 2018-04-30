# https://www.careercup.com/question?id=6255535581036544


def combinations(string, result='', index=0):
    if index >= len(string):
        print result
        return

    combinations(string, result + string[index].lower(), index+1)
    combinations(string, result + string[index].upper(), index+1)




if __name__ == '__main__':
    combinations('abc')
