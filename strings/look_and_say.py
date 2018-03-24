# Implement a function that outputs the Look and Say sequence:
# 1 
# 11
# 21
# 1211
# 111221
# 312211
# 13112221
# 1113213211
# 31131211131221
# 13211311123113112211


def look_and_say(input_str=None):
    if input_str is None:
        return '1'

    output_str = ''
    count = 0
    last_char = ''

    for char in input_str:
        if char != last_char:
            if count:
                output_str += str(count) + last_char
            last_char = char
            count = 1
        else:
            count += 1

    if count:
        output_str += str(count) + last_char
    return output_str

if __name__ == '__main__':
    result = look_and_say()

    for i in range(10):
        print result
        result = look_and_say(result)


