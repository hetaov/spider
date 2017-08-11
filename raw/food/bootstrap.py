# -*- coding: utf-8 -*-

import pandas as pds

def main():

    sheets = range(35)

    cols = range(3, 34)

    for sheet in sheets[0:1]:

        df = pds.read_excel('data/raw/chinese_food.xls', encoding='utf-8', sheetname=sheet)
        
        '''
        add_word(df)
        '''
        result = list()
        for index, a in df[7:10].iterrows():
            #print a
            line = list()
            for i, col in enumerate(a):
                if type(a[i]) is unicode and i > 1:
                    #line.append((col, i))
                    line.append(col)
                else:
                    if i > 1:
                        line.append('')


            #print line
            result.append(line)

        handle(result)



def add_word(df):
    
    for column in df[7:10]:
        print column
        for item in df[column]:
            print item
            print '-->'

def handle(result):


    un_row = result[2:3][0]
    en_row = result[1:2][0]
    cn_row = result[0:1][0]

    flag = None
    cn_flag = None

    for i in range(1, 33):
        if en_row[i - 1] != '':
            flag = en_row[i - 1]
        if cn_row[i - 1] != '':
            cn_flag = cn_row[i - 1]
        print '%s, %s, %s' % (un_row[i - 1], flag, cn_flag)

    #print ','.join(en_row)
    #print ','.join(cn_row)




if __name__ == '__main__':
    main()
