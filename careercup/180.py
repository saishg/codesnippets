# https://www.careercup.com/question?id=5804910846148608
# print all the numbers with the number of specified digits that look the same upside down


NUM_LIST = ["0", "1", "6", "8", "9"]
UPSIDE_DOWN = {
    "0" : "0",
    "1" : "1",
    "6" : "9",
    "8" : "8",
    "9" : "6"
}

def get180(digits):
    if digits == 0:
        return ['']

    if digits == 1:
        return filter(lambda x: UPSIDE_DOWN[x] == x, NUM_LIST)

    middle_list = get180(digits - 2)
    result_list = []
    for number in NUM_LIST:
        for middle in middle_list:
            result_list.append(number + middle + UPSIDE_DOWN[number])
    return result_list


if __name__ == '__main__':
    for i in range(5):
        print get180(i)



