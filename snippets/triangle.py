# given two sides of a triangle, find the minimum
# and maximum length of the third side


def is_triangle(a, b, c):
    if a + b <= c:
        return False

    if b + c <= a:
        return False

    if a + c <= b:
        return False

    return True

def third_side_range(a, b):
    min_len = abs(a - b) - 1
    max_len = a + b
    return min_len, max_len

if __name__ == '__main__':
    print third_side_range(5, 7)
