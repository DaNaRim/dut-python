import csv
import json
import os
import sys

import bs4
import requests

# 1
os.makedirs('headerRemoved', exist_ok=True)
# Цикл, що проходить кожний файл в поточній директорії
for csvFilename in os.listdir('../pr1-lb1'):
    if not csvFilename.endswith('.csv'):
        continue  # skip non-csv files
    print('Removing header from ' + csvFilename + '...')
    # Зчитує CSV-файл (пропускаючи перший рядок).
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue  # пропуска’ перший рядок
    csvRows.append(row)
    csvFileObj.close()
    # Записує дані в CSV-файл.
    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
        csvFileObj.close()

# 2 JSON
# Визначає кількість переданих аргументів.
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])
# Завантажує JSON дані з OpenWeatherMap.org
url ='http://api.openweathermap.org/data/2.5/weather?q=%s&cnt=3&appid=707d738c92ca835297381e002b64975a' % (location)
response = requests.get(url)
response.raise_for_status()
# Перетворює JSON дані в Python структуру.
weatherData = json.loads(response.text)
# Виводить дані про погоду.
w = weatherData['weather']
print('Current weather in %s:' % (location))
print(w[0]['main'], '-', w[0]['description'])
print()
print('Tomorrow:')
print(w[1]['main'], '-', w[1]['description'])
print()
print('Day after tomorrow:')
print(w[2]['main'], '-', w[2]['description'])
# 401 "Invalid API key. "

# 2 XML
# Визначає кількість переданих аргументів.
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])
# Завантажує XML дані з OpenWeatherMap.org
url ='http://api.openweathermap.org/data/2.5/weather?q=%s&cnt=3&appid=707d738c92ca835297381e002b64975a' % (location)
response = requests.get(url)
response.raise_for_status()
# Зберігає XML дані в файлі.
weatherFile = open('weather.xml', 'wb')
for chunk in response.iter_content(100000):
    weatherFile.write(chunk)
weatherFile.close()
# Відкриває файл XML.
weatherFile = open('weather.xml')
# Зчитує файл XML.
weatherXml = bs4.BeautifulSoup(weatherFile.read(), 'xml')
# Закриває файл XML.
weatherFile.close()
# Знаходить всі елементи <weather> .
w = weatherXml.select('weather')
print('Current weather in %s:' % (location))
print(w[0].get('value'))
print()
print('Tomorrow:')
print(w[1].get('value'))
print()
print('Day after tomorrow:')
print(w[2].get('value'))


