
STUDENTS = []
CANDIES = []

ONE_MORE_ROUND = True


def forward():
    for i in range(1, len(STUDENTS)):
        if STUDENTS[i] > STUDENTS[i - 1]:
            CANDIES[i] = max(CANDIES[i], CANDIES[i - 1] + 1)
        elif STUDENTS[i] < STUDENTS[i - 1]:
            CANDIES[i] = min(CANDIES[i], CANDIES[i - 1] - 1)
            if CANDIES[i] < 1:
                CANDIES[i] = 1
        if CANDIES[i] <

def reverse():
    for i in range(len(STUDENTS) - 2, -1, -1):
        if STUDENTS[i] > STUDENTS[i + 1]:
            CANDIES[i] = max(CANDIES[i], CANDIES[i + 1] + 1)
        elif STUDENTS[i] < STUDENTS[i - 1]:
            CANDIES[i] = min(CANDIES[i], CANDIES[i + 1] - 1)


def read_input():
    num_candies = int(raw_input())
    for i in range(num_candies):
        STUDENTS.append(int(raw_input()))
        CANDIES.append(1)

if __name__ == '__main__':
    read_input()
    forward()
    reverse()
    print STUDENTS
    print CANDIES
    print sum(CANDIES)
