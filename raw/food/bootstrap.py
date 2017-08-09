# -*- coding: utf-8 -*-

import pandas as pds

def main():
    df = pds.read_excel('data/raw/chinese_food.xls', encoding='utf-8', sheetname=4)

    for index, a in df[7:13].iterrows():
        print a

if __name__ == '__main__':
    main()
