# -*- coding: utf-8 -*-

import pandas as pds
import re

def main():

    df = pds.read_excel('data/raw/symblos.xlsx', encoding='utf-8')
    result = set()

    regex = re.compile(u'\s+')


    for index, symptom in df.iterrows():
        #result.add(symptom[3])
        print symptom[5]
        if type(symptom[5]) is unicode:
            flag = re.split(regex, symptom[5])

            result = result | set(flag)

    
    print len(result)
    print '='.join(result)
    #pds.DataFrame(data={'name': list(result)}).to_csv('data/word/symptom.csv', index=False, encoding="utf-8")
    pds.DataFrame(data={'name': list(result)}).to_csv('data/ontology_source/part.csv', index=False, encoding="utf-8")

def source():

    df = pds.read_excel('data/raw/symblos.xlsx', encoding='utf-8')
    result = set()

    for index, symptom in df.iterrows():
        result.add(symptom[3])
    
    print len(result)
    pds.DataFrame(data={'name': list(result)}).to_csv('data/ontology_source/symptom.csv', index=False, encoding="utf-8")

def to_word():
    df = pds.read_csv('data/word/symptom.csv', encoding='utf-8')
    pds.DataFrame(data={'name': df['name']}).to_csv('data/word/symptom.txt', index=False, encoding="utf-8", header=None)

if __name__ == '__main__':
    main()
    #source()
    #to_word()
