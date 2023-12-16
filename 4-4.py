# Write a Python function (task1) to find the maximum of three numbers.
def task1(number1, number2, number3):
    return max(number1, number2, number3)


# Write a Python function (task2)  to sum all the numbers in a list.
def task2(list):
    return sum(list)


# Write a Python function (task3)  to multiply all the numbers in a list.
def task3(list):
    result = 1
    for i in list:
        result *= i
    return result


# Write a Python function (task4)  to reverse a string. Sample String : "1234abcd"
def task4(string):
    return string[::-1]


# Write a Python function (task5) to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def task5(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


# Write a Python function (task6)  to check whether a number falls within a given range.
def task6(number, start, end):
    return start <= number <= end


# Write a Python function (task7)  that accepts a string and counts the number of upper and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12
def task7(string):
    upper = 0
    lower = 0
    for i in string:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    return upper, lower


# Write a Python function (task8)  that takes a list and returns a new list with distinct elements from the first list. Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]
def task8(listArg):
    return list(set(listArg))


# Write a Python function (task9) to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]
def task9(list):
    return [i for i in list if i % 2 == 0]


# Write a Python function (task10)  that prints out the first n rows of Pascal's triangle.
def task10(n):
    result = []
    for i in range(n):
        if i == 0:
            result.append([1])
            continue
        result.append([])
        result[i].append(1)
        for j in range(1, i):
            result[i].append(result[i - 1][j - 1] + result[i - 1][j])
        if n != 0:
            result[i].append(1)
    return result


# if __name__ == '__main__':
#     print(task1(1, 2, 3))
#     print(task2([8, 2, 3, 0, 7]))
#     print(task3([8, 2, 3, -1, 7]))
#     print(task4('1234abcd'))
#     print(task5(5))
#     print(task6(5, 1, 10))
#     print(task7('The quick Brow Fox'))
#     print(task8([1, 2, 3, 3, 3, 3, 4, 5]))
#     print(task9([1, 2, 3, 4, 5, 6, 7, 8, 9]))
#     print(task10(5))
