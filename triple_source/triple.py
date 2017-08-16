# -*- coding: utf-8 -*-

from model.ontology_source import DBSession, Ontology
from model.ontology_query import get_by_cn

def save_onto(df, category):

    session = DBSession()

    result = list()

    for index, row in df.iterrows():
        flag = get_by_cn(row[0])
        if flag.empty:
            category.id = int(category.id)
            #ontology = Ontology(label_cn=row[0], category=category.id)
            ontology = get_by_len(row, category)
            result.append(ontology)

    session.bulk_save_objects(result)

    session.commit()
    session.close()

def get_by_len(row, category):

    labels = row[0].split('|')

    return Ontology(label_cn=labels[0], category=category.id, keywords_cn=row[0])

