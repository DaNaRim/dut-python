# Напишіть функцію «task1» яка приймає значення «my_list». Створіть список «my_list» з чисел (10, 20, 30, 40, 50, 60). Додайте у створений список число -5 розмістивши його на другу позицію у списку.
# Знайдіть мінімальний «min_element» та максимальний «max_element» елемент списку.
# До отриманого списку додайте елемент у вигляді списку [1,2,3] на третю позицію.
# В кінці списку додайте новий елемент в якому відобразіть ваше прізвище та ім’я.
# Визначте кількість елементів списку «list_length».
# Результати виведіть на екран.
# Поверніть значення «my_list», «min_element», «max_element», «list_length», (в такому порядку).
def task1(my_list):
    my_list.insert(1, -5)
    min_element = min(my_list)
    max_element = max(my_list)
    my_list.insert(2, [1, 2, 3])
    my_list.append(-1, 'Horshevikov Nazar')
    list_length = len(my_list)
    return my_list, min_element, max_element, list_length


# На складі зберігається 20 видів товарів. До списку «A» занесено назву товару, до списку «B» занесено кількість одиниць кожного товару, до списку «C» - ціни цих товарів.
# Обчисліть загальну вартість «total_cost» товарів на складі та середню ціну «average_price». Визначте якого товару найбільше «most_stocked_item» на складі.
# Реалізуйте рішення задачі через функцію «task2» яка приймає значення «A», «B», «C», та на виході повертає значення «total_cost», «average_price», «most_stocked_item» (в такому порядку).
def task2(A, B, C):
    total_cost = sum([quantity * price for quantity, price in zip(B, C)])
    average_price = total_cost / sum(B)
    most_stocked_item = A[B.index(max(B))]
    return total_cost, average_price, most_stocked_item


# Напишіть функцію «task3». Сформуйте список із 50 елементів що знаходяться в діапазоні від – 25 до 25. Всі додатні елементи записати у список «А1», від’ємні в «А2». Отримані списки вивести на екран та повернути значення «А1» та «А2» (в такому порядку).
def task3():
    A1 = []
    A2 = []
    for i in range(-25, 26):
        if i > 0:
            A1.append(i)
        elif i < 0:
            A2.append(i)
    return A1, A2


# Створіть текстову змінну з таким текстом
# “Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.Massa eget egestas purus viverra accumsan.Eu volutpat odio facilisis mauris sit amet.In metus vulputate eu scelerisque felis imperdiet proin.Velit euismod in pellentesque massa placerat duis ultricies lacus.”.
# Підрахуйте кількість символів “а” у тексті.
# Виведіть на екран створений рядок розміщуючи по одному реченню у екранному рядку.
# Повернути кількість символів “а” у тексті.
def task4(text):
    return text.count('a')


# Напишіть функцію «task5». Створіть текстову змінну str в яку запишіть “DUT is GOOD”. З створеного рядка виведіть на екран тільки “DUT”. В рядку str замініть “GOOD” на “NICE” і виведіть змінений рядок «modified_str» на екран.
# Виконайте розподіл рядка по пробілу та обчисліть кількість «word_count» слів у вашому рядку.
# Повернути значення «modified_str», «word_count» (в такому порядку)
def task5(str):
    modified_str = str.replace('GOOD', 'NICE')
    word_count = len(str.split())
    return modified_str, word_count


# Напишіть функцію «task6» на мові Python, яка підсумовує всі елементи списку від 1 до 5 і повертає значення «total_sum».
def task6(list0):
    return sum(list0)


# Напишіть функцію «task7», яка приймає значення «my_list» знайде у ньому числа, що діляться на 7 і кратні 5, записує
# їх у масив «result» і повертає значення «result».
def task7(my_list):
    result = []
    for i in my_list:
        if i % 7 == 0 and i % 5 == 0:
            result.append(i)
    return result
