# -*- coding: utf-8 -*-

import pandas as pds
from model.ontology_query import get_by_en
from triple import save_onto

def main():
    df = pds.read_csv('data/ontology_source/symptom.csv', encoding='utf-8')
    category = get_by_en('symptom')

    save_onto(df, category)

if __name__ == '__main__':
    main()
