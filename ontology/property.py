# -*- coding: utf-8 -*-

import pandas as pds
from util.prefix import all

def main():

    df = pds.read_csv('word/properties/medicine.csv')

    pro = open('data/ontology/pro.ttl', 'w')
    pro.write(all())

    pro.write('\n\n\n')

    for index, row in df.iterrows():
        pro.write('prom:P%d rdfs:label "%s"@cn .\n' % (index, row['name']))

    pro.close()
    

if __name__ == '__main__':
    main()
