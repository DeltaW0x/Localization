import sys
import csv
import json

locale_map = {}

with open(sys.argv[1], mode='r', encoding='utf-8') as fd:
    loc_dict = {}
    tsv_file = csv.reader(fd, delimiter='\t', quotechar='"')
    tsv_tbl = []
    for row in tsv_file:
        tsv_tbl.append(row)
    
    locale_id_count = len(tsv_tbl[0])
    translation_key_count = len(tsv_tbl)

    for locale_id_index in range(1, locale_id_count):
        translation_pairs = {}
        for translation_key_index in range(1, translation_key_count):
            translation_pairs[tsv_tbl[translation_key_index][0]] = tsv_tbl[translation_key_index][locale_id_index]
        loc_dict[tsv_tbl[0][locale_id_index]] = translation_pairs

    locale_map["localeMap"] = loc_dict

with open(sys.argv[2], mode='w', encoding='utf-8') as jsonfile:
    json.dump(locale_map, jsonfile, indent=4)