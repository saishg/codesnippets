# https://www.careercup.com/question?id=8758252

def playOpp(numbers, my_num, opp_num):
    if not numbers:
        print my_num, sum(my_num[1:]), opp_num, sum(opp_num[1:])
        return sum(opp_num[1:])

    value1 = play(numbers[1:], my_num, opp_num+(numbers[0],))
    value2 = 0
    if len(numbers) > 1:
        value2 = play(numbers[:-1], my_num, opp_num+(numbers[-1],))
    return max(value1, value2)


def play(numbers, my_num=('A',), opp_num=('B',)):
    if not numbers:
        print my_num, sum(my_num[1:]), opp_num, sum(opp_num[1:])
        return

    value1 = playOpp(numbers[1:], my_num+(numbers[0],), opp_num)
    value2 = 0
    if len(numbers) > 1:
        value2 = playOpp(numbers[:-1], my_num+(numbers[-1],), opp_num)
    return max(value1, value2)



if __name__ == '__main__':
    play((12, 24, 10, 5))
