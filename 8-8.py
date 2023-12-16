# 1.	Write a def(task1) that reads a text file and counts the number of occurrences of each word in the file. The program should return a list of the top 10 most common words and their frequencies.
import csv
import json


def task1(file):
    with open(file, 'r', encoding='utf-8') as file:
        text = file.read()
        words = text.split()
        words_dict = {}
        for word in words:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1
        words_dict = sorted(words_dict.items(), key=lambda x: x[1], reverse=True)
        return words_dict[:10]


# 2.	Write a def(task2) that reads a CSV file and calculates the total number of rows and columns in the file. The program should return the row and column counts.
def task2(file):
    with open(file, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)
        row_count = len(rows)
        column_count = len(rows[0]) if row_count > 0 else 0

    return row_count, column_count


# 3.	Write a def(task4) that reads a text file and replaces all occurrences of a specified word with a different word and returns a string of completed text.
def task4(file, word1, word2):
    with open(file, 'r') as file:
        text = file.read()
        return text.replace(word1, word2)


# 4.	Write a def(task6) that reads a JSON file and outputs a list of all the keys in the file.
def task6(file):
    import json
    with open(file, 'r') as file:
        text = file.read()
        return list(json.loads(text).keys())


# 5.	Write a def(task7) that reads a JSON file and calculates the total number of objects and arrays in the file.
# The program should output the object and array counts.
def task7(file):
    with open(file, 'r') as file:
        text = file.read()
        return text.count('{'), text.count('[')


# 6.	Write a def(task8) that reads a JSON file and filters its contents based on a specified key-value pair.
# The program should output the filtered data to a separate file.
def task8(file, key, value, output_file):
    with open(file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    filtered_data = [item for item in data if item.get(key) == value]

    with open(output_file, 'w', encoding='utf-8') as out_file:
        json.dump(filtered_data, out_file, ensure_ascii=False, indent=2)
