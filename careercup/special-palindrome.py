# https://www.careercup.com/question?id=4741489669177344


def is_special_palindrom(string):
    string = string.lower()
    start_index = 0
    end_index = len(string) - 1

    while start_index < end_index:
        while not string[start_index].isalpha() and start_index < end_index:
            start_index += 1

        while not string[end_index].isalpha() and start_index < end_index:
            end_index -= 1

        if string[start_index] != string[end_index]:
            return False
        else:
            start_index += 1
            end_index -= 1
    return True

if __name__ == '__main__':
    print is_special_palindrom('L*&EVe)))l')
    print is_special_palindrom('-^$&$&')
    print is_special_palindrom('b+++++++A++++++++')
