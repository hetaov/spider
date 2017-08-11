# -*- coding: utf-8 -*-

import pandas as pds
from util.source import get_symptom, get_disease, get_department, get_part
import re
from util.prefix import all
from util.str_h import remove_all_html

regex = re.compile(u'\s+|；|;')

d_1, d_2 = get_department()
sym_dict, sym_words = get_symptom()
disease_dict, disease_words = get_disease()
part_dict, part_words = get_part()

def main():

    df = pds.read_excel('data/raw/symblos.xlsx', encoding="utf-8")

    symptom_dict, words = get_symptom()

    fl = open('data/ontology/symptom.ttl', 'w')

    print len(df)
    fl.write(all())
    l = len(df)
    line_s = list()

    for index, symptom in df.iterrows():
        symptom_uri = symptom_dict.get(symptom[3])
        #print symptom
        if type(symptom[9]) is unicode:
            line_s.append('symptom:Q%s rdfs:comment "%s"@cn .' % (symptom_uri, remove_all_html(symptom[9]).encode('utf-8')))

        line_s.append('symptom:Q%s rdfs:label "%s"@cn .' % (symptom_uri, symptom[3].encode('utf-8')))
        line_s.append(build_disease(symptom, symptom_uri))
        line_s.append(build_department(symptom, symptom_uri))
        line_s.append(build_symptom(symptom, symptom_uri))
        line_s.append(build_part(symptom, symptom_uri))
        build_food(symptom, symptom_uri)
        #fl.write('\n\n')

        print 'finished: %d: %d' % (index, l)
    fl.write('\n\n'.join(line_s))
    fl.close()


def build_food(row, index):

    regex = re.compile(u'\d\s?[、.]([^(\d(、|.))]+)')
    m_l = re.compile('[\r\n]')
    m_d = re.compile('\d\s*[.、](?:\D)')
    m_d_s = re.compile('\d\s*[.、]')

    if type(row[14]) is unicode:
        al =  re.split(m_l, row[14])
        for el in al:
            if re.search(m_d, el):
                print '<-->'.join(re.split(m_d_s, el))
            else:
                print el
        good = re.findall(regex, row[14])

    #print '-------------- split finished'
    if type(row[15]) is unicode:
        al =  re.split(m_l, row[15])
        for el in al:
            if re.search(m_d, el):
                print '<-->'.join(re.split(m_d_s, el))
            else:
                print el
        good = re.findall(regex, row[15])

    #print '-------------- line finished'

#科室
def build_department(row, index):
    if type(row[6]) is not unicode:
        return ''
    

    d_1_dict = {x:index for index, x in enumerate(d_1)}
    d_2_dict = {x:index for index, x in enumerate(d_2)}

    d_1_s = set(d_1)
    d_2_s = set(d_2)

    #print d_1_dict.get(row[1])

    #print d_2_dict.get(row[2])
    line = []
    if d_1_dict.get(row[1]):
        line.append(build_line(index, 'P30', 'department_1:Q%s .' % d_1_dict.get(row[1])))
    if d_2_dict.get(row[2]):
        line.append(build_line(index, 'P30', 'department_2:Q%s .' % d_2_dict.get(row[2])))
    return '\n'.join(line)

#相关疾病
def build_disease(row, index):

    if type(row[7]) is not unicode:
        return ''


    regex = re.compile(u'\s+')
    disease_arr = re.split(regex, row[7])
    disease = set(disease_arr).intersection(disease_words)

    return '\n'.join([build_line(index, 'P25', 'disease:Q%d .' % disease_dict.get(x)) for x in disease])

#部位
def build_part(row, index):
    if type(row[5]) is not unicode:
        return ''

    words = set(part_words)

    part_arr = re.split(regex, row[5])
    part = set(part_arr).intersection(words)

    return '\n'.join([build_line(index, 'P29', 'part:Q%d .' % part_dict.get(x)) for x in part])

#症状
def build_symptom(row, index):
    if type(row[8]) is not unicode:
        return ''

    words = set(sym_words)

    symbol_arr = re.split(regex, row[8])
    symptom = set(symbol_arr).intersection(words)

    return '\n'.join([build_line(index, 'P23', 'symptom:Q%d .' % sym_dict.get(x)) for x in symptom])

def build_line(disease_uri, pro_uri, w_uri):
    return 'symptom:Q%s prom:%s %s' %(disease_uri, pro_uri, w_uri)

if __name__ == '__main__':
    main()
