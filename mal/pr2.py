import os

text = '''Hello!
I am a text file. And I had been written with a Python script
before you opened me, so look up the docs and try to delete
me using Python, too.'''


def read_file(fname):
    """
    1-2. Функція для зчитування файлу fname та виведення його вмісту на екран
    """
    file = open(fname, 'r')  # відкриття файлу для зчитування
    print('File ' + fname + ':')  # виведення назви файлу
    # Зчитування вмісту файлу по рядкам
    for line in file:
        print(line, end='')
    file.close()  # Закриття файлу


def write_text_to_file(filename, text):
    """Функція для запису у файл filename рядка text"""
    f = open(filename, "w")  # відкриття файла для запису
    f.write(text)  # Запис рядка text у файл
    f.close()  # Закриття файлу


if __name__ == '__main__':
    read_file('data/file.txt')
    read_file(os.path.join('data', 'file.txt'))
    write_text_to_file(os.path.join('data', 'example02.txt'), text)

    # 4
    filename = os.path.join('data', 'file.txt')  # побудова імені файлу
    # Оператор with закриє файл по закінченню виконання
    # операторів усередині нього або виникненні виключення
    with open(filename) as file:
        print(file.read())

    # 5
    filename = os.path.join('data', 'example07.txt')
    # Зчитування файла
    with open(filename, 'r') as file:
        lines = file.readlines()
    # Модифікація даних
    lines.insert(2, 'inserted line\n')
    # Перезапис файла
    with open(filename, 'w') as file:
        file.writelines(lines)
