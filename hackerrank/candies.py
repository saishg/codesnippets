
STUDENTS = []
CANDIES = []


def compare_with_prev(i):
    if i == 0:
        return True
    elif STUDENTS[i] > STUDENTS[i - 1]:
        CANDIES[i] = max(CANDIES[i], CANDIES[i - 1] + 1)
        return True
    elif STUDENTS[i] < STUDENTS[i - 1]:
        return CANDIES[i] < CANDIES[i - 1]
    else:
        return True
        
def compare_with_next(i):
    if i == len(STUDENTS) - 1:
        return True
    elif STUDENTS[i] > STUDENTS[i + 1]:
        CANDIES[i] = max(CANDIES[i], CANDIES[i + 1] + 1)
        return True
    else:
        return True

def recurse(i=0):
    if i == len(STUDENTS):
        return True

    if compare_with_prev(i) and compare_with_next(i):
        recurse(i+1)
    else:
        return False


def read_input():
    num_candies = int(raw_input())
    for i in range(num_candies):
        STUDENTS.append(int(raw_input()))
        CANDIES.append(1)

if __name__ == '__main__':
    read_input()
    recurse()
#    print STUDENTS
#    print CANDIES
    print sum(CANDIES)
