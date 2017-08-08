# -*- coding: utf-8 -*-

import pandas as pds
import os
import re
import math
from util.str_h import remove_special_character, format_formula


def main():

    df = pds.read_excel('data/raw/medicine.xlsx', encoding="utf-8")

    medicine = set()
    detail = set()
    manufacturer = set()

    components = list()
    #print len(df[u'是否医保'])

    dosage_form = set()

    formula = set()

    for index, row in df.iterrows():
        #print row
        if type(row[3]) is unicode:
            arr = row[3].split(u'：')
            #print ','.join(arr)
            components.append(row[3])

        if type(row[30]) is unicode:
            medicine.add(row[30])
        if type(row[2]) is unicode:
            detail.add(row[2])

        if type(row[14]) is unicode:
            manufacturer.add(row[14])

        if type(row[21]) is unicode:
            formula.add(format_formula(row[21]))

        if type(row[22]) is float and not math.isnan(row[22]):
            #print row[22]
            #print '------------->'
            pass
            #formula.add(re.sub('\r', '', row[21]))


        build_dosage_form(row, dosage_form)

    #print len(formula)
    #print '-'.join(formula)
    #print formula

    #pds.DataFrame(data={'name': components}).to_csv('data/word/components.csv', index=False, encoding="utf-8")
    #pds.DataFrame(data={'name': list(dosage_form)}).to_csv('data/ontology_source/dosage_form.csv', index=False, encoding="utf-8")
    if '' in formula:
        formula.remove('')

    pds.DataFrame(data={'name': list(formula)}).to_csv('data/ontology_source/formula.csv', index=False, encoding="utf-8")

    #dif =  medicine.difference(detail)

    #build_csv(manufacturer, medicine, detail)


def build_csv(manufacturer, medicine, detail):

    dataframe = pds.DataFrame(data={'name': list(manufacturer)})

    dataframe.to_csv('data/word/manufacturer.csv', index=False, encoding="utf-8")

    pds.DataFrame(data={'name': list(medicine)}).to_csv('data/word/medicine_name.csv', index=False, encoding="utf-8")
    pds.DataFrame(data={'name': list(detail)}).to_csv('data/word/medicine_m_name.csv', index=False, encoding="utf-8")

def build_dosage_form(row, dosage_form):
    if type(row[6]) is unicode:
        dosage_form.add(remove_special_character(row[6]))



if __name__ == '__main__':
    main()
