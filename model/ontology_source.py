# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Ontology(Base):

    __tablename__ = 'ontology'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20))
    category = Column(Integer)
    alias = Column(String(5))
    comment = Column(String(255))
	#1:property,0:ontology
    pro_onto = Column(Integer(1))

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/ontology?charset=utf8')

DBSession = sessionmaker(bind=engine)
