# -*- coding: utf-8 -*-

import pandas as pds
from model.ontology_source import DBSession, Ontology
from sqlalchemy.orm import aliased

def main():

    session = DBSession()

    df = pds.read_csv('data/ontology_source/symptom.csv', encoding='utf-8')

    result = list()

    for index, row in df.iterrows():

        ontology = Ontology(label_cn=row[0], pro_onto=0)
        result.append(ontology)

    session.bulk_save_objects(result)

    session.commit()
    session.close()

def architecture():

    df = pds.read_csv('data/ontology_source/root.csv', encoding='utf-8')

    for i in range(1,4):
        print i
        f1 = df.loc[df['level'] == i]
        build_level(f1)

def build_level(df):
    session = DBSession()
    result = list()

    flag = aliased(Ontology)

    for index, row in df.iterrows():
        en = ''
        cn = ''
        description = ''
        category = None
        if type(row[0]) is unicode:
            en = row[0]

        if type(row[1]) is unicode:
            cn = row[1]

        if type(row[2]) is unicode:
            description = row[2]

        if row[4] > 1 and type(row[3]) is unicode:
            level = row[4]

            a = session.query(Ontology).filter_by(label_en=row[3]).first()
            if a:
                category = a.id

        ontology = Ontology(label_cn=cn, label_en=en, category=category, comment_cn=description)

        result.append(ontology)

    session.bulk_save_objects(result)

    session.commit()
    session.close()

if __name__ == '__main__':
    #main()
    architecture()


