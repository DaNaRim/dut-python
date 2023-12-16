# Write a Python function (task1), where create a tuple containing two numbers and then return their sum.
def task1(tuple1):
    return sum(tuple1)


# Write a Python function (task2), where Create a tuple that contains several numbers and strings, and return its length.
def task2(tuple1):
    return len(tuple1)


# Write a Python function (task3), where Create a tuple from a list of numbers, sort it in descending order, and return the first element.
def task3(tuple1):
    return sorted(tuple1, reverse=True)[0]


# Write a Python function (task4), where Create a tuple that contains a dictionary, and return the value of the key "name".
def task4(tuple1):
    return tuple1[0]['name']


# Write a Python function (task5), that takes a tuple from a list of tuples, sort it by ascending length of the
# first element of each tuple, and return the last element of the last tuple.
def task5(tuple1):
    tuple1 = sorted(tuple1, key=lambda x: len(x[0]))
    return tuple1[-1][-1]


# Write a Python function (task6), where Create a tuple that contains several lists, filter out all odd numbers, and return their product.
def task6(tuple1):
    all_numbers = [number
                   for sublist in tuple1
                   for number in sublist
                   if isinstance(number, int) and number % 2 == 0
                   ]
    product = 1
    for number in all_numbers:
        product *= number
    return product


# Write a Python function (task7), where Create a tuple that contains several tuples with two numbers each, and return the sum of all second elements of each tuple.
def task7(tuple1):
    return sum([i[1] for i in tuple1])
