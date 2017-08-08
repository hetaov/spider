# -*- coding: utf-8 -*-

from util.source import get_component 
from util.prefix import all

def main():
    word_dict, words = get_component()

    fl = open('data/ontology/component.ttl', 'w')

    line = list()
    fl.write(all())
    fl.write('\n\n')
    for index, row in enumerate(words):
        line.append('ele:Q%d rdfs:label "%s"@cn .' % (index, row))

    fl.write('\n\n'.join(line).encode('utf-8'))

if __name__ == '__main__':
    main()

