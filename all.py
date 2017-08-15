# -*- coding: utf-8 -*-

import pandas as pds
from model.ontology_source import DBSession, Ontology

def main():

	session = DBSession()

	df = pds.read_csv('data/ontology_source/symptom.csv', encoding='utf-8')

	result = list()

	for index, row in df.iterrows():

            ontology = Ontology(name=row[0], pro_onto=0)
            result.append(ontology)

	session.bulk_save_objects(result)

	session.commit()
	session.close()

if __name__ == '__main__':
    main()


