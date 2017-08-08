# -*- coding: utf-8 -*-

import pandas as pds
from util.prefix import all

def main():

    df = pds.read_csv('data/word/manufacturer.csv')

    manufacturer = open('data/ontology/manufacturer.ttl', 'w')
    manufacturer.write(all())

    manufacturer.write('\n\n\n')

    for index, row in df.iterrows():
        manufacturer.write('org:Q%d rdfs:label "%s"@cn .\n' % (index, row['name']))

    manufacturer.close()
    

if __name__ == '__main__':
    main()
