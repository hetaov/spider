# -*- coding: utf-8 -*-

import pandas as pds
import re

def main():

    df = pds.read_excel('data/raw/symblos.xlsx', encoding='utf-8')
    result = set()

    regex = re.compile(u'\s+')
    
    g_c = list()
    g_d = list()
    b_c = list()
    b_f = list()


    for index, symptom in df.iterrows():
        #result.add(symptom[3])
        '''
        print symptom[5]
        if type(symptom[5]) is unicode:
            flag = re.split(regex, symptom[5])

            result = result | set(flag)
        '''
        good_category, good_food, bad_category, bad_food = food(symptom)
        g_c = g_c + good_category
        g_d = g_d + good_food
        b_c = b_c + bad_category
        b_f = b_f + bad_food

    
    #print len(result)
    #print '='.join(result)
    #pds.DataFrame(data={'name': list(result)}).to_csv('data/word/symptom.csv', index=False, encoding="utf-8")
    #pds.DataFrame(data={'name': list(result)}).to_csv('data/ontology_source/part.csv', index=False, encoding="utf-8")
    pds.DataFrame(data={'name': list(g_c)}).to_csv('data/word/good_category.csv', index=False, encoding="utf-8")
    pds.DataFrame(data={'name': list(g_d)}).to_csv('data/word/good_food.csv', index=False, encoding="utf-8")
    pds.DataFrame(data={'name': list(b_c)}).to_csv('data/word/bad_category.csv', index=False, encoding="utf-8")
    pds.DataFrame(data={'name': list(b_f)}).to_csv('data/word/bad_food.csv', index=False, encoding="utf-8")

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

def food(row):
    regex = re.compile(u'\d\s?[、.]([^(\d(、|.))]+)')
    m_l = re.compile('[\r\n]')
    m_d = re.compile('\d\s*[.、](?:\D)')
    m_d_s = re.compile('\d\s*[.、]')

    good_category = list()
    good_food = list()

    bad_category = list()
    bad_food = list()

    if type(row[14]) is unicode:
        al =  re.split(m_l, row[14])
        for el in al:
            if re.search(m_d, el):
                #print '<-->'.join(re.split(m_d_s, el))
                good_category = good_category + re.split(m_d_s, el)
            else:
                #print el
                good_food.append(el)
        #good = re.findall(regex, row[14])

    #print '-------------- split finished'
    if type(row[15]) is unicode:
        al =  re.split(m_l, row[15])
        for el in al:
            if re.search(m_d, el):
                #print '<-->'.join(re.split(m_d_s, el))
                bad_category = bad_category + re.split(m_d_s, el)
            else:
                #print el
                bad_food.append(el)
        #good = re.findall(regex, row[15])

    #print '-------------- line finished'
    return (good_category, good_food, bad_category, bad_food)


if __name__ == '__main__':
    main()
    #source()
    #to_word()
