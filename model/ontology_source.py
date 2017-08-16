# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Ontology(Base):

    __tablename__ = 'ontology'

    id = Column(Integer, primary_key=True, autoincrement=True)
    label_en = Column(String(100))
    label_cn = Column(String(150))
    category = Column(Integer)
    comment_cn = Column(String(255))
    comment_en = Column(String(255))
    keywords_en = Column(String(250))
    keywords_cn = Column(String(250))

engine = create_engine('mysql+pymysql://root:123456@localhost:3306/ontology?charset=utf8')

DBSession = sessionmaker(bind=engine)
