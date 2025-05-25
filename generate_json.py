import csv
import json

with open('localization_table.csv', mode='r', newline='', encoding='utf-8') as csvfile:
    data = list(csv.DictReader(csvfile))

with open('localization_table.json', mode='w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, indent=4)