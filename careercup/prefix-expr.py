# https://www.careercup.com/question?id=5714599960641536


def evaluate(expression):
    expression = expression.strip()
    operand = expression[0]
    numbers = map(int, expression[1:].split())
    if operand == '*':
        result = 1
        for number in numbers:
            result *= number
        return result
    elif operand == '+':
        result = 0
        for number in numbers:
            result += number
        return result
    else:
        print "unknown operand:", operand
        return 0

def get_value(expression):
    start_index = 0
    while '(' in expression:
        start_index = expression.find('(', start_index) + 1
        bracket_count = 1
        for end_index in range(start_index, len(expression)):
            if expression[end_index] == '(':
                bracket_count += 1
            elif expression[end_index] == ')':
                bracket_count -= 1
                if bracket_count == 0:
                    break
        expression = ' '.join((expression[:start_index - 1],
                              str(get_value(expression[start_index:end_index])),
                              expression[end_index + 1:]))

    return evaluate(expression)

if __name__ == '__main__':
    print get_value('+ 7 (* 8 12 ) (* 2 (+ 9 4 ) 7 3 )')
    print get_value('+ 3 4 5')
