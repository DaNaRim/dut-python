def task1(number1, znak, number2):
    if znak == '>':
        return number1 > number2
    elif znak == '<':
        return number1 < number2
    elif znak == '>=':
        return number1 >= number2
    elif znak == '<=':
        return number1 <= number2
    elif znak == '==':
        return number1 == number2
    elif znak == '!=':
        return number1 != number2
    else:
        return 'Error'


def task2(text: str, number: int):
    if len(text) > number:
        return len(text)
    else:
        return number


def task3(number1, number2, number3):
    return number1 == number2 == number3



