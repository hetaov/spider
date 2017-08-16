# -*- coding: utf-8 -*-

import pandas as pds
from model.ontology_query import get_by_en, get_by_cn
from triple import save_onto

def main():
    df = pds.read_csv('data/word/department_1.csv', encoding='utf-8')
    category = get_by_en('department')

    save_onto(df, category)

def department_2():
    df1 = pds.read_csv('data/word/department_1.csv', encoding='utf-8')
    df2 = pds.read_csv('data/word/department_2.csv', encoding='utf-8').groupby('parent')

    category = get_by_en('department')


    for name, group in df2:

        print name

        #for index, row in group.iterrows():
        par = df1.loc[df1['uri'] == name]
        flag = par.iloc[0][0]

            #print flag
        category_2 = get_by_cn(flag, int(category.id))

            #print category_2
        save_onto(group, category_2)


if __name__ == '__main__':
    #main()
    department_2()

