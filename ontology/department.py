# -*- coding: utf-8 -*-

from util.source import get_department 
from util.prefix import all

def main():
    department_1, department_2 = get_department()
    fl_1 = open('data/ontology/department_1.ttl', 'w')
    fl_2 = open('data/ontology/department_2.ttl', 'w')
    
    fl_1.write(all())
    fl_2.write(all())

    line_1_s = list()
    line_2_s = list()

    fl_1.write('\n\n')
    fl_2.write('\n\n')

    for index, row in enumerate(department_1):
        line_1_s.append('department_1:Q%d rdfs:label "%s"@cn .' % (index, row))

    for index, row in enumerate(department_2):
        line_2_s.append('department_2:Q%d rdfs:label "%s"@cn .' % (index, row))

    fl_1.write('\n'.join(line_1_s).encode('utf-8'))
    fl_1.close()
    fl_2.write('\n'.join(line_2_s).encode('utf-8'))
    fl_2.close()


if __name__ == '__main__':
    main()
