# -*- coding: utf-8 -*-

import pandas as pds
import re
import jieba
from util.prefix import all
from util.str_h import remove_all_html

regex = re.compile(u'\s+')

symptom_obj = ()
check_obj = ()
department_obj = ()
medicine_obj = ()
disease_obj = ()
arr = range(26)
arr = set(arr)

for i in [1, 2, 3, 5, 10, 12, 13, 14]:
    arr.remove(i)

arr = list(arr)

def remove_gar(target):
    regex = re.compile(u'\s*小儿剧烈咳嗽\s*-->')
    return re.sub(regex, '', target)

def get_symptom():
    global symptom_obj

    if not symptom_obj:
        df = pds.read_csv('data/ontology_source/symptom.csv', encoding='utf-8')
        symptom_obj = ({x[0]:index for index, x in df.iterrows()}, df['name'])

    return symptom_obj

def get_check():
    global check_obj
    if not check_obj:
        df = pds.read_csv('data/ontology_source/check.csv', encoding='utf-8')
        check_obj = ({x[0]:index for index, x in df.iterrows()}, df['name'])
    return check_obj

def get_department():
    global department_obj
    if not department_obj:
        df_1 = pds.read_csv('data/word/department_1.csv', encoding='utf-8')
        df_2 = pds.read_csv('data/word/department_2.csv', encoding='utf-8')
        department_obj = (df_1[u'名称'], df_2[u'名称'])

    return department_obj

def get_medicine():
    global medicine_obj
    if not medicine_obj:
        df = pds.read_csv('data/word/medicine_name.csv', encoding='utf-8')
        medicine_obj = ({x[0]:index for index, x in df.iterrows()}, df['name'])

    return medicine_obj

def build_medicine(row, index):
    if type(row[12]) is not unicode:
        return '' 

    medicine_dict, words = get_medicine()

    medicine_arr = re.split(regex, row[12])

    #print '='.join(medicine_arr)

    return '\n'.join([build_line(index, 'P27', 'drug_generic:Q%d .' % medicine_dict.get(x)) for x in medicine_arr if medicine_dict.get(x) is not None])


def build_department(row, index):
    
    d_1, d_2 = get_department()

    d_1_dict = {x:index for index, x in enumerate(d_1)}
    d_2_dict = {x:index for index, x in enumerate(d_2)}

    d_1_s = set(d_1)
    d_2_s = set(d_2)

    #print d_1_dict.get(row[1])

    #print d_2_dict.get(row[2])
    line = []
    if d_1_dict.get(row[1]):
        line.append(build_line(index, 'P27', 'department_1:%s .' % d_1_dict.get(row[1])))
    if d_2_dict.get(row[2]):
        line.append(build_line(index, 'P27', 'department_2:%s .' % d_2_dict.get(row[2])))
    return '\n'.join(line)


def get_disease():
    global disease_obj
    if not disease_obj:
        df = pds.read_csv('data/ontology_source/disease.csv', encoding='utf-8')
        disease_dict = {}
        words = []
        for index, x in df.iterrows():
            row = x[0].split('|')
            disease_dict.update({z:index for z in row})
            words = words + row
        disease_obj = (disease_dict, words)
    return disease_obj


def main():
    df = pds.read_excel('data/raw/disease.xlsx', encoding='utf-8')

    disease_dict, words = get_disease()

    fl = open('data/ontology/disease.ttl', 'w')

    fl.write(all())
    fl.write('\n\n')

    l = len(df)

    cols = df.columns

    for index, row in df.iterrows():
        #print row
        disease_uri = disease_dict.get(row[3])

        if type(row[5]) is unicode:
            fl.write('disease:Q%s rdfs:comment "%s"@cn .' %(disease_uri, remove_all_html(row[5]).encode('utf-8')))
            fl.write('\n\n')
        fl.write('disease:Q%s rdfs:label "%s"@cn .' %(disease_uri, row[3].encode('utf-8')))
        fl.write('\n\n')

        department_str = build_department(row, disease_uri)
        fl.write(department_str)
        fl.write('\n\n')
        #print department_str
        sym_str = build_symptom(row, index)
        fl.write(sym_str)
        fl.write('\n\n')
        #print sym_str
        check_str = build_check(row, disease_uri)
        fl.write(check_str)
        fl.write('\n\n')
        #print check_str

        disease_str = build_disease(row, disease_uri)
        fl.write(disease_str)
        fl.write('\n\n')
        #print disease_str

        medicine_str = build_medicine(row, index)
        fl.write(medicine_str)
        fl.write('\n\n')

        other_str = build_other(row, index, cols)
        fl.write(other_str.encode('utf-8'))
        fl.write('\n\n')
        print('finised:%d of %d' %(index, l))
        #print medicine_str

    fl.close()


def build_other(row, index, cols):
    lines = list()
    pros = {5:"rdfs:comment"}
    for i in arr:
        print '%d:%s------>%s' % (i, cols[i], row[i])
        item = pros.get(i)
        if item:
            lines.append('disease:Q%d %s "%s"cn .' % (index, item, row[i]))

    return '\n'.join(lines)
    #print len(arr)
    #print arr
    #print row[25]
    #print row[0]

def build_symptom(row, index):

    if type(row[14]) is not unicode:
        return ''

    sym_dict, words = get_symptom()
    words = set(words)

    #flag = remove_gar(row[14])
    #symbol_arr = set(jieba.cut(flag, cut_all=False))
    symbol_arr = re.split(regex, row[14])
    symptom = set(symbol_arr).intersection(words)

    return '\n'.join([build_line(index, 'P23', 'symptom:Q%d .' % sym_dict.get(x)) for x in symptom])

def build_check(row, index):

    if type(row[10]) is not unicode:
        return ''

    check_dict, words = get_check()
    words = set(words)

    #flag = remove_gar(row[10])
    check_arr = re.split(regex, row[10])
    check = set(check_arr).intersection(words)

    return '\n'.join([build_line(index, 'P24', 'check:Q%d .' % check_dict.get(x)) for x in check])




def build_line(disease_uri, pro_uri, w_uri):
    return 'disease:Q%s prom:%s %s' %(disease_uri, pro_uri, w_uri)

def build_disease(row, index):

    if type(row[13]) is not unicode:
        return ''

    disease_dict, words = get_disease()
    words = set(words)

    #flag = remove_gar(row[13])
    regex = re.compile(u'\s+')
    disease_arr = re.split(regex, row[13])
    disease = set(disease_arr).intersection(words)

    #print '-'.join(disease_arr)
    #print '='.join(disease)

    return '\n'.join([build_line(index, 'P25', 'disease:Q%d .' % disease_dict.get(x)) for x in disease])


if __name__ == '__main__':
    jieba.load_userdict('data/word/symptom.txt')
    jieba.load_userdict('data/word/check.txt')
    main()
