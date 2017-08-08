# -*- coding: utf-8 -*-

import pandas as pds
from util.source import get_medicine_product, get_medicine
from util.prefix import all

def main():
    build_generic()
    #build_product()

def build_generic():
    medicine_dict, words = get_medicine()

    fl = open('data/ontology/medicine_generic.ttl', 'w')

    line_s = list()

    for index, row in enumerate(words):
        print row
        print index
        print '------>'
        #fl.write('medicine:Q%d rdfs:label "%s"@cn' % (index, row))
        line_s.append('drug_generic:Q%d rdfs:label "%s"@cn .' % (index, row))

    fl.write(all())
    fl.write('\n\n'.join(line_s).encode('utf-8'))
    fl.close()

def build_product():
    medicine_dict, words = get_medicine_product()

    fl = open('data/ontology/medicine_product.ttl', 'w')

    line_s = list()

    for index, row in enumerate(words):
        print row
        print index
        print '------>'
        #fl.write('medicine:Q%d rdfs:label "%s"@cn' % (index, row))
        line_s.append('drug:Q%d rdfs:label "%s"@cn .' % (index, row))

    fl.write(all())
    fl.write('\n\n'.join(line_s).encode('utf-8'))
    fl.close()



if __name__ == '__main__':
    main()
