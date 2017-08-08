# -*- coding: utf-8 -*-

import pandas as pds

def entity(name):
    return "@prefix %s: <http://www.semioe.org/entity/medicine/%s#> .\n" % (name, name)

def property(name):
    return "@prefix %s: <http://www.semioe.org/prop/%s#> .\n" % (name, name)

def all():
    df = pds.read_csv('util/prefix.csv')
    return property('prom') + '@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n' + ''.join([entity(x[0]) for i, x in df.iterrows()])

if __name__ == '__main__':
    print all()

