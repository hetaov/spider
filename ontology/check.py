# -*- coding: utf-8 -*-

from util.source import get_check 
from util.prefix import all

def main():
    word_dict, words = get_check()

    fl = open('data/ontology/check.ttl', 'w')

    line = list()
    fl.write(all())
    fl.write('\n\n')
    for index, row in enumerate(words):
        line.append('check:Q%d rdfs:label "%s"@cn .' % (index, row))

    fl.write('\n\n'.join(line).encode('utf-8'))

def build_category():
	
	pass

if __name__ == '__main__':
    main()


