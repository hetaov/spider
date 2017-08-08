# -*- coding: utf-8 -*-

import pandas as pds
import re

def main():

    df = pds.read_excel('data/raw/disease.xlsx', encoding='utf-8')

    regex = re.compile(u',|，|、|(\s+)|和|-')

    regex_num = re.compile(u'\d{1,2}[.、]')

    regex_trim = re.compile(u'^((通过)|(可由)|(大多由)|(经))|。|\s+|((传播)|(等))')

    result = set() 
    #人群
    group = set()

    #传染方式
    infe = set()

    #检查项
    check = set()

    l = len(df[u'名称'])


    for index, disease in df.iterrows():

        print disease
        print '%d:%d' % (index, l)

        if type(disease[10]) is unicode:
            check = check | set(re.split(regex, disease[10]))

        if type(disease[8]) is unicode:
            group.add(disease[8])

        if type(disease[9]) is unicode:

            flag = re.sub(regex_num, '', disease[9])

            flag = re.split(regex, flag)

            flag = [re.sub(regex_trim, '', x) for x in flag if x is not None]
            #infe.add(disease[9])
            if flag:
                infe = infe | set(flag)

        if type(disease[3]) is unicode:
            result.add(disease[3])

        if type(disease[4]) is unicode:
            other = re.split(regex, disease[4])
            result = result | set(other)

    #print len(group)
    #print '-'.join(group)

    #infe.remove('')
    #print len(infe)
    #print '-'.join(infe)
    #print infe

    #print len(check)
    #print '-'.join(check)

    #print len(result)
    #pds.DataFrame(data={'name': list(result)}).to_csv('data/word/disease.csv', index=False, encoding="utf-8")
    #pds.DataFrame(data={'name': list(check)}).to_csv('data/ontology_source/check.csv', index=False, encoding="utf-8")
    #pds.DataFrame(data={'name': list(infe)}).to_csv('data/ontology_source/infe.csv', index=False, encoding="utf-8")
    #pds.DataFrame(data={'name': list(group)}).to_csv('data/ontology_source/group.csv', index=False, encoding="utf-8")

def source():
    df = pds.read_excel('data/raw/disease.xlsx', encoding='utf-8')

    regex = re.compile(u',|，')

    result = set()

    for index, disease in df.iterrows():

        row = set()

        if type(disease[3]) is unicode:
            #result.add(disease[3])
            row .add(disease[3])

        if type(disease[4]) is unicode:
            other = re.split(regex, disease[4])
            row = row | set(other)

        result.add('|'.join(row))
    
    print len(result)

    #pds.DataFrame(data={'name': list(result)}).to_csv('data/ontology_source/disease.csv', index=False, encoding="utf-8")

def to_word():
    df = pds.read_csv('data/word/disease.csv', encoding='utf-8')

    pds.DataFrame(data={'name': df['name']}).to_csv('data/word/disease.txt', index=False, encoding="utf-8", header=None)

def check_to_word():
    df = pds.read_csv('data/ontology_source/check.csv', encoding='utf-8')

    pds.DataFrame(data={'name': df['name']}).to_csv('data/word/check.txt', index=False, encoding="utf-8", header=None)



if __name__ == '__main__':
    main()
    #source()
    #to_word()
    #check_to_word()


