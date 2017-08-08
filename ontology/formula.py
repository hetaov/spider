# -*- coding: utf-8 -*-

from util.source import get_formula 
from util.prefix import all

def main():
    word_dict, words = get_formula()

    fl = open('data/ontology/formula.ttl', 'w')

    line = list()
    fl.write(all())
    fl.write('\n\n')
    for index, row in enumerate(words):
        line.append('formula:Q%d rdfs:label "%s"@cn .' % (index, row))

    fl.write('\n\n'.join(line).encode('utf-8'))

if __name__ == '__main__':
    main()

