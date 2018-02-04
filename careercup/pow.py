#https://www.careercup.com/question?id=5733237978562560

count = 0


def power(number, exp):
    global count
    count += 1
    if exp == 1:
        return number

    half_power = power(number, exp/2)

    if exp % 2 == 1:
        return number * half_power * half_power
    else:
        return half_power * half_power



if __name__ == '__main__':
    print power(2, 10000)
    print count
