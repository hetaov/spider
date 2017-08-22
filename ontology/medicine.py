# -*- coding: utf-8 -*-

import pandas as pds
from util.prefix import all
import jieba
import math
from util.str_h import remove_html, remove_special_character, format_formula, remove_all_html
from model.ontology_query import get_by_keyword

df_symptom = pds.read_csv('data/ontology_source/symptom.csv', encoding='utf-8')
df_disease = pds.read_csv('data/ontology_source/disease.csv', encoding='utf-8')
df_disease_word = pds.read_csv('data/word/disease.csv', encoding='utf-8')
symptom_dict = {x: index for index, x in enumerate(df_symptom['name'])}

disease_dict = {}

for index, row in df_disease.iterrows():
    word_l = row[0].split('|')
    disease_dict.update({x:index for x in word_l})

def manufacturer():
    df = pds.read_csv('data/word/manufacturer.csv', encoding="utf-8")

    dict_name = {}
    for index, x in enumerate(df['name']):
        dict_name[x] = 'Q%d' % index

    return dict_name

def dosage_form():
    df_w = pds.read_csv('data/ontology_source/dosage_form.csv', encoding='utf-8')
    return {x[0]:index for index, x in df_w.iterrows()}

def get_words():
    df_w = pds.read_csv('data/word/medicine_final.csv', encoding='utf-8')
    return df_w['name']

def element(words):
    #df_w = pds.read_csv('data/word/medicine_final.csv', encoding='utf-8')
    return {x:index for index, x in enumerate(words)}

def extrat(words, target):
    symbol_arr = set(jieba.cut(target, cut_all=False))
    return symbol_arr.intersection(words)

def get_medicine():
    df = pds.read_csv('data/word/medicine_m_name.csv', encoding='utf-8')
    return {x[0]:index for index, x in df.iterrows()}

def get_generic_medicine():
    df = pds.read_csv('data/word/medicine_name.csv', encoding='utf-8')
    return {x[0]:index for index, x in df.iterrows()}

def get_formula():
    df = pds.read_csv('data/ontology_source/formula.csv', encoding='utf-8')
    return {x[0]:index for index, x in df.iterrows()}


def main():

    medicine_dict = get_medicine()

    df = pds.read_csv('word/properties/medicine.csv', encoding="utf-8")

    m_words = get_words()

    m_dict = element(m_words)

    medicine_x = pds.read_excel('data/raw/medicine.xlsx', encoding="utf-8")

    medicine_o = open('data/triple/medicine.ttl', 'w')

    ls = df['name']


    dict_name = {}
    for index, x in enumerate(ls):
        dict_name[x] = 'P%d' % index


    medicine_o.write(all())

    medicine_o.write('\n\n\n')

    man_dict = manufacturer()

    dosage_dict = dosage_form()
    
    formula_dict = get_formula()

    generic_dict = get_generic_medicine()

    line_s = list()

    l = len(medicine_x)

    for index, medicine in medicine_x.iterrows():

        #print medicine
        #medicine_uri = medicine_dict.get(medicine[2])
        print medicine[2]
        medicine_uri = get_by_keyword(medicine[2])
        print medicine_uri
        print '==============='
        medicine_uri = int(medicine_uri.id)
        #print medicine[30]
        #print medicine[2]
        for col_i, col in enumerate(medicine_x.columns):

            #print col
            pid = dict_name.get(col)
            prop = medicine.get(col)
            #print prop
            #print pid
            if col == u'是否医保' and prop == 1:
                line_s.append('drug:Q%d prom:%s %s . \n' % (medicine_uri, 'P30', 'medicine:Q1'))
                continue

            if pid and col == u'分子量' and prop and type(prop) is float and not math.isnan(prop):
                line_s.append('drug:Q%d prom:%s %s . \n' % (medicine_uri, 'P18', prop))
                continue

            if pid and prop and type(prop) is unicode:
                if col == u'生产企业':
                    #pass
                    line_s.append('drug:Q%d prom:%s org:%s . \n' % (medicine_uri, dict_name.get(col), man_dict.get(prop)))
                    continue
                elif col == u'主要成份':
                    ele_str = remove_html(prop)
                    els = extrat(m_words, ele_str)
                    if len(els) > 0:
                        for el in els:
                            el_pro = m_dict.get(el)
                            line_s.append('drug:Q%d prom:%s ele:Q%s . \n' % (medicine_uri, dict_name.get(col), el_pro))
                    continue
                    #print ','.join(els)
                elif col == u'适应症':
                    line_s.append(indications(prop, medicine_uri, 'P8'))
                    line_s.append('\n')
                    line_s.append(indications_sym(prop, medicine_uri, 'P8'))
                    line_s.append('\n')
                    continue
                elif col == u'剂型':
                    form_str = remove_special_character(prop)
                    line_s.append('drug:Q%d prom:P31 dosage_form:Q%d .' % (medicine_uri, dosage_dict.get(form_str)))
                    line_s.append('\n')
                    continue
                elif col == u'药品名称':
                    line_s.append('drug:Q%d prom:P1 drug_generic:Q%d .' % (medicine_uri, generic_dict.get(prop)))
                    line_s.append('\n')
                    continue
                elif col == u'禁忌':
                    line_s.append(indications(prop, medicine_uri, 'P11'))
                    line_s.append('\n')
                    line_s.append(indications_sym(prop, medicine_uri, 'P11'))
                    line_s.append('\n')
                    continue
                elif col == u'分子式':

                    formula_str = format_formula(prop)
                    if formula_str and formula_dict.get(formula_str):
                        line_s.append('drug:Q%d prom:%s formula:Q%s . \n' % (medicine_uri, 'P17', formula_dict.get(formula_str)))
                        line_s.append('\n')

                    continue
                elif col == u'不良反应':
                    #line_s.append(indications(prop, medicine_uri, 'P11'))
                    #line_s.append('\n')
                    line_s.append(indications_sym(prop, medicine_uri, 'P10'))
                    line_s.append('\n')
                    continue
                else:
                    prop = remove_html(prop)
                    #pass
                    line_s.append('drug:Q%d prom:%s "%s"@cn . \n' % (medicine_uri, dict_name.get(col), remove_all_html(prop).encode('utf-8')))
                    line_s.append('\n')
                    continue

        line_s.append('\n\n\n')
        print '<---------:%d of %d' % (index, l)

    medicine_o.write(''.join(line_s))
    medicine_o.close()

def build_line():
    return 'drug:Q%d prom:%s ele:%s . \n' % (index, dict_name.get(col), el_pro)

#适应病处理
def indications(prop, q, prom):
    words = set(df_disease_word['name'])


    symbol_arr = set(jieba.cut(prop, cut_all=False))

    diseases = symbol_arr.intersection(words)

    return '\n'.join(['drug:Q%d prom:%s disease:Q%s .' % (q, prom, disease_dict.get(x)) for x in diseases])

#适应症处理
def indications_sym(prop, q, prom):

    words = set(df_symptom['name'])

    symbol_arr = set(jieba.cut(prop, cut_all=False))
    symptom = symbol_arr.intersection(words)

    #print '|'.join(symptom)
    return '\n'.join(['drug:Q%d prom:%s symptom:Q%s .' % (q, prom, symptom_dict.get(x)) for x in symptom])




if __name__ == '__main__':
    jieba.load_userdict('data/word/disease.txt')
    jieba.load_userdict('data/word/symptom.txt')
    jieba.load_userdict('data/word/medicine_final.txt')
    main()
