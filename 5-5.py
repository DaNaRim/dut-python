import array
import binascii


# Create a def(task1) which merge two Python dictionaries.
def task1(dict1, dict2):
    return {**dict1, **dict2}


# Write a def(task2) that reads a string and interprets it as an array of machine values.
# Sample Output:
# array1: array('i', [7, 8, 9, 10])
# Bytes: b'0700000008000000090000000a000000'
# array2: array('i', [7, 8, 9, 10])
def task2():
    array1 = array.array('i', [7, 8, 9, 10])
    as_bytes = array1.tobytes()
    array2 = array.array('i')
    array2.frombytes(as_bytes)
    return array1, binascii.hexlify(as_bytes), array2


# Write a def(task3) that removes all duplicate elements from an array and returns a new array.
# Sample Output:
# Original array: 1 3 5 1 3 7 9
# After removing duplicate elements from the said array: 1 3 5 7 9
# Original array: 2 4 2 6 4 8
# After removing duplicate elements from the said array: 2 4 6 8
def task3(list0):
    res = []
    for i in list0:
        if i not in res:
            res.append(i)
    return res


# Write a def(task4) to find the missing number in a given array of numbers between 10 and 20.
# Sample Output:
# Original array: 10 11 12 13 14 16 17 18 19 20
# Missing number in the said array (10-20): 15
# Original array: 10 11 12 13 14 15 16 17 18 19
# Missing number in the said array (10-20): 20
def task4(list0):
    full_array = set(range(10, 21))
    return list(full_array - set(list0))[0]


# Write a def(task5) to returns all distinct values in a dictionary. Output count of unique values.
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
def task5(list0):
    return len(set([list(i.values())[0] for i in list0]))


# Write a def(task6) function that returns the number of all possible combinations of letters from the dictionaries it receives.
# Sample data : {'a':5,'b':7} , {'v':1,'n':6}
# Expected Output: 4
def task6(dict1, dict2):
    return len(dict1) * len(dict2)


# Write a def(task7) function that returns the list of the largest 3 values of the corresponding keys in the dictionary. The keys will be int only.
# Sample data : {3:2 , 4:7, 0:2 , 12:0}
# Expected Output: [3,4,0,12]
def task7(dict0):
    return sorted(dict0.keys())[-3:]


# Write a def(task8) to combine values in a list of dictionaries.
# Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# Expected Output:{'item1': 1150, 'item2': 300}
def task8(list0):
    result_dict = {}
    for item in list0:
        if item['item'] not in result_dict:
            result_dict[item['item']] = item['amount']
        else:
            result_dict[item['item']] += item['amount']
    return dict(result_dict)


# if __name__ == '__main__':
#     print(task1({1: 10, 2: 20}, {3: 30, 4: 40}))
#     task2('Hello world!')
#     print(task3([1, 3, 5, 1, 3, 7, 9]))
#     print(task4([10, 11, 12, 13, 14, 16, 17, 18, 19, 20]))
#     print(task5([{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]))
#     print(task6({'a': 5, 'b': 7}, {'v': 1, 'n': 6}))
#     print(task7({3: 2, 4: 7, 0: 2, 12: 0}))
#     print(task8([{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]))
