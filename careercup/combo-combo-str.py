# https://www.careercup.com/question?id=5634222671790080

MAPPING = {
    '1' : ['A', 'B', 'C'],
    '2' : ['D', 'E'],
    '12': ['X'],
    '3' : ['P', 'Q'],
}

RESULT_LIST = []

def value_combinations(key_list, result=''):
    if not key_list:
        RESULT_LIST.append(result)
        return

    key = key_list[0]
    key_list = key_list[1:]

    for value in MAPPING[key]:
        value_combinations(key_list, result+value)


def key_combinations(string, key_list=()):
    if string == '':
       value_combinations(key_list)
       return

    for key in MAPPING:
       if string.startswith(key):
           key_combinations(string[len(key):], key_list + (key,))



if __name__ == '__main__':
    key_combinations('123')
    print RESULT_LIST
