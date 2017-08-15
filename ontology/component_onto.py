# -*- coding: utf-8 -*-

from util.source import get_component
from util.prefix import all
from util.str_h import remove_all_html

import pandas as pds


def main():
    word_dict, words = get_component()

    fl = open('data/ontology/component_desc.ttl', 'w')

    df = pds.read_csv('data/word/components_word_new.csv', encoding='utf-8')

    line = list()
    fl.write(all())
    fl.write('\n\n')

    for index, row in df.iterrows():
        if word_dict.get(row[0]):
            line.append('ele:Q%d rdfs:comment "%s"@cn .' % (word_dict.get(row[0]), remove_all_html(row[1])))

    fl.write('\n\n'.join(line).encode('utf-8'))


if __name__ == '__main__':
    main()


