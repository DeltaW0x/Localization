import sys
import csv
import json


with open(sys.argv[1], mode='r', newline='', encoding='utf-8') as csvfile:
    data = list(csv.DictReader(csvfile))

with open(sys.argv[2], mode='w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, indent=4)