# -*- coding: utf-8 -*-

import pandas as pds
from model.ontology_source import DBSession, Ontology
from sqlalchemy.orm import aliased
import numpy
import re

df = pds.DataFrame()

def get_by_key(key, key_type, category=None):

    global df

    if df.empty:
        session = DBSession()
        result = session.query(Ontology).all()

        df = pds.DataFrame([item.__dict__ for item in result])
        df = df.astype(int,errors='ignore')
        session.commit()
        session.close()
        

    if category:
        f1 = df.loc[(df[key_type] == key) & (df['category'] == category)]
    else:
        f1 = df.loc[df[key_type] == key]

    if not f1.empty:
        return f1.iloc[0]
    else:
        return f1

def get_by_cn(key, category=None):
    return get_by_key(key, 'label_cn', category)

def get_by_en(key, category=None):
    return get_by_key(key, 'label_en', category)

def get_by_keyword(key, category=None):
    global df

    if df.empty:
        session = DBSession()
        result = session.query(Ontology).all()

        df = pds.DataFrame([item.__dict__ for item in result])
        df = df.astype(int,errors='ignore')

        #df = df[df.keywords_cn.notnull()]
        session.commit()
        session.close()

    regex = re.compile(u'\|?%s\|?' % re.escape(key))
        

    if category:
        f1 = df.loc[((df['label_cn'] == key) | (df['keywords_cn'].str.contains(regex, na=False))) & (df['category'] == category)]
    else:
        f1 = df.loc[(df['label_cn'] == key) | (df['keywords_cn'].str.contains(regex, na=False))]

    if not f1.empty:
        return f1.iloc[0]
    else:
        return f1

if __name__ == '__main__':
    print get_by_en('drug')
    print get_by_cn(u'药')
    print get_by_keyword(u'脊柱外科')

