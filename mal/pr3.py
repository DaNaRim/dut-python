# 1
def hello_world():
    print('Hello, World!')


# Виклик функції
hello_world()


# 2
def print_numbers(limit):
    for i in range(limit):
        print(i)


# Виклик функції print_numbers, її формальний
# параметр limit замінюють фактичним параметром 10
print_numbers(10)

# 3
# Виклик функції з фактичним параметром n
# print_numbers
n = int(input('Введіть n: '))
print_numbers(n)


# 4
def print_numbers(limit):
    for i in range(limit):
        print(i)


def main():
    n = int(input('Введіть n: '))
    print_numbers(n)


# Виклик функції
main()


# 5
def add_numbers(a, b):
    return a + b  # вихід функції - сума параметрів


# Виклик функції
x = add_numbers(2, 3)
print(x)


# 6
def function(**kwargs):
    print(kwargs)


function(arg1='value1', arg2='value2')
# Можна розпакувати відображення
# в іменовані параметри при виклику функції
options = {
    'sep': ', ',
    'end': ';\n'
}
print('value1', 'value2', **options)


# 7
def hello(name='Alex'):
    print('Hello, ', name, '!', sep='')


# Виклик функції
hello('Python')
hello()
