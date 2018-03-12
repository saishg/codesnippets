# https://www.careercup.com/question?id=5699926989209600
# \b = backspace, \c = capslock
# Python and Java do not have immutable strings, solution is more apt for C


def process(string):
    string = list(string)
    write_index = 0
    special = False
    upper = False

    for read_index in range(len(string)):
        if special is True:
            special = False
            if string[read_index] == 'b':
                write_index -= 1
            elif string[read_index] == 'c':
                upper = True
        else:
            if string[read_index] == '\\':
                special = True
            else:
                if upper:
                    upper = False
                    string[write_index] = string[read_index].upper()
                else:
                    string[write_index] = string[read_index]
                write_index += 1

    return ''.join(string[:write_index])



def compare(string1, string2):
    return process(string1) == process(string2)


if __name__ == '__main__':
    print compare(r'abcd\b\bef\cG', 'abefG')
   
