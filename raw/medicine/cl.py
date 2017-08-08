# -*- coding: utf-8 -*-

import pandas as pds
from util.str_h import remove_html
import jieba

def main():

    df = pds.read_excel('data/raw/medicine.xlsx', encoding='utf-8')

    jieba.load_userdict('data/word/medicine_final.txt')

    df_w = pds.read_csv('data/word/medicine_final.csv', encoding='utf-8')

    words = set(df_w['name'])

    for index, row in df.iterrows():
        if type(row[3]) is unicode:
            row[3] = remove_html(row[3])
            symbol_arr = set(jieba.cut(row[3], cut_all=False))

            result = symbol_arr.intersection(words)
            #print ';,'.join(symbol_arr)
            print ','.join(result)

if __name__ == '__main__':
    main()
