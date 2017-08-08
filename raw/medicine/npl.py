# -*- coding: utf-8 -*-

import pandas as pds

def main():
    df_1 = pds.read_csv('data/word/components_word.csv', encoding='utf-8')
    df_2 = pds.read_csv('data/word/components_word_chinese.csv', encoding='utf-8')
    df_3 = pds.read_csv('data/word/medicine.csv', encoding='utf-8')

    result_1 = set()
    result_2 = set()
    result_3 = set()

    for index, row in df_1.iterrows():
        result_1.add(row[0])

    for index, row in df_2.iterrows():
        result_2.add(row[0])

    for index, row in df_3.iterrows():
        result_3.add(row[0])

    result = result_1 | result_2 | result_3

    print len(result)
    print ','.join(result)



    pds.DataFrame(data={'name': list(result)}).to_csv('data/word/medicine_final.txt', index=False, encoding="utf-8")

if __name__ == '__main__':
    main()
