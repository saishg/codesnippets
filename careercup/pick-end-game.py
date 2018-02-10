# https://www.careercup.com/question?id=8758252

class Player:
    def __init__(self, name, nums=()):
        self.name = name
        self.nums = nums
        self.total = sum(self.nums)

    def add(self, num):
        return Player(self.name, self.nums + (num,))

    def __repr__(self):
        return "[Player-{} {} Sum:{}]".format(self.name, self.nums, self.total)


def play2(numbers, player1, player2):
    if not numbers:
        print "tail", player1, player2
        return player1, player2

    o1player1, o1player2 = play1(numbers[1:], player1, player2.add(numbers[0]))
    o2player1, o2player2 = play1(numbers[:-1], player1, player2.add(numbers[-1]))
    if o1player2.total > o2player2.total:
        return o1player1, o1player2
    else:
        return o2player1, o2player2


def play1(numbers, player1, player2):
    if not numbers:
        print "tail", player1, player2
        return player1, player2

    o1player1, o1player2 = play2(numbers[1:], player1.add(numbers[0]), player2)
    o2player1, o2player2 = play2(numbers[:-1], player1.add(numbers[-1],), player2)
    if o1player1.total > o2player1.total:
        return o1player1, o1player2
    else:
        return o2player1, o2player2


if __name__ == '__main__':
#   Player("One").add(1).display()

#    print play1((12, 24, 10, 5), Player("One"), Player("Two"))
    print play1((1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3), Player("One"), Player("Two"))
