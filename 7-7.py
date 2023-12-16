# Write a Python function (task1) that takes the user's age (not from INPUT, but as an argument) and returns it.
# If the user enters a non-numeric value, the program should return an error message.
def task1(age):
    try:
        return int(age)
    except ValueError:
        return 'Error'


# Write a Python function (task2) that takes two numbers (not from INPUT, but as an argument) and returns their product.
# If the user enters a non-numeric value, the program should return an error message.
def task2(num1, num2):
    try:
        return int(num1) * int(num2)
    except ValueError:
        return 'Error'

# Write a Python function (task3) that takes a string(not from INPUT, but as an argument) and returns its length.
# If the user does not enter a string, the program should return an error message.
def task3(string):
    try:
        return len(string)
    except TypeError:
        return 'Error'

# Write a Python function (task4) that takes a list of integers (not from INPUT, but as an argument) returns their sum.
# If a value that is not an integer, the program should return None.
def task4(list):
    try:
        return sum(list)
    except TypeError:
        return None


# Write a Python function (task5) that takes a list of tuples, where each tuple contains a student's name and grade, and returns a list of tuples where the first element is the student's average grade and the second element is the student's name. If an error occurs while processing the list, the function should return the string "List processing error!".
# Example: data = [('John', (2,2,3)), ('Jane', (4,3,5)), ('Jack', (5,4,4))] print(process_data(data)) # [(3.33, 'John'), (4.33, 'Jane'), (5.0, 'Jack')]
def task5(list):
    try:
        return [(sum(i[1]) / len(i[1]), i[0]) for i in list]
    except TypeError:
        return 'List processing error!'
