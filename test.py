# -*- coding: utf-8 -*-

from model.ontology_source import DBSession, Ontology

session = DBSession()

ontology = Ontology(name=u'不是')

session.add(ontology)

session.commit()
session.close()
