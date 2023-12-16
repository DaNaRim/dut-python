def task1(string):
    return len(string)


def task2(number1, znak, number2):
    if znak == '+':
        return number1 + number2
    elif znak == '-':
        return number1 - number2
    elif znak == '/':
        return number1 / number2
    elif znak == '//':
        return number1 // number2
    elif znak == '**':
        return number1 ** number2
    elif znak == '*':
        return number1 * number2
    else:
        return 'Error'


def task3(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max


print(task1('Hello world!'))
print(task2(1, '+', 2))
print(task3([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
