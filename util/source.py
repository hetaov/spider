# -*- coding: utf-8 -*-

import pandas as pds


def get_symptom():
    df = pds.read_csv('data/ontology_source/symptom.csv', encoding='utf-8')
    return ({x[0]:index for index, x in df.iterrows()}, df['name'])

def get_check():
    df = pds.read_csv('data/ontology_source/check.csv', encoding='utf-8')
    return ({x[0]:index for index, x in df.iterrows()}, df['name'])

def get_department():
    df_1 = pds.read_csv('data/word/department_1.csv', encoding='utf-8')
    df_2 = pds.read_csv('data/word/department_2.csv', encoding='utf-8')

    return (df_1[u'名称'], df_2[u'名称'])

def get_medicine():
    df = pds.read_csv('data/word/medicine_name.csv', encoding='utf-8')
    return ({x[0]:index for index, x in df.iterrows()}, df['name'])

def get_component():
    df = pds.read_csv('data/word/medicine_final.csv', encoding='utf-8')
    return ({x[0]:index for index, x in df.iterrows()}, df['name'])

def get_dosage_form():
    df = pds.read_csv('data/ontology_source/dosage_form.csv', encoding='utf-8')
    return ({x[0]:index for index, x in df.iterrows()}, df['name'])

def get_formula():
    df = pds.read_csv('data/ontology_source/formula.csv', encoding='utf-8')
    return ({x[0]:index for index, x in df.iterrows()}, df['name'])

def get_medicine_product():
    df = pds.read_csv('data/word/medicine_m_name.csv', encoding='utf-8')
    return ({x[0]:index for index, x in df.iterrows()}, df['name'])


def get_part():
    df = pds.read_csv('data/ontology_source/part.csv', encoding='utf-8')
    return ({x[0]:index for index, x in df.iterrows()}, df['name'])

def get_disease():
    df = pds.read_csv('data/ontology_source/disease.csv', encoding='utf-8')
    disease_dict = {}
    words = []
    for index, x in df.iterrows():
        row = x[0].split('|')
        disease_dict.update({z:index for z in row})
        words = words + row
    return (disease_dict, words)
