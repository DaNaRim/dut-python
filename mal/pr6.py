# 1 A
s1 = "Рядок 1"
s2 = 'Рядок 2'
print(s1, s2)
# формування рядка з іншого значення
s3 = str(8)
print(s3)
# рядки, які складаються з багатьох рядків
s4 = """ Lesson2. Variables and Data Types
Some data types explained in this lesson:
- int, - bool, - float, - complex, - str """
print(s4)
# символ \ використовують, щоб продовжити рядок
# або будь-який вираз в Python з наступного рядка кода
s5 = "started\
continued"
print(s5)

# 1 Б
string = "a string"  # Створення рядка
# Виведення окремих символів рядка
print(string[0])  # 'a'
print(string[2])  # 's'
print(string[-1])  # 'g'

# 1 В
string = "a string"  # Створення рядка
# Виведення зрізів (групи символів) рядка
print(string[2:5])  # str
print(string[:5])  # a str
print(string[2:])  # string
print(string[::2])  # asrn
# Отримання окремих елементів рядка та їх конкатенація
print(string[2] + string[-3:])  # sing

# 1 Г
string = input('Введіть рядок: ')  # Введення рядка
# Перевірка, чи є в даному рядку символ «q»
if 'q' in string:
    print('В цьому рядку є символ "q"')
else:
    print('В цьому рядку немає символу "q"')

# 1 Д
string = input('Введіть рядок: ')  # Введення рядка
# Виведення довжини рядка
print('Довжина цього рядка:', len(string))

# 2
str1 = 'hel'
str2 = 'lo'
result = str1 + str2  # конкатенація рядків
print(result)
# форматування рядків
a = 48
b = 73
message1 = '%d + %d = %d' % (a, b, a + b)
print(message1)
message2 = '{} - {} = {}'.format(a, b, a - b)
print(message2)
# індексація рядків
s = 'Hello, World!'
print(s[0])  # індексація розпочинається з нуля
print(s[4])  # четвертий (п‘ятий реально) елемент (символ)
print(s[-1])  # від‘ємні числа – індексація розпочинається з кінця
print(s[2:7])
# - символи з 2 (включно) по 7 (не включно)
print(s[2:7:2])  # теж саме, але з кроком два

# 3
try:
    N = int(input('Введіть N = '))
except Exception:
    print('Введіть число!!!')
else:
    M = N
    pp = ''
    while M != 0:
        i = M
    L = []
    while i != 0:
        if i <= M:
            L.append(str(i))
    i -= 1
    a = list(L)
    pp = ''.join(a)
    print(pp)
    M = M - 1

# 4
a = input('Input first number: ')
if not a.isdigit():
    print("String value can not be entered")
    print("or number is negative, restart the program!")
    exit()
else:
    a = int(a)
if a == 0:
    print("The number can not be zero")
    input()
count = 0
ar = 0
while True:
    ar += a
    count += 1
    try:
        a = int(input('Input next number or Enter 0 to finish: '))
    except:
        print("String value can not be entered")
        print("or number is negative, restart the program!")
        exit()
    else:
        if a == 0:
            break

ar = ar / count
print("Average: ", ar)
